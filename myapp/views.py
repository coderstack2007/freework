from django.http import HttpResponse
from django.shortcuts import render, redirect
import pyrebase
from django.template.loader import render_to_string
from .forms import MyForm
from .forms import MyForm2
from .forms import MyForm3
from .models import MyModel
from .models import MyModel2
from .models import MyModel3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

config = {
  "apiKey": "AIzaSyBRYYCsGzrO2XZ69ZNU3gYgPT_198WGVsc",
  "authDomain": "project-sensorika.firebaseapp.com",
  "databaseURL": "",
  "storageBucket": "project-sensorika.appspot.com"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()



#HOME
def home(request):  
  return render(request, "index.html")



#MAKE
def make(request):
      context = {}
      if request.method == "POST":
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/account/")
        else:
            print("Error")

      form = MyForm()
      
      context["form"] = form
      context["dbdata"] = MyModel.objects.all()
    
      return render(request, "make.html", context=context)
  


#index
def index(request):
  if request.method == "POST":
      sea = request.POST.get("search")

    # #COPY#
    #   if sea == "project":
    #     return redirect("/copy/")
    #   if sea == "проэкт":
    #     return redirect("/copy/")
    #   if sea == "projects":
    #     return redirect("/copy/")
    #   if sea == "Projects":
    #     return redirect("/copy/")
    #   if sea == "Проэкты":
    #     return redirect("/copy/")
    #   if sea == "Project":
    #     return redirect("/copy/")
    #   if sea == "Проэкт":
    #     return redirect("/copy/")
    #   if sea == "копия сайтов":
    #     return redirect("/copy/")
    #   if sea == "копия":
    #     return redirect("/copy/")
    #   if sea == "copy":
    #     return redirect("/copy/")

    #IT#
      if sea == "Разработка и ИТ":
        return redirect("/index2/")
      if sea == "IT":
        return redirect("/index2/")
      if sea == "It":
        return redirect("/index2/")
      if sea == "it":
        return redirect("/index2/")
      if sea == "Разработка и IT":
        return redirect("/index2/")
      if sea == "разработка и ит":
        return redirect("/index2/")
      if sea == "Разработка":
        return redirect("/index2/")
      if sea == "Разработка и айти":
        return redirect("/index2/")

    #DIZAYN#
      if sea == "Дизайн": 
        return redirect("/index3/")
      if sea == "дизайн":
        return redirect("/index3/")
      if sea == "Dizayn":
        return redirect("/index3/")
      if sea == "dizayn":
        return redirect("/index3/")

    #Sign#
      if sea == "Sign in":
        return redirect("/Sign/")
      if sea == "Sign":
        return redirect("/Sign/")
      if sea == "sign":
        return redirect("/Sign/")

      if sea == "Войти":
        return redirect("/Sign/")
      if sea == "войти":
        return redirect("/Sign/")

    #Log in#  
      if sea == "Log in":
        return redirect("/register/")
      if sea == "log in":
        return redirect("/register/")
      if sea == "Регистрация":
        return redirect("/register/") 
      if sea == "регистрация":
        return redirect("/register/")
      
    #feedback#
      if sea == "Служба поддержки":
        return redirect("/feedback/")
      if sea == "служба поддержки":
        return redirect("/feedback/")
      if sea == "Обратный связь":
        return redirect("/feedback/")
      if sea == "обратный связь":
        return redirect("/feedback/")
      if sea == "Feedback":
        return redirect("/feedback/")
      if sea == "feedback":
        return redirect("/feedback/")
    
    #404# 
      else:
        return redirect("/notfound/")

  return render(request, "index.html")




#index2
def index2(request):
    return render(request, "index2.html")    




#index3
def index3(request):
    return render(request, "index3.html") 




#action#
def action(request): 
  form = MyForm()
  contest = {}
  context = {}
  context["form"] = form

  context["dbdata"] = MyModel.objects.all()
  contest["dbdats"] = MyModel.objects.all()
  return render(request, "action.html", context) 



#account
def account(request):
    form = MyForm()

    context = {}

  
    context["dbdata"] = MyModel.objects.all()

    return render(request, "account.html", context)
    


#Sign
def Sign(request):
  context = {}
  if request.method == "GET":
    return  render(request, "Sign.html")


  if request.method == "POST":
    input1 = request.POST.get("email")
    input2 = request.POST.get("password")


    try:
      auth.sign_in_with_email_and_password(input1, input2)
      context["info"] = "Success"
      return redirect("/action/")
    except:
      context["info"] = "Error"
 

    return render(request, "Sign.html", context=context )



#copy
def copy(request):
    form = MyForm2()

    context = {}
    context["formalar"] = form
  
    context["dbdatalar"] = MyModel2.objects.all()
    return render(request, "copy.html", context)


#makeproject
def makeproject(request):
    context = {}
    function = {}
    context2 = {}
    if request == "POST":
      choose = request.form.get("select")
      if choose == "/copy/":
        redirect("/copy/")
    
    

    
    if request.method == "POST":
      form = MyForm2(request.POST, request.FILES )

      if form.is_valid():
          form.save()
          return redirect("/copy/")
      else:
        pass

      form = MyForm2()
      context["formalar"] = form
      context["dbdatalar"] = MyModel2.objects.all()
      context2["newdates"] = MyModel2.objects.all()    

    elif request.method == "GET":
      render(request, "makeproject.html", context=context)
    return render(request, "makeproject.html", context=context) 

    function = {
          "select" : choose,      
        }
#register
def register(request):
    context = {}
    if request.method == "GET":
      return  render(request,"register.html")


    if request.method == "POST":
      input1 = request.POST.get("email")
      input2 = request.POST.get("password")


      try:
        auth.create_user_with_email_and_password(input1, input2)
        context["info"] = "Success"
        return redirect("/make/")
      except:
        context["info"] = "Error"
        return redirect("/register/")
    return render(request, "register.html", context)



#dizayn
def dizayn(request):
  return render(request, "dizayn.html")



#it
def it(request):
  return render(request, "it.html")

def feedback(request):
    context = {}
    if request.method == "POST":
        form = MyForm3(request.POST, request.FILES )
        if form.is_valid():
            form.save()
    


    form = MyForm3()
    context["from"] = form
    context["datadata"] = MyModel3.objects.all()
    model = MyModel.objects.all()
    return render(request, "feedback.html", context=context)

def pay(request):
    context = {}
    if True:
      if request.method == "POST":
        number = request.POST.get("pay")
        amount = request.POST.get("py")
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--log-level=3")
        driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
        driver.get("https://payme.uz/home/main")
        time.sleep(1)
        driver.find_element(By.ID, "phone").send_keys("992673880")
        driver.find_element(By.ID, "amount").send_keys("500")
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/app-root/app-home/div/app-home-main-page/app-home-mobile/div/div[2]/div/form/div/div[3]/button").click()
        time.sleep(30) 
        
        driver.close()
        driver.quit()
    
        context = {
          "pay" : number,
          "py" : amount

        }
        return redirect("/files/")
    
      
      
    elif request.method == "GET":
      return render(request, "pay.html")
    return render(request, "pay.html", context)    

  
def notfound(request):
  return render(request, "notfound.html")

def about(request):
  return render(request, "about.html")

def files(request):
    form = MyForm2()

    context = {}
    context["formalar"] = form
  
    context["dbdatalar"] = MyModel2.objects.all() 
    return render(request, "files.html", context)

def customer(request):
  return render(request, "customer.html" )

def experement(request):
 
  context = {}
  if True:
    if request.method == "POST":
      number = request.POST.get("pay")
      amount = request.POST.get("py")
      chrome_options = webdriver.ChromeOptions()
      # chrome_options.add_argument("--headless")
      chrome_options.add_argument("--disable-gpu")
      chrome_options.add_argument("--log-level=3")
      driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
      driver.get("https://payme.uz/home/main")
      time.sleep(1)
      driver.find_element(By.ID, "phone").send_keys("992673880")
      driver.find_element(By.ID, "amount").send_keys("500")
      time.sleep(1)

      driver.find_element(By.XPATH, "/html/body/app-root/app-home/div/app-home-main-page/app-home-mobile/div/div[2]/div/form/div/div[3]/button").click()
      time.sleep(30) 
      
      driver.close()
      driver.quit()
  
      context = {
        "pay" : number,
        "py" : amount

      }
      return redirect("/files/")
    
        
  return render(request, "experement.html")