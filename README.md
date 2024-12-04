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

![Capture d’écran (198)](https://github.com/user-attachments/assets/16df77c1-d696-40be-8e64-8923c16fa6ea)



10-declaring a parameter with = none it means that it s optional , Without the None it would be required (as is the body in the case with PUT).

11- FastAPI automatically parses the JSON payload into a Python object (or Pydantic model) .

12-If the incoming JSON does not conform to the rules(defined in the schema like the Item Pydantic model), FastAPI will automatically return a detailed validation error.


****************************************************************************************

DAY 2 :

HELLO EVERYONE AGAIN THIS IS NOUREDDINE , AND THIS IS OUR SECOND DAY WITH FAST API .

*what i want to do today? :

-if u guys noticed im using mysql as a DataBase , with spring boot i only had to specify the mysql driver and the db source in order to use the mysql db,
and i had to tell spring boot that such a class is a sql table by only using @Entity, and i used other annotations to specify some details about that table .

what im sure about , and we all know is rich with libraries that helps reduce code, reduce tasks ,gain more time and makes things so easy ,

SO WHAT IM GOING TO DO NOW  : ill make a little search in order to find some libraries to help us making sql tables without typing so much as 
this screenshot shows :







  ![Capture d’écran (200)](https://github.com/user-attachments/assets/1dc08cbf-8f7a-4862-8a99-5273755e0250)






************************************************

after making a little search i found that everyone is making sql query inside the code in order to use sql , maybe inshallah ill make a library 

that makes the life of python devs easier , where this library that will detect the classes that should be tables in the database and it will create them when starting the app.


* after more searching(i asked chat gpt if there is python libraries  that makes using mysql easier) and i found there is a library called SQLAlchemy that can help let s test it and find out .

1- i read the SQLAlchemy doc 

2- i installed the latest version of  SQLAlchemy v 2.0.36

3- after reading this documentation https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html 

i just learned that when u make a transaction the changes that u made with that transaction will not be instantly applied 

because we need to commit those changes by calling conn.commit in our case , or we can rollback and if we don t commit the changes and we release the connection

a rollback will be automatically  will be called .

to gain some time i only will test the commit and rollback in our project and im not gonna test the documentation examples to gain some time .

4-learned about the engine.begin() that helps with managing database transaction and making commits and rollbacks automatically

********************************************************************************************************************************

DAY 3 :

hello guys again , hope you are good , we are not getting feedback from anyone on how we are learning , that s ok at-least we are learning 

and im really enjoying this journey and that  s what matter ! so let s get started !

1-i think im getting so deep with the sql and this is not our main purpose  so what im gonna do is searching on how to convert a normal class to a database table !

2-we have to use declarative_base() instead of baseModel because we have BaseModel is primarily used for data validation and serialization, not for direct database table creation.

3- i found that if we want to use a string (varchar) we must define it s number of characters

4- learned about session and added our first class instance to the database

5-"after adding the new ClassRoom instance to the session and restarting the app we got a problem that say Class <class 'model.ClassRoom.ClassRoom'> does not have a __table__ or __tablename__
so i fixed that by adding  __tablename__ = 'ClassRoom' when defining the class


***************************************************************************

DAY 4 :

hello guys, this our 4th day, let s have a productive day!


WE HAVE SOME GOOD NEWS : 

**we got some feedback from coding betounsi(1)  and a software at tracekey solutions gmbH(2) :

*(1) : they advised us to keep up like that and learn more about ddl autocommit ,and lean more about the orm .

*(2) : he also advised us to keep up like that and advised us to share our progress in wordPress in order to share our experience later in our cv,

also we have to change the project file structure and the file naming , and we have to improve our english .

***I'm truly grateful for such positive feedback it means a lot to me! Honestly, I'm not entirely sure if sharing this feedback is appropriate,
but my intention is to share it openly to help others discover valuable learning opportunities.



----------------------------------------------------------------------------------------------------------------------------------------------
so until now we learned how we make database tables, let s make the rest of classes as table then let s see what we are going to do next.

1- after creating one instance from each class

2- we got a problem that say we have to define a relationship (inherit condition) between person and professor , we have to define a foreign key .

3- we successfully fixed the problem by making professor id a foreign key in the person class , so im going to make the director and the student also foreign keys .

4- so what we're going to  do now is :making CRUD (Create,Read,Update,Delete) api, after finishing this task we will inshallah learn more   
about the ORM  and the ddl autocommit and improve our code .

5-when i tried to make the endpoint that create a new person i got a lot of questions :
  *should i use request body or request params to be honest i don't know when to use the body and when to use the params ill make a search
  to find out .

  *how to get the data from the request in order to create a new person ... ? 


6- i don't know if im forcing the response to be 201 in all cases but 

im getting this :







![Capture d’écran (201)](https://github.com/user-attachments/assets/3dc74d07-46f4-4431-bff8-9a4a84247172)



but when i check  the database i dont find the created person so let s find out where is the problem



![Capture d’écran (202)](https://github.com/user-attachments/assets/92b229c4-279d-43af-a349-18a15f9026b2)



SORRY GUYS ALL GOOD THE PERSON IS BEING CREATED




this is the sql query :

select * from person where age = 22 ; 

![Capture d’écran (203)](https://github.com/user-attachments/assets/7a9fbc66-c731-4984-b3f1-85ce7784557a)


and this is the result





![Capture d’écran (204)](https://github.com/user-attachments/assets/4328b67f-0c49-40fd-aeab-409952c7a595)


**************************************************************************************************************************************************************
DAY 5 :

HELLO ! this is me again this is our DAY 5 (the half of it technically) in our journey ,no matter what DON'T YOU EVER GIVE UP ! 

* so until now we made an endpoint to create a new person , i know it s going to be a repetitive work, but we have to create the endpoints 

that create other instances of the other classes (why? to get used with python and fastapi maybe ).

1-*When creating a new student, the student is being saved in the person table because it inherits from Person, 
and it's also saved in the student table because it is a Student. However,
I noticed that the superclass attributes are being saved as NULL in the student table.
Even though I’ve worked on projects like this before and didn’t notice the issue,
I’m not ashamed of it better late than never. What matters is that we identify and learn from it.

*let s learn more about that !

*after dropping the db and creating a new one we no longer getting this problem what did i learn :
SQLAlchemy(our ORM) does not automatically create or modify the database schema during runtime .

*NOTE FORE SPRINGBOOT DEVS : next time when  u talk about hibernate u have to say the POWERFUL HIBERNATE

*NOTE FOR EVERYONE: I’m sure there’s a library that can help with auto-updating the database schema. I just want to describe myself as someone who has just bought a brand new, fully equipped car but doesn't yet know how to use all its features.

*in my next project inshallah i will make a search for the libraries that i need for my project before i start developping my solution .

*by the way i didn't forget about the feedback and the advices we got i will do that inshallah after finishing this little project , and we will also optimize and clean our code as possible as we can .

*** let s complete our boring CRUD operations in hope we get some problems that we can learn from it .



2-we made all the endpoints that's responsible for creating an instance of al the classes . 

*My next task is to develop the endpoint that updates a person. After that, 
I will use ChatGPT to create the update endpoints for the other classes to save some time.

3- when tried to make the update endpoint , the first question i had in my mind :

how to fetch that person from the db ? :

**********************************************************************************************************************


hello everyone, I hope you are all good !

this is our :

DAY 6 :

let s find an answer for that last question!


* - we successfully fetched(by using session.get()) the user and made our first update endpoint but we have to improve the way of updating the 
person

* i replaced updating the person manually by using this code
"
@app.put("/person/update/{id}", status_code=status.HTTP_200_OK)
def updatePerson(request: UpdatePersonRequest, id: int):
    person1db = session.get(Person, id)

    if not person1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    # exclude_unset=True means that we exclude any values that would be there just for being the default values
    person1data = request.model_dump(exclude_unset=True)

    person1db.sqlmodel_update = person1data

    session.add(person1db)
    session.commit()
    session.refresh(person1db)


    return {person1db}

"

when i try to update the person im getting this : 













