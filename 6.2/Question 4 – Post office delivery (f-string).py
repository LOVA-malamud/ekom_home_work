last_name: str = input('enter your last name')
while last_name.isupper() == False:
    print('your last name must be all uppercase.')
    last_name: str = input('enter your last name again:')
first_name: str = input('enter your first name')
while first_name.islower() == False:
    print('your first name must be all lowercase.')
    first_name: str = input('enter your first name again:')
country: str = input('enter your country with 3 letters ')
while country.isalpha() == False or len(country) > 3:
    print('your country must be only 3 letters')
    country: str = input('enter your country with 3 letters again:')
city_address = input('enter your city address')
zip_code: int = (input('enter you zip code'))
while zip_code.isdigit() == False or len(zip_code) < 4:
    print('your zip code must be at least 4 digits')
    zip_code = input('enter your zip code again:')


print(f'FOR:{last_name}, {first_name}')
print(f'COUMTRY: {country}')
print(f'ADDRESS: {city_address}')
print(f'ZIPCODE: {zip_code}')
