# -*- coding: utf-8 -*-
import gtk
from gtk import glade
from google import *

class FtoC:
    def __init__(self):
	self.xml = glade.XML("buscaengoogle.glade", None, None)
       # self.xml.signal_connect("on_fahr_value_changed", self.on_spin_change)
        self.xml.signal_connect("on_btnclick",self.btnclick)       
	self.xml.signal_connect("on_window1_destroy", lambda w: gtk.main_quit())
       # self.spin = self.xml.get_widget("fahr")
       # self.result = self.xml.get_widget("celsius")
	self.text1 = self.xml.get_widget("entry1")
	self.btn1  = self.xml.get_widget("button1")
	self.textview1  = self.xml.get_widget("textview1")

    def on_spin_change(self, w):
        fahr = self.spin.get_value_as_int();
        cent = (fahr - 32) / 1.8
        texto = "%.2f C" % cent
        self.result.set_label(texto)

    def btnclick(self, w):
    	texto = "funciona"
        #self.textview1.insertText(texto)
        resultados=google(self.text1.get_text())
        if resultados != None and  resultados > 0:
	        for x in resultados:
		        self.textview1.get_buffer().insert_at_cursor(x+'  \n')        
        		#self.textview1.get_buffer().insert_at_cursor('  \n')
			#self.textview1.get_buffer().insert_at_cursor('  Edit as necc.\n')
	elif resultados == -2:
		self.textview1.get_buffer().insert_at_cursor('Tu búsqueda para  no ha arrojado resultados  \n')        
	elif resultados == -1:
		self.textview1.get_buffer().insert_at_cursor('No se ha podido efectuar la conexión  \n')        
   
if __name__ == "__main__":
    ftoc = FtoC()
    gtk.main()
