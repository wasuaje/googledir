#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################################
# Programa desarrollado por T. Javier Robles Prado          
# Informar bugs o sugerencias a tjavier@usuarios.retecal.es #
# Visite http://users.servicios.retecal.es/tjavier           
##############################################################

#Este programa hace una consulta en google y devuelve los resultados
#ejemplo de uso:

#[jav@eva python]$ python -i google.py
#>>> google('programacion python principiantes', 8)
#http://users.servicios.retecal.es/tjavier/
#http://www.abcdatos.com/tutoriales/tutorial/l5248.html
#http://www.abcdatos.com/tutoriales/programacion/python.html
#http://www.maestrosdelweb.com/editorial/python
#http://www.maestrosdelweb.com/editorial/index.php?cat=3
#http://es.tldp.org/COMO-INSFLUG/COMOs/Lenguajes-Programacion-miniCOMO/
#http://ar.dir.yahoo.com/Internet_y_computadoras/Programacion_y_desarrollo/
#http://es.dir.yahoo.com/Internet_y_ordenadores/Programacion_y_desarrollo/

import httplib,sys

URL                 = 'www.google.com'
COD_BUSQUEDA        = '/search?&q='
#CABECERA        = ' <b>...</b> \n<br><font color=#008000>'
#CABECERA        = ' <a>...</a> \n'
#CABECERA        = '<a>'
#CABECERA        = '<i>'
#CABECERA        = "<li class=\"g w0\"><h3 class=\"r\">\n"
CABECERA        = '<li class=\"g w0\"><h3 class=\"r\">'
FIN                = ' '
NUM_RESULTADOS        = 150
MAX_RESULTADOS  = 100

def formateaQuery(query):
        from string import join
        a = query.split()
        return join(a, '+')

def google(query = None , n = None):
        
        if n is None:
                n = NUM_RESULTADOS
                
        if query is None:
                print "No se ha efectuado búsqueda"
                return - 1
        
        busqueda = run (query,n)
        
        if busqueda == -2:
                #print 'Tu búsqueda para %s no ha arrojado resultados.' % (query.replace('+',' '))
                return busqueda
        if busqueda == -1:
                #print 'No se ha podido efectuar la conexión'
                return busqueda

        for x in busqueda:
                print x
        #return busqueda

def run(query , n):
        #print URL+COD_BUSQUEDA+query.replace('+',' ')                
        try:

                conn = httplib.HTTPConnection(URL)
                conn.request("GET", COD_BUSQUEDA + formateaQuery(query))
                #conn.request("GET", COD_BUSQUEDA + query.replace('+',' '))                
                r = conn.getresponse()
                
        except:
                #print 'No se ha podido efectuar la conexión'
                return -1
                
        if r.reason == 'OK':
                data = r.read()
        else:
                return -1
        conn.close()
        aux = data.split(CABECERA)
        #print aux
        print CABECERA
        print 'leng = ',
        print len(aux)
        #Hay que desechar el primer elemento porque tiene el doctype
        aux.pop(0)
        if len(aux) == 0:
                return -2
                
        busqueda = []
        i = 0
        while n != 0 and i < MAX_RESULTADOS:
                try:
                        a =  aux[i].split(FIN,2)[0]
                        if a != '':
                                busqueda.append('http://'+a)
                                n -=  1
                except:
                        pass
                i +=  1
        return busqueda
                
google(sys.argv[1])

