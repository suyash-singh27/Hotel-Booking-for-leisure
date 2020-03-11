#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mysql.connector


# In[8]:


def connect_to_sql(db):
    if len(db)>0:
        mydb = mysql.connector.connect(
          host="localhost",
          user="suyash-singh",
          passwd="Helloworld27!",
        database=db
        )
    else:
        mydb = mysql.connector.connect(
          host="localhost",
          user="suyash-singh",
          passwd="Helloworld27!"
         )
    return mydb


# In[4]:


def create_database():
    mycursor.execute("CREATE DATABASE DW_MINOR_PROJECT")


# In[18]:


mydb = connect_to_sql("DW_MINOR_PROJECT")


# In[22]:


def create_tables(mydb):
    mycursor=mydb.cursor()
    mycursor.execute("CREATE TABLE HotelData (HotelID Int NOT NULL, state Char(20), city Char(20), area_code Char(20), geyser Char(20), Air_conditioning Char(20), Television Char(20), wifi Char(20), view Char(20), free_breakfast Char(20), early_check_ins Char(20), distance_to_the_railway_station Int, distance_to_the_airport Int,number_of_eateries_closer_than_3_km Int, distance_to_the_downtown_of_the_city Int, number_of_monuments Int);")
    mycursor.execute("CREATE TABLE HotelDataValue (HotelID Int NOT NULL, base_price Int, discount_offered Int, cgst Int, sgst Int, service_charges Int, loyalty_points Int);")
    mycursor.execute("CREATE TABLE CustomerData (CustomerID Int NOT NULL, state_req Char(20), city_req Char(20), area_code_req Char(20), geyser_req Char(20), Air_conditioning_req Char(20), Television_req Char(20), wifi_req Char(20), view_req Char(20), free_breakfast_req Char(20), early_check_ins_req Char(20), distance_to_the_railway_station_req Int, distance_to_the_airport_req Int,number_of_eateries_closer_than_3_km_req Int, distance_to_the_downtown_of_the_city_req Int, number_of_monuments_req Int,base_price_req Int );")
    
    for i in mycursor:
        print(i)


# In[21]:


create_tables(mydb)

