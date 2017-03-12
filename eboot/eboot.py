#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import *
import random
import cPickle
import threading

import re, collections
from tkMessageBox import *
from Tkinter import *
import os

#################CENTRO DE ARCHIVOS###########################
animo = [100]


def crear():
    """
    if os.path.exists("datos2.dat"):
        pass
    else:
        pass
        datos2 = {}
        datos2 = cPickle.dump(datos2,open("datos2.dat","wb"))
    """
    if os.path.exists("db.dat"):
        pass
    else:
        memoria = {}
        db = cPickle.dump(memoria, open("db.dat", "wb"))
        showinfo(title="Error de Database", message="No se encontro una DB,se creo una nueva.")
    if os.path.exists("plantillas.dat"):
        pass
    else:
        plantillas = {"muerte": ["Mi * murio de * en *"],
                      "color": ["Mi color favorito es el *", "Me gusta el color *"],
                      "nick": ["Me llamo *", "Mi nombre es *", "Me llamo *"],
                      "ser_presente": ["La * es *", "Mi * es *", "Mi * era *", "El * es *"],
                      "estar_presente": ["Estoy en mi *", "Esta en *"],
                      "negacion": ["El no era *", "Ella no era *"],
                      "ser_pasado": ["Era *", "El era *", "Ella era *", "Ellos eran *"],
                      "estar_pasado": ["Estube *", "Estaba en mi *", "Estube en *"],
                      "gusto": ["Me gusta *", "Me gustan *", "Me gustan las *"],
                      "ser": ["Mi * es *", "Mi * tiene *"],
                      "odio": ["Odio *", "Odio que *", "Odio el *"],
                      "amar": ["Amo el *", "Amo *", "Amo * en * el * los *"],
                      "apodo": ["Me llaman *", "Me dicen *"],
                      "negacion de hecho": ["Pero no hago *"],
                      "tener": ["Tengo *"],
                      "email": ["Mi email es *", "Mi correo es *"],
                      "posesion": ["Tengo un *"]
                      }
        plantillas = cPickle.dump(plantillas, open("plantillas.dat", "wb"))
    if os.path.exists("datos.dat"):
        pass
    else:
        datos = {"%minick": ["Astrid"], "%nick": ["guille"]}
        datos = cPickle.dump(datos, open("datos.dat", "wb"))


crear()
memoria = cPickle.load(open("db.dat", "rb"))


def reset():
    datos2 = {}
    cPickle.dump(datos2, open("datos2.dat", "wb"))


#################CENTRO DE CONOCIMIENTO#######################
incorrecto = ["Error 101"]
plantillas = cPickle.load(open("plantillas.dat", "rb"))
datos = cPickle.load(open("datos.dat", "rb"))  # BASE DE DATOS
# datos2 = cPickle.load(open("datos2.dat","rb"))
saludo = ["Bienvenido de nuevo ", "Hola "]
lrepeticion = ["Basta de repetir", "Basta", "Deja de repetir :p", "...", "Es lo unico que hay para decir?", ":p",
               "Deja de repetir"]
comprension = ["Interesante", "Ah", "Ok"]
vocabulario = 'vocabulario.txt'
nada = ["...", "Por que no decis nada?"]
paginas = {"google": "www.google.com", "facebook": "www.facebook.com", "taringa": "www.taringa.net",
           "twitter": "www.twitter.com", "youtube": "www.youtube.com"}
prefijos1 = ["es", "esta", "era", "mi", "se"]
prefijos2 = ["esta", "es", "estaba", "era", "fue", "hizo", "se"]
vacio = ["Lo siento,no conozco nada aun", "Entrename", "No se nada", "Lo siento,no se nada", "No puedo responderte",
         "Lo siento,no puedo contestarte"]
articulos = {"indeterminantes": ["el", "la", "los", "las"], "determinantes": ["un", "una", "unos", "unas"]}
apregunta = ["que", "como", "cual", "quien", "cuando", "donde"]
sf = ["esta", "la", "era", "fue", "un", "el", "las", "los", "se"]
articulosf = ["yo", "me", "el", "la", "mi", "su"]
cacherepeticion = []
omisiones = [",", "y", "pero", "ademas", "encima"]
parar = []
recordarr = ["que te dije?", "que te acabo de decir?", "que dije?", "Que dije recien?", "Que dije anteriormente?",
             "Que dije?", "que eh dicho?"]
par = []
cache_usuario = []  # RAM donde se guarda la conversacion con el usuario.
cache_robot = []  # Se guarda la conversacion del robot
cache_azar = 0
cachpc = []
cachusuario = []
cac = [0]
humor_malo = ["insulto", "desconocida", "insulto ir"]
humor_bueno = ["saludo", "pregunta", "pregutna de estado"]
nombre_user = ["Usuario"]
compr = [1]


######################NUCLEO############################################28
class nucleo:
    def prueba(self):
        print "Lel"

    def apartir(self, que, donde):  # (HOLA COMO ESTAS)-COMO-=COMO ESTAS)
        if que in donde:
            ub = donde.index(que)
        ca = []
        for i in donde[ub:]:
            ca.append(i)
        h = "".join(str(o) for o in ca)
        return h

    def mensaje(self, titu, mensaje):
        showinfo(title=titu, message=mensaje)

    def obclas(self, dd, clase):  # lanzar valor al azar con clase
        ab = []
        for i in dd:
            a = dd[i]
            clase = a[0]
            if clase == clase:
                ab.append(i)
            else:
                pass
        return random.choice(ab)

    def recargar(self):  # Recargar Bases de datos
        memoria = cPickle.load(open("db.dat", "rb"))
        plantillas = cPickle.load(open("plantillas.dat", "rb"))  # BASE DE DATOS
        datos = cPickle.load(open("datos.dat", "rb"))  # BASE DE DATOS

    def reguardar(self):  # Guardar Datos
        cPickle.dump(datos, open("datos.dat", "wb"))

    def guardar_db(self):
        cPickle.dump(memoria, open("db.dat", "wb"))

    def computar(self, oracion):  # Analizis De String (hola,ola,la,a)
        def desca(d):
            buf1 = 0
            buf2 = []
            buf3 = []
            for e in oracion[d:len(oracion)]:
                buf2.append(e)
                if buf2 == []:
                    pass
                else:
                    l = "".join(str(unicode(x).encode("utf-8")) for x in buf2)
                    buf3.append(l)
            return buf3

        def final1():
            f = []
            j = 0
            while True:
                f.append(desca(j))
                if j == len(oracion):
                    return f
                    break
                else:
                    j += 1

        buf = []
        for g in final1():
            for b in g:
                buf.append(b)
        return buf

    def hora(self):  # Manejo de hora
        base = datetime.now()
        hora = base.hour
        hor = []
        if hora >= 12:
            hor.append("tarde")
        if hora >= 1:
            hor.append("noche")
        if hora >= 6:
            hor.append("maniana")
        if hora >= 20:
            hor.append("noche")
        else:
            hor.append("")
        minutos = base.minute
        segundos = base.second
        rep = []
        ee = hora, "y", minutos, "minutos", "de la", hor[0]
        for i in ee:
            rep.append(i)
        g = " ".join(str(h) for h in rep)
        return g

    def gdatos(self):  # Guardar Datos de actualizacion continua
        datos["%time"] = core.hora()

    def recordar(self, x):  # GUARDA TODO EN EL CACHE
        o = x.lower()
        h = o.replace("me", "te").replace("tu", "mi").replace("mi", "tu")
        if h in recordarr:
            pass
        else:
            if cache_usuario == []:
                cache_usuario.append(h)
            else:
                cache_usuario.append(h)

    def recordar_bot(self, x):
        cache_robot.append(x)

    def recordar_azar(self, x):
        cache_azar.append(x)

    def detectar_repeticion(self, y, x):  # detecta repeticion
        if x in recordarr:
            if len(cache_usuario) < 2:
                y.append("No dijiste nada")
            else:
                y.append("Dijiste " + "'" + cache_usuario[len(cache_usuario) - 1] + "'")
        else:
            pass

    def mayor(self, lista):  # Buscar string mayor en lista
        buf = [""]
        for i in lista:
            if len(i) >= len(buf[0]):
                buf.pop(0)
                buf.append(i)
            else:
                pass
        if buf[0] == "":
            return []
        else:
            return buf

    def mayor2(self, lista):  # Buscar string mayor en string
        buf = [0]
        for i in lista:
            if i >= buf[0]:
                buf.pop(0)
                buf.append(i)
            else:
                pass
        if buf[0] == "":
            return []
        else:
            return buf

    def upper(self):
        l = x.lower()
        m = l.upper()[0]
        fin = x.replace(x[0], m)
        return fin

    def bajar(self, x):
        p1 = x.lower()
        l = p1[0:1]
        ja = p1.replace(l, l.upper())
        return ja

    def encontrar_mayor(self, x):  # encontrar mayor key en diccionario,numerico
        cache = 0
        for i in x:
            if i < cache:
                pass
            else:
                cache = 0
                cache += i
        return x[cache]

    def obtener_dato(self, dato):  # Obtener dato de diccionario
        try:
            b = datos[nombre_user[0]]
        except:
            datos[nombre_user[0]] = {"%nick": [nombre_user[0]]}
        b = datos[nombre_user[0]]
        j = b[dato]
        return j[0]

    def obtener_dato_exterior(self, dato):
        b = datos[dato]
        return b[0]

    def obtener_var(self, articulos, var):  # Obtener valores de una clave
        return articulos[x]

    def comprobar(self, mensaje1, diccionario):  # Escanea y clasifica palabras
        palabra11 = core.computar(mensaje1)
        val = []
        for i in palabra11:
            je = [i]
            for t in diccionario:
                if unicode(t).encode("utf-8") in je:
                    val.append(i)
        b = core.mayor(val)
        if palabra11 == []:
            b.append("%nada")
        return b

    def navegar(self, x):  # despues de sufijos
        pal = x.split(" ")
        sufi = sf
        for g in sufi:
            if g in pal:
                u = pal.index(g)
                h = " ".join(str(g) for g in pal[u:])
                return h
        else:
            return x

    def navegar2(self, x):  # antes de los sufihos
        pal = x.split(" ")
        sufi = sf
        for g in sufi:
            if g in pal:
                u = pal.index(g)
                h = " ".join(str(g) for g in pal[:u])
                return h
        else:
            return x

    def remp(self, lista, dic):  # remplaza valores por los definidos en un diccionario
        g = []
        regex = re.compile("(%s)" % "|".join(map(re.escape, dic.keys())))
        nueva_cadena = regex.sub(lambda x: str(dic[x.string[x.start():x.end()]]), lista)
        k = nueva_cadena.replace("""['""""", "").replace("""']""""", "")
        return k

    def remp2(self, lista):  # remplaza valores/lista
        g = []
        try:
            h = datos[nombre_user[0]]
        except:
            datos[nombre_user[0]] = {"%nick": [nombre_user[0]]}
        h = datos[nombre_user[0]]
        regex = re.compile("(%s)" % "|".join(map(re.escape, h.keys())))
        nueva_cadena = regex.sub(lambda x: str(h[x.string[x.start():x.end()]]), lista)
        k = nueva_cadena.replace("""['""""", "").replace("""']""""", "")
        return k

    def buscar_en_datos(self, mensaje):
        c = core.computar(mensaje)
        for a in c:
            for b in datos:
                if a == b:
                    l = a
        h = mensaje.replace(a, datos[a])
        return h

    def dplanear(self, plantillas, entrada):  # Deteccion de plantillas
        def buscar_posicion_de_plantillas(base, mensaje):
            c = []
            for i in base:
                m = base[i]
                g = m[0].replace("*", "")
                if g.lower() in mensaje.lower():
                    a = mensaje.index(g.lower())
                    c.append(a)
            v1 = 0
            v2 = 1
            m = 0
            local = []
            c.sort()
            while m == 0:
                if v1 == len(c) - 1:
                    m = 1
                try:
                    local.append(mensaje[c[v1]:c[v2]])
                except:
                    local.append(mensaje[c[v1]:])
                v1 += 1
                v2 += 1
            return local

        def mayor(lista):  # Buscar string mayor en lista
            buf = [""]
            for i in lista:
                if len(i) >= len(buf[0]):
                    buf.pop(0)
                    buf.append(i)
                else:
                    pass
            if buf[0] == "":
                return []
            else:
                return buf

        def encontrar_mayor(en):  # busca mayor en dic  "hola":33<---
            if en == {}:
                pass
            else:
                b = 1
                r = 0
                for i in en:
                    if en[i] > b:
                        b = en[i]
                        r = i
                    else:
                        pass
                return r

        def encontrar_menor(en):  # busca menor en dic  "hola":33<---
            if en == {}:
                pass
            else:
                b = 9999999
                r = 0
                for i in en:
                    if en[i] < b:
                        b = en[i]
                        r = i
                    else:
                        pass
                return r

        def encontrar_menor_lista(en):  # busca menor en dic  "hola":33<---
            if en == {}:
                pass
            else:
                ca = []
                ca.append(encontrar_menor(en))
                b = 9999999999
                r = 0
                for i in en:
                    if en[i] == b:
                        ca.append(i)
                    if en[i] < b:
                        b = en[i]
                        r = i
                    else:
                        pass
                return ca

        def encontrar_mayor_lista(en):  # busca mayor en dic  "hola":33<---
            if en == {}:
                pass
            else:
                ca = []
                ca.append(encontrar_mayor(en))
                b = 0
                r = 0
                for i in en:
                    if en[i] == b:
                        ca.append(i)

                    else:
                        pass
                return ca

        def obtener(plantillas, mensaje, desde):
            mensaje = mensaje.lower()
            cach = []
            or1 = mensaje.split(" ")
            plantas = []
            posicionamiento = []

            def matrix(de, en):
                def navegar():
                    ap = []
                    for i in en:
                        if i not in de:
                            ap.append(en.index(i))
                    return ap

                ap = navegar()

                def escane(g):
                    def detectar():  # INTERA SOBRE LISTA Y DEFINE LA POSICION DE CADA OBJETO,EN EL CASO DE LISTA NUMERICA
                        re = {}
                        j = 0
                        for i in g:
                            re[i] = j
                            j += 1
                        return re

                    posicion = []

                    def b(apartir, lista):
                        f = []
                        a = lista[apartir]
                        for t in lista[apartir:]:
                            if t == a:
                                f.append(t)
                            else:
                                up = g.index(t)
                                break
                            a += 1
                        lista = detectar()
                        posicion.append(lista[f[len(f) - 1]] + 1)
                        return [f[0], f[len(f) - 1] + 1]

                    poses = []
                    poses.append(b(posicionamiento[0], g))
                    d = 0
                    try:
                        while True:
                            poses.append(b(posicion[d], g))
                            d += 1
                    except:
                        pass
                    return poses

                ad = escane(ap)
                lis = []
                for i in ad:
                    lis.append(" ".join(str(z) for z in en[i[0]:i[1]]))
                return lis

            def buscar_coincidencias(x):
                h = 0
                cache = {}
                cuenta = 0

                def escan(p):
                    cuenta = 0
                    c = 0
                    m = 0
                    while m == 0:
                        try:
                            cue = 0
                            if c == len(x):
                                m += 1
                            for i in p:
                                if x == len(x):
                                    return c
                                if i == x[c]:
                                    c += 1
                                    cue += 1
                                    cache[" ".join(str(y) for y in p)] = cue
                                else:
                                    if i == "*":
                                        c += 1
                                        cue += 0.5
                                        cache[" ".join(str(y) for y in p)] = cue
                                    else:
                                        c += 1
                                        break
                        except:
                            pass

                for m in plantillas:
                    for t in plantillas[m]:
                        lol = []
                        for l in t.split(" "):
                            lol.append(l.lower())
                        escan(lol)
                if cache == {}:
                    pass
                else:
                    afir = encontrar_mayor_lista(cache)
                    if afir == [0]:
                        pass
                    else:
                        j = {}

                        def ateri():
                            c = 0
                            for t in afir:
                                for i in t:
                                    if i == "*":
                                        c += 1
                                    j[t] = c
                                c = 0

                        ateri()
                        afir3 = encontrar_menor_lista(j)
                        afir2 = mayor(afir3)
                        for y in plantillas:
                            v = []
                            for t in plantillas[y]:
                                if afir2[0] == t.lower():
                                    v.append(t.lower())
                            if afir2[0] in v:
                                h = y
                        af = afir2[0].split(" ")
                        posicionamiento.append(or1.index(af[0]))
                        return [afir2[0], h]

            desde = desde.lower()
            panel = desde.split(" ")
            plantilla = []
            try:
                plantilla.append(buscar_coincidencias(panel))
                planti = plantilla[0]
                try:
                    if plantilla == None:
                        return None
                    else:
                        if plantilla[0] == None:
                            return None
                        else:
                            datos_remp = []
                            datos = matrix(planti[0], panel)
                            for t in datos:
                                for m in omisiones:
                                    datos_remp.append(t.replace(m, ""))
                                    break
                            try:
                                return [planti[1], datos_remp]
                            except:
                                return [planti[1], datos_remp]
                except:
                    return "Error"
            except:
                return "Error"

        def obtener2(plantillas, mensaje):
            mensaje = mensaje.lower()
            cach = []
            or1 = mensaje.split(" ")
            plantas = []
            posicionamiento = []
            defi = []

            def buscar_coincidencias(x):
                h = 0
                cache = {}
                cuenta = 0

                def escan(p):
                    cuenta = 0
                    c = 0
                    m = 0
                    while m == 0:
                        try:
                            cue = 0
                            if c == len(x):
                                m += 1
                            for i in p:
                                if x == len(x):
                                    return c
                                if i == x[c] or i == "*":
                                    defi.append(x)
                                    c += 1
                                    cue += 1
                                    cache[" ".join(str(y) for y in p)] = cue
                                else:
                                    c += 1
                                    break
                        except:
                            pass

                for m in plantillas:
                    for t in plantillas[m]:
                        lol = []
                        for l in t.split(" "):
                            lol.append(l.lower())
                        escan(lol)
                if cache == {}:
                    pass
                else:
                    afir = encontrar_mayor_lista(cache)
                    if afir == [0]:
                        pass
                    else:
                        j = {}

                        def ateri():
                            c = 0
                            for t in afir:
                                for i in t:
                                    if i == "*":
                                        c += 1
                                    j[t] = c
                                c = 0

                        ateri()
                        afir3 = encontrar_menor_lista(j)
                        afir2 = mayor(afir3)
                        for y in plantillas:
                            v = []
                            for t in plantillas[y]:
                                if afir2[0] == t.lower():
                                    v.append(t.lower())
                            if afir2[0] in v:
                                h = y
                        af = afir2[0].split(" ")
                        posicionamiento.append(or1.index(af[0]))
                        return [afir2[0], h]

            plantilla = []
            plantilla.append(buscar_coincidencias(or1[0:]))
            a = plantilla[0]
            return " ".join(str(g) for g in defi[0])

        obtencion = obtener2(plantillas, entrada)
        try:
            posiciones = buscar_posicion_de_plantillas(plantillas, entrada)
        except:
            posiciones = [obtencion]
        print posiciones
        resultado = []
        for m in posiciones:
            h = obtener(plantillas, m, m)
            if h == None:
                resultado.append(h)
            else:
                resultado.append(h)
        return resultado

    def dplantilla(self, mensaje):
        try:
            resultado = core.dplanear(plantillas, mensaje)
            res = resultado[0]
            ad = "%" + res[0]
            try:
                ap = datos[nombre_user[0]]
            except:
                datos[nombre_user[0]] = {}
                ap = datos[nombre_user[0]]

            ap[ad] = res[1]
        except:
            pass

    def cquestions(self, x, mensaje):  # DETECTA CONSULTA Y RESPONDE
        prefijos = apregunta
        msj = mensaje.split(" ")
        for g in prefijos:
            for o in msj:
                if o == g:
                    try:
                        x.append(core.que(mensaje))
                    except:
                        pass
        if x == []:
            pass
        else:
            return x[0]

    def crear(self, master, pos):  # MUESTRA VALORES DE UN VALOR DE DIC: valor:[[1],[2],[3]]
        buff = []
        k = master[pos]
        for i in k:
            buff.append(i)
        a = []
        for i in buff:
            a.append(core.remp2(i))
        return a

    def corrector(self, palabra):
        def words(text):
            return re.findall(u'[\xf1\xe1\xe9\xed\xf3\xfaa-z]+', unicode(text.lower(), 'utf-8'))

        def train(features):
            model = collections.defaultdict(lambda: 1)
            for f in features:
                model[f] += 1
            list = []
            return model

        NWORDS = train(words(file(vocabulario).read()))
        alphabet = u'abcdefghijklmnopqrstuvwxyz\xf1\xe1\xe9\xed\xf3\xfa'

        def edits1(word):
            s = [(word[:i], word[i:]) for i in range(len(word) + 1)]
            deletes = [a + b[1:] for a, b in s if b]
            transposes = [a + b[1] + b[0] + b[2:] for a, b in s if len(b) > 1]
            replaces = [a + c + b[1:] for a, b in s for c in alphabet if b]
            inserts = [a + c + b for a, b in s for c in alphabet]
            return set(deletes + transposes + replaces + inserts)

        def known_edits2(word):
            return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

        def known(words):
            return set(w for w in words if w in NWORDS)

        def correct(word):
            word = unicode(word.lower())
            candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
            return max(candidates, key=NWORDS.get).encode('utf-8')

        return correct(palabra)

    def repetido2(self):  # Detecta repeticiones
        cacherepeticion.append("0")
        if len(cacherepeticion) >= 3:
            parar.append("0")
            if len(parar) >= 4:
                par.append("0")
            if len(parar) >= 6:
                return "otra cosa"
            else:
                pass
            return "repetido"
        else:
            return ""

    def cresponder(self, obtencion):  # RESPUESTA SEGUN ANIMO
        g1 = obtencion[0]
        humor = memoria[g1]
        humor1 = humor[0]
        humor2 = [humor1[0].replace("\n", "").lower()]
        ##############################ANALISIS DE PALABRA Y HUMOR
        if humor2[0] in humor_malo:
            hfin = animo[0] - 10
            animo.pop(0)
            animo.append(hfin)
        if humor2[0] in humor_bueno:
            hfin1 = animo[0] + 1
            if animo[0] == 100:
                pass
            else:
                animo.pop(0)
                animo.append(hfin1)
        ##################################fin de analisis
        una = memoria[obtencion[0]]
        dos = una[0]
        normal = core.crear(una, 1)
        buena = core.crear(una, 2)
        mala = core.crear(una, 3)

        def repeticion(respuesta, respuestacache):  # deteccion de repeticion e imporvisacion de respuesta
            if cachusuario == []:
                pass
            else:
                pass
            re1 = memoria[g1]
            re1v = re1[0]
            re1a = re1v[0]
            if cachusuario == []:
                cachusuario.append("temp")
            if cachusuario[0] == re1a:
                respuestacache.append(core.repetido2())
            cachusuario.pop(0)
            cachusuario.append(re1a)

        def rmala():
            if mala == []:
                pass
            else:
                resp0 = random.choice(mala)
                resp0c = []
                repeticion(resp0, resp0c)
                if resp0c == ["error002"]:
                    ev = cac[0]
                    cac.pop(0)
                    cac.append(ev + 1)
                    return random.choice(lrepeticion)
                else:
                    return resp0

        def rnormal():
            if normal == []:
                pass
            else:
                resp1 = random.choice(normal)
                resp1c = []
                repeticion(resp1, resp1c)
                if resp1c == ["error002"]:
                    return random.choice(lrepeticion)
                else:
                    return resp1

        def rbuena():
            if buena == []:
                pass
            else:
                resp2 = random.choice(buena)
                resp2c = []
                repeticion(resp2, resp2c)
                if resp2c == ["error002"]:
                    return random.choice(lrepeticion)
                else:
                    if resp2c == ["otra cosa"]:
                        return core.obclas(memoria, ["pregunta robot"])
                    else:
                        return resp2

        if animo[0] <= 0:  # ANIMO
            return rmala()
        if animo[0] <= 50:
            return rnormal()
        if animo[0] <= 100:
            return rbuena()

    def comandar(self, y, x):  # Activa core de comandos
        m = x.split(" ")
        for i in indice_de_comandos:
            k = 0
            try:
                if i in m:
                    o = m.index(i)
                    k = 1
                    re = " ".join(str(u) for u in m[o + 1:])
                    y.append(indice_de_comandos[i](re))
            except:
                return "Error de comando"

    def mandar_a_caja(self, x):
        x.append("asd")

    def comprobar_usuario(self, x):
        if compr[0] == 1:
            def comp(object):
                global nombre_user
                if x in datos:
                    print "ya estaba"
                    nombre_user.pop(0)
                    nombre_user.append(x)
                    compr.pop(0)
                    compr.append(0)
                else:
                    print "Se creo un user nuevo"
                    datos[x] = {"%nick": [x]}
                    nombre_user.pop(0)
                    nombre_user.append(x)
                    compr.pop(0)
                    compr.append(0)


def compilar():
    def car():
        can = 0
        archivo = file("memori.txt", "rb")
        o = []
        for i in archivo:
            i.strip()
            o.append(i)
        op = []

        def add(x):
            cache = []
            for i in o[x:]:
                if i == "\n":
                    break
                cache.append(i)
            op.append(cache)

        v = 0
        k = 0
        while k == 0:
            add(v)
            v += 6
            if [] in op:
                k += 1
            else:
                can += 1

        def sa(pos):
            def nav():
                ope = []
                for t in op[pos]:
                    j = t.split(";")
                    ope.append(j)
                return ope

            return nav()

        bf = {}

        def agre(x):
            for i in sa(x)[0]:
                bf[i.replace("\n", "")] = [sa(x)[1], sa(x)[2], sa(x)[3], sa(x)[4]]

        for i in range(0, can):
            agre(i)
        return bf

    memori = car()

    def actualizar():
        cPickle.dump(memori, open("db.dat", "wb"))

    showinfo(title="Compilado", message="Base de datos recompilada con exito!")
    cargar()
    actualizar()


class comandos:
    def abrir(self, x):
        y = []
        for i in paginas:
            if x == i:
                y.append(paginas[i])
            else:
                pass
        if y == []:
            pass
        else:
            a = "start " + y[0]
            c = os.system(a)
            if c == 0:
                return "Se abrio correctamente " + y[0]
            else:
                return "Error,no se pudo abrir " + y[0]

    def finalizar(self, x):
        a = "taskkill /F /IM " + x
        c = os.system(a)
        if c == 0:
            return "Se cerro " + x
        else:
            return "No se encontro el proceso " + x

    def googlea(self, x):
        y = []
        k = x.split(" ")
        l = "+".join(str(c) for c in k)
        a = "start https://www.google.com.ar/?q=0#q=%s" % (l)
        c = os.system(a)
        if c == 0:
            return "Busqueda Procesada"
        else:
            return "Error en la busqueda :("

    def youtubea(self, x):
        y = []
        k = x.split(" ")
        l = "+".join(str(c) for c in k)
        a = "start https://www.youtube.com/results?search_query=%s" % (l)
        c = os.system(a)
        if c == 0:
            return "Busqueda Procesada"
        else:
            return "Error en la busqueda :("

    def cerrate(self):
        os.system("taskkill /F /IM python.exe")
        os.system("taskkill /F /IM cmd.exe")

    def ping(self, x):
        pass

    def comandos_secundarios(self, x):
        if x == "chau":
            charla.insert(END, "Gestor de Base de datos Iniciado")
            mensaje.delete(0, END)
            ven.destroy()
            charla.yview(END)
            return True
        if x == "/admin":
            charla.insert(END, "Gestor de Base de datos Iniciado")
            mensaje.delete(0, END)
            os.system("start gestor.py")
            charla.yview(END)
            return True
        if x == "/delcmd":
            charla.insert(END, "Consola reiniciada")
            mensaje.delete(0, END)
            os.system("cls")
            charla.yview(END)
            return True
        if x == "/datos":
            charla.insert(END, "Datos Impresos")
            mensaje.delete(0, END)
            print datos
            charla.yview(END)
            return True
        if x == "/udatos":
            charla.insert(END, "Datos Impresos")
            mensaje.delete(0, END)
            print datos[nombre_user[0]]
            charla.yview(END)
            return True
        if x == "/reset":
            charla.insert(END, "Reseteado :D")
            mensaje.delete(0, END)
            reset()
            core.recargar()
            print datos2
            charla.yview(END)
            return True
        if x == "/recargar":
            charla.insert(END, "Recargado :D")
            mensaje.delete(0, END)
            reset()
            core.recargar()
            charla.yview(END)
            return True
        if x == "/cls":
            charla.delete(0, END)
            mensaje.delete(0, END)
            return True
        return False


cmd = comandos()
indice_de_comandos = {"youtubea": cmd.youtubea, "cerrate": cmd.cerrate, "abre": cmd.abrir, "finaliza": cmd.finalizar,
                      "googlea": cmd.googlea, "busca": cmd.googlea}
core = nucleo()
modo = "charla"
cache_anterior = 0


def analizar(mensaje2):  # FUNCION MAESTRA DE RESPUESTA
    if modo == "charla":
        buffering1 = []
        try:
            p = {"nombre": ["Yo soy *", "Hola soy *", "Soy *"]}
            aa = core.dplanear(p, mensaje2)
            s = aa[0]
            m = s[1]
            a = m[0]
            nombre_user.pop(0)
            nombre_user.append(a)
            return random.choice(saludo) + nombre_user[0]
        except:
            pass
        core.reguardar()
        core.recargar()
        mensaje = mensaje2
        core.gdatos()
        obtencion = core.comprobar(mensaje, memoria)
        #####################################################
        core.recordar(mensaje)
        core.detectar_repeticion(buffering1, mensaje)
        core.dplantilla(mensaje)
        core.comandar(buffering1, mensaje)  # ACTIVA EL MODULO DE COMANDOS
        if buffering1 == []:  # Buffer valorico que usa core como medio externo
            pass
        else:
            return buffering1[0]
        #####################################################
        if obtencion == []:  # POR SI ESTA VACIO
            obtencion.append("error_000")
        if obtencion[0] in memoria:  # RECONOCIMIENTO Y RESPUESTA
            if obtencion[0] == ["error_000"]:
                cachpc.append("deconocida")
            else:
                return core.cresponder(obtencion)
            ######3POST RESPUESTA##################3333
            """
            conj = conjugacion.respuesta(mensaje)
            if conj == None:
                sup = mensaje+"?"
                charla.insert(END,sup)
                cache_anterior = mensaje
                modo = "aprender"
                return sup
            else:
                return conj
            """


##############################INTERFAZ GRAFICA#

ven = Tk()
ven.title("E-Boot v4")
ven.iconbitmap()
ven.geometry("520x209+250+250")
ven.resizable(width=FALSE, height=FALSE)
escri = StringVar()
s = Label(textvar=escri)
s.place(relx=0.000000001, rely=0.02, relwidth=0.17, relheight=0.06)
animo1 = StringVar()
an = "Animo:", animo[0]
animo1.set(an)
s = Label(textvar=animo1)
s.place(relx=0.50, rely=0.010, relwidth=0.17, relheight=0.06)


def Acerca_de():
    ventan = Tk()
    ventan.title("Sobre Eboot v4")
    caja = Text(ventan, width=78, height=18, bg="#BFD6C0")
    caja.pack()
    text = open("Leer.txt", "rb")
    for i in text:
        caja.insert(END, i)
    ventan.mainloop()


def admin():
    os.system("start gestor.py")


Acerca = Button(text="Info", command=Acerca_de)
Acerca.place(relx=0.83, rely=0.0001, relwidth=0.17, relheight=0.10)
Acerca = Button(text="Admin", command=admin)
Acerca.place(relx=0.66, rely=0.0001, relwidth=0.17, relheight=0.10)
Label(ven, text="").pack()
scrollbar = Scrollbar(ven)
scrollbar.pack(side=RIGHT, fill=Y)
charla = Listbox(ven, width=80, height=10)
charla.pack()
charla.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=charla.yview)
mensaje = Entry(ven, width=80, bg="#C6D8DD")
mensaje.pack()


def hablar(object):  # impresion en la caja de charla de la interfaz.
    oracion1 = mensaje.get().lower()
    cmd2 = cmd.comandos_secundarios(oracion1)

    if oracion1 == "":
        pass
    else:
        if cmd2 == True:
            pass
        else:
            oracion = oracion1
            ap = analizar(oracion)
            m = []
            if ap == None:
                m.append(random.choice(incorrecto))
            else:
                m.append(ap)
            usuario1 = core.obtener_dato("%nick") + ":" + mensaje.get()
            robot = core.obtener_dato_exterior("%minick") + ": " + m[0]
            core.recordar_bot(m[0])
            charla.insert(END, usuario1)
            charla.yview(END)

            # Notificacion de Humor
            def Preparar_Animo():
                ana = "Animo:", animo[0]
                animo1.set(ana)

            Preparar_Animo()

            # Notificacion de Escribiendo
            def Notificacion_Escribiendo():
                escri.set("Escribiendo...")

            tim = threading.Timer(0.5, Notificacion_Escribiendo)
            tim.start()

            def Respuesta_Robot():
                charla.insert(END, robot)
                escri.set("")
                charla.yview(END)

            esperar = threading.Timer(1, Respuesta_Robot)
            esperar.start()
            mensaje.delete(0, END)
            core.reguardar()


def eliminar_mensaje(object):
    i = charla.curselection()[0]
    charla.delete(i)


charla.bind("<Delete>", eliminar_mensaje)
ven.bind("<Return>", hablar)
ven.mainloop()
# Rokerlauncher96
