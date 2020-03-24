import json
def user_info():
  useOldData = input('Do you want to use your old data?')
  file = open('data.json')
  old_data = json.load(file)
  if(useOldData.lower() == 'yes'):
    profession = old_data['profession']
    age = old_data['age']
    style = old_data['style']
  elif(useOldData.lower() == 'no'):
    profession = input('Is he or she a doctor or lawyer:')
    age = int(input('How old is he or she:'))
    style = input('The style is classic or artsy:')
    old_data['profession'] = profession
    old_data['age'] = age
    old_data['style'] = style
    file = open("data.json", "w")
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
  
