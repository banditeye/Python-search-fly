# -*- coding: utf-8 -*-
import selenium
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from bs4 import BeautifulSoup
import Connectdb
import sys

class Postesky():

    br=''
    wynik=''

    def driver(self):
        
        """ self.br=webdriver.Remote(
        command_executor="http://127.0.0.1:4444/wd/hub",
        desired_capabilities=webdriver.DesiredCapabilities.HTMLUNITWITHJS.copy())"""

        self.br=webdriver.Firefox()
        self.br.get('http://www.esky.pl/loty/wyszukiwanie_zaawansowane')

    """Pierwsze miasto"""
    def selectcountryone(self,departure):
        try:
            search=self.br.find_element_by_id('Fly-0-DepartureCity')
            search.clear()
            search.send_keys(departure)
        except Exception:
            self.selectcountryone(self,departure)

    def selectcountrytwo(self,arrival):
        """Drugie miasto"""
        search=self.br.find_element_by_id('Fly-0-ArrivalCity')
        search.clear()
        search.send_keys(arrival)
       

    def calendarone(self,day,month,year,binary):
        
      
        """otwarcie okna z kalendarzem 1"""
        search=self.br.find_element_by_name('Fly[0][DepartureDate]').click()
        """pierwszy kalendarz"""
        actualdate=datetime.datetime.now()
        miesiac=actualdate.month
        rok=actualdate.year
       
        if binary==0:
              pierwszywynik=(year-rok)*12+month-miesiac 
              for i in range(pierwszywynik):
                self.br.find_element_by_css_selector("span.ui-icon.ui-icon-circle-triangle-e").click()
        
        elif binary==1:
            wynik=1   
            print wynik
            for i in range(wynik):
                self.br.find_element_by_css_selector("span.ui-icon.ui-icon-circle-triangle-e").click()
        else:
            print 'kamis'
        
        self.br.find_element_by_link_text(str(day)).click()
      
           


    def calendartwo(self,day,month,year):
      
        """otwarcie okna z kalendarzem 2"""
        search=self.br.find_element_by_name('Fly[1][DepartureDate]').click()
        """ drugi kalendarz"""
        actualdate=datetime.datetime.now()
        miesiac=actualdate.month
        rok=actualdate.year        
        wynik=(year-rok)*12+month-miesiac-self.wynik
        print wynik
        for i in range(wynik):
            self.br.find_element_by_css_selector("span.ui-icon.ui-icon-circle-triangle-e").click()
            print i

        




        self.br.find_element_by_link_text(str(day)).click()

    def onewayticket(self):
        self.br.find_element_by_id('TripType_oneway').click()

     
    def zatwierdz(self): 
        """SZUKAJ"""
        search=self.br.find_element_by_class_name('c-34').submit()
        
    def oczekujnakalendarz(self):
        element = WebDriverWait(self.br, 80).until(
        EC.element_to_be_clickable((By.ID, 'Fly-0-DepartureDate-1')))

    def oczekujnalotniskodeparture(self):
        element = WebDriverWait(self.br, 80).until(
        EC.element_to_be_clickable((By.ID, 'Fly-0-DepartureCity')))

    def oczekujnabraklotu(self):
        element=WebDriverWait(self.br, 80).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, 'flight-not-found')))      
          
    def delay(self):
        while(True):
         try:
            element = WebDriverWait(self.br, 80).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="available-flights"]/form[1]/div[2]/div')))
            print element
            break
         finally:
                self.parser()
    
    def back(self):
        self.br.back()
        
        
        
    def returnairport(self,lotnisko_wylotu,lotnisko_przylotu):
        self.parser(lotnisko_wylotu,lotnisko_przylotu)
        

    def parser(self):
        """cena"""
        cena = self.br.find_element_by_xpath('//*[@id="available-flights"]/form[1]/div[2]/div')
        cena_text = cena.text 
        cena_text=cena_text[:-3]
        cena_text=int(cena_text)
        print cena_text
        
        """data wylotu"""
        from datetime import datetime
        data_wylotu=self.br.find_element_by_name('Fly[0][DepartureDate]')
        data_wylotu=str(data_wylotu.get_attribute("value"))
        konwersja=datetime.strptime(data_wylotu, '%d.%m.%Y').strftime('%Y-%m-%d')
        print konwersja
       
       
        """lotnisko wylotu"""
        lotnisko_wylotu=self.br.find_element_by_name('Fly[0][DepartureCity]')
        lotnisko_wylotu=lotnisko_wylotu.get_attribute("value")
        print (lotnisko_wylotu)
        """lotnisko przylotu"""
        lotnisko_przylotu=self.br.find_element_by_name('Fly[0][ArrivalCity]')
        lotnisko_przylotu=str(lotnisko_przylotu.get_attribute("value"))
        print lotnisko_przylotu

        """godzina wylotu"""
        godzina_wylotu=self.br.find_element_by_xpath('//*[@id="available-flights"]/form[1]/div[3]/div[1]/label/span[2]')
        godzina_wylotu_text=godzina_wylotu.text
        print godzina_wylotu_text
        
        """godzina przylotu"""
        godzina_przylotu=self.br.find_element_by_xpath('//*[@id="available-flights"]/form[1]/div[3]/div[1]/label/span[4]')
        godzina_przylotu_text=godzina_przylotu.text
        print godzina_przylotu_text
        
        """przesiadki"""
        przesiadki=self.br.find_element_by_xpath('//*[@id="available-flights"]/form[1]/div[3]/div[1]/label/a')
        przesiadki_text=przesiadki.text
        print przesiadki_text
        
        """operator"""
        operator=self.br.find_element_by_xpath('//*[@id="available-flights"]/form[1]/div[3]/div[1]/label')
        operator=operator.get_attribute('data-ac')
        operator1=operator.encode('utf-8')
        print operator1
         
        

        
        a=Connectdb.Connectdb()
        a.create_connection()
        a.save_fly_to_db(konwersja,lotnisko_wylotu,lotnisko_przylotu,godzina_wylotu_text,godzina_przylotu_text,przesiadki_text,operator1,cena_text) 
        a.closeconnection()
 
        
        
        
        
        
        
    