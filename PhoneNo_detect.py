import phonenumbers
from phonenumbers import timezone,geocoder,carrier   #timezone will provide exact time of the area where the SIM is and
                                               #geocoder will provide service to check the SIM carrier
number = input("Enter your valid Number with +__ :")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone) 
car = carrier.name_for_number(phone,"en") #en is used for that number we passed here it will show the place name in english 
reg = geocoder.description_for_number(phone,"en")                                  
print(phone)
print(time)
print(car)
print(reg)