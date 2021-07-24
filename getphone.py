

import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import pyttsx3

engine = pyttsx3.init()
engine.say("please enter the phone number")

mobileNo = input("enter mobile number with country code: ")
mobileNo = phonenumbers.parse(mobileNo)

#get timezone a phone number
print(timezone.time_zones_for_number(mobileNo))



#get carrier of a phone number
print(carrier.name_for_number(mobileNo, "en"))


#get region information
print(geocoder.description_for_number(mobileNo, "en"))


#validating a phone number
print("valid mobile number: ", phonenumbers.is_valid_number(mobileNo))


#checking possibility of a number
print("checking possibility of a number: ", phonenumbers.is_possible_number(mobileNo))

engine.say("thank you")
engine.runAndWait()






