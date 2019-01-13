---
layout: post
title: sqlalchemy .one() vs .first() vs .one_or_none()
feature-img: "assets/img/tools.jpg"
thumbnail: "assets/img/tools.jpg"
tags: [Narzędzia, SQLAlchemy]
comments: true
---

`Query.one()` - zwraca wartość albo w przypadku braku wartości lub zbyt wielu rzuca wyjątkiem (`NoResultFound` w przypadku braku wartości lub `MultipleResultsFound` jeśli w wyniku otrzymamy więcej niż jeden) 

`Query.first()` - zwraca pierwszą znalezioną wartość lub `None` w przypadku braku wartości

`Query.one_or_none()` - zwraca wartość lub w przypadku braku wartości `None`, natomiast jeśli zwrócone zostały dwie lub więcej rzucony zostanie `MultipleResultsFound` 



Źródło: [dokumentacja SQLAlchemy](https://docs.sqlalchemy.org/en/latest/orm/tutorial.html#querying)