cars=100
space_in_a_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capasity=cars_not_driven*space_in_a_car
avrege_people_in_car=passengers/cars_driven
print("there are",cars,"cars avalible")
print("there are only",drivers,"drivers avalible")
print("there will be",cars_not_driven,"cars empty today")
print("we can transport",carpool_capasity,"people today")
print("we have",passengers,"people to carpool today")
print("we need to put",avrege_people_in_car,"in each car")