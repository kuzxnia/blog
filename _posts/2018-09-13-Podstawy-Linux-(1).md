---
layout: post
title: Nauka Linux'a od podstaw (1)
feature-img: "assets/img/pexels/bash.png"
thumbnail: "assets/img/pexels/bash.png"
tags: [Linux, Unix]
comments: true
---

Linuxa używam właściwie od dawna. Zawsze podobała mi się możliwość personalizacji, brak ograniczeń, moc. Jednak dopiero za sprawą serialu Mr.Robot poczułem potrzebę nauczenia się płynnej obsługi terminala. Spodobało mi się. :)

<div style="width:100%;height:0;padding-bottom:62%;position:relative;"><iframe src="https://giphy.com/embed/UqxVRm1IaaIGk" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>

### O co chodzi z tym `Tab-em`?

**`TAB`** - czyli najbardziej wytarty klawisz u każdego linuxarza :). Znam jego 2 zastosowania

1. podpowiada drugą część polecenia np. `cd ~/Doc` wciskamy `tab` i mamy `cd ~/Documents`
2. podpowiada co możemy wpisać w 2 części polecenia np.

```bash
$ cd D 		#w tym momencie wcistamy tab 2-krotnie, i 
Documents/		Downloads/
```

### Podstawowe polecenia

* `pwd` (print working directory) - wskazuje ścieżkę do katalogu bieżącego

* `cd` (change directory) - zmienia katalog 
  * `cd ..` - zmienia katalog na jeden niżej
  * `cd ~/Documents` - zmienia katalog na `Documents` w katalogu głównym

* `ls` (list directory) - zawartość katalogu
  * `ls -a` (all) - wyświetli ukryte pliki
  * `ls -l` (long) - wyświetli w długim formacie (z pozwoleniami)

```bash
$ ls
workspace/
blog/

$ ls -a
workspace/
blog/
.themes/
.git/
.bashrc
```

dodatkowo możemy wykorzystać wzorce uogólniające (są podobne do wyrażeń regularnych), za ich pomocą jesteśmy w stanie wyświetlić np. pliki o podanym rozszerzeniu/niach itp.

Oto najbardziej podstawowe z nich: 

* `*` - zastępujemy nim ciąg znaków

* `?` - zasptępujemy nim jeden znak

* `[]` - zastępuje znak w nawiasie

* `{}` - zastępuje wybrany wyraz z nawiasu

```bash
$ ls *.{jpg,png,jpeg}
zdjecie.jpg     zdj.png     zdj.jpeg

$ ls index.*
index.html      index.js      index.css
```

### Operacje na plikach i katalogach 

#### Tworzenie

* `mkdir` (make directory) - tworzenie katalogu

```bash
$ mkdir folder
folder/
```

* `touch` - tworzenie pliku (możemy zastosować wzorzec uogólniający np. do stworzenia kilku plików z różnymi rozszerzeniami)

```bash
$ touch plik.txt
plik.txt

$ touch plik.{txt,md}
plik.txt	plik.md
```

#### Usuwanie

* `rm`(remove) - usuń 
  * `rm -r`(recursive) - usunie plik/folder z zawartością (w głąb)
  * `rm -i` - zapyta przed usunięciem pliku
  * `rm -d` - usunie puste katalogi

```bash
$ rm plik
$ rm -r plik
$ rm -d katalog/
```

* `rmdir`(remove directory) - usuń katalog

  jeśli usuwany folder nie będzie pusty dostaniemy error

```bash
$ rmdir katalog/
```

#### Przenoszenie/Kopiowanie

* `cp`(copy) - skopiuj
* `mv`(move/rename) - przenieś lub zmień nazwę

```bash
$ cp pic.jpg pic2.jpg	#stworzy kopię pliku pic.jpg
$ cp pic.jpg home/Pictures/pic.jpg		#stworzy kopię o nazwie pic.jpg w katalogu Pictures
$ mv pic.jpg home/Pictures/	#przeniesie plik do katalogu Pictures/
$ mv pic.jpg picture.jpg	#zmieni nazwę pliku
```



#### Łączenie

* `cat`(concatenate) - łączenie plików (wyświetli wynik na ekran, aby zapisać należy przekierować do pliku np. `> plik.txt`)

```bash
cat plik.txt plik2.txt > nowy_plik.txt
```

#### Procesy

* `ps` (process status)- pokaż procesy
  * `ps -f` (full) -pełne informacje o procesie
  * `ps -e` (every) -wszystkie procesy
  * `ps -ef` - połączenie dwóch powyższych 
* `kill` - zakończ proces
  * `kill -9` - spowoduje natychmiastowe zakończenie procesu (bez zapisywania zmian)

```bash
$ ps
	PID TTY			TIME CMD
10324 pts/0 	00:00:00 firefox
10329 pts/0 	00:00:00 bash
10614 pts/0 	00:00:00 ps

$ kill -9 10324

$ ps
	PID TTY			TIME CMD
10329 pts/0 	00:00:00 bash
10614 pts/0 	00:00:00 ps
```

### Wyszukiwanie

* `find` - znajdź (bez parametrów wyświetli listy plików, podkatalogów, `"."`- na początku oznacza - w bierzącym katalogu)

  **wyszukiwanie wzorcem**

  * `find -name '*.txt'` lub zaprzeczenie `find not -name '*.txt'` - wyszuka plik o rozszerzeniu `.txt` lub wyszuka pliki o rozszerzeniu innnym niż `.txt`

  **wyszukiwanie plików lub folderów**

  * `find -type f - name 'xyz*'` - wyszuka pliki (`f`  (file) - plik, `d` (directory) - folder) zaczynające się od `xyz`

* `grep` - dopasowanie do wzorca, wzór `grep 'wzorzec_tekstu' nazwa_pliku`

Po co używamy tego polecenia? Osobiście używam go do znalezienia czy w pliku są numery telefonu, adresy email itp.

```bash
$ grep 'hello' plik.txt

$ grep 'hello' plik*	#przeszuka pliki zaczynające się od 'plik'
```

Dodatkowo kilka opcji polecenia grep

`i` - NIE uwzględnia wielkości liter

`n` - dla każdego pliku zostanie wyświetlony numer lini w której znaleziono wzorzec

`I` - wyświetli nazwy plików, gdzie został znaleziony wzorzec

`v` - zaprzeczenie wzorca - wyświetli linie, które nie zawierają wzorca 

`w` - wyszukuje cały wyraz pasujący do wzorca

##### Wyrażenia regularne 

jak już na pewno zauważyłeś używamy ich przy wyszukiwaniu wzorcem ale nie tylko do tego są potrzebne programiście. Możemy ich używać do np. walidacji formularza email, sprawdzać czy użytkownik podał poprawny numer telefonu i wiele więcej.

`.` - zastępuje znak

`[abc]` - za cały nawias wstawiana jest jedna litera z nawiasu

`[a-z]` - tak jak wyżej tylko wybieramy jedną literę z zakresu `a-z`

`[^ ]` - zaprzeczenie np. `[^aA]`

`^` - początek linii

`$` - koniec linii

kilka przykładów powinno rozjaśnić

```bash
$ grep '^[0-9]' plik*
$ grep '[eE]$' plik*
$ grep '\$' Pictures/* 	#znaku '/' znakiem 'zabiera mu funkcję' tzn. wyszukujemy tego znaku
```

### Strumienie

Umożliwiają nam przekierowanie wyniku polecenia.

* `polecenie > plik` - przeadresowanie std wyjścia - wynika polecenia zostanie wysłany do pliku ( zostanie utworzony nowy plik o tej nazwie lub plik zostanie nadpisany) np. `history > plik.txt`

* `polecenie >> plik` - jak wyżej z tą różnicą, że jeśli plik istnieje to wynik polecenia zostanie dopisany na końcu pliku

* `polecenie < plik` - przekierowanie zawartości pliku do standardowego wyjścia 

### Potoki

Pozwalają łączyć polecenia.

```bash
$ history | head -5 > pierwsze_polecenia.txt	#o poleceniach history, head niżej
$ history | grep ls > head >> ls.txt
```

### Inne przydatne polecenia

* `man` - pokazuje pomoc dla polecenia np. `man ps`
* `head i tail` - pokaż linie od początku/końca (można skorzystać z wzorców uogólniających)

```bash
$ head -20 pan_tadeusz.txt 	#'-20' oznacza liczbę lini od początku do wyświetlenia
$ tail -15 pan_tadeusz.txt
$ head -12 plik[12].txt
```

* `clear` - wyczyści terminal, chociaż bardziej polecam skrót klawiszowy `ctrl` + `l`
* `history` - wyświetla polecenia wpisane do terminala
* `exit` - zamyka terminal
* `shutdown` - zamyka system

### Narzędzia

* `tree` - konsolowe narzędzie do przeglądania struktury katalogów (używamy jak polecenia `cd`)

```bash
$ tree 
$ tree pod_katalog/
```

więcej o tym narzędziu poczytasz tutaj: https://www.geeksforgeeks.org/tree-command-unixlinux/

* `git` - rozproszony system kontroli wersji używany do wersjonowania kodu. Jest to bardzo rozbudowane narzędzie, można go używać zarówno przez terminal jak i programem okienkowym (np. SmartGit). Nie długo pojawi się wpis o tym narzędziu.



Mam nadzieję, że nieco rozjaśniłem Ci jak działa konsola linux'a. Niedługo pojawi się kolejna część. Tym razem o instalowaniu pakietów, narzędzi, programów i troszeczkę o dostosowaniu środowiska pod własne preferencje.