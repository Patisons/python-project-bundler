# =============================================================================
# project_bundler.py
# Python Project Files Bundler & Restorer (OOP version)
# Backup and restore Python project files via text archives
# =============================================================================

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
import datetime
import re
from typing import Dict, List, Tuple, Optional


class ProjectManager:
    """Class for managing project folder operations"""

    def __init__(self, initial_dir: Optional[Path] = None):
        self.project_dir = initial_dir or Path.cwd()

    def get_py_files(self) -> List[Path]:
        """Returns all .py files in the project directory"""
        return list(self.project_dir.glob("*.py"))

    def file_exists(self, filename: str) -> bool:
        """Check if file already exists in the project directory"""
        return (self.project_dir / filename).exists()

    def write_file(self, filename: str, content: str) -> bool:
        """Write file to the project directory"""
        try:
            (self.project_dir / filename).write_text(content, encoding="utf-8")
            return True
        except Exception:
            return False

    def read_file(self, filename: str) -> Optional[str]:
        """Read file from the project directory"""
        try:
            return (self.project_dir / filename).read_text(encoding="utf-8")
        except Exception:
            return None


class ArchiveManager:
    """Class for managing text archive operations"""

    @staticmethod
    def create_archive(project_name: str, files: Dict[str, str]) -> str:
        """Create archive content from files dictionary"""
        content_lines = [
            f"# Project Archive – {project_name}",
            f"# Date: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}",
            f"# Total files: {len(files)}",
            ""
        ]

        for filename, file_content in sorted(files.items()):
            content_lines.extend([
                f"=== {filename} ===",
                file_content.rstrip(),
                "\n=== END ===\n"
            ])

        return "\n".join(content_lines)

    @staticmethod
    def parse_archive(archive_content: str) -> Tuple[List[str], Dict[str, str]]:
        """Parse archive content, return file list and content"""
        # Find first marker
        first_marker_pos = archive_content.find("===")
        if first_marker_pos == -1:
            raise ValueError("No '===' marker found in the text file")

        content = archive_content[first_marker_pos:]
        blocks = re.split(r'(?m)^=== END ===\s*$', content)

        file_list = []
        file_data = {}

        for block in blocks:
            block = block.strip()
            if not block:
                continue

            match = re.match(r'^=== (.+?) ===\s*(.+)', block, re.DOTALL)
            if match:
                filename = match.group(1).strip()
                file_content = match.group(2).rstrip()

                if filename:
                    file_list.append(filename)
                    file_data[filename] = file_content

        return sorted(file_list), file_data


class UIBuilder:
    """Class for creating GUI elements"""

    @staticmethod
    def create_button(parent, text, command, **kwargs):
        """Create button with standard styles"""
        return tk.Button(parent, text=text, command=command, **kwargs)

    @staticmethod
    def create_label(parent, text, **kwargs):
        """Create label with standard styles"""
        return tk.Label(parent, text=text, **kwargs)

    @staticmethod
    def create_separator(parent):
        """Create horizontal separator"""
        return ttk.Separator(parent, orient="horizontal")


class FileSelectionDialog:
    """Dialog window for file selection during restoration"""

    def __init__(self, parent, file_list: List[str], project_manager: ProjectManager):
        self.parent = parent
        self.file_list = file_list
        self.project_manager = project_manager
        self.proceed = False
        self.selected_files = []
        self.auto_create = False

        self.dialog = tk.Toplevel(parent)
        self._setup_dialog()

    def _setup_dialog(self):
        """Setup dialog window"""
        self.dialog.title("Restoration Selection")
        self.dialog.geometry("620x520")
        self.dialog.transient(self.parent)
        self.dialog.grab_set()
        self.dialog.protocol("WM_DELETE_WINDOW", self._on_cancel)

        # Header
        tk.Label(self.dialog, text="Choose which files to restore:",
                 font=("Segoe UI", 11, "bold")).pack(pady=(14, 4), anchor="w", padx=18)
        
        # Instructions
        instructions = tk.Label(self.dialog, 
                               text="• No selection = restore all files\n"
                                    "• With selection = restore only selected\n"
                                    "• 'Select Existing' = select only existing files",
                               font=("Segoe UI", 9), fg="#555555", justify="left")
        instructions.pack(anchor="w", padx=18, pady=(0, 6))

        # Checkbox
        self.auto_create_var = tk.BooleanVar(value=False)
        checkbox = tk.Checkbutton(self.dialog,
                                  text="Ask before creating non-existing files",
                                  variable=self.auto_create_var,
                                  font=("Segoe UI", 10))
        checkbox.pack(anchor="w", padx=18, pady=6)

        # Legend
        self._create_legend()

        # Treeview with file list
        self._create_file_tree()

        # Buttons
        self._create_buttons()

    def _create_legend(self):
        """Create color legend"""
        legend = tk.Frame(self.dialog)
        legend.pack(anchor="w", padx=18, pady=(0, 10))
        tk.Label(legend, text="● Green  = already exists in project (will be overwritten)", 
                 fg="#1b5e20").pack(anchor="w")
        tk.Label(legend, text="● Orange = doesn't exist (will be created if selected)", 
                 fg="#e65100").pack(anchor="w")

    def _create_file_tree(self):
        """Create Treeview with file list"""
        tree_frame = tk.Frame(self.dialog)
        tree_frame.pack(fill="both", expand=True, padx=16, pady=(4, 12))

        columns = ("filename", "status")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings", selectmode="extended")
        self.tree.heading("filename", text="File")
        self.tree.heading("status", text="Status")
        self.tree.column("filename", width=300)
        self.tree.column("status", width=200)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.config(yscrollcommand=scrollbar.set)
        self.tree.pack(fill="both", expand=True)

        # Color tags
        self.tree.tag_configure("exists", foreground="#1b5e20")
        self.tree.tag_configure("new", foreground="#e65100")

        # Populate with files
        self._populate_file_tree()

    def _populate_file_tree(self):
        """Populate Treeview with file information"""
        for filename in sorted(self.file_list):
            if self.project_manager.file_exists(filename):
                tag = "exists"
                status = "Already exists (will overwrite)"
            else:
                tag = "new"
                status = "Doesn't exist (will create)"

            self.tree.insert("", "end", values=(filename, status), tags=(tag,))

    def _create_buttons(self):
        """Create buttons at the bottom of dialog"""
        btn_frame = tk.Frame(self.dialog)
        btn_frame.pack(pady=16)

        tk.Button(btn_frame, text="Select Existing", command=self._select_existing,
                  width=14, bg="#2196f3", fg="white").pack(side="left", padx=5)

        tk.Button(btn_frame, text="Unselect All", command=self._unselect_all,
                  width=14, bg="#ff9800", fg="white").pack(side="left", padx=5)

        tk.Button(btn_frame, text="Cancel", command=self._on_cancel,
                  width=14, bg="#f44336", fg="white").pack(side="left", padx=5)

        tk.Button(btn_frame, text="Continue Restoration",
                  command=self._on_continue, width=20,
                  bg="#4caf50", fg="white").pack(side="left", padx=5)

    def _on_cancel(self):
        """Handle cancel action"""
        self.proceed = False
        self.dialog.destroy()

    def _select_existing(self):
        """Select all existing files in the tree"""
        # First unselect all
        for item in self.tree.selection():
            self.tree.selection_remove(item)
        
        # Then select only existing files (green ones)
        for item in self.tree.get_children():
            filename = self.tree.item(item)["values"][0]
            if self.project_manager.file_exists(filename):
                self.tree.selection_add(item)

    def _unselect_all(self):
        """Unselect all files in the tree"""
        for item in self.tree.selection():
            self.tree.selection_remove(item)

    def _on_continue(self):
        """Handle continue action"""
        selected = self.tree.selection()
        self.selected_files = [self.tree.item(item)["values"][0] for item in selected]
        self.auto_create = self.auto_create_var.get()
        self.proceed = True
        self.dialog.destroy()

    def show(self) -> Tuple[bool, List[str], bool]:
        """Show dialog and return results"""
        self.dialog.wait_window()
        return self.proceed, self.selected_files, self.auto_create


class FileListWindow:
    """Window for displaying file list from archive"""

    def __init__(self, parent, title: str, file_list: List[str], 
                 project_manager: ProjectManager, extra_text: str = ""):
        self.parent = parent
        self.file_list = file_list
        self.project_manager = project_manager
        self.extra_text = extra_text

        self.window = tk.Toplevel(parent)
        self._setup_window(title)

    def _setup_window(self, title: str):
        """Setup window"""
        self.window.title(title)
        self.window.geometry("600x450")
        self.window.transient(self.parent)

        # Header
        header = tk.Label(self.window, text=f"{title}:", font=("Segoe UI", 11, "bold"))
        header.pack(pady=(14, 8), anchor="w", padx=18)

        # Treeview
        self._create_file_tree()

        # Extra info
        if self.extra_text:
            info = tk.Label(self.window, text=self.extra_text, 
                           font=("Segoe UI", 9), justify="left")
            info.pack(pady=10, anchor="w", padx=18)

        # Close button
        tk.Button(self.window, text="Close", command=self.window.destroy,
                  width=12, bg="#607d8b", fg="white").pack(pady=12)

    def _create_file_tree(self):
        """Create Treeview with file list"""
        tree_frame = tk.Frame(self.window)
        tree_frame.pack(fill="both", expand=True, padx=16, pady=(4, 12))

        columns = ("filename", "status")
        tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
        tree.heading("filename", text="File")
        tree.heading("status", text="Status")
        tree.column("filename", width=300)
        tree.column("status", width=200)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.config(yscrollcommand=scrollbar.set)
        tree.pack(fill="both", expand=True)

        # Tags
        tree.tag_configure("exists", foreground="#1b5e20")
        tree.tag_configure("new", foreground="#e65100")

        # Populate
        for filename in sorted(self.file_list):
            if self.project_manager.file_exists(filename):
                tag = "exists"
                status = "Exists in project"
            else:
                tag = "new"
                status = "Not in project"

            tree.insert("", "end", values=(filename, status), tags=(tag,))


class ProjectBundlerApp:
    """Main application class"""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.project_manager = ProjectManager()
        self._setup_ui()

    def _setup_ui(self):
        """Setup user interface"""
        self.root.title("Python Project Bundler & Restorer")
        self.root.geometry("740x420")
        self.root.resizable(False, False)

        # === Header ===
        header = tk.Label(self.root, 
                         text="Python Project Files – Backup & Restore",
                         font=("Segoe UI", 14, "bold"), bg="#1565c0", fg="white", pady=12)
        header.pack(fill="x")

        # === Folder Selection ===
        folder_frame = tk.Frame(self.root, bg="#e3f2fd", pady=14)
        folder_frame.pack(fill="x", padx=20, pady=(16, 0))

        tk.Label(folder_frame, text="Project Folder:", 
                font=("Segoe UI", 10, "bold"), bg="#e3f2fd").pack(anchor="w", padx=12)

        self.folder_label = tk.Label(folder_frame, 
                                     text=str(self.project_manager.project_dir),
                                     font=("Segoe UI", 9), bg="white", 
                                     anchor="w", relief="sunken", padx=8, pady=6)
        self.folder_label.pack(fill="x", padx=12, pady=(4, 8))

        tk.Button(folder_frame, text="📁 Choose Project Folder", 
                 command=self.choose_project_folder,
                 bg="#0277bd", fg="white", font=("Segoe UI", 10), 
                 width=25).pack(pady=(0, 8))

        # === Main Actions ===
        actions_frame = tk.Frame(self.root)
        actions_frame.pack(pady=20)

        btn_config = {"width": 30, "height": 2, "font": ("Segoe UI", 10, "bold")}

        tk.Button(actions_frame, text="📦 Bundle → Create .txt Archive",
                  command=self.bundle_files, bg="#4caf50", fg="white", 
                  **btn_config).grid(row=0, column=0, padx=10, pady=8)

        tk.Button(actions_frame, text="📥 Restore ← From .txt Archive",
                  command=self.restore_files, bg="#ff9800", fg="white", 
                  **btn_config).grid(row=0, column=1, padx=10, pady=8)

        tk.Button(actions_frame, text="📋 View .txt Archive Contents",
                  command=self.show_txt_file_list, bg="#03a9f4", fg="white", 
                  **btn_config).grid(row=1, column=0, columnspan=2, pady=8)

        # === Status Bar ===
        status_frame = tk.Frame(self.root, bg="#37474f")
        status_frame.pack(side="bottom", fill="x")

        self.status_var = tk.StringVar(value="Ready. Choose project folder to begin.")
        self.status_label = tk.Label(status_frame, textvariable=self.status_var, 
                bg="#37474f", fg="white", font=("Segoe UI", 9), 
                wraplength=700, justify="left", pady=10)
        self.status_label.pack(padx=12, fill="x")

        # Initial folder display update
        self._update_folder_display()

    def _update_folder_display(self):
        """Update folder path display"""
        text = str(self.project_manager.project_dir).replace(str(Path.home()), "~")
        self.folder_label.config(text=text)
        self.status_var.set(f"Selected folder: {self.project_manager.project_dir.name}")

    def choose_project_folder(self):
        """Choose project folder"""
        chosen = filedialog.askdirectory(title="Choose project folder")
        if chosen:
            self.project_manager.project_dir = Path(chosen).resolve()
            self._update_folder_display()

    def set_status(self, msg: str, color: str = "black"):
        """Set status message"""
        self.status_var.set(msg)
        self.root.update_idletasks()

    def bundle_files(self):
        """Bundle .py files into single .txt archive"""
        if not self.project_manager.project_dir.is_dir():
            messagebox.showwarning("Warning", "Please choose a valid project folder first.")
            return

        py_files = self.project_manager.get_py_files()

        if not py_files:
            messagebox.showinfo("Info", "No .py files found in the selected folder.")
            return

        # Prepare file contents
        files_content = {}
        for file_path in py_files:
            content = self.project_manager.read_file(file_path.name)
            if content is not None:
                files_content[file_path.name] = content

        # Create archive
        archive_content = ArchiveManager.create_archive(
            self.project_manager.project_dir.name,
            files_content
        )

        # Ask for save location
        now = datetime.datetime.now()
        default_name = f"{self.project_manager.project_dir.name}_{now:%Y-%m-%d_%H-%M}.txt"
        default_dir = str(self.project_manager.project_dir)

        out_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text file", "*.txt")],
            initialdir=default_dir,
            initialfile=default_name,
            title="Where to save the bundled file?"
        )

        if not out_path:
            return

        # Save archive
        try:
            Path(out_path).write_text(archive_content, encoding="utf-8")
            self.set_status(f"Saved: {Path(out_path).name}  ({len(py_files)} files)", "#006600")
        except Exception as e:
            self.set_status(f"Error: {str(e)}", "darkred")
            messagebox.showerror("Error", str(e))

    def restore_files(self):
        """Restore files from .txt archive"""
        if not self.project_manager.project_dir.is_dir():
            messagebox.showwarning("Warning", "Please choose a project folder first.")
            return

        # Choose archive file
        in_path = filedialog.askopenfilename(
            filetypes=[("Text file", "*.txt")],
            initialdir=str(self.project_manager.project_dir),
            title="Choose the bundled .txt file"
        )

        if not in_path:
            return

        try:
            # Read and parse archive
            archive_content = Path(in_path).read_text(encoding="utf-8")
            file_list, file_data = ArchiveManager.parse_archive(archive_content)

            if not file_list:
                messagebox.showinfo("Info", "No valid .py files found in the text file.")
                return

            # Show file selection dialog
            dialog = FileSelectionDialog(self.root, file_list, self.project_manager)
            proceed, selected_files, auto_create = dialog.show()

            if not proceed:
                self.set_status("Restoration cancelled", "#f57c00")
                return

            # Perform restoration
            restored, created_new, skipped, errors = self._perform_restoration(
                file_list, file_data, selected_files, auto_create
            )

            # Show results
            self._show_restoration_results(restored, created_new, skipped, errors)

        except Exception as e:
            self.set_status(f"Error during restoration: {str(e)}", "darkred")
            messagebox.showerror("Error", str(e))

    def _perform_restoration(self, file_list: List[str], file_data: Dict[str, str],
                             selected_files: List[str], auto_create: bool) -> Tuple[int, int, int, int]:
        """Perform file restoration"""
        restored = created_new = skipped = errors = 0

        # Determine which files to process
        files_to_process = self._determine_files_to_process(file_list, selected_files, auto_create)

        # Process each file
        for filename in files_to_process:
            if filename not in file_data:
                continue

            exists = self.project_manager.file_exists(filename)

            if exists:
                # Overwrite existing file
                if self.project_manager.write_file(filename, file_data[filename]):
                    restored += 1
                else:
                    errors += 1
            else:
                # New file - logic depends on selection
                if selected_files:
                    # Files are selected - restore them without asking
                    if self.project_manager.write_file(filename, file_data[filename]):
                        created_new += 1
                    else:
                        errors += 1
                elif auto_create:
                    # No selection, but auto_create checked - ask for each new file
                    if messagebox.askyesno("New file", f"Create {filename}?"):
                        if self.project_manager.write_file(filename, file_data[filename]):
                            created_new += 1
                        else:
                            errors += 1
                    else:
                        skipped += 1
                else:
                    # No selection, no auto_create - create all new files without asking
                    if self.project_manager.write_file(filename, file_data[filename]):
                        created_new += 1
                    else:
                        errors += 1

        return restored, created_new, skipped, errors

    def _determine_files_to_process(self, file_list: List[str],
                                    selected_files: List[str],
                                    auto_create: bool) -> List[str]:
        """Determine which files to process"""
        if selected_files:
            # Files are selected - process only those
            return selected_files
        else:
            # No selection - process all files
            return file_list

    def _show_restoration_results(self, restored: int, created_new: int,
                                  skipped: int, errors: int):
        """Show restoration results"""
        msg_lines = ["Completed."]
        if restored:   msg_lines.append(f"Overwritten existing: {restored}")
        if created_new: msg_lines.append(f"Created new: {created_new}")
        if skipped:    msg_lines.append(f"Skipped non-existing: {skipped}")
        if errors:     msg_lines.append(f"Errors: {errors}")

        msg = "\n".join(msg_lines) or "Nothing was changed."
        color = "#006600" if errors == 0 else "darkred"
        self.set_status(msg, color)

    def show_txt_file_list(self):
        """Show file list from .txt archive"""
        in_path = filedialog.askopenfilename(
            filetypes=[("Text file", "*.txt")],
            initialdir=str(self.project_manager.project_dir),
            title="Choose .txt file to view contents"
        )

        if not in_path:
            return

        try:
            # Read and parse archive
            archive_content = Path(in_path).read_text(encoding="utf-8")
            file_list, _ = ArchiveManager.parse_archive(archive_content)

            if not file_list:
                messagebox.showinfo("Info", "No valid .py files found in the text file.")
                return

            # Show file list in window
            extra_text = f"\n\nTotal: {len(file_list)} files\n\nFile: {Path(in_path).name}"
            FileListWindow(
                self.root,
                "Files in txt Archive",
                file_list,
                self.project_manager,
                extra_text
            )

            self.set_status(f"Viewed list from: {Path(in_path).name}", "#006064")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to process txt file:\n{str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectBundlerApp(root)
    root.mainloop()
