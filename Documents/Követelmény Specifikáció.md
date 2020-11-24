# Követelmény Specifikáció

## Áttekintés
 Mindannyiunk számára ismert elearning weboldalra épült a mi programunk. Regisztráció segítségével a felhasználó hozzáférhet az adataihoz, tanulmányaihoz, tantárgyaihoz. Ezen a felületen egy chatet is létrehoztunk, ami eddig meg nem szokott volt a rendszerben. Itt a jelenlegi helyzet miatt jobban tudják tartani egymással a kapcsolatot a diákok. Annyi feltétellel, hogy csak azok közt működik a chat, akik egy csoportba tartoznak, egyes órákon. Csoportmunkák megvalósítását is nagyban elősegítheti ez a felület. Tanárok értesítéseket tudnak küldeni a tanítványaik felé, hiszen nekik olyan plusz engedéllyel rendelkeznek, aminek a segítségével láthatják diákjaik aktivitását az oldalon. Mennyi időt töltenek a felületen, mikre kattintottak, esetleg nem nyitották e meg zh-k közben. A rendszer azonnal kiszűri, ha valaki nem megfelelő célra használja a fórumot. A weboldal nagyban elősegíti a távoktatást.

## Jelenlegi helyzet

 Szeretnénk a felhasználók számára egy egyszerűen használható, könnyen hozzáférhető lehetőséget a rendezett információk eljuttatásához, tanár-diák között. Azoknak biztosítunk hozzáférést, akik egy intézményben tanulnak, ezt a diákigazolvány szám segítségével valósítható meg. Mindenki egy egyéni 6 karakterből álló kód segítségével juthat be a rendszerbe, és saját maga által választót jelszó segítségével. Az oktatást szeretnénk a XXI. század trendjei és technológiái segítségével fölülmúlni.
## Jelenlegi üzleti folyamatok

Mivel a mai körülmények miatt, a gimnáziumi, egyetemista, levelezős diákok nem léphetnek be az intézmény területére, így ez a lehetőség lenne a számukra a legkedvezőbb. Hiszen egyes tanárokhoz akár 200-300 diák is tartozhat, így lehetetlen lenne mindenkinek külön-külön megtartani az órát, elküldeni a tananyagot.
## Igényelt üzleti folyamatok

Tervezünk egy kezdőfelületet, amin a felhasználó egy email-ben kapott kóddal, jelszóval (amit a bejelentkezés után köteles megváltoztatni) bejelentkezhet az oldalra. Ezt követően a felhasználó átkerül a képernyőtervben látható központi felületre, ahol az egyetemisták kiválaszthatják a hozzájuk tartozó kart. A menüsorban látható lehetőségek: értesítések, beállítások, profil, chat, kurzusok. Az értesítésben láthatóak azok az üzenetek, amiket tanáraitok, intézményetek vezetője (egyes helyeken igazgató,rektor,dékán) írhatott nektek. Rájuk kattintva eltudjátok olvasni a levelet, ez visszajelzést ad a küldőnek, hogy megnézte a levelét. A beállításokban lehet megváltoztatni a jelszavukat. Minimális dizájnt is lehet egyénileg állítani. A profilban a felhasználó saját adatai jelennek meg. Mint pl.: teljes neve, lakcíme, telefonszáma, email címe, (gimnazistáknak) az osztályának a száma és betűjele, egyetemistáknak a neptun kódjuk, jelen helyzeti félévük, karjának a neve és a szaknak a neve, amire a hallgató jár.
## Vágyálom rendszer

 A projekt célja egy olyan weboldal létrehozása, ahol a tanárok könnyedén el tudják juttatni a megfelelő tananyagot. Cél egy könnyen átlátható és felhasználó barát fórum létrehozása, ahol a felhasználók a regisztráció után pár alapvető szűrés segítségével, amit a felhasználó nem észlelve belép a saját tanulmányi oldalára. Itt könnyedén megtalálják az órarendűket és a hozzájuk kapcsolódó tárgyakat. Mindegyik tantárgy külön mappába helyezkedik el. A tanárok csak a hozzájuk kapcsolódó tárgyat, és diák mappáját tudják szerkeszteni, törölni, feltölteni rá adatokat. A diákok nem jogosulnak a mappák szerkesztésére, ők csak megnyitni tudják azokat. Ezen a felületen az osztályzás is végbemegy. Amelyik diáknak tárgyon belül 5-ös az átlaga az kapjon a mappájára egy matricát.
## Funkcionális követelmények

 A felhasználó az oldal betöltése után a bejelentkező felület fogadja, ahol be tud lépni az oldalra. Bejelentkezés gombra kattintva, akkor be kell írnia a felhasználónak az egyéni 6 karakterből álló kódját, majd jelszavát. Ha sikeresen bejelentkezett, akkor máris elérhető neki minden funkció, amire van jogosultsága. Jobb sarokban megjelenik a Profil, ahol a saját adatai ellenőrizheti a felhasználó. Tőle jobbra sorakoznak fel a többi gombok. Közvetlen mellette található a beállítások gomb, ahol a jelszavát tudja majd megváltoztatni. Ezt követi a tanulmányok listája, ahol ha rákattintva felsorakoznak a diákok tantárgyai. Bármelyikre kattintva azon tárgy adatai, fognak meglenni. Mint pl.: a tanár, aki azt az órát tartja, a tananyag, hozzá tartozó feladatok, beadandók. Bal sarokban található a chat, amin a hallgatók saját szaktársaikkal, osztálytársaikkal tudnak kommunikálni.
## Fogalomtár

Reszponzív felület –-> PC-n igazodik a képernyőhöz a felület mérete, azaz különböző méretarányú és felbontású kijelzőkön is probléma nélkül megjeleníthető.

 Matrica –-> mikor a felhasználó bizonyos tárgyon belül kiemelkedően teljesített, ami azt jelenti, hogy a tanulmányi átlaga 5%-os. Ilyenkor a tantárgy hátterén egy matrica jelenik meg.

 Értesítés –-> Hallgatók és a hierarchiában felsőbb rétegben tartozók között zajlik. A felsőbb felhasználók értesítéseket, fontos híreket tudnak közölni a hallgatókkal.
 
 Feliratkozás --> A felhasználók feliratkozhatnak bejegyzésekre ami jelzi ha új hozzászólás történt.

 Szűrők --> A felhasználó szűkebb körben kereshet bejegyzéseket, hozzászólásokat. Csak azokat a felhasználókat adja ki a kereső mező, ami megfelel a beállított feltételeknek.

 Profil --> A felhasználó itt testre szabhatja saját profilképét. Készíthet rövid leírást magáról hogy jobban megismerjék.

 Feliratkozás felület --> A felhasználót értesíti az oldal ha a bejegyzésnél új hozzászólás történt, vagy szavaztak az ő által elkészitett szavazáson.

 Reszponzív felület --> Az oldal méretei automatikusan igazodnak az aktuális eszközön.
 
# Rendszerre vonatkozó törvények
## Általános Információk

A Weboldalhoz való hozzáférést és annak használatát az alkalmazandó jogszabályok és jelen Felhasználási Feltételek és Adatkezelési tájékoztatók ( a továbbiakban Felhasználási Feltételek) szabályozzák. Az alkalmazást használók ( a továbbiakban: a Felhasználók) elfogadják a jelen felhasználási feltételeket. Amennyiben ezen Felhasználási Feltételeket és az Oldal Tájékoztatóját nem fogadják e, nem jogosultak az oldal használatára.

 A jelen Felhasználási Feltétételekre a magyar jog az irányadó, tekintet nélkül a nemzetközi magánjog előírásaira. Az Alkalmazás Felhasználói kifejezetten hozzájárulnak ahhoz, hogy a jogvitákra a magyar hatóságoknak és bíróságoknak legyen kizárólagos joghatóságuk a magyar jog alapján.
## Szellemi tulajdon

Az weboldal és valamennyi kapcsolódó védjegy, szerzői jogi alkotás és egyéb – akár bejegyzett, akár be nem jegyzett – szellemi tulajdon (a továbbiakban együttesen: Szellemi Tulajdon) tulajdonosa az KRK és/vagy KRK Szolgáltató, valamint az alkalmazáshoz kedvezményt nyújtó partnerek. A Felhasználók az Alkalmazást a Szellemi Tulajdon maximális tiszteletben tartásával jogosultak használni. A Szellemi Tulajdon kiterjed különösen, de nem kizárólagosan valamennyi szoftverre, logóra, márkajelre, márkanévre, fényképre, szövegre, grafikára, adatbázisra. A Szellemi Tulajdonnak tilos bárminemű megsértése, bitorlása, másolása, átdolgozása és tilos azt bármilyen egyéb módon megsérteni, azt jogosulatlanul felhasználni, továbbadni, megterhelni, azzal bármilyen módon rendelkezni, visszaélni. Ezen szabályok megsértése az Alkalmazás használati lehetőségeinek azonnali hatályú megszüntetése mellett a megfelelő jogi lépések megtételét – beleértve esetleges büntetőjogi lépések megtételét is – vonja maga után a Felhasználóval, más jogsértő személlyel szemben a Tulajdonos és/vagy a Szellemi Tulajdon egyéb jogosultjai által.
## Használat

Az Alkalmazás Felhasználói 14 éven felüli természetes személyek lehetnek. Az Oldal díjmentesen vehető igénybe, kizárólag az oktatási rendszerben résztvevő 14-év feletti hallgatók, és azok tanárai használhatják a jelen Felhasználási Feltételek szerint.

A Felhasználási Feltételek és az Oldal működésének a módosítására, az Oldal működésének a megszüntetésére az Intézményvezető bármikor jogosult, a Felhasználó előzetes értesítése nélkül. Az Oldalon való hozzáférést az Intézményvezető bármikor visszavonhatja akár az adott Felhasználóra nézve, akár szélesebb körben vagy teljes körűen előzetes értesítés, figyelmeztetés nélkül.
## Felelősségi szabályok

Intézményvezető fenntartja magának a jogot arra, hogy amennyiben valamely Felhasználó részéről bármilyen manipulációt, tömegesen generált letöltést, illetve az Oldal szellemével bármilyen módon összeférhetetlen vagy azt sértő magatartást tapasztal, vagy ennek megalapozott gyanúja felmerül, úgy a Felhasználót azonnali hatállyal kizárja az Oldal felhasználói köréből.

Az Oldalhoz kapcsolódó adatbázis módosítása kizárólag az Üzemeltető által, illetve az Oldalt üzemeltető webkiszolgálón keresztül lehetséges. Bármilyen külső, nem az Oldal részeként elérhető eszközzel történő beavatkozás a Felhasználó azonnali kizárását eredményezi.

Ha a Felhasználó az Oldalt használat közben bezárja, vagy ha a kapcsolat (bármely okból) megszakad a kiszolgáló webhelyével, abban az esetben az adatok elvesztéséért az Intézményvezető semmilyen felelősséget nem vállal. Az Intézményvezető és az Üzemeltető a rendelkezésére álló eszközökkel biztosítja, hogy az Oldal használata technikai szempontból biztonságosnak minősüljön. Az Oldalhoz való csatlakozás miatt bekövetkező károkért, az internetes hálózat esetleges üzemkimaradásából, az elérési út hibájából, bármely nem várt technikai hibából eredő adatvesztésért, vírusból, vagy más károkért az Intézményvezető nem felelős. A Felhasználóknak minden esetben fel kell mérniük, hogy rendelkeznek-e az Oldal használatához szükséges ismeretekkel, technikai követelményekkel és teljesítményekkel.
## Technikai követelmények

Az Oldal használatához szükséges technikai feltételek: Android operációs rendszer 4.0.3 vagy későbbi verziójával ellátott mobiltelefon vagy iOS operációs rendszer 9.0 vagy későbbi verziójával ellátott mobiltelefon, valamint a használathoz megfelelő sávszélességű internetelérés. A technikai feltételeket az Oldal megnyitásához és használatához a Felhasználónak kell teljesítenie. A technikai feltételek nem teljesüléséért az Intézményvezető nem vonható felelősségre. Ugyanígy nem vonható felelősségre az Intézményvezető az Oldal használatából a készüléken bekövetkező adatvesztésért, meghibásodásért. Az Intézményvezető kizár minden kártérítési felelősséget az Oldalhoz csatlakozó minden külső szerver által nyújtott, vagy megjelenített adattal, információval kapcsolatban is.

Az Oldal megnyitás, bizonyos funkciói pedig regisztrációt követően vehetők használatba. A megjelenítés kizárólag a Google Chrome, Safari, Opera, Microsoft Edge felületén keresztül engedélyezett.

Az Oldal verziózott, a mobiltelefonon futó operációs rendszer – beállításoktól függően – rendszeresen frissíti magát. Amennyiben a Google Chrome, illetve a Safarin elérhető frissítést észlel a rendszer, az operációs rendszer automatikusan frissíti az oldalt. A Google Chrome, illetve a Sagari és az operációs rendszer működéséért az Intézményvezető semmilyen felelősséggel nem tartozik.

 Amennyiben más készüléken szándékozik megnyitni az oldalt Az új eszközön, azonban nem igényel újabb regisztrációt és a korábbi, programban tárolt információk is elérhetőek maradnak bejelentkezést követően. Mobiltelefonszám cseréjekor a Felhasználónak nincs teendője az Alkalmazással kapcsolatban.

## Regisztráció és tárolt adatok

A regisztráció csak egyféle képpen mehet végbe. Minden egyes intézményi diák, tanár egy bizonyos azonosítóval él a rendszerükbe.  Az weboldalba való bejutáshoz az Intézmények a tanulóinak, tanárainak alkot egy 6 karakterből álló kódot, amit eljuttat a felhasználójának, és egy ideiglenes jelszót, amit a felhasználó az első belépésekor megváltoztat. Így jön létre a bejelentkezés. A regisztráció során megadott adatok helyességéért a Tulajdonos, illetve az Üzemeltető semminemű felelősséget nem vállal.

 A regisztrációt követően Üzemeltető és/vagy Tulajdonos a Felhasználó részére az Weboldal működésével kapcsolatosan, különösen versenyjelentkezéssel kapcsolatos tájékoztatást, visszaigazolást, alkalmazás frissítésével kapcsolatos tájékoztató leveleket küldhet a Felhasználó e-mail címére.

Az Oldal adatbázisából előzetes értesítés nélkül törlésre kerülhet az a Felhasználó, aki az általa megosztott tartalmakkal megsérti harmadik fél személyiségi vagy egyéb jogait, valamint a szerzői jogot, bármilyen Szellemi Tulajdonnal kapcsolatos jogot vagy bármilyen egyéb jogszabály rendelkezéseit, kereskedelmi, üzleti célú hirdetéseket jelenít meg (ún. spam) formájában akár saját profiljával, akár a közösségi felületeken megosztott üzenetekkel, más Felhasználókat zaklat, megfélemlít, rágalmaz saját profiljával. Az Alkalmazás adatbázisából előzetes értesítés nélkül törlésre kerülhet az a Felhasználó is, aki az Oldal saját nevében terjeszti, részben vagy egészben másolja, átdolgozza, a Szellemi Tulajdont bármilyen egyéb módon bitorolja, másolja, azzal visszaél, jogosulatlanul használja az Oldal és az Intézményvezető védjegyeit, kárt tesz az Oldalban bármilyen módon, pl. szoftverek és távközlési berendezések segítségével a jelen Felhasználási Feltételekben foglaltakat bármilyen egyéb módon megszegi.

 Az Intézményvezető bármikor kérheti regisztrációs hiba esetén segítséget a [KRK@gmail.com](mailto:KRK@gmail.com) email címre küldött levelében.
## Értesítések

 Az Oldal használata során, a beépített üzenetküldő szolgáltatás segítségével értesítéseket kaphat a Felhasználó az Oldallal kapcsolatosan. Az oldal megnyitása követően az első lépésként az Oldal engedélyt kér a rendszerszintű értesítésekhez ezeket lemondani az oldalon lévő Beállításaiban lehetséges.
## Garancia és kártérítés

Az Oldal használatához a felhasználói oldalon szükséges – fent meghatározott vagy bármely egyéb - technikai feltételeket a Felhasználónak kell biztosítania, teljesítenie. Ezen technikai feltételek nem teljesüléséért az Intézményvezető nem vonható felelősségre. Ugyanígy nem vonható felelősségre az Intézményvezető az Oldal használatából adódóan, a készüléken bekövetkező adatvesztésért, meghibásodásért. Az Intézményvezető kizár minden kártérítési felelősséget az Oldalhoz csatlakozó minden külső szoftver által nyújtott (így kiemelten adatok átvétele) vagy megjelenített adattal, információval kapcsolatban. Az Intézményvezető nem vállal garanciát az Oldal megszakításmentes működéséért, valamint vis major hibákért. Az ebből eredő adatvesztésért, tartalom vesztésért az Intézményvezető szintén nem tartozik kártérítési felelősséggel.
## Egyéb rendelkezések

Jelen Felhasználási Feltételekben nem szabályozott kérdésekben a hatályos jogszabályok – különösen, de nem kizárólagosan a Polgári Törvénykönyvről szóló 2013. évi V. törvény, az Európai Parlament és Tanács 2016. április 27-i (EU) 2016/679. Rendelete a természetes személyeknek a személyes adatok kezelése tekintetében történő védelméről és az ilyen adatok szabad áramlásáról, valamint a 95/46/EK irányelv hatályon kívül helyezéséről, az információs önrendelkezési jogról és az információ szabadságról szóló 2011. évi CXII. törvény, a szerzői jogról szóló 1999. évi LXXVI. törvény, valamint az elektronikus kereskedelmi szolgáltatások, valamint az információs társadalommal összefüggő szolgáltatások egyes kérdéseiről szóló 2001. évi CVIII. törvény – rendelkezései az irányadóak.
## Kapcsolat

Az Oldal támogatását az Üzemeltető végzi munkanapokon, 8:00 és 16:00 között. Az Oldal működésével kapcsolatban az Intézményvezető [KRK@gmail.com](mailto:KRK@gmail.com) e-mail címre küldheti kérdéseit, amelyre az Üzemeltető a fenti időszakban válaszol. Teljes bizalommal forduljon hozzánk.
## Követelménylista

|   Modul   | ID |  Név   |  Verzió  |
|-----------|----|--------|----------|
|Jogosultság| K1 | Bejelentkezés|1.0|
|Jogosultság|K2|Regisztráció|1.0|
|Jogosultság|K3|Jogosultsági szintek|1.0|
|Modifikáció|K4|Felhasználó módosítása|1.0|
|Modifikáció|K5|Jelszó módosítása|1.0|
|Modifikáció|K6|Elfelejtett felhasználónév/jelszó|1.0|
|Statisztika|K7|Összes megtekintések|1.0|
|Felület|K8|Profil|1.0|
|Felület|K9|Témák, Bejegyzések, Hozzászólások, Szavazás|1.0|
|Jogosultság|K10|Admin felület|1.0|
|Jogosultság|K11|Moderátor felület|1.0|
|Adatbázis|K12|Adatbázis rendszer|1.0|

### Kifejtés    
#### ID
- K1  A felhasználó a "Bejelentkezés" gombbal be tud jelentkezni a megadott felhasználónév és jelszó párossal. Ha bármelyik mező hiányzik, vagy hibásan van kitöltve, az aktuális mező fölött piros betűkkel tudatja velünk.

- K2  A "Regisztráció gombra kattintva a felhasználó megadhatja az oldal használatához szükséges adatokat: "felhasználó" mezőbe egy egyedi felhasználónevet; "email" mezőbe a saját érvényes email címét; "jelszó" mezőbe egy egyedi kulcsszót, amit harmadik személynek semmiféleképpen nem adhatunk ki.
Ha bármelyik mező hiányzik, vagy hibásan van kitöltve, az aktuális mező fölött piros betűkkel tudatja velünk.

- K3  Felhasználói-Rendszerhozzáférés, like-olhat, küldhet üzenetet, tölthet fel profilképet, bemutatkozó szöveget.

- K4 A felhasználó módosítani tudja saját Felhasználónevét a saját profil beállításain belül. Ehhez szükséges a régi és az új felhasználók megadása, az új megerősítése, valamint a felhasználó jelszojának megadása. 

- K5 A felhasználó módosítani tudja saját jelszavát a saját profil beállításain belül. Ehhez szükséges a régi és az új jelszojának megadása, valamint az új megerősítése.

- K6 Ha a felhasználó elfelejtette a felhasználónevét vagy jelszavát, akkor ezzel az opcióval egy Adminhoz tud fordulni email címen keresztül.

- K7 Egy lista a bejegyzések, hozzászólásokról illetve a témákról ezekről különféle statisztika.(megtekintés, legfelkapottabb,stb...)

- K8 A felhasználónak lehetősége van a profilján található bemutatkozó szöveg módosítására.

- K9 A felhasználók hozzáférnek egy reszponzív felülethez ami témákban lévő bejegyzésekhez amikhez hozzászólhatnak illetve új bejegyzéseket hozhatnak létre, amikben szavazásokat is indithatnak, feliratkozhatnak bejegyzésekre.

- K10 Felület az admin fiókkal rendelkező felhasználó számára. Tartalmazza egyes felhasználói csoport jogok szerkesztését, bejegyzések,hozzászólások moderátori részét, új témák létrehozását.

- K11  Felület az moderátor fiókkal rendelkező felhasználó számára. Tartalmazza egyes felhasználói csoport jogok szerkesztését, bejegyzések,hozzászólások moderátori részét, új témák létrehozását.

- K12 Adatbázis kapcsolat megtervezése és létrehozása.
