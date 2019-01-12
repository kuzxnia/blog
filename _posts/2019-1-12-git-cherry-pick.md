---
layout: post
title: git cherry-pick
feature-img: "assets/img/commit.jpeg"
thumbnail: "assets/img/commit.jpeg"
tags: [Linux, Git]
comments: true
---

Mam dla Ciebie ciekawostkę a za razem bardzo przydatny feature gita.

## cherry-pick

![cherry-pick]({{ site.baseurl }}/assets/img/cherry-pick.png)



Zasada działania jest prosta używając polecenia 

```bash
git cherry-pick future_x
```

bierzemy ostatni commit z brancha future_x i nakładamy go na wszystkie commity na branchu na którym się znajdujemy.

##### No dobra ale komu to potrzebne ?

Sytuacja wygląda następująco - zadanie które realizowałeś uznano za bardzo istotne i zdecydowano, że wejdzie jako quick fix. Odbijałeś od develop który ma zmiany z innych zadań a tylko twoje wchodzi na master. Najłatwiej będzie odbić nowy branch od master, zrobić na nim cherry-pick twojego brancha zadaniowego i wystawić pull request. :)

