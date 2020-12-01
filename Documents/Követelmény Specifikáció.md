# Követelmény Specifikáció

## Áttekintés
 Mindannyiunk számára ismert e-learning weboldalra épült a mi programunk. Regisztráció segítségével a felhasználó hozzáférhet az adataihoz, tanulmányaihoz, tantárgyaihoz. Ezen a felületen egy chatet is létrehoztunk, aminek a használata eddig nem volt megszokott a rendszerben. Itt a jelenlegi vírushelyzet miatt jobban tudják tartani egymással a kapcsolatot a diákok. Azzal a feltétellel, hogy csak azok között működik a chat, akik egy csoportba tartoznak az egyes órákon. A csoportmunkák megvalósítását is nagyban elősegítheti ez a felület. A tanárok értesítéseket tudnak küldeni tanítványaiknak, hiszen ők olyan plusz engedéllyel rendelkeznek, aminek a segítségével láthatják diákjaik aktivitását az oldalon. Figyelemmel kísérhetik, hogy mennyi időt töltenek a felületen, mikre kattintottak, esetleg nem nyitották-e meg zh-k közben a nem engedélyezett oldalakat. A rendszer azonnal kiszűri, ha valaki nem megfelelő célra használja a fórumot. A weboldal nagyban elősegíti a távoktatást.

## Jelenlegi helyzet

 Szeretnénk a felhasználók számára egy egyszerűen használható, könnyen hozzáférhető felületet biztosítani tanár és diák között, amin keresztül a rendezett információk eljutnak bármelyik félhez. Azoknak biztosítunk hozzáférést akik egy intézményben tanulnak, ez a tanulói azonosító szám segítségével állapítható meg. Mindenki egy egyéni, 6 karakterből álló kód, és a saját maga által választott jelszó segítségével juthat be a rendszerbe. Az oktatás színvonalát szeretnénk emelni és támogatni a XXI. század trendjeinek és technológiáinak segítségével.
 
## Jelenlegi üzleti folyamatok

A jelenleg érvényben lévő veszélyhelyzeti kormányzati intézkedések miatt a gimnáziumi, egyetemista és levelezős diákok nem léphetnek be az intézmény területére, így az általunk biztosított lehetőség lenne számukra a legkedvezőbb csatorna, amin keresztül tartani tudják a kapcsolatot, az intézménnyel, és a tanárokkal. Mivel egy tanárhoz akár 200-300 diák is tartozhat, így lehetetlen lenne mindenkinek külön-külön megtartani az órát, elküldeni a tananyagot.

## Igényelt üzleti folyamatok

Tervezünk egy kezdőfelületet, amin a felhasználó egy email-ben kapott kóddal, jelszóval (amit a bejelentkezés után köteles megváltoztatni) bejelentkezhet az oldalra. Ezt követően a felhasználó átkerül a képernyőtervben látható központi felületre, ahol az egyetemisták kiválaszthatják a hozzájuk tartozó kart. A menüsorban látható lehetőségek: értesítések, beállítások, profil, chat, kurzusok. Az értesítésben láthatók azok az üzenetek, amiket a tanárok, az intézmény vezetője (egyes helyeken igazgató, rektor, dékán) írhatott a diákoknak. Az üzenetre kattintva lehet elolvasni a levelet, ez automatikusan visszajelzést ad a küldőnek, hogy olvasták a levelét. A beállításokban van lehetőség megváltoztatni a jelszót. Minimális dizájnt is lehet egyénileg állítani. A profilban a felhasználó saját adatai jelennek meg (teljes név, lakcím, telefonszám, e-mail cím, gimnazisták esetében az osztály száma és betűjele, egyetemistáknál a Neptun-kód, jelenleg aktív félév, a szak és a kar neve, amire a hallgató jár.

## Vágyálom rendszer

 A projekt célja egy olyan weboldal létrehozása, ahol a tanárok könnyedén el tudják juttatni a megfelelő tananyagot diákjaiknak. A cél egy könnyen átlátható és felhasználóbarát fórum létrehozása, ahol a felhasználók a regisztráció után belépnek a saját tanulmányi oldalukra, amit a háttérben, általuk nem tapasztalható módon pár alapvető szűrés segítségével állítunk be. Itt könnyedén megtalálják az órarendjüket és a felvett tárgyakat. Minden tantárgy külön mappában helyezkedik el.
A tanárok csak az általuk tanított tárgyat, annak dokumentumait tudják szerkeszteni, törölni, illetve arra adatokat feltölteni. A diák láthatja a tantárgy mappáját. A diákok nem jogosulnak a mappák szerkesztésére, ők csak megnyitni tudják azokat. Ezen a felületen történik az osztályzás is. Amelyik diáknak az adott tárgyból 5-ös az átlaga, az kap egy "kitűzőt" a mappájára.

## Funkcionális követelmények

 A felhasználót az oldal betöltésekor a bejelentkező felület fogadja, amin keresztül be tud lépni az oldalra. A bejelentkezéshez a "Bejelentkezés" gombra kattintva be kell írnia az egyéni, 6 karakterből álló kódját, majd jelszavát. Ha sikeresen bejelentkezett, akkor számára elérhető minden funkció, amire jogosultsága van. A jobb felső sarokban a felhasználó név alatt legördülő menüben jelenik meg a "Profil", ahol a saját adatai ellenőrizheti a felhasználó. Ez alatt találhatóak a további lehetőségek: "Beállítások", ahol többek között a jelszavát is meg tudja majd változtatni. Ebből a menüből érhető el az üzenet, a blog és a kitűző is.
 Az egyéni kódjával egy sorban, a bal oldalon található a "Kurzusaim" legördülő menü. Ebben található a tanulmányok listája, ahol rákattintva felsorakoznak a felhasználó tantárgyai. Kiválasztva az adott kurzust, annak minden paramétere megjelenik: a tanár, aki azt az órát tartja, a tananyag, a hozzá tartozó feladatok, a beadandók, a kurzus résztvevői. Bal sarokban található a chat, amin a hallgatók saját szaktársaikkal, osztálytársaikkal tudnak kommunikálni.
 
## Fogalomtár

Reszponzív felület –-> PC-n igazodik a képernyőhöz a felület mérete, azaz különböző méretarányú és felbontású kijelzőkön is probléma nélkül megjeleníthető.

 Kitűző –-> Amikor a hallgató egy bizonyos tárgyon belül kiemelkedően teljesített (tanulmányi átlaga eléri az 5-öst), a tantárgy hátterén egy kitűző jelenik meg.

 Értesítés –-> A hallgatóknak címzett értesítések, fontos hírek, melyeket a tanárok, az intézmény vezető, vagy a felső vezetés tagjai küldenek.
 
 Feliratkozás --> A felhasználók feliratkozhatnak bejegyzésekre, amiknél kommenteltek, vagy megjelölték. Jelzi, ha új hozzászólás történt.

 Szűrők --> Segítségükkel a felhasználó szűkebb körben kereshet bejegyzéseket, hozzászólásokat, melyekből csak azokat adja ki a kereső mező, amik megfelelnek a beállított feltételeknek.

 Profil --> A felhasználó itt testre szabhatja saját profilképét, készíthet rövid leírást magáról, hogy jobban megismerjék.

 Feliratkozás felület --> A felhasználót értesíti az oldal, ha a bejegyzésnél új hozzászólás történt, vagy szavaztak az általa készített szavazáson.
 
# Rendszerre vonatkozó törvények
## Általános Információk

A Weboldalhoz való hozzáférést és annak használatát az alkalmazandó jogszabályok és jelen Felhasználási Feltételek és Adatkezelési tájékoztatók (a továbbiakban Felhasználási Feltételek) szabályozzák. Az alkalmazást használók (a továbbiakban: a Felhasználók) elfogadják a jelen felhasználási feltételeket. Amennyiben ezen Felhasználási Feltételeket és az Oldal Tájékoztatóját nem fogadják el, abban az esetben nem jogosultak az oldal használatára.

 A jelen Felhasználási Feltételekre vonatkozóan a magyar jog az irányadó, tekintet nélkül a nemzetközi magánjog előírásaira. Az Alkalmazás Felhasználói kifejezetten hozzájárulnak ahhoz, hogy jogvita esetén a magyar hatóságoknak és bíróságoknak kizárólagos joghatóságuk van a magyar jog alapján.

## Szellemi tulajdon

Az weboldal és valamennyi kapcsolódó védjegy, szerzői jogi alkotás és egyéb – akár bejegyzett, akár be nem jegyzett – szellemi tulajdon (a továbbiakban együttesen: Szellemi Tulajdon) tulajdonosa az KRK és/vagy KRK Szolgáltató, valamint az alkalmazáshoz kedvezményt nyújtó partnerek. A Felhasználók az Alkalmazást a Szellemi Tulajdon maximális tiszteletben tartásával jogosultak használni. A Szellemi Tulajdon kiterjed különösen, de nem kizárólagosan valamennyi szoftverre, logóra, márkajelre, márkanévre, fényképre, szövegre, grafikára, adatbázisra. A Szellemi Tulajdonnak tilos bárminemű megsértése, bitorlása, másolása, átdolgozása, és tilos azt bármilyen egyéb módon megsérteni, azt jogosulatlanul felhasználni, továbbadni, megterhelni, azzal bármilyen módon rendelkezni, visszaélni. Ezen szabályok megsértése az Alkalmazás használati lehetőségeinek azonnali hatályú megszüntetése mellett a megfelelő jogi lépések megtételét – beleértve esetleges büntetőjogi lépések megtételét is – vonja maga után a Felhasználóval, más jogsértő személlyel szemben a Tulajdonos és/vagy a Szellemi Tulajdon egyéb jogosultjai által.

## Használat

Az Alkalmazás Felhasználói 14 éven felüli természetes személyek lehetnek. Az Oldal díjmentesen vehető igénybe, kizárólag az oktatási rendszerben résztvevő 14-év feletti hallgatók, és azok tanárai, illetve a felsőbb jogosultsági körrel rendelkezők használhatják a jelen Felhasználási Feltételek szerint.

A Felhasználási Feltételek és az Oldal működésének a módosítására, az Oldal működésének a megszüntetésére az Intézményvezető bármikor jogosult, a Felhasználó előzetes értesítése nélkül. Az Oldalon való hozzáférést az Intézményvezető bármikor visszavonhatja akár az adott Felhasználóra nézve, akár szélesebb körben vagy teljes körűen előzetes értesítés, figyelmeztetés nélkül.

## Felelősségi szabályok

Intézményvezető fenntartja magának a jogot arra, hogy amennyiben valamely Felhasználó részéről bármilyen manipulációt, tömegesen generált letöltést, illetve az Oldal szellemével bármilyen módon összeférhetetlen, vagy azt sértő magatartást tapasztal, vagy ennek megalapozott gyanúja felmerül, úgy a Felhasználót azonnali hatállyal kizárja az Oldal felhasználói köréből.

Az Oldalhoz kapcsolódó adatbázis módosítása kizárólag az Üzemeltető által, illetve az Oldalt üzemeltető webkiszolgálón keresztül lehetséges. Bármilyen külső, nem az Oldal részeként elérhető eszközzel történő beavatkozás a Felhasználó azonnali kizárását eredményezi.

Ha a Felhasználó az Oldalt használat közben bezárja, vagy ha a kapcsolat (bármely okból) megszakad a kiszolgáló webhelyével, abban az esetben az adatok elvesztéséért az Intézményvezető/Üzemeltető semmilyen felelősséget nem vállal. Az Intézményvezető és az Üzemeltető a rendelkezésére álló eszközökkel biztosítja, hogy az Oldal használata technikai szempontból biztonságosnak minősüljön. Az Oldalhoz való csatlakozás miatt bekövetkező károkért, az internetes hálózat esetleges üzemkimaradásából, az elérési út hibájából, bármely nem várt technikai hibából eredő adatvesztésért, vírus által okozott, vagy más károkért az Intézményvezető nem felelős. A Felhasználóknak minden esetben fel kell mérniük, hogy rendelkeznek-e az Oldal használatához szükséges ismeretekkel, technikai követelményekkel.

## Technikai követelmények

Az Oldal használatához szükséges technikai feltételek: Android operációs rendszer 4.0.3, vagy későbbi verziójával ellátott mobiltelefon, vagy iOS operációs rendszer 9.0, vagy későbbi verziójával ellátott mobiltelefon, valamint a használathoz megfelelő sávszélességű internetelérés. A technikai feltételeket az Oldal megnyitásához és használatához a Felhasználónak kell teljesítenie. A technikai feltételek nem teljesüléséért az Intézményvezető nem vonható felelősségre. Ugyanígy nem vonható felelősségre az Intézményvezető az Oldal használatából a készüléken bekövetkező adatvesztésért, meghibásodásért. Az Intézményvezető kizár minden kártérítési felelősséget az Oldalhoz csatlakozó minden külső szerver által nyújtott, vagy megjelenített adattal, információval kapcsolatban is.

Az Oldal bizonyos funkciói csak regisztrációt követően vehetők használatba. A megjelenítés kizárólag a Google Chrome, Safari, Opera, Microsoft Edge felületén keresztül támogatott.

Az Oldal verziózott, a mobiltelefonon futó operációs rendszer – beállításoktól függően – rendszeresen frissíti magát. Amennyiben a Google Chrome, illetve a Safarin elérhető frissítést észlel a rendszer, az operációs rendszer automatikusan frissíti az oldalt. A Google Chrome, illetve a Safari és az operációs rendszer működéséért az Intézményvezető/Üzemeltető semmilyen felelősséggel nem tartozik.

Amennyiben más készüléken szándékozik megnyitni az oldalt az új eszközön nem igényel újabb regisztrációt és a korábbi, programban tárolt információk is elérhetőek maradnak bejelentkezést követően. Mobiltelefonszám cseréjekor a Felhasználónak nincs teendője az Alkalmazással kapcsolatban.

## Regisztráció és tárolt adatok

Regisztrálni csak egyféleképpen lehet. Minden hallgató, vagy tanár egy bizonyos azonosítóval van regisztrálva a rendszerben. A weboldalhoz való csatlakozáshoz szükséges egy 6 karakterből álló kód és egy jelszó, amit a rendszer eljuttat a felhasználónak. Ezt az ideiglenes jelszót a felhasználó az első belépéskor meg kell változtasson. Így jön létre a bejelentkezés. A regisztráció során megadott adatok helyességéért a Tulajdonos, illetve az Üzemeltető semminemű felelősséget nem vállal/azok valódiságát nem ellenőrzi.

A regisztrációt követően Üzemeltető és/vagy Tulajdonos a Felhasználó részére az Weboldal működésével kapcsolatosan, különösen versenyjelentkezéssel kapcsolatos tájékoztatást, visszaigazolást, alkalmazás frissítésével kapcsolatos tájékoztató leveleket küldhet a Felhasználó e-mail címére.

Az Oldal adatbázisából előzetes értesítés nélkül törlésre kerülhet az a Felhasználó, aki az általa megosztott tartalmakkal megsérti harmadik fél személyiségi vagy egyéb jogait, valamint a szerzői jogot, bármilyen Szellemi Tulajdonnal kapcsolatos jogot, vagy bármilyen egyéb jogszabály rendelkezéseit, illetve aki kereskedelmi, üzleti célú hirdetéseket jelenít meg (ún. spam formájában). Akár saját profiljával, akár a közösségi felületeken megosztott üzenetekkel más Felhasználókat zaklat, megfélemlít, rágalmaz törlésre kerül. Az Alkalmazás adatbázisából előzetes értesítés nélkül törlésre kerülhet az a Felhasználó is: aki az Oldalt saját nevében terjeszti, részben vagy egészben másolja, átdolgozza, a Szellemi Tulajdont bármilyen egyéb módon bitorolja, azzal visszaél, jogosulatlanul használja az Oldal és az Intézményvezető védjegyeit, kárt tesz az Oldalban bármilyen módon, pl. szoftverek és távközlési berendezések segítségével a jelen Felhasználási Feltételekben foglaltakat bármilyen egyéb módon megszegi.

A Felhasználó regisztrációs hiba esetén bármikor kérhet segítséget a [KRK@gmail.com](mailto:KRK@gmail.com) e-mail címre küldött levelében.

## Értesítések

Az Oldal használata során, a beépített üzenetküldő szolgáltatás segítségével értesítéseket kaphat a Felhasználó az Oldallal kapcsolatosan. Az oldal megnyitását követően első lépésként az Oldal engedélyt kér a rendszerszintű értesítésekhez, ezeket lemondani az oldalon lévő "Beállítások"-ban lehetséges.

## Garancia és kártérítés

Az Oldal használatához a felhasználói oldalon szükséges – fent meghatározott, vagy bármely egyéb - technikai feltételeket a Felhasználónak kell biztosítania, teljesítenie. Ezen technikai feltételek nem teljesüléséért az Intézményvezető nem vonható felelősségre. Ugyanígy nem vonható felelősségre az Intézményvezető az Oldal használatából adódóan a készüléken bekövetkező adatvesztésért, meghibásodásért. Az Intézményvezető kizár minden kártérítési felelősséget az Oldalhoz csatlakozó minden külső szoftver által nyújtott (így kiemelten az adatok átvétele) vagy megjelenített adattal, információval kapcsolatban. Az Intézményvezető nem vállal garanciát az Oldal megszakításmentes működéséért, valamint vis major hibákért. Az ebből eredő adatvesztésért, tartalom vesztésért az Intézményvezető szintén nem tartozik kártérítési felelősséggel.

## Egyéb rendelkezések

Jelen Felhasználási Feltételekben nem szabályozott kérdésekben a hatályos jogszabályok – különösen, de nem kizárólagosan a Polgári Törvénykönyvről szóló 2013. évi V. törvény, az Európai Parlament és Tanács 2016. április 27-i (EU) 2016/679. Rendelete a természetes személyeknek a személyes adatok kezelése tekintetében történő védelméről és az ilyen adatok szabad áramlásáról, valamint a 95/46/EK irányelv hatályon kívül helyezéséről, az információs önrendelkezési jogról és az információ szabadságról szóló 2011. évi CXII. törvény, a szerzői jogról szóló 1999. évi LXXVI. törvény, valamint az elektronikus kereskedelmi szolgáltatások, valamint az információs társadalommal összefüggő szolgáltatások egyes kérdéseiről szóló 2001. évi CVIII. törvény – rendelkezései az irányadóak.

## Kapcsolat

Az Oldal támogatását az Üzemeltető végzi munkanapokon, 8:00 és 16:00 között. Az Oldal működésével kapcsolatban a Felhasználó a [KRK@gmail.com](mailto:KRK@gmail.com) e-mail címre küldheti kérdéseit, amelyre az Üzemeltető a fenti időszakban válaszol. Forduljon hozzánk teljes bizalommal.

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
- K1  A felhasználó a "Bejelentkezés" gombbal be tud jelentkezni a megadott felhasználónév és jelszó párossal. Ha bármelyik mező hiányzik, vagy hibásan van kitöltve, az aktuális mező fölött piros betűkkel tudatja velünk a rendszer.

- K2  A "Regisztráció" gombra kattintva a felhasználó megadhatja az oldal használatához szükséges adatokat: "Felhasználó" mezőbe egy egyedi felhasználónevet; "e-mail" mezőbe a saját érvényes e-mail címét; "Jelszó" mezőbe egy egyedi kulcsszót, amit harmadik személynek semmiféleképpen nem adhatunk ki.
Ha bármelyik mező hiányzik, vagy hibásan van kitöltve, az aktuális mező fölött piros betűkkel tudatja velünk a rendszer.

- K3  Felhasználói-Rendszerhozzáférés, like-olhat, küldhet üzenetet, tölthet fel profilképet, bemutatkozó szöveget.

- K4 A felhasználó módosítani tudja saját Felhasználónevét a saját profil beállításain belül. Ehhez szükséges a régi és az új felhasználó név megadása, az új megerősítése, valamint a felhasználó jelszavának megadása.

- K5 A felhasználó módosítani tudja saját jelszavát a saját profil beállításain belül. Ehhez szükséges a régi és az új jelszavának megadása, valamint az új megerősítése.

- K6 Ha a felhasználó elfelejtette a felhasználónevét vagy jelszavát, akkor ezzel az opcióval egy Adminhoz tud fordulni e-mail címen keresztül.

- K7 Egy lista a bejegyzésekről, hozzászólásokról, illetve témákról, valamint ezekről különféle statisztikák. (megtekintés, legfelkapottabb, stb.)

- K8 A felhasználónak lehetősége van a profilján található bemutatkozó szöveg módosítására.

- K9 Ez egy reszponzív felület, amin keresztül a felhasználók hozzáférhetnek a témákban lévő bejegyzésekhez, hozzászólhatnak, illetve új bejegyzéseket hozhatnak létre, feliratkozhatnak bejegyzésekre, valamint szavazásokat is indíthatnak.

- K10 Ez egy felület az admin fiókkal rendelkező felhasználók számára. Tartalmazza az egyes felhasználói csoportok jogainak szerkesztését, bejegyzések, hozzászólások moderátori jelzését, új témák létrehozását.

- K11 Ez egy felület a moderátor fiókkal rendelkező felhasználók számára. Tartalmazza az egyes felhasználói csoportok jogainak szerkesztését, bejegyzések, hozzászólások moderálási jogait, új témák létrehozását.

- K12 Adatbázis kapcsolat megtervezése és létrehozása.
