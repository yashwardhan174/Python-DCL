def order_food(hotel_name , *starter ,drink="water" , **mainCourse):
    print(hotel_name)
    print(starter)
    print(drink)
    print(mainCourse)


order_food("Marriot" , "Paneer Tikka" , "Soya Chaap" , "Chini Chapti" , drink="Coke", roti ="ButterNaan",gravy ="Kaju Masala",rice = "Veg Biryani" ,dessert="Gulab Jamun")