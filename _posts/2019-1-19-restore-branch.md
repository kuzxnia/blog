---
layout: post
title: Przywracanie usuniętego brancha
feature-img: "assets/img/commit.jpeg"
thumbnail: "assets/img/commit.jpeg"
tags: [Linux, Git]
comments: true
---

Kilka dni temu w pracy zdarzyło mi się przez pomyłkę usunąć nie ten branch roboczy co trzeba. Świadomość utraty 20h pracy nad zadaniem nie było zbyt przyjemna. Na szczęście udało się odzyskać usunięte zmiany.

<div style="width:100%;height:0;padding-bottom:68%;position:relative;"><iframe src="https://giphy.com/embed/13YroVUrUrLCec" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>

## git checkout -b

```bash
$ git branch -d test
Deleted branch test (was 2894f31).

$ git checkout -b test 2894f31
```