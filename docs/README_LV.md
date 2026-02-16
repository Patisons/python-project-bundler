# Python Project Bundler & Restorer

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: DWTFYW](https://img.shields.io/badge/License-Do%20What%20You%20Want-green.svg)](../LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)](https://github.com/yourusername/python-project-bundler)

Vienkāršs rīks ar grafisko interfeisu Python projektu dublēšanai un atjaunošanai, apvienojot visus `.py` failus vienā teksta arhīvā.

**🌍 Valodas:** [English](../README.md) | [Русский](README_RU.md) | [Latviešu](#)

---

## 📋 Saturs

- [Iespējas](#-iespējas)
- [Ekrānuzņēmumi](#-ekrānuzņēmumi)
- [Instalācija](#-instalācija)
- [Lietošana](#-lietošana)
- [Kā tas darbojas](#-kā-tas-darbojas)
- [Prasības](#-prasības)
- [Līdzdalība](#-līdzdalība)
- [Licence](#-licence)

---

## ✨ Iespējas

- **📦 Projektu apvienošana**: Apvieno visus Python failus mapē vienā `.txt` arhīvā
- **📥 Projektu atjaunošana**: Izvelk un atjauno failus no arhīva atpakaļ projekta mapē
- **🎯 Selektīva atjaunošana**: Izvēlies, kurus failus atjaunot caur vizuālo interfeisu
- **🔍 Arhīva priekšskatījums**: Apskatīt arhīva saturu bez atjaunošanas
- **🎨 Lietotājam draudzīgs GUI**: Tīrs, moderns Tkinter interfeiss
- **🛡️ Drošas operācijas**: Krāsu kodēti brīdinājumi esošajiem failiem
- **⚙️ Elastīgs**: Izvēlies gan projekta mapi, gan arhīva saglabāšanas vietu

---

## 📸 Ekrānuzņēmumi

### Galvenais logs
![Galvenais logs](images/main_window.png)
*Galvenais interfeiss ar trim pamata darbībām*

### Failu izvēles dialogs
![Failu izvēle](images/file_selection.png)
*Izvēlies, kurus failus atjaunot ar krāsu kodētu statusu*

---

## 🚀 Instalācija

### Priekšnosacījumi

- Python 3.7 vai jaunāks
- tkinter (parasti iekļauts Python komplektā)

### Ātrā palaišana

1. **Klonē repozitoriju:**
   ```bash
   git clone https://github.com/Patisons/python-project-bundler.git
   cd python-project-bundler
   ```

2. **Palaid aplikāciju:**
   ```bash
   python project_bundler.py
   ```

Tas ir viss! Nav nepieciešamas ārējās atkarības.

---

## 📖 Lietošana

### 1. Failu apvienošana (Arhīva izveidošana)

1. Spied **"Choose Project Folder"** un izvēlies sava Python projekta direktoriju
2. Spied **"📦 Bundle → Create .txt Archive"**
3. Izvēlies, kur saglabāt arhīvu (noklusējums: projekta mape ar laika zīmogu)
4. Gatavs! Visi `.py` faili tagad apvienoti vienā teksta failā

### 2. Failu atjaunošana (No arhīva)

1. Spied **"Choose Project Folder"**, lai izvēlētos mērķa mapi
2. Spied **"📥 Restore ← From .txt Archive"**
3. Izvēlies arhīva failu atjaunošanai
4. Izvēles dialogā:
   - **Zaļie** faili = jau eksistē (tiks pārrakstīti)
   - **Oranžie** faili = neeksistē (tiks izveidoti)
5. Izvēlies failus atjaunošanai (vai neizvēlies neko, lai atjaunotu visus esošos failus)
6. Pēc izvēles atzīmē "Ask before creating non-existing files"
7. Spied **"Continue Restoration"**

### 3. Arhīva satura skatīšana

1. Spied **"📋 View .txt Archive Contents"**
2. Izvēlies arhīva failu
3. Apskati visus failus, kas glabājas arhīvā, tos neatjaunojot

---

## 🔧 Kā tas darbojas

### Arhīva formāts

Rīks izveido cilvēkiem lasāmus teksta arhīvus ar šādu struktūru:

```
# Project Archive – MansProjekts
# Date: 2026-02-15 12:30:45
# Total files: 3

=== main.py ===
import tkinter as tk
...
=== END ===

=== utils.py ===
def helper():
    ...
=== END ===

=== config.py ===
settings = {}
...
=== END ===
```

### Galvenie komponenti

- **ProjectManager**: Pārvalda failu operācijas projekta direktorijā
- **ArchiveManager**: Izveido un parsē teksta arhīvus
- **FileSelectionDialog**: Interaktīva failu izvēle atjaunošanai
- **ProjectBundlerApp**: Galvenā GUI aplikācija

---

## 📦 Prasības

- **Python**: 3.7+
- **Tikai iebūvētie moduļi**:
  - `tkinter` - GUI ietvars
  - `pathlib` - Failu ceļu operācijas
  - `datetime` - Laika zīmogi
  - `re` - Arhīva parsēšana

---

## 🤝 Līdzdalība

Ieguldījumi ir apsveicami! Kā vari palīdzēt:

1. Forkē repozitoriju
2. Izveido funkcijas zaru (`git checkout -b feature/BrīnišķīgaFunkcija`)
3. Commit savas izmaiņas (`git commit -m 'Pievienot BrīnišķīguFunkciju'`)
4. Push uz zaru (`git push origin feature/BrīnišķīgaFunkcija`)
5. Atver Pull Request

### Uzlabošanas virzieni

- Pievienot atbalstu citiem failu tipiem (`.txt`, `.md`, `.json` utt.)
- Implementēt kompresiju lieliem projektiem
- Pievienot projektu šablonus
- Izveidot CLI versiju
- Pievienot arhīva šifrēšanas opciju

---

## 📄 Licence

**Do What You Want License** - Izmanto, kā vēlies. Bez ierobežojumiem. Bez nosacījumiem. Tikai nevainojiet, ja kaut kas salūzt! 😄

Skat. [LICENSE](../LICENSE) failu pilnajam "juridiskajam bļa-bļa-bļa" (spoileris: tas ir ļoti īss un cilvēkiem lasāms).

**Gribi pateikties?** Pārbaudi LICENSE failu izvēles veidiem, kā atbalstīt projektu.

---

## 👨‍💼 Autors

Izveidots ar ❤️ **Pats-MK** un **Claude**

---

## 🙏 Pateicības

- Būvēts, izmantojot tikai Python standarta bibliotēku
- Iedvesmots no vajadzības pēc vienkāršām, pārnēsājamām projektu rezerves kopijām
- Paldies Python kopienai par izcilu dokumentāciju

---

## 📞 Atbalsts

Ja saskaries ar problēmām vai ir jautājumi:

1. Pārbaudi [Issues](https://github.com/Patisons/python-project-bundler/issues) lapu
2. Izveido jaunu problēmu, norādot:
   - Tavu Python versiju
   - Operētājsistēmu
   - Soļus problēmas reproducēšanai
   - Kļūdu ziņojumus (ja ir)

---

**⭐ Ja šis rīks ir noderīgs, lūdzu, apsver iespēju dot tam zvaigznīti!**
