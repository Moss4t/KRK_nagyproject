# Funkcionális Specifikáció

## Áttekintés
A weblapunk lényege hogy közösséget formáljon a fórum használata által. A fórummal szeretnénk megtalálni azokat a személyeket akik erre vevők. 
A fórum használata ingyenes viszont regisztrációhoz kötött.
Felhasználók böngészhetnek a témák között és ha regisztrálnak az oldalra akkor bejegyzéseket hozhatnak létre illetve hozzászólhatnak témákhoz, bejegyzésekhez, segithetnek másoknak, segitséget kérhetnek másoktól, információt oszthatnak meg másokkal illetve véleményt formálhatnak ésszerűkeretek között. 
A fórum moderátorok által felügyelve lesz ezzel segitve a felhasználókat illetve az adminisztrátorokat.
Bizunk benne hogy a fórumon egy jó közösség alakul ki akik összetartanak.

## Jelenlegi helyzet
A jelenlegi helyzetet adódóan 	megnőtt az internetezők száma és megnőtt az érdeklődési ráta fórumok felé ezért szeretnénk ehhez lehetőséget nyújtani hogy könnyen és egyszerűen használható fórum felületet biztositsunk a közösséghez csatlakozó személyek számára. Az emberek többsége hamar be tud csatlakozni egy ilyen online közösségébe és reméljük ez itt is igy fog alakulni és egy nagyon jó közösség fog ki alakulni.

## Jelenlegi üzleti folyamatok modellje

A mai világban ahol már mindent összeköt az internet és sokkal könnyebben tarthatjuk a kapcsolatot meglévő ismerősökkel , barátokkal. A közösség formálás egy fontos dolog ezért probálunk ebben segiteni.
Szeretnénk azt elérni hogy egy jó közösség alakuljon ki ezzel segitve egymást. Illetve segiteni akarjuk azokat a felhasználókat akik sokat keresnek dolgok után az interneten azzal hogy a közösségben többféle embertől tud véleményt kikérni. Reméljük hogy az országban egy kis online közösséget tudunk alkotni és bőviteni ezt. 

## Igényelt üzleti folyamatok modellje

Azért hogy egyszerűbbé tegyük közösség formálodását létrehoztuk egy weblapot ami a mai kornak megfelelően helyt tud állni az elektronikai világban. Felhasználóinknak így egyszerűbb lesz bármiről információt megosztani, valamint segiteni másokon vagy segitséget kérni. Ismerkedésre nyitott személyek számára megfelelő hely ebben biztosak vagyunk. Eddigi ismeretlen dolgokról való információ szerzés egy fontos pontja a fórumnak. A legfontosabb pedig az információ csere.

## Használati esetek
**Admin**: Az Admin elérheti az összes, minden más felhasználó által elérhető funkciót, hogy azok hibamentes működését ellenőrizhesse. Az Admin(ok) feladata a rendszer problémamentes működtetése. Ez egyben jár azzal, hogy az egész rendszerhez van hozzáférésük. Az Admin(ok-nak hozzá kell tudni férniük a felhasználók listájához, ahol mindent láthatnak és módosíthatnak egy felhasználó profilján. Tudniuk kell a felhasználók jogosultságait, szerepkörét, jelszavát, és felhasználónevét módosítani. Továbbá képesnek kell lenniük arra, hogy felhasználókat vegyenek fel rendszerbe és, amennyiben a felhasználó nem tartja be a felhasználási feltételeket, hogy eltávolítsák őket.
**Moderátor**: A Moderátor hasonló az adminhoz viszont kevesebb joggal rendelkezik, segiti az admin munkáját abban hogy a moderálja a fórumon történő hozzászólásokat, bejegyzéseket. Segit az oldalon megtalálható hibák feltárásában, javitásában.	
**Felhasználó**: A Felhasználó bejelentkezés után eléri saját profilját, és azok profiljának publikus részét akik regisztráltak. Továbbá képes a témákba belépni és ott bejegyzéseket létrehozni, szavazásokat inditani, hozzászólni bejegyzésekhez. A User(ek)nek hozzá kell férniük saját profiljukhoz, amin módosítani kell tudniuk saját személyes adataikat (Felhasználó, jelszó, e-mail), és meg kell tudni jelölniük azokat privátnak vagy publikusnak. Meg kell tudniuk változtatni jelszavukat biztonsági okokból. Keresést tudnak inditani "szürők" alapján.
**Vendég**: A Vendég olvashatja a témákban lévő bejegyzéseket,hozzászólásokat több joga/elérhetősége nincs.

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

## Fogalomszótár
	- Feliratkozás: A felhasználók feliratkozhatnak bejegyzésekre ami jelzi ha új hozzászólás történt.

	- Szűrők: A felhasználó szűkebb körben kereshet bejegyzéseket, hozzászólásokat. Csak azokat a felhasználókat adja ki a kereső mező, ami megfelel a beállított feltételeknek.

	- Profil: A felhasználó itt testre szabhatja saját profilképét. Készíthet rövid leírást magáról hogy jobban megismerjék.

	- Feliratkozás felület: A felhasználót értesíti az oldal ha a bejegyzésnél új hozzászólás történt, vagy szavaztak az ő által elkészitett szavazáson.

	- Reszponzív felület: Az oldal méretei automatikusan igazodnak az aktuális eszközön.