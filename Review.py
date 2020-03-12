from tkinter import *


def chooseHotel():
    root = Tk()
    root.title("Choose Hotel")
    root.geometry("400x1000")

    frame0 = Frame(root)
    frame0.pack()

    Label(frame0,text="Search Hotels",font=("Times New Roman",40)).pack()
    Label(frame0).pack()

    # Locality
    frame1 = Frame(root)
    frame1.pack()

    Label(frame1, text='Locality', font=("Verdana", 20)).grid(row=0, column=0, sticky="w")
    Label(frame1).grid(row=1)
    Label(frame1, text="State :").grid(row=2, sticky="w")
    Label(frame1, text="Area-Code :").grid(row=3, sticky="w")
    Label(frame1, text="City :").grid(row=4, sticky="w")

    stateEntry = Entry(frame1).grid(row=2, column=1)
    areaCodeEntry = Entry(frame1).grid(row=3, column=1)
    cityEntry = Entry(frame1).grid(row=4, column=1)

    # Amenities

    frame2 = Frame(root)
    frame2.pack()

    Label(frame2).grid(row=5)
    Label(frame2, text='Amenities', font=("Verdana", 20)).grid(row=6, column=0, sticky="w")
    Label(frame2).grid(row=7)

    wifi = IntVar()
    ac = IntVar()
    shuttleservice = IntVar()
    swimmingpool = IntVar()
    parking = IntVar()
    breakfast = IntVar()
    spa = IntVar()
    coffeemaker = IntVar()
    gym = IntVar()
    tv = IntVar()

    wifi_cb = Checkbutton(frame2, text='Free WiFi', variable=wifi, onvalue=1, offvalue=0).grid(row=8, column=0,
                                                                                               sticky="w")
    ac_cb = Checkbutton(frame2, text='AC', variable=ac, onvalue=1, offvalue=0).grid(row=8, column=1, sticky="w")
    shuttleservice_cb = Checkbutton(frame2, text='Shuttle Service', variable=shuttleservice, onvalue=1,
                                    offvalue=0).grid(row=9, column=0, sticky="w")
    swimmingpool_cb = Checkbutton(frame2, text='Swimming Pool', variable=swimmingpool, onvalue=1, offvalue=0).grid(
        row=9, column=1, sticky="w")
    parking_cb = Checkbutton(frame2, text='Parking', variable=parking, onvalue=1, offvalue=0).grid(row=10, column=0,
                                                                                                   sticky="w")
    breakfast_cb = Checkbutton(frame2, text='Breakfast', variable=breakfast, onvalue=1, offvalue=0).grid(row=10,
                                                                                                         column=1,
                                                                                                         sticky="w")
    spa_cb = Checkbutton(frame2, text='Spa & Wellness Center', variable=spa, onvalue=1, offvalue=0).grid(row=11,
                                                                                                         column=0,
                                                                                                         sticky="w")
    coffeemaker_cb = Checkbutton(frame2, text='Coffee Maker', variable=coffeemaker, onvalue=1, offvalue=0).grid(row=11,
                                                                                                                column=1,
                                                                                                                sticky="w")
    gym_cb = Checkbutton(frame2, text='Gym', variable=gym, onvalue=1, offvalue=0).grid(row=12, column=0, sticky="w")
    tv_cb = Checkbutton(frame2, text='TV', variable=tv, onvalue=1, offvalue=0).grid(row=12, column=1, sticky="w")

    # Accessibilities

    frame3 = Frame(root)
    frame3.pack()

    Label(frame2).grid(row=13)
    Label(frame2, text='Accessibilities', font=("Verdana", 20)).grid(row=14, column=0, sticky="w")
    Label(frame2).grid(row=15)

    distance_list = ['0 KM', '5 KM', '10 KM', '15 KM', '20 KM', '25 KM', '30 KM', '35 KM', '40 KM']

    optionvariable_rs = StringVar(frame3)
    optionvariable_rs.set(distance_list[0])

    Label(frame3, text='Distance from Railway Station : ').grid(row=16, column=0, sticky="w")
    dist_railway = OptionMenu(frame3, optionvariable_rs, *distance_list).grid(row=16, column=1, sticky="w")

    optionvariable_air = StringVar(frame3)
    optionvariable_air.set(distance_list[0])

    Label(frame3, text='Distance from Airport : ').grid(row=17, column=0, sticky="w")
    dist_airport = OptionMenu(frame3, optionvariable_air, *distance_list).grid(row=17, column=1, sticky="w")

    optionvariable_downtown = StringVar(frame3)
    optionvariable_downtown.set(distance_list[0])

    Label(frame3, text='Distance from Downtown : ').grid(row=18, column=0, sticky="w")
    dist_downtown = OptionMenu(frame3, optionvariable_downtown, *distance_list).grid(row=18, column=1, sticky="w")

    optionvariable_tourist = StringVar(frame3)
    optionvariable_tourist.set(distance_list[0])

    Label(frame3, text='Distance from Tourist Attractions : ').grid(row=19, column=0, sticky="w")
    dist_tourist = OptionMenu(frame3, optionvariable_tourist, *distance_list).grid(row=19, column=1, sticky="w")

    # Review

    frame4 = Frame(root)
    frame4.pack()

    Label(frame4).grid(row=20)
    Label(frame4, text='Review', font=("Verdana", 20)).grid(row=21, column=0, sticky="w")
    Label(frame4).grid(row=22)

    Label(frame4, text='Average Review :').grid(row=23, column=0, sticky="w")
    review_spinbox = Spinbox(frame4, from_=0, to=5).grid(row=23, column=1, sticky="w")

    

    # Budget

    frame5 = Frame(root)
    frame5.pack()

    Label(frame5).grid(row=25)
    Label(frame5, text='Budget', font=("Verdana", 20)).grid(row=26, column=0, sticky="w")
    Label(frame5).grid(row=27)

    Label(frame5, text='Your Estimated Budget  :').grid(row=28, column=0, sticky="w")
    Entry(frame5).grid(row=28, column=1, sticky="w")

    Label(frame5).grid(row=29)

    searchbutton = Button(frame5, text="Search", font=("Helvatica", 15)).grid(row=30, column=0)

    root.mainloop()


chooseHotel()