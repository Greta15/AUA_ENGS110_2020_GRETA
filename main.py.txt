import json
def user_info():
  useOldData = input('Do you want to use your old data?')
  file = open('data.json')
  old_data = json.load(file)
  if(useOldData.lower() == 'yes'):
    gender = old_data['gender']
    price = old_data['price']
  elif(useOldData.lower() == 'no'):
    gender = input('What is your gender:')
    price = int(input('How much do you want to spend:'))
    old_data['gender'] = gender
    old_data['price'] = price
    file = open("data.json", "w")
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

