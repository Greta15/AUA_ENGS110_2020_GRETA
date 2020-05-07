mport json

def user_info():

  useOldData = input('Do you want to use your old data?')

  old_data = getData()

  if(useOldData.lower() == 'yes'):
    print(old_data)
    choiceOfUser = int(input('Which one do you want to use?'))-1
    profession = old_data[choiceOfUser]['profession']
    age = old_data[choiceOfUser]['age']
    style = old_data[choiceOfUser]['style']
  elif(useOldData.lower() == 'no'):
    profession = input('Is he or she a doctor or lawyer:')
    age = int(input('How old is he or she:'))
    style = input('The style is classic or artsy:')
    addToJson(profession,age,style,old_data)     
  printSolution(profession,age,style)
def getData():
  file = open('data2.json')
  return json.load(file)
def addToJson(profession,age,style,old_data):
  obj = {}
  obj['profession'] = profession
  obj['age'] = age
  obj['style'] = style
  old_data.append(obj)
  file = open("data2.json", "w")
  file.write(json.dumps(old_data))
  file.close()
  
def printSolution(profession,age,style):
  if (profession == 'doctor'):
    if(age <= 40):
      if(style == 'classic'):
       print("The app suggests you to choose  a wireless blood pressure cuff or lab coat.")
      elif(style == "artsy"):
        print("The app suggests to choose  scarf or hat.")    
    elif(age >= 40):
      if(style == 'classic'):
        print("The app suggests you to choose  the finest espresso machine or stethoscope.")
      elif(style == "artsy"):
        print("The app suggests to choose  book or belt.")    
  if(profession == 'lawyer'):
    if(age <= 40):
      if(style == 'classic'):
        print("The app suggests you to choose  Pocket Watch or Tie.")
      elif(style == "artsy"):
        print("The app suggests to choose  glasses or  gloves.") 
    elif(age >= 40):
      if(style == 'classic'):
       print("The app suggests you to choose  Personalized Engraved Leather Journal Gift or PackLeather Lawyer Briefcase.")  
      elif(style == "artsy"):
        print("The app suggests to choose  watch or umbrella.")        
user_info()