# StockFinder
To clone and run a Django app, you'll need the following prerequisites:

    1. Python: Django is a Python web framework, so you need Python installed on your system. 
    2. Virtual Environment (Optional): It's a good practice to create a virtual environment for your Django project. This isolates your project's dependencies from the system-wide Python installation.
    
**Step 1:** First you have to clone the repository using given below command:
            git clone https://github.com/OmParkash1996/StockFinder.git

**Step 2:** You can install this project requirments through following command:

            pip install -r requirements.txt

**Step 3:** After that you have to run the server through following commands:

            python manage.py runserver

**Step 4:** Go to the "StockFinder/product_details/product/templates" directory and click on the **signup.html** file.

Following below are the end_points, input and output parameters for **API** perspective,
   
1.      endpoint: http://127.0.0.1:8000/api-token-auth/
        description: It will return the jwt token for the authentication.
        request_type: POST
        input: {
                "username":"omparkash",
                "password":"omparkash123"
                }

        output: {
                    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im9tcGFya2FzaCIsImV4cCI6MTY5ODAzNjIwNiwiZW1haWwiOiIifQ.5xitedM3b8LONFuhmx9rh0sWo-N1BijP15lzsUInN_4"
                }

2.      endpoint: http://127.0.0.1:8000/user-signup/
        description: It will create the user.
        request_type: POST
        input: {
                    "username":"noman",
                    "email":"noman@gmail.com",
                    "password":"noman123",
                    "first_name":"Noman",
                    "last_name":"Khalid"
                }

        output: {
                    "error": "",
                    "error_code": "",
                    "data": {
                        "user_id": 16
                    }
                }

3.      endpoint: http://127.0.0.1:8000/get-product-details/
        description: It will return the product details.
        request_type: GET
        headers: {
                    "Authorization": "jwt eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNiwidXNlcm5hbWUiOiJub21hbiIsImV4cCI6MTY5ODAzNjg5MiwiZW1haWwiOiJub21hbkBnbWFpbC5jb20ifQ.ICTQQhqESddtfXPCYqnpcuS4h5qTMqcJ1QCu3s2g2ZY"
                }
                
        output: {
                    "error": "",
                    "error_code": "",
                    "data": {
                        "user_email": "noman@gmail.com",
                        "product_details": [
                            {
                                "id": 1,
                                "name": "Iphone 15 pro max",
                                "description": "UAE version",
                                "price": "5100.00",
                                "available_stock": 10
                            },
                            {
                                "id": 2,
                                "name": "Iphone 14 pro max",
                                "description": "UAE version",
                                "price": "4200.00",
                                "available_stock": 20
                            },
                            {
                                "id": 3,
                                "name": "Iphone 15 pro",
                                "description": "UAE version",
                                "price": "4700.00",
                                "available_stock": 30
                            }
                        ]
                    }
                }

4.      endpoint: http://127.0.0.1:8000/create-product-details/
        description: It will return the product details.
        request_type: POST
        headers: {
                    "Authorization": "jwt eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNiwidXNlcm5hbWUiOiJub21hbiIsImV4cCI6MTY5ODAzNjg5MiwiZW1haWwiOiJub21hbkBnbWFpbC5jb20ifQ.ICTQQhqESddtfXPCYqnpcuS4h5qTMqcJ1QCu3s2g2ZY"
                }
        input: {
                "name":"Iphone 12 pro",
                "description":"HK version",
                "price":2500,
                "available_stock":5
                }
                
        output: {
                    "error": "",
                    "error_code": "",
                    "data": {
                        "product_details": {
                            "id": 4,
                            "name": "Iphone 11 pro",
                            "description": "HK version",
                            "price": "2500.00",
                            "available_stock": 5
                        }
                    }
                }
