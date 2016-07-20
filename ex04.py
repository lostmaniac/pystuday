#!/usr/bin/env 
# -- coding: utf-8 --

cars = 100
#赋值100给cars变量
space_in_a_car = 4.0
#赋值4.0浮点数，给变量space_in_a_car
drivers = 30
#赋值30给drivers
passengers = 90
#赋值90给passengers
cars_not_driven = cars - drivers
#用cars的100减去drivers的30，并且把新的值赋给cars_not_driven变量
cars_driven = drivers
#用变量drivers的数值30，赋值给cars_driven
carpool_capacity = cars_driven * space_in_a_car
#用cars_driven的值30乘以space_in_a_car4.0，并且赋值给新的变量carpool_capacity
average_passengers_per_car = passengers / cars_driven
#用passengers的数值90除以cars_driven，因为cars_driven = drivers，所以cars_driven的数值也是30，得到的结果赋值给新的变量average_passengers_per_car
#然后就是各种打印，自己理解一下就好
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "ineach car."
