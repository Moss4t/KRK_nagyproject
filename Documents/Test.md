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

### 3.3 Integrációs teszt
Az integrációs teszt célja a rendszer más rendszerekhez történő illesztésének vizsgálata, a több rendszereken keresztül átívelő funkciók tesztelésének érdekében. Az adatmigrációs tesztelés az integrációs teszteléshez tartozik, ennek lényege, hogy a bevezetendő rendszerbe áttöltik azokat az adatokat, amelyekkel a rendszer dolgozni fog és letesztelik a betöltött adatok, illetve az adatokat kezelő funkciók helyességét. 
**Módszere:**
A program adatbázisába valós adatok kerülnek betöltésre.

### 3.4 Elfogadási teszt
Az elfogadási teszt (angolul User Acceptance Test) célja a rendszer teljes funkcionalitásának vizsgálata a felhasználók szemszögéből
**Módszere:**
A teszt egy kontrol csoportal zajlik, egy külső cégen keresztül.

### 3.5 Terheléses teszt
A terheléses teszt célja a tervezett kapacitások, valamint a rendelkezésre álló növekedési potenciál meghatározása.
**Módszere:**
A próba telepítést követően egy meghívott teszt közönéggel zajlik, szimulálva egy átlagos napi használatot.

### 3.6 Biztonsági teszt (audit):
Biztonsági tesztelésre akkor van szükség, ha a rendszer szenzitív (pl. személyes vagy pénzügyi) adatokat kezel, vagy szabadon elérhető az internetről. 
**Módszere:**
A tesztett egy megbízott külső cég végzi.

### 3.7 Go live teszt
A go-live teszt egy próbaélesítés, melynek során a korábbi rendszerek továbbra is üzemelnek annak érdekében, hogy az élesítéskor keletkező problémák ne befolyásolják a normál üzemi működést.
**Módszere:**
A próba telepítés a megrendelő által választott webtárhelyen történik, a programot a jövőben üzemeltető adminisztrátorok közreműködésével.


### 3.8 Tesztelési feladatok, teszt-esetek leírása
A tesztelési feladat a következő teszt-eseteket foglalja magában:
- Fejlesztői teszt
- Prototípus (modul)

## 4 Tesztelési ütemterv, függőségek – tesztforgatókönyv

### 4.1 Tesztelési jelentés
A tesztelési jelentést a tesztkoordinátor készíti el. Ez egy részletes áttekintése a lefutott teszteknek, azok eredményeinek, státuszának és a megjegyzéseknek.
A tesztkoordinátor juttatja el a projektmenedzsernek a tesztelési jelentést. 

## 5 Tesztjegyzőkönyv
### 5.1 Tesztelési jegyzőkönyv - 1. Bejelentkezés, regisztráció funkcó tesztelése

|   |   |
|---|---|
| A teszt-eset leírás és célja:  | A bejelentkezés menüpont tesztelése |
| A tesztelt folyamat/funkció leírása:  |  A felület viselkedése hibás felhasználónév / jelszó megadása esetén, megfelelő adatok esetén illetve többszöri hibás bevitelekor, továbbá új felhasználó fiók sikeres-e regisztrálása  |
| A tesztelés előfeltételei:  |  A programnak rendelkeznie kell minimum egy dummy adatbázissal |
| A tesztelés dátuma és időpontja:  |  2020.11.25 10:25 |
| A tesztet végző személy(ek):  | Kurán Bertalan  |
| A tesztelt rendszer beállításai:  | A program specifikációjában szereplő alap beálítások  |
| A teszt-eset elvárt eredménye:  |  A specifikációban taglalt viselkedés |
| A tesztelés eredménye:  | **Megfelelt/élesíthető**  |
| Megjegyzések:  | -  |

**Tesztelést elvégezte**

|   |   |
|---|---|
|  Név: |  Kurán Bertalan |
|  Szervezeti egység/ beosztás: | Projekt manager, Test manager  |
|  Dátum: |  2020.11.25 11:15  |

### 5.2 Tesztelési jegyzőkönyv - 2. Jogosultsági szint tesztelése

|   |   |
|---|---|
| A teszt-eset leírás és célja:  | Jogosultság tesztelése |
| A tesztelt folyamat/funkció leírása:  |  Az alkalmazás Jogosultság funkció tesztelése |
| A tesztelés előfeltételei:  |  A programnak rendelkeznie kell minimum egy dummy adatbázissal |
| A tesztelés dátuma és időpontja:  |  2020.11.25 11:38 |
| A tesztadatok típusa:  | szöveg  |
| A tesztet végző személy(ek):  | Zsadányi Rózsa  |
| A tesztelt rendszer beállításai:  | A program specifikációjában szereplő alap beálítások  |
| A teszt-eset elvárt eredménye:  |  A szövegszerkesztő optimális működése |
| A tesztelés eredménye:  | **Megfelelt/élesíthető**  |
| Megjegyzések:  | -  |

**Tesztelést elvégezte**

|   |   |
|---|---|
|  Név: |  Zsadányi Rózsa |
|  Szervezeti egység/ beosztás: | Projekt manager, Test manager  |
|  Dátum: |  2020.11.25 12:15  |

### 5.3 Tesztelési jegyzőkönyv - 3. Profil szerkesztés funkció

|   |   |
|---|---|
| A teszt-eset leírás és célja:  | A felhasználó tudja módositani az adatait , kereséseti  |
| A tesztelt folyamat/funkció leírása:  | A felhasználó tudja módositani az adatait , kereséseti|
| A tesztelés előfeltételei:  |  A programnak rendelkeznie kell minimum egy dummy adatbázissal  |
| A tesztelés dátuma és időpontja:  |  2020.11.25 13:31 |
| A tesztadatok típusa:  | szöveg |
| A tesztet végző személy(ek):  | Zsadányi Rózsa  |
| A tesztelt rendszer beállításai:  | A program specifikációjában szereplő alap beálítások  |
| A teszt-eset elvárt eredménye:  |  A specifikációban taglalt viselkedés |
| A tesztelés eredménye:  | **Megfelelt/élesíthető**  |
| Megjegyzések:  | -  |

**Tesztelést elvégezte**

|   |   |
|---|---|
|  Név: |  Zsadányi Rózsa |
|  Szervezeti egység/ beosztás: | Adatbázis fejlesztő  |
|  Dátum: |  2020.11.25 13:58  |

### 5.4 Jóváhagyások

|   |   |
|---|---|
|  Név: |  Kurán Bertalan |
|  Szervezeti egység/ beosztás: | Projekt Manager  |
|  Dátum: |  2020.01.07 11:00  |

## 6 Tesztelési jelentés 

### 6.1 Tesztelési jelentés -  1. Bejelentkezés, regisztráció funkció tesztelése 
|   |   |
|---|---|
| A hivatkozott tesztjegyzőkönyvek rövid leírása és eredménye:  | "A bejentkezés és regisztráció opció lépésről lépésre tesztelésre került hibás és megfelelő adatokkal, a connection miatt nem működik megfelelően" |
| A tesztelt folyamatok/funkciók/modulok leírása: | Insert, Select |
| A tesztadatok típusa:  | String, int  |
| A tesztelt rendszer beállításai:  | A program specifikációjában szereplő alap beálítások  |
| A tesztelés eredménye:  | **élesíthető**  |
| Megjegyzések:  | BUG |

**Tesztelést elvégezte**

|   |   |
|---|---|
|  Név: |  Zsadányi Rózsa |
|  Szervezeti egység/ beosztás: | Projekt Manager  |
|  Dátum: |  2020.11.25 12:15  |
|   |   |
|  Név: |  Kurán Bertalan  |
|  Szervezeti egység/ beosztás: |  Vezető adatbázis fejlesztő |
|  Dátum: |  2020.11.25 14:36  |

### 6.2 Tesztelési jelentés - 2. Profil szerkesztés funkció
|   |   |
|---|---|
| A hivatkozott tesztjegyzőkönyvek rövid leírása és eredménye:  | "A felhasználó tudja módositani az adatait , kereséseti  " |
| A tesztelt folyamatok/funkciók/modulok leírása: | A felhasználó tudja módositani az adatait , kereséseti   |
| A tesztadatok típusa:  | szöveg  |
| A tesztelt rendszer beállításai:  | A program specifikációjában szereplő alap beálítások  |
| A tesztelés eredménye:  | **Megfelelt/élesíthető**  |
| Megjegyzések:  | -  |

**Tesztelést elvégezte**

|   |   |
|---|---|
|  Név: |  Zsadányi Rózsa |
|  Szervezeti egység/ beosztás: | Adatbázis fejlesztő  |
|  Dátum: |  2020.11.25 13:58  |

### 7 Jóváhagyások

|   |   |
|---|---|
|  Név: |  Kurán Bertalan |
|  Szervezeti egység/ beosztás: | Projekt Manager  |
|  Dátum: |  2020.11.26 11:00  |


## #1: GUI teszt:
A gui hibátlanul elindul, megnyitja a bejelentkező felületet. A textboxok működnek, a jelszó textbox titkosítva. A bejelenkezés gomb visszajelez panelváltást, de nem *vált* panelt, az elfelejtett jelszó gomb ugyanaz. A regisztrációs gomb ~120 hibát dob.

