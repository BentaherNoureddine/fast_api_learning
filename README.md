hello everyone, im learning fastapi , ill try to share everything i learned here.

HOW I STARTED MY LEARNING JOURNEY : *currently i started following the fastapi official documentation https://fastapi.tiangolo.com/  .

PROGRESS :

day 1 : 

FOR THE INSTALLATION : 
fastapi is based on python so i had to intall the latest version of python .

for someone is a big fan of jetbrains i installed pycharm as my main cli .

TRYING THE DOCUMENTATION SAMPlE APPS :

*for making a new fastapi project i only needed to create a new fast_api project using pycharm and it installed and created everything i need like the virtual envirement(each fastapi project need a virtual envirement to isolate the packages you install for each project)

*WHAT DID I NOTICED IN THIS SAMPLE APP :

 as a java spring boot dev , i noticed :

 1- app = FastAPI()  

 i asked chatgpt to explain me this line of code and it appeared that it Creates an instance of the FastAPI application. This instance is used to define routes and configure the application.

 2-so to define routes we should use for exemple app.get("/") to define the root endpoint when it s like @GetMapping("/") in spring boot

 3-to create a method u have to type def nameOfTheMethod() : instead of exemple : public nameOfTheMethod(){}; in spring boot

 4- the query param can have multiple types like this method shows :

   def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


  the q variable can get str or none type and it has None as a default value and for now i think None = null .

5-  the http response in the last method is a Map with key value so it return  "item_id" as a key and item_id as a value and we have to use : between the key and the value

6-to define the type of the request we only need to do this : @app.typeOfTheRequest and it can be Get,Put,Delete ...  .

7-The fastapi dev server  reload automatically.

8-class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

this class Defines a Pydantic model called Item, which represents the structure of data sent in requests. i think it s like defining DTO in spring boot


9- after trying this request this was the response :
<img src="C:\Users\Nourdine\Pictures\Screenshots\Capture d’écran (198).png"/>



10-declaring a parameter with = none it means that it s optional , Without the None it would be required (as is the body in the case with PUT).

11- FastAPI automatically parses the JSON payload into a Python object (or Pydantic model) .

12-If the incoming JSON does not conform to the rules(defined in the schema like the Item Pydantic model), FastAPI will automatically return a detailed validation error.


****************************************************************************************

HELLO EVERYONE AGAIN THIS IS NOUREDDINE , AND THIS IS OUR SECOND DAY WITH FAST API .

*what i want to do today? :

-if u guys noticed im using mysql as a DataBase , with spring boot i only had to specify the mysql driver and the db source in order to use the mysql db,
and i had to tell spring boot that such a class is a sql table by only using @Entity, and i used other annotations to specify some details about that table .

what im sure about , and we all know is rich with libraries that helps reduce code, reduce tasks ,gain more time and makes things so easy ,

SO WHAT IM GONNA DO NOW  : ill make a little search in order to find some libraries to help us making sql tables without typing so much as 
this screenshot shows :







  ![Capture d’écran (200)](https://github.com/user-attachments/assets/1dc08cbf-8f7a-4862-8a99-5273755e0250)






************************************************

after making a little search i found that everyone is making sql query inside the code in order to use sql , maybe inshallah ill make a library 

that makes the life of python devs easier , where this library that will detect the classes that should be tables in the database and it will create them when starting the app.





