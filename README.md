## Purpose of the project
___
   * The purpose of the project is to create an e-commerce site to apply all knowledge gained thorugh the course. The site is built using django. 
   *The site represent a ficticious gym that offers subscriptions,Personal Trainer plans and meal plans. 

## Personas 

For this project we have identified the following personas based on the expected usage of the site: 
- Visiting user: 
  - This persona is still not a client and is just gathering information or browsing the site before commiting. 
- Registered User/Shopper 
  - This person is ready to commit to a purchase or has already purchased one item and it is a recurring shopper 
- Business Owner
  - This persona is a business owner or admin that will control the site and access to parts like reviews, contact form queries, etc..

## User Stories
| User Story                                                                           | Ticket Number |
| :-----------                                                                         | :----:       |
|            Visiting User                          |
|          #2                               |  As a visiting user I can browse the site   |
|          #7                    |   As a visiting user I want to browse the products  |
|           Shopper                           |
|          #13                               |   As a shopper I wan to add products to the bag    |
|          #29                      |  As a shopper I can adjust the bag before paying for it    |
|          #29                                |   As a shopper I can checkout to pay for the items    |
|          #67             |   As a shopper I can leave comments in products    |
|                                Business Owners       |
|          #32                      |   As a business ower I can review and adjust the ordesr so that I can have visibility on my clients purchases   |
|           #52                     |  As a business owner I can add new products so that I can keep updating my site   |
|           #86                    |   Story As a business owner I am able to see the contact enquiries   |
|                                |      |
|                                |      |
|                                |      |

## Features
___
   *  Ability to browser the site.
   *  Ability Register in the site 
   *  Ability Request a new password
   *  Ability to view the different products available for purchase on different pages 
   *  Ability to sort out by product, ie: meal plan, personal trainer plan, etc..
   *  Ability to viw product details
   *  Ability to add items the cart and update the cart to remove or keep adding items.
   *  Ability to perfom a payment to obtain those items
   *  Ability to see and update their personal information 
   *  Ability to track and update their progress 
   *  Ability to track see their reviews and edit them
   *  Ability to Contact the business via form

## Future features
___
   * Ability to book specific classes 
   * Ability to book sessions with the PT


## Marketing Stategies
___

### Search Engine Optimization (SEO)

* 

## Desing and Diagrams
___
   ### Database Diagrams
   * ER diagram 
     
    
   ### Wireframes
   * 
   

## Technology
___
   ### Languages
   * HTML
   * CSS
   * Javascript
   * Python 3.8
   ### APIs
   * [Stripe](www.stripe.com)
     * API used to proccess client payments
   * Amazon S3 Storage
     * Using amazon S3 Storage to storage media and static files for deployment.
   ### Database
   * PostgresQL. This databased is hostes by [ElephantSQL](https://www.elephantsql.com/)
   ### Framework 
   * Django 4.0
   ### Libraries
   * [Allauth](https://django-allauth.readthedocs.io/en/latest/overview.html)
   * [Crispy Forms]()

## Test Cases 
___
| Test  | Expected Result | Actual Result | Pass/Fail |
| ----- | ----- | ----- |  -----|
| Browse to site |  User wil be directed to the landing page | User is directed to the landing page |**Pass** |
| Click in the nav links |  User will be directed to specific page |  User is directed to the page clicked| **Pass** |
| DropDown menu for products | User will see the product category dropdown menu  | Is presented with the dropdown menu |**Pass** |
| Browse to Classes |  User is directed to the landing page |  |**Pass** |
| Click in Classes | A modal will popup with more info about the class  |  |**Pass** |
| Browse to Contact Us |  User is directed to the landing page |  |**Pass** |
| User send a new query |  User receives an email confirming their query |  |**Pass** |
| Browse to Trainers |  User is directed to the landing page |  |**Pass** |
| User Registration |   |  |**Pass** |
| User Login |   | | **Pass** |
| User Password Reset |   |  |**Pass** |
| User Profile |   | | **Pass** |
| User Profile My Progress |   | | **Pass** |
| User Profile My Reviews |   |  |**Pass** |
| Display Items per Category | A overlay load and the user see the product's category |  |**Pass** |
| See a product details |   |  |**Pass** |
| Return to the product list |   |  |**Pass** |
| Add product to the bag |   |  |**Pass** |
|  |   |  |**Pass** |
|  |   |  |**Pass** |
|  |   |  |**Pass** |
|  |   |  |**Pass** |



## Fixed bugs
___
- 
## Supported screens and Browsers
___
   - 
## Deployment
___
   * [Heroku](heroku.com) deployment   
     - Browse to heroku and login
     - Upper right corner. Click in New and select New App
     - Choose a Name for the app and a Region
     - Click in your App name if you are not redirect to it. 
     - Click in Settings, under builpacks select: 
       - Heroku/Python
     - Click in Resources
     - [ElephantSQL.com](https://www.elephantsql.com/) database 
       - Navigate [ElephantSQL.com](https://www.elephantsql.com/) and click “Get a managed database today”
       - Select “Try now for FREE”
       - Select “Log in with GitHub” and proceed with authorization
       - Create a database
       - Set up your plan - Tiny Turtle is a free tier
       - In “Select Region” choose the closed to you or your users
       - Click “Review”
       - Click "Create Instance"
     - [Stripe](stripe.com)
       - Click in register and complete the registration process
       - Click in Developers
       - Click in API Keys
       - Writedown the apis as they will be used in the Heroku config below
       - Cick in Webhook
       - Click in Add Endpoint and add https://fitbodies.herokuapp.com/checkout/wh/
       - Take note of the endpoint secret. This will be used in the Heroku Config below
     - [Amazon](aws.amazon.com)
       - Create an amazon account
       - Go to Amazon dashboard and search for S3
       - Create a bucket called fitbodies
       - Select your AWS Region
       - Uncheck "Block all public acess" and check the warning message
       - Navigate to Properties
       - Navigate to Static and click edit
       - Turn On Static Website Hosting
       - Enter index.html and error.html in their respective fields 
       - In Permissions, click edit in the CORS section and enter the [FOLLOWING]() configuration
       - Click edit in buckect policy and generate the FOLLOWING policy
       - The above generates THIS policy 
       - In Access Control List set the List permissions to everyone under Public Access
       - Go to IAM. 
       - Click on Policies and Create Policy
       - Click in JSON and import the Amazon pre-built policy AmazonS3FullAccess
       - Click in Review Policy. 
       - Set a name and description
       - Click in Create Policy
       - Click in Add User to create a user
       - Add the user 
       - Download the CSV files with the keys that we will using in heroku
     - Click in Settings again
     - Click Reveal Config Vars
     - In Config Vars click in Add and add the following
       - DATABASE_URL - 
       - SECRET_KEY - Secret Key from Django
       - PORT - 8000
       - STRIPE_WH_SECRET - Stripe webhook secret key
       - USE_AWS - True
       - AWS_SECRET_ACCESS_KEY - AWS user access key from the amazon download CSV file
       - AWS_ACCESS_KEY_ID - AWS user key ID from the amazon download CSV file
       - EMAIL_HOST_PASS - App password to send email in this case gmail app password
       - EMAIL_HOST_USER - Email selected for sending email
     - Return to your Code Editor where your code lives
     - Create a Procfile
       - Inside enter web: gunicorn alfresco.wsgi
     - In settings.py navigate to ALLOWED_HOST
       - Add heroku APP URL 
     - In settings.py set DEBUG=False
     - Run pip3 freeze >> requirements.txt to ensure packages and libraries are captured.
     - Commit and push your code as needed.
     - Once that is completed. Click in Deploy
       - In Deploy Method clink under GitHub 
       - Connect your Github repository to Heroku
       - At the bottom under Manual Deployment select the Branch you want to deploy. Main by default
       - Click in Deploy Branch
       - Click in the View button to open deployed app.
   * Local deployment
     - Clone the repository 
     - Ensure your ENV variables are correct
     - Run the command python3 manage.py migrate if required.
     - Run the command python3 manage.py runserver
     - In settings.py modify ALLOWED_HOST to resolve any connectivity issues.
    
## Credits
___
   * Official docummenation https://djangoproject.com
   * Bootstrap code https://getbootstrap.com/
   * E-Commerce core functionality by Code Institute boutique Ado
   * Images 