""" demo for the IO """
try:
    name = input('enter the name:')
    city = input('enter the city:')
    zip_code = int(input('enter the  zip code:'))

    print('name :', name)
    print('city :', city)
    print('zip code :', zip_code)
except ValueError as err:
    print(err)

print("Next statement after try catch block")
