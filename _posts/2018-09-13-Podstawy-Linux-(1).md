---
layout: post
title: Nauka Linux'a od podstaw (1)
feature-img: "assets/img/pexels/bash.png"
tags: [Linux, Unix]
---



### Tab

czyli najbardziej wytarty klawisz u każdego linuxarza :). Znam jego 2 zastosowania

1. podpowiada drugą część polecenia np. `cd ~/Doc` wciskamy `tab` i mamy `cd ~/Documents`
2. podpowiada co możemy wpisać w 2 części polecenia np.

```bash
$ cd D 		#w tym momencie wcistamy tab 2-krotnie
Documents/
Downloads/
```

### Podstawowe polecenia

* `pwd` (print working directory) - wskazuje ścieżkę do katalogu bieżącego

* `cd` (change directory) - zmienia katalog 
  * `cd ..` - zmienia katalog na jeden niżej
  * `cd ~/Documents` - zmienia katalog na `Documents` w katalogu głównym

* `ls` (list directory) - zawartość katalogu (z przełącznikiem -a -la wyświetli ukryte pliki)
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
zdjecie.jpg
zdj.png

$ ls index.*
index.html
index.js
index.css
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
plik.txt
plik.md
```

#### Usuwanie

* `rm` (remove) - usuń 
  * `rm -r`(recursive) - usunie plik/folder z zawartością (w głąb)
  * `rm -i` - zapyta przed usunięciem pliku
  * `rm -d` - usunie puste katalogi

```bash
$ rm plik
$ rm -r plik
$ rm -d katalog/
```

* `rmdir` (remove directory) - usuń katalog

  jeśli usuwany folder nie będzie pusty dostaniemy error

```bash
$ rmdir katalog/
```

#### Przenoszenie/Kopiowanie

* `cp` - skopiuj
* `mv` - przenieś

#### Łączenie

* `cat` - łączenie plików (wyświetli wynik na ekran, aby zapisać należy przekierować do pliku np. `> plik.txt`)

```bash
cat plik.txt plik2.txt > nowy_plik.txt
```

#### Procesy

* `ps` - pokaż procesy
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
$ grep '\$' Pictures/* 	<- znaku '/' znakiem 'zabiera mu funkcję' tzn. wyszukujemy tego znaku
```

### Strumienie

Umożliwiają nam przekierowanie wyniku polecenia.

` polecenie > plik` - przeadresowanie std wyjścia - wynika polecenia zostanie wysłany do pliku ( zostanie utworzony nowy plik o tej nazwie lub plik zostanie nadpisany)

`polecenie >> plik` - jak wyżej z tą różnicą, że jeśli plik istnieje to wynik polecenia zostanie dopisany na końcu pliku

### Potoki

Pozwalają łączyć polecenia.

```bash
$ history | head -5 > pierwsze_polecenia.txt	<- o poleceniach history, head niżej
$ history | grep ls > head >> ls.txt
```

### Ciekawostki

* `head i tail` - pokaż linie od początku/końca (można skorzystać z wzorców uogólniających)

```bash
$ head -20 pan_tadeusz.txt 	<- '-20' oznacza liczbę lini od początku do wyświetlenia
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

więcej o tym narzędziu poczytasz tutaj:

* `git` - rozproszony system kontroli wersji 

