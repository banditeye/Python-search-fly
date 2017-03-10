# -*- coding: utf-8 -*-

import cx_Oracle
import mysql.connector
import mysql
import sys
from mysql.connector import errorcode


class Connectdb():

    connection=''
    def create_connection(self):
        """self.connection=cx_Oracle.connect('system/Wisienka.kw1@projektesky')"""
        try:
            self.connection=mysql.connector.connect(user='user809w_kamil ', password='wisienka1',
                                                host='78.47.160.209',
                                                database='user809w_esky')
           
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exists")
            else:
                print err 
        

    def save_fly_to_db(self,data_wylotu,lotnisko_wylotu,lotnisko_przylotu,godzina_wylotu,godzina_przylotu,przesiadki,operator,cena):
        cursor = self.connection.cursor()
        print 'DANE'
        print('''INSERT into avalibefly (data_wylotu, lotnisko_wylotu,lotnisko_przylotu, godzina_wylotu, godzina_przylotu, przesiadki, operator, cena)
                  values ('%s', '%s', '%s', '%s','%s', '%s', '%s', '%s')''' % (data_wylotu,lotnisko_wylotu,lotnisko_przylotu,godzina_wylotu,godzina_przylotu,przesiadki,operator,cena))
        sql = ('''INSERT into avalibefly (data_wylotu, lotnisko_wylotu,lotnisko_przylotu, godzina_wylotu, godzina_przylotu, przesiadki, operator, cena)
                  values ('%s', '%s', '%s', '%s','%s', '%s', '%s', '%s')''' % (data_wylotu,lotnisko_wylotu,lotnisko_przylotu,godzina_wylotu,godzina_przylotu,przesiadki,operator,cena))
        cursor.execute(sql)
        self.connection.commit()
        cursor.close()
    
        
        
    
        
    def selectairportone(self,i):
        cursor=self.connection.cursor()
        sql=("Select lotnisko_wylotu from airport where id_airport=%s " %i)  
        cursor.execute(sql)
        a=[]
        for i in cursor:
            print(i)     
            for lot in i:
                s=str(lot)
                print(s)
                a.append(s)
        return a
        cursor.close()

    def selectairporttwo(self,i):
        sql=("Select lotnisko_przylotu from airport where id_airport=%s " %i)
        cursor=self.connection.cursor()
        cursor.execute(sql)
        a=[]
        for i in cursor:
            print(i)     
            for lot in i:
                s=str(lot)
                print(s)
                a.append(s)
        return a
        cursor.close()
    def countairport (self):
        cursor=self.connection.cursor()
        sql=('Select count(*) from airport ')  
        cursor.execute(sql)
       
        
        
        for lot in cursor:
            print lot
            b=int(''.join(map(str,lot)))
            return b   
        
        cursor.close() 
        

    def closeconnection(self):
        self.connection.close()