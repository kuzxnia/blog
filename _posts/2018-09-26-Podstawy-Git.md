---
layout: post
title: Nauka Git' z poziomu terminala
feature-img: "assets/img/pexels/commit.jpeg"
thumbnail: "assets/img/pexels/commit.jpeg"
tags: [Linux, Git]
comments: true
---

### Co to ten Git?
Git to darmowy, rozproszony system kontroli wersji (`scm` - source code managment). Czyli w prostszych słowach, jest to narzędzie archiwizujące zmiany dokonywane podczas rozwoju projektu.

### Podstawy teoretyczne

* `repozytorium` - jest to przestrzeń (możesz wyobrazić to sobie jako folder na sterydach), w której umieszczamy kod. W jednym repozytorium zazwyczaj rozwijamy jeden projekt. Umożliwia ono podgląd zmian(commit'ów) jakie dany projekt przeszedł wraz z rozwojem.
* `commit` - jest to proces rejestrowania zmian do repozytorium.
* `branch` (ang. gałąź) - jest to wersja kodu. Rozgałęziamy kod, aby umożliwić pracę wielu osobom jednocześnie. Domyślnym branch'em jest `master`(powininne być na nim tylko działające wersje kodu!) **`UWAGA`** Dobrą praktyką jest tworzenie brancha do każdego zadania (task'a), aby w razie pojawienia się przeszkody była możliwość rozpoczęcia innego zadania(zmieniamy gałąź)
* `merge` - jest to proces scalania zmian (np. dwa branch'e), który może spowodować błędy (konfilikty), które należy ręcznie rozwiązać 

<div style="width:100%;height:0;padding-bottom:56%;position:relative;"><iframe src="https://giphy.com/embed/cFkiFMDg3iFoI" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>

### Co mam zainstalować, jak mam zacząć ?
Jako, że jestem fanem Linux'a, pokażę Ci alternatywne podejście do obsługi Git'a. Uważam, że jeśli zrozumiesz działanie poszczególnych poleceń, to obsługa żadnego klienta git'a nie będzie dla Ciebie problemem.

##### Zaczniemy od pobrania programu Git.
Na Linux'ie sprawa jest prosta, wystarczy w oknie terminala wspisać:
```bash
$ sudo apt-get install git
```
Aby zainstalować git'a na Windows [pobierz](https://git-scm.com/download/win) instalkę.
Asystent instalacji jest dość intuicyjny, lecz jeśli napotkałeś jakiś problem to napisz do mnie w komentarzu.

##### Kolejnym krokiem będzie założenie konta w dowolnym hostingu repozytoriów.
Osobiście polecam [Github'a](https://github.com/), jednak nie jest to najlepsze rozwiązanie jeśli nie mamy konta dla uczniów/studentów (darmowe, prywatne repozytoria), w tej sytuacji poleciłbym Ci [Bitbucket'a](https://bitbucket.org/)

##### Ostatnim krokiem będzie połączenie hostingu z naszym komputerem poprzez ssh.

W tym miejscu odeślę Cię do [dokumentacji](https://help.github.com/articles/connecting-to-github-with-ssh/).

### Ok. Wszystko już mam, od czego zaczynamy?
Na początku zajmiemy się konfiguracją, potem pokażę Ci sposób użycia poszczególnych poleceń. Wisienką na torcie będą aliasy, czyli sposób na przyspieszenie pracy z tym narzędziem.

##### Podstawowa konfiguracja
Wystarczy nam ustawienie adresu email i nazwy użytkownika (widoczne będą w autorze commit'a). Możemy to zrobić w następujący sposób.
```bash
$ git config --global user.name "moja_nazwa"
$ git config --global user.email "moj_email"
```
Warto sprawdzić czy dane zostały ustawione poprawnie, możemy zrobić to następującym poleceniem:
```bash
$ git config --global user.name
moja_nazwa
```

##### Tworzenie projektu
* `git init <nazwa_repozytorium>` - tworzy repozytorium
* `git clone <ssh/http>` - pobiera repozytorium do katalogu bierzącego

##### Podstawowe polecenia
* `git add <plik>` - dodaje zmiany do zatwierdzenia

    * `git add .` - dodaje wyszystkie zmiany do zatwierdzenia
* `git commit` - zatwiedza zmiany (zostajesz przekierowany do edytora konsolowego aby podać tytuł commita)
    * `git commit -m "tytuł_commita"` - zatwierdza zmiany (widomość podajemy w tej samej linii)
    ```bash
    $ git commit -m "my first ever commit <3"
    ```
* `git status` - pokazuje zmodyfikowane/dodane/usunięte pliki

    * `git status -sb` - czytelniejsza forma


![linux_status]({{ site.baseurl }}/assets/img/pexels/linux/linux_status.png)

* `git log` - pokazuje listę commitów
    * `git log --oneline` - czytelniejsza forma

![linux_status]({{ site.baseurl }}/assets/img/pexels/linux/linux_log.png)

* `git clean` - czyszczenie nieśledzonych plików i pustych folderów
  * `git clean -n` - wypisze co usunie
  * `git clean -fd` - usunie pliki i foldery 
* `git reset` - cofa zmiany (commit'y)
  * `git reset --mixed` - cofa commit, a zmienione pliki pozostają w drzewie projektu
  * `git reset --hard` - cofa commit, i usuwa trwale poczynione zmiany
* `git revert` - tworzy commit cofający zmianę

![linux_status]({{ site.baseurl }}/assets/img/pexels/linux/linux_revert.png)

* `git rm <nazwa_pliku>` - jest to właściwie odwrotność `git add`, mianowicie polecenie wyłącza śledzenie pliku (nie będzie go w repozytorium)

##### Operacje na gałęziach
* `git branch` - pokazuje listę lokalnych gałęzi 
  * `git branch -v` - lista lokalnych gałęzi + tytuł ostatniego commita
  * `git branch -a` - lista wszystkich gałęzi
  * `git branch -d` - bezpieczne usuwanie
  * `git branch -D <nazwa_gałęzi>` - usuwanie z 'forcem' (np. z niezatwierdzonymi zmianami)

![linux_status]({{ site.baseurl }}/assets/img/pexels/linux/linux_branch.png)

* `git checkout <nazwa_gałęzi>` - przenosi na gałąź o podanej nazwie

  * `git checkout -b <nazwa_gałęzi>` - tworzy nowy branch jako kopia aktywnego

* `git merge <nazwa_gałęzi>` - scala gałąź o podanej nazwie do gałęzi bieżącej 

  * `git merge -no-ff <nazwa_gałęzi>` - scala i tworzy dodatkowy commit o mergowaniu (tzn. no fast forward)



Jako, że samo scalanie branch'y nie jest skomplikowane, o tyle rozwiązywanie konfliktów nie jest aż tak intuicyjne. To jest jedyny moment w którym nie używam terminala, ponieważ nie jest to ani wydajne, ani wygodne.

  ```bash
  $ git merge fastfix_1
  ```

następnie mamy konflikt o czym informuje nas monit w terminalu 

  ![linux_status]({{ site.baseurl }}/assets/img/pexels/linux/linux_merge_monit.png)

do rozwiązania używamy narzędzia tzw. `mergetool` w moim przypadku jest to plugin w Intellij IDEA, ale jest dużo podobnych. [poradnik](https://gist.github.com/karenyyng/f19ff75c60f18b4b8149)



Zaczynamy od otwarcia pliku z konfliktem, po czym klikamy PPM i `resolve conflict` wybieramy konflikt, w tym przypadku mamy jeden (jeśli było więcej plików edytowanych może być więcej)

  ![linux_status]({{ site.baseurl }}/assets/img/pexels/linux/linux_merge_c1.png)

Ukazuje sie nam następujące okno, musimy wybrać kod z którego brancha jest poprawny, możemy to zrobić poprzez kliknięcie zielonej strzałki.

  ![linux_status]({{ site.baseurl }}/assets/img/pexels/linux/linux_merge_c2.png)

 Po wybraniu otrzymujemy coś takiego, pozostał nam jedynie commit dokumentujący merge.

  ![linux_status]({{ site.baseurl }}/assets/img/pexels/linux/linux_merge_c3.png)

Oczywiście konflikty mogą być inne. Czasami występują sytuacje, w których bez ręcznej edycji pliku się nie obejdzie, ale zakaładam, że wiesz już jak to zrobić.

* `git stash` - zapisuje zmiany do stosu (czyści zmiany), nie zapisuje nowych plików tylko modyfikacje
  * `git stash pop` - cofa do drzewa projektu

  * `git stash -u` - dodaje wszystkie pliki do stosu

  * `git stash save` - zapisuje stos `dobrą praktyką jest wiadomość przy zapisywaniu stosu`

  * `git stash list` - lista stosów

  * `git stash drop stash@{1}` - usuwa stos pierwszy

  * `git stash clean` - usuwa wszystkie stosy


##### Repozytorium zdalne
* `git remote` - adres zdalnego repozytorium 
  * `git remote -v` - lista zdalnych repozytoriów
  * `git remote add` - dodaje adres zdalnego repozytorium 
  * `git remote rm <nazwa>` - usuwa adres repozytorium zdalnego
  * `git remote rename <stara_nazwa> <nowa_nazwa>` - zmienia nazwę
* `git pull` - pobiera zmiany z repozytorium zdalnego i dodaje do aktywnego brancha
* `git fetch` - pobiera zmiany z repozytorium zdalnego do nowego brancha, czyli  `pull` = `fetch` + `merge`
* `git push` - wypycha zmiany lokalne do repozytorium zdalnego

#### Aliasy - czyli sposób na automatyzacje
Na koniec zostało nam omówienie sposobu na przyspieszenie pracy z git'em. **`UWAGA`** Nie polecam używania aliasów na początku nauki, ponieważ to może spowodować, że nie będziesz znał poleceń tylko ich skróty

A teraz do konkretów. Aliasy to bardzo proste narzędzie wbudowane w git'a.
Wystarczy w oknie terminala wpisać `git config --global -e` i dodawać własne aliasy w postaci `<nazwa> = <polecenie>` (np. `lg = log --oneline`),. Użycie jest intuicyjne, wywołanie powyższego polecenia robimy następująco `git lg`.



Mam dla Ciebie bonus, otóż pod [tym](https://gist.github.com/kuzxnia/83ee25bd0ce81753dcec3bc642e22fbf) linkem, możesz znaleźć aliasy które używam sam.



W kolejniej części postaram się pokazać Ci czym jest `git flow`, czyli o produkcyjnym podejściu do git'a.