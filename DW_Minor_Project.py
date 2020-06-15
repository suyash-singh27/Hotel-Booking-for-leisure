

import mysql.connector
import login

def connect_to_sql(db):
    if len(db)>0:
        mydb = mysql.connector.connect(
          host="localhost",
          user="User",
          passwd="passwd",
        database=db
        )
    else:
        mydb = mysql.connector.connect(
          host="localhost",
          user="User",
          passwd="Passwd"
         )
    return mydb


def create_tables(mydb):
    mycursor=mydb.cursor()
    stmt = "SHOW TABLES LIKE 'HotelData'"
    mycursor.execute(stmt)
    result = mycursor.fetchone()
    if result:
      pass
    else:
      mycursor.execute("CREATE TABLE HotelData (HotelID Int NOT NULL, state Char(20), city Char(20), area_code Char(20), geyser Char(20), Air_conditioning Char(20), Television Char(20), wifi Char(20), view Char(20), free_breakfast Char(20), early_check_ins Char(20), distance_to_the_railway_station Int, distance_to_the_airport Int,number_of_eateries_closer_than_3_km Int, distance_to_the_downtown_of_the_city Int, number_of_monuments Int);")
    stmt = "SHOW TABLES LIKE 'HotelDataValue'"
    mycursor.execute(stmt)
    result = mycursor.fetchone()
    if result:
      pass
    else:
      mycursor.execute("CREATE TABLE HotelDataValue (HotelID Int NOT NULL, base_price Int, discount_offered Int, cgst Int, sgst Int, service_charges Int, loyalty_points Int);")
    stmt = "SHOW TABLES LIKE 'CustomerData'"
    mycursor.execute(stmt)
    result = mycursor.fetchone()
    if result:
      pass
    else:
      mycursor.execute("CREATE TABLE CustomerData (CustomerID Int NOT NULL, state_req Char(20), city_req Char(20), area_code_req Char(20), geyser_req Char(20), Air_conditioning_req Char(20), Television_req Char(20), wifi_req Char(20), view_req Char(20), free_breakfast_req Char(20), early_check_ins_req Char(20), distance_to_the_railway_station_req Int, distance_to_the_airport_req Int,number_of_eateries_closer_than_3_km_req Int, distance_to_the_downtown_of_the_city_req Int, number_of_monuments_req Int,base_price_req Int );")
    stmt = "SHOW TABLES LIKE 'Review'"
    mycursor.execute(stmt)
    result = mycursor.fetchone()
    if result:
        pass
    else:
      mycursor.execute("CREATE TABLE Review (CustomerID Int NOT NULL,HotelID Int NOT NULL, staff_service Int, amenities_provided Int, hygiene Int, food_quality Int);")
    stmt = "SHOW TABLES LIKE 'Validation'"
    mycursor.execute(stmt)
    result = mycursor.fetchone()
    if result:
      pass
    else:
      mycursor.execute("CREATE TABLE Validation (CustomerID Int NOT NULL UNIQUE, Password Char(20), EmailID Char(30));")

class project:
    def __init__(self,database):
        self.mydb = connect_to_sql(database)
        create_tables(self.mydb)

class build:
  def __init__(self):
    self.pr = project("DW_MINOR_PROJECT")

