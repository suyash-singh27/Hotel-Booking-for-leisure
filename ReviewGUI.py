from tkinter import *

class Review:
    def __init__(self,win,build,Id):
        self.build = build
        self.top = win
        self.Id = Id
        self.ReviewGUI()
    def submit_review(self):
        hotelID = self.hotel_entry.get()
        staff =  self.staffservice_entry.get()
        amenities = self.amenities_entry.get()
        food = self.foodquality_entry.get()
        value = self.hygiene_entry.get()
        sql_query = "Insert into Review (CustomerID,HotelID, staff_service, amenities_provided, hygiene, food_quality) Values ("+self.Id+","+hotelID+","+staff+","+amenities+","+value+","+food+");"
        mycursor=self.build.pr.mydb.cursor()
        mycursor.execute(sql_query)
        mycursor.execute("Select * from Review;")
        for i in mycursor:
            print(i)
    def ReviewGUI(self):
        self.root = Tk()
        self.root.title("Review Hotel")
        self.root.geometry("400x400")


        frame0 = Frame(self.root)
        frame0.pack()

        Label(frame0).pack()
        Label(frame0,text="Roseate Hotels",font=("Times New Roman",40)).pack()
        Label(frame0).pack()

        frame1 = Frame(self.root)
        frame1.pack()

        Label(frame1,text="Hotel ID/Name : ").grid(row=1,column=0,sticky="W")
        self.hotel_entry=Entry(frame1)
        self.hotel_entry.grid(row=1,column=1,sticky="w")

        Label(frame1).grid(row=2)
        Label(frame1, text='Review', font=("Verdana ", 30)).grid(row=3, column=0, sticky="w")
        Label(frame1).grid(row=4)

        Label(frame1, text="Staff Service : ").grid(row=5, column=0, sticky="W")
        self.staffservice_entry = Entry(frame1)
        self.staffservice_entry.grid(row=5, column=1, sticky="w")

        Label(frame1, text="Amenities : ").grid(row=6, column=0, sticky="W")
        self.amenities_entry = Entry(frame1)
        self.amenities_entry.grid(row=6, column=1, sticky="w")

        Label(frame1, text="Food Quality : ").grid(row=7, column=0, sticky="W")
        self.foodquality_entry = Entry(frame1)
        self.foodquality_entry.grid(row=7, column=1, sticky="w")

        Label(frame1, text="Hygiene : ").grid(row=8, column=0, sticky="W")
        self.hygiene_entry = Entry(frame1)
        self.hygiene_entry.grid(row=8, column=1, sticky="w")

        

        Label(frame1).grid(row=9)

        self.submitreview_button = Button(frame1, text='Submit',fg='red',command=self.submit_review)
        self.submitreview_button.grid(row=10)

        self.root.mainloop()