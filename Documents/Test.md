# Tesztjegyzőkönyv
### Main Project

|  Dokumentum címe: (azonosítója) |  KRK_afp1 - "KRK_Forum" |
|---|:-:|
| **Minősítés: (állapot)**  |  Jóváhagyott |
| **Verziószám:**  |  Beta 1.0 |
| **Projekt név:** |  KRK_Forum|
| **Készítette:** | KRK_afp1 |
| **Utolsó mentés kelte:** | 2020.11.30 |
| **Dokumentum célja:** | A projekt aktualis állapotának 

### Projektben résztvevő fejlesztők:

|  Név | Szerepkör |
|---|:-:|
| Zsadányi Rózsa |  Projekt manager, Test manager |
| Kurán Bertalan  |  Vezető adatbázis fejlesztő |
| Németi Nikoletta | Adatbázis fejlesztő |

## 1. Bevezetés
Tesztelés célja a projektben megtalálható felépítésbeli vagy formatervezési hibák feltárása.
### 1.1 Tesztelési terv hatóköre, célja:

- A tesztelési terv célja a tesztelés teljes körűségének biztosítása, a tesztelés során alkalmazott eljárások és megoldások meghatározása.
- A teszt végrehajtásáért ez esetben a test manager fele , és a tesztelést az általa összeállított tesztcsapat hajtja végre a 2.1. fejezetben meghatározott módon.

### 1.2 Elvárások
#### Az alábbi alap elvárások képezik ennek a teszttervnek az alapját:
- Az olvasó ismeri az alapdokumentumokat, amelyek meghatározzák a rendszert. 
- Az **KRK_afp1** projektcsapat felelős a tesztadatok előállításáért.

## 2 Szükséges erőforrások
Ez a fejezet a teszteléshez szükséges erőforrásokat fejti ki.

### 2.1 Feladatkörök és felelősségek (tesztcsapat meghatározása)
| Feladatkör  |  Felelősség/tevékenység |  Személy  |
|---|---|---|
|  **Tesztelő, Teszt-koordinátor:** |  A teszt végrehajtása, észrevételek dokumentálása, teszt dokumentáció archiválása.Teszt terv készítése.  A tesztterv jóváhagyatása a projektmenedzserrel.  Teszt forgatókönyvek létrehozása  Inkonzisztenciák kezelése.  Helyes és időbeni hibakezelés.  Szükség esetén problémák eszkalálása a projekt menedzsernek.  Végső riport készítése.  Teszt dokumentum archiválása.  Az észrevételek státuszának követése, ill. dokumentálása |  Zsadányi Rózsa |
| **Szakértő:**  |  A szakértő az észrevételek elemzi és megoldást javasol. |  Kurán Bertalan  |
|**Projektvezető:**| Teszt terv jóváhagyása  Teszt forgatókönyv (testscript)| Németi Nikoletta |

### 2.2 Tesztadatok
A teszt végrehajtásához szükséges rekordok (tesztadatok) száma: 4
A tesztadatok elkészítéséért és feltöltéséért felelős személy: Zsadányi Rózsa

A tesztadatoknak az alábbi követelményeknek kell megfelelniük:
- Az adatbázisba felvitt adatoknak csak is az UTF-8 kódtáblában található karaktereket szabad tartalmaznia.

## 3 Tesztelési terv
Ez a fejezet leírja a teszt típusát, a metodológiáját és a riport készítés módszerét. Emellett meghatározza a teszt elvárásokat, a teszt-esetek elvárt eredményeit, sikerességének kritériumait, a kockázatok kezelését és a hatáskörön kívül eseteket.

### 3.1 Fejlesztői teszt
A fejlesztői tesztelés célja a rendszer alapvető funkcióinak ellenőrzése, a hibakezelés és az alapvető funkciók működésének vizsgálata
**Módszere:**
A program SQL adatbázisa "DUMMY" (*Nem valós*) adatokkal kerül feltültésre a tesztelés adat.
Ezen adatok többségét úgynevett "Lorem Ipsum" típusú véletlenül generált adat teszi ki.

### 3.2 Prototípus (modul) teszt
A prototípustesztelés (vagy másik nevén modultesztelés) célja a rendszer már működő moduljainak önálló tesztelése, a modulon belüli hibák azonosításának és kiküszöbölésének érdekében. 
**Módszere:** 
A szegmensek validálása egyénileg történik. A tesztelés visszont a szegmensek föggőségeire is ki terjed.
