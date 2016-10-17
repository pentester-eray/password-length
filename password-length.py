#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Belirtilen parolayı, 15 karakterden uzun 6 karakterden kısa olmama teorisine göre ayarlamayı sağlar.

while True:
    parola = input("Bir parola belirleyin: ")

    if not parola:
        print("lütfen parolayı girin!")

    elif len(parola) > 8 or len(parola) < 3:
        print("parola 15 karakterden uzun 6 karakterden kısa olmamalı")

    else:
        print("Yeni parolanız", parola)
        break
