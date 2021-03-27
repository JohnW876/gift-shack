# **Gift Shack**


### About
* Gift Shack is an e-commerce website selling gifts and homeware featuring unique patterns and designs.


Link to website - https://gift-shack.herokuapp.com

### User goals:
* To be able to visit the online store and find unique and original gifts to purchase
* To be able to register an account and login to view their personal profile showing their order history and payment details.
* To be able to easily navigate the site and find products they’re interested in.
* To be able to search for specific products by name, price or category.
* To be able to easily add items to a shopping cart and checkout later once they have finished shopping.
* To feel that they are using a secure and trustworthy site.

### Business goals of the website:
* To generate online sales  
* To provide an excellent overall user experience.
* To make it easy for the user to see and visit the areas of the website that are the most relevant to them via strong UX and UI design.
* To act as the main showcase and home for all current and future products.
* To build a strong, recognisable brand in the giftware market. 

## **UX**

The user types can be defined as but not restricted to the following:

* Shoppers tending towards the broad design led category.
* Shoppers more specifically interested in illustration, art and pattern design products.
* Shoppers looking for gifts in general.
* Shoppers looking for specific categories of products sold in the store. (Mugs, cushions, greetings cards, stationery etc) 
* Buyers representing resellers and marketplaces such as Wayfair, Amazon and other online retailers stocking design led products. 
* Buyers representing independent retailers such as high street gift shops and department stores both on and offline. 


The site has been primarily designed to meet the needs of these user types.
Clear sections which relate specifically to all of the user stories below are built into the website's design.
A mobile first approach was taken to create this project with consideration of ease of use and intuitive navigation to each of the features/sections.

### **User Stories**

| User Story No.               | As a…                     | I want to be able to…                                                 | So that I can…                                                                                  |
|------------------------------|---------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Views and Navigation         |                           |                                                                       |                                                                                                 |
| 1                            | Shopper                   | View all products at a glance                                         | Choose which ones I’d like to buy                                                               |
| 2                            | Shopper                   | View individual items for sale                                        | Assess the products details prior to purchasing. (Price, product description, available images) |
| 3                            | Shopper                   | View different categories of products                                 | Easily find the types of products I’m looking for                                               |
| 4                            | Shopper                   | View a running total of my chosen products on each page               | Manage how much I spend                                                                         |
| 5                            | Shopper                   | Easily find useful and relevant links                                 | Visit the store's social media pages and blog pages                                             |
| 6                            | Shopper                   | Contact the store owner                                               | Make customer enquiries about products, discounts, refunds, etc.                                |
| 7                            | Buyer                     | Contact the store owner                                               | Enquire about potentially stocking products in other stores both on and offline.                |
| Registration & User Accounts |                           |                                                                       |                                                                                                 |
| 8                            | Site User                 | Register for an account easily                                        | View my personal account profile                                                                |
| 9                            | Site User                 | Log in and logout easily                                              | Access my account and all relevant information                                                  |
| 10                           | Site User                 | Recover my password if I forget it                                    | Regain access to my account easily                                                              |
| 11                           | Site User                 | Receive a confirmation email after I register for an account          | Verify that I registered successfully                                                           |
| 12                           | Site User                 | Have my own user profile                                              | See my order history and know that my payment info is saved                                     |
| Sort & Search                |                           |                                                                       |                                                                                                 |
| 13                           | Shopper                   | Sort all available products                                           | View the products according to price or category                                                |
| 14                           | Shopper                   | Sort a specific category of product                                   | View the products in that category by price or name                                             |
| 15                           | Shopper                   | Search for specific items by their name or product description        | Find a particular product I’m interested in                                                     |
| 16                           | Shopper                   | See my search results                                                 | Check product availability and suitability                                                      |
| Purchasing & Checkout        |                           |                                                                       |                                                                                                 |
| 17                           | Shopper                   | Select the quantity of product easily                                 | Choose how many I would like to purchase                                                        |
| 18                           | Shopper                   | View all items in my shopping cart                                    | Easily see the total cost and the exact items I can expect to receive                           |
| 19                           | Shopper                   | Manually adjust the quantity of items in my shopping cart             | Control the number of items I want and make any final changes prior to checkout                 |
| 20                           | Shopper                   | Easily submit my payment details                                      | Checkout easily and quickly without any problems                                                |
| 21                           | Shopper                   | See a confirmation of my order after checkout                         | Be certain everything went as expected and verify that no mistakes were made                    |
| 22                           | Shopper                   | Receive an order confirmation email following checkout                | Have proof of purchase and a record of the transaction for future reference                     |
| Admin & Store Management     |                           |                                                                       |                                                                                                 |
| 23                           | Store owner/Administrator | Add new product(s)                                                    | List new products to sell in the store                                                          |
| 24                           | Store owner/Administrator | Edit product(s)                                                       | Make necessary changes to product details including images, descriptions, prices etc            |
| 25                           | Store owner/Administrator | Delete product(s)                                                     | Remove products from store when no longer required                                              |
| Blogs & Comments             |                           |                                                                       |                                                                                                 |
| 26                           | Site visitor              | Easily find the website blog articles                                 | Read the ones I'm interested in                                                                 |
| 27                           | Site visitor              | Write a comment about a blog post                                     | Contribute and offer my opinion relating to the article.




Further information and screenshots showing how this project meets the user's needs can be
found in the separate [TESTING.md](https://github.com/JohnW876/gift-shack/blob/master/TESTING.md) file.

### **Data design**

When designing the database for the app I stuck closely to the needs represented in the user stories.

**Product Model**

| Field       | Type         |
|-------------|--------------|
| id          |  integer     |
| category    | binary       |
| sku         | varchar(254) |
| name        | varchar(254) |
| description | text         |
| price       | decimal      |
| rating      | decimal      |
| image       | blob         |

**Category Model**

| Field         | Type          |
|---------------|---------------|
| name          |  varchar(254) |
| friendly_name | varchar(254)  |

**Order Model**

| Field           | Type         |
|-----------------|--------------|
| id              | integer      |
| order_number    | varchar(32)  |
| user_profile    | varchar      |
| full_name       | varchar(50)  |
| email           | string(254)  |
| phone_number    | varchar(20)  |
| street_address1 | varchar(80)  |
| street_address2 | varchar(80)  |
| town_or_city    | varchar(40)  |
| county          | varchar(80)  |
| post_code       | varchar(20)  |
| country         | varchar(80)  |
| date            | datetime     |
| delivery_cost   | decimal(6)   |
| order_total     | decimal(10)  |
| grand_total     | decimal(10)  |
| original_bag    | text         |
| stripe_pid      | varchar(254) |

**Order Line Item Model**

| Field          | Type          |
|----------------|---------------|
| order          |  varchar(255) |
| product        | varchar(255)  |
| quantity       | integer       |
| lineitem_total | decimal(6)    |

**User Profile Model**

| Field                   | Type        |
|-------------------------|-------------|
| user                    |  string     |
| default_phone_number    | varchar(20) |
| default_street_address1 | varchar(80) |
| default_street_address2 | varchar(80) |
| default_town_or_city    | varchar(40) |
| default_county          | varchar(80) |
| default_postcode        | varchar(20) |
| default_country         | varchar(20) |

**Blog Posts Model**

| Field      | Type          |
|------------|---------------|
| title      |  varchar(200) |
| slug       | varchar(200)  |
| author     | varchar(200)  |
| updated_on | datetime      |
| content    | text          |
| created_on | datetime      |
| status     | integer       |
| image_url  | blob          |
| image      | blob          |

**Comments Model**

| Field      | Type          |
|------------|---------------|
| post       |  varchar(200) |
| name       | varchar(80)   |
| email      | varchar(80)   |
| body       | text          |
| created_on | datetime      |
| active     | boolean       |

### **Wireframe mockups:**
Below is a link to the project's wireframe mockups which were created using Balsamiq Wireframes software prior to development to help with visualisation of features and layout. 

https://github.com/JohnW876//tree/master/wireframes
 
Wireframe mockups were created for every page of the website at mobile, tablet and desktop sizes and I referred to them throughout development. 


### **User Expectations:**
* What will they expect to see? - Users will expect to see an intuitive app with accessible features and a well designed user interface. 
* Does the site look credible and trustworthy? - Many elements will contribute to the first impression of a trustworthy site. These include, clear and intuitive navigation, good design and functionality. 
* Does the site offer what the user wants? - The features will need to meet the user's goals whilst delivering expected functionality and a valuable user experience.
* Does the site seem valuable enough for users to stay and return? - The features, functionality, usability and design will need to meet or exceed expectations to provide the value needed to ensure continued usage.  
  

### **Market Research:**
* Online research shows a number of apps to help writers work on their technique and improve their writing skills.
* There are also a good number of apps that deliver work by famous poets in either spoken word or purely textual formats.
* However there are very few that allow any user, regardless of skill level, to contribute their own work to a community and to create their own collection and/or manage a store of their work. 
* This app aims to fill that gap in the market and be available to all poets as an accessible and useful tool to help develop their body of work.


### **Visual Design:**
* Colour scheme -
  When designing the site I wanted to convey themes relevant to poetry such as passion and human emotions. In colour psychology these themes closely align to red which suggests passion, danger, life and love. 
  Red is used consistently throughout the site in the key elements such as the brand logo, page headings, edit form buttons, form icons, nav mobile dropdown and the social footer background. 
  With red as such a dominant colour it would not help to introduce another strong colour but does balance in a classic scheme with black, white and grey and is suggestive of paper and ink colours and poetry writing.

* Imagery - I also wanted to think of the design from a poet's point of view giving an analogue writer's feel to the homepage with background images of paper textures. 
* This was also the reason I chose to use Materialize CSS to help build the site as I felt the Material Design ethos offered simplicity whilst being inspired by paper and ink and was appropriate for poetry.
* Typography - For the main body of the site including headings and navigation, the chosen font is Open Sans for clarity and legibility. I did consider a script type in reference to handwriting but wanted to keep the site looking modern and accessible and thought a script would look too old fashioned and stuffy!
* For the poem text I used 'pre' tags in html which helps with the problem of how to display poems with appropriate line breaks. The Courier font used with the poems allows the text to stand out and is more easy to read from a user's perspective. 
* The brand logo uses Averia Serif Libre font which is intended to be a warm and friendly rather than too stiff and formal. 
  
## **Features**

* 
* 
* 
* 
* 
* 


### **Homepage**
There are a number of carefully chosen features on the homepage:

* 


### **Register Page**
* 

### **Login Page**
* 

### **Profile Page**
* 

### **Edit Poem**
* 

### **Add Poem Page**
* 

### **Manage Types Page (Admin user only)**
* 

### **Log Out**
* 

### **Flash Messages**
* User friendly flash messages display on the screen to guide and inform the user at key events.

### **Features to implement in future**
When considering the trade off between importance and viability, the following features could not be implemented at this stage but would make valuable additions in future and improve the user experience.

*
*
*

## **Languages Used** 
* HTML, CSS, Javascript and Python are used in this project.

## **Technologies Used**
* [Gitpod](https://www.gitpod.io/) Gitpod IDE was used to develop the website.
* [Bootstrap](https://getbootstrap.com/) A front-end framework used to help build the site and make it responsive on all devices.
* [FontAwesome](https://fontawesome.com/v4.7.0/) Icons were used in social links and forms. 
* [Google Fonts](https://fonts.google.com/) Font styles chosen for the website were sourced from here. 
* [Balsamiq Wireframes](https://balsamiq.com/) Used pre-development to help with UX/UI design and consulted throughout development.
* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) To inspect the code, test the data and preview changes on all device sizes.
* [Django](https://www.djangoproject.com/) A python web framework which was used to help build the site. 
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) Used to style and control how the site's forms are rendered. 
* [Django-allauth](https://django-allauth.readthedocs.io/en/latest/) A set of Django applications used for the site's authentication, registration and account management. 
* [Django template language](https://docs.djangoproject.com/en/3.1/ref/templates/) Used to dynamically generate HTML templates.
* [Stripe](https://stripe.com/gb) Used for secure online payment processing. 
* [Sqlite3](https://sqlite.org/index.html) To store the site's database during development.
* [Heroku](https://www.heroku.com/) To deploy the site.
* [Heroku Postgres](https://www.heroku.com/postgres) To store the production database.


## **Testing**

Information regarding testing can be found in this separate [TESTING.md](https://github.com/JohnW876/gift-shack/blob/master/TESTING.md) file.

---
## **Deployment**



---

## **Credits**

### **Content**
All site content was written by John Withey.

### **Media**
All images used in this project were created by John Withey. 


### **Code**
I used code from
* https://www.




### **Acknowledgements**
As an artist and illustrator I wanted to design and build a website that I could actually use to help promote and sell the products that I create.
It's been fun and a great challenge to produce an app that has real world value and will be used to hopefully generate sales in the future.
I'd like to thank my mentor Aaron Sinnott, once again, for helping with positive and constructive feedback during the project and throughout the course! 
