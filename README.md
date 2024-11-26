hello everyone, im learning fastapi , ill try to share everything i learned here.

HOW I STARTED MY LEARNING JOURNEY : *currently i started following the fastapi official documentation https://fastapi.tiangolo.com/  .

PROGRESS :

day 1 : 

FOR THE INSTALLATION : 
fastapi is based on python so i had to intall the latest version of python .

for someone is a big fan of jetbrains i installed pycharm as my main cli .

TRYING THE DOCUMENTATION SAMPE APPS :

*for making a new fastapi project i only needed to create a new fast_api project using pycharm and it installed and created eveyting i need like the virtual envirement(each fastapi project need a virtual envirement to isolate the packages you install for each project)

*WHAT DID I NOTICED IN THIS SAMPLE APP :

 as a java spring boot dev , i noticed :

 1- app = FastAPI()  

 i asked chatgpt to explain me this line of code and it appeared that it Creates an instance of the FastAPI application. This instance is used to define routes and configure the application.

 2-so to define routes we should use for exemple app.get("/") to define the root endpoint when it s like @GetMapping("/") in spring boot

 3-to create a method u have to type def nameOfTheMetod() : instead of exemple : public nameOfTheMethod(){}; in spring boot

 4- the querry param can have multiple types like this method shows :

   def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


  the q variable can get str or none type and it has None as a default value and for now i think None = null .

5-  the http response in the last method is a json with key value so it return  "item_id" as a key and item_id as a value and we have to use : between the key and the value

  









