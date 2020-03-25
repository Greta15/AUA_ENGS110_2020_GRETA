import json

def user_info():

  useOldData = input('Do you want to use your old data?')

  file = open('data2.json')

  old_data = json.load(file)
  print(old_data)
  

  if(useOldData.lower() == 'yes'):
    choiceOfUser = int(input('Which one do you want to use?'))-1

    profession = old_data[choiceOfUser]['profession']

    age = old_data[choiceOfUser]['age']

    style = old_data[choiceOfUser]['style']

  elif(useOldData.lower() == 'no'):
    profession = input('Is he or she a doctor or lawyer:')
    age = int(input('How old is he or she:'))
    style = input('The style is classic or artsy:')
    obj = {}
    obj['profession'] = profession
    obj['age'] = age
    obj['style'] = style
    old_data.append(obj)
    file = open("data2.json", "w")
    file.write(json.dumps(old_data))
    file.close()
  if (profession == 'doctor'):

    if(age <= 40):

      if(style == 'classic'):

       print("The app suggests you to choose  a wireless blood pressure cuff or lab coat.")

    elif(age >= 40):

      if(style == 'classic'):

        print("The app suggests you to choose  the finest espresso machine or stethoscope.")

    if(age <= 40):

      if(style == "artsy"):

        print("The app suggests to choose  scarf or hat.")   

    elif(age >= 40):

      if(style == "artsy"):

        print("The app suggests to choose  book or belt.")  

  if(profession == 'lawyer'):

    if(age <= 40):

      if(style == 'classic'):

        print("The app suggests you to choose  Pocket Watch or Tie.")

    elif(age >= 40):

     if(style == 'classic'):

       print("The app suggests you to choose  Personalized Engraved Leather Journal Gift or PackLeather Lawyer Briefcase.")  

    if(age <= 40):

      if(style == "artsy"):

        print("The app suggests to choose  glasses or  gloves.")    

    elif(age >= 40):

      if(style == "artsy"):

        print("The app suggests to choose  watch or umbrella.")        

  

user_info()