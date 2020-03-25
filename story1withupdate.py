import json

def user_info():

  useOldData = input('Do you want to use your old data?')
  file = open('data1withupdate.json')

  old_data = json.load(file)

  if(useOldData.lower() == 'yes'):
    print(old_data)
    choiceOfUser = int(input('Which one do you prefer?'))-1
    gender = old_data[choiceOfUser]['gender']
    price = old_data[choiceOfUser]['price']

  elif(useOldData.lower() == 'no'):
    gender = input('What is your gender:')
    price = int(input('How much do you want to spend:'))
    for element in old_data:
      if(element['gender'] == gender):
        if((price < 50 and element['price'] < 50) or (price > 50 and element['price'] > 50)):
          element['price'] = price
    file = open("data1withupdate.json", "w")
    file.write(json.dumps(old_data))
    file.close()

  if (gender == 'male'):
    if(price <= 50):
      print("You will be asked to choose belt or watch.")
    elif(price > 50):
      print("You will be asked to choose wallet or perfume.")
  elif (gender == 'female'):
      if(price <= 50):
        print("You will be asked to choose bag or perfume.")
      elif(price > 50):
        print("You will be asked to choose accessories or dress.")

user_info()