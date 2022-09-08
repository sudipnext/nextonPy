import phonenumbers
from phonenumbers import geocoder

a=input("Enter a phone num")
phonenumber = phonenumbers.parse(a)
print(geocoder.description_for_number(phonenumber, 'en'))