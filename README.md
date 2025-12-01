# Ex04 Places Around Me
# Date:01-12-25
# AIM
To develop a website to display details about the places around my house.

# DESIGN STEPS
## STEP 1
Create a Django admin interface.

## STEP 2
Download your city map from Google.

## STEP 3
Using <map> tag name the map.

## STEP 4
Create clickable regions in the image using <area> tag.

## STEP 5
Write HTML programs for all the regions identified.

## STEP 6
Execute the programs and publish them.

# CODE
~~~~~~~~~~~~~~~~

map_image.html 

{% load static %}
<!DOCTYPE html>

<html>
    <head>
        <title>Image Map</title>
        <link rel="stylesheet" href="{% static 'CSS.css' %}">
        <link rel="icon" href="{% static 'mapicon.png' %}"

    </head>
    <body class="main-page">
        <center>
            <h1> <u><b>CHENNAI </b></u>
        </center>
    </h1>
    <center>
        <img src="{% static 'mapp_ss.png'%}" usemap="#image_map" class="center-img">
        <map name="#image_map">
            <area shape="rect" coords="500,440,370,301" alt="Ractangle" href="/mount" title="St.Thomas Mount">
            <area shape="circle" coords="141,523,109" alt="Circle" href="/flight" title="Chennai International Airport"> 
            <area shape="rect" coords="770,10,900,100" alt="Ractangle" href="/shop" title="T.Nagar">
            <area shape="circle" coords="1220,200,110" alt="Circle" href="/church" title="Santhome Cathedral Bascilica">
            <area shape="circle" coords="1100,460,75" alt="Circle" href="/beach" title="Adyar Beach">

        </map>
    </center>
    </body>
</html>
-----

Mount.html

{% load static %}
<html>
    <head>
        <title>St.Thomas Mount</title>
        <link rel="stylesheet" href="{% static 'CSS.css' %}">
        <link rel="icon" href="{% static 'mounticon.png' %}"
    </head>
    
    <body class="new-page mount1">
        <center>
            <h2 class="page-title">St.Thomas Mount</h2>
            <img src="{% static 'st.thomas.jpg'%}" height="600" width="700">
            <div class="right-text">
        <p> St. Thomas Mount is a historic and sacred site in Chennai, Tamil Nadu, named after St. Thomas, one of the twelve apostles of Jesus Christ, who is believed to have been martyred there in the 1st century AD. The mount is home to the St. Thomas Mount National Shrine Basilica, a hilltop church built by the Portuguese in the 16th century, which attracts pilgrims and tourists from across India and abroad. Visitors can climb a series of stone steps to reach the church, where they can see the Bleeding Cross, an ancient cross carved into the rock, believed by devotees to have miraculous powers. The hill offers panoramic views of Chennai city and the surrounding areas, including the nearby Guindy neighborhood and the Chennai International Airport. St. Thomas Mount not only holds religious significance but also represents the rich cultural and colonial heritage of the city, making it a popular destination for history enthusiasts, pilgrims, and casual visitors alike. The area around the mount has developed into a lively neighborhood with markets, educational institutions, and transport links, blending spiritual tradition with urban life.
        </p>
        </center>
        </div>
    </body>
</html>
------

Flight.html

{% load static %}
<html>
    <head>
        <title>Chennai International Airport</title>
        <link rel="stylesheet" href="{% static 'CSS.css' %}">
        <link rel="icon" href="{% static 'flighticon.png' %}"
    </head>

    <body class="new-page flight1">
        <center>
            <h2 class="page-title">Chennai International Airport, Meenambakam</h2>
            <img src="{% static 'airport.jpg' %}" height="600" width="700">
            <div class="right-text">
        <p>
            Chennai International Airport is the primary airport serving Chennai, Tamil Nadu, and one of the busiest airports in South India. It is located in the Tirusulam area, close to the city center, and is easily accessible from major neighborhoods including St. Thomas Mount and Guindy. The airport has two passenger terminals: Terminal 1 for domestic flights and Terminal 4 for international flights, handling millions of travelers every year. It serves as a major hub for both domestic and international airlines, connecting Chennai to cities across India, Asia, the Middle East, Europe, and beyond. The airport is equipped with modern facilities including lounges, shopping areas, restaurants, and efficient transport services like taxis, buses, and the nearby metro station. Over the years, Chennai International Airport has expanded its runways and terminals to accommodate growing passenger traffic, making it a key gateway for trade, tourism, and business in South India. Its proximity to important landmarks, IT hubs, and industrial zones enhances its strategic importance for the city and the region.
        </p>
        </center>
        </div>
    </body>
</html>
-------

Shop.html

{% load static %}
<html>
    <head>
        <title>T.Nagar</title>
        <link rel="stylesheet" href="{% static 'CSS.css' %}">
        <link rel="icon" href="{% static 'shopicon.png' %}"
    </head>
    <body class="new-page shop1">
        <center>
            <h2 class="page-title">Pondy Bazaar, T.Nagar</h2>
            <img src="{% static 'Tnagar.jpg' %}"height="600" width="690">
            <div class="right-text">
        <p>
            T. Nagar is one of Chennai’s most vibrant and bustling commercial hubs, famous for its shopping streets, jewelry stores, textile showrooms, and traditional South Indian clothing. It is considered the heart of Chennai’s retail scene, attracting shoppers from across the city and neighboring states, especially during festival seasons. Pondy Bazaar, located within T. Nagar, is one of the busiest streets, offering a mix of branded stores, street vendors, electronics shops, and food stalls. The area is always crowded with locals and tourists looking for bargains, festive shopping, or a lively market experience. T. Nagar and Pondy Bazaar are easily accessible by road, buses, and the Chennai Metro, and their mix of modern retail outlets and traditional bazaars reflects the city’s commercial energy. Beyond shopping, the area also has theaters, restaurants, and cultural landmarks, making it a complete destination for entertainment and urban life in Chennai.
        </p>
        </center>
        </div>
    </body>
</html>
--------

Church.html

{% load static %}
<html>
    <head>
        <title>Santhome Cathedral Basilica</title>
        <link rel="stylesheet" href="{% static 'CSS.css' %}">
        <link rel="icon" href="{% static 'churchicon.png' %}"
    </head>

    <body class="new-page church1">
        <center>
            <h2 class="page-title">Santhome Cathedral Basilica, Mylapore</h2>
            <img src="{% static 'santhome.jpg'%}" height="600" width="700">
            <div class="right-text">
        <p>
            Santhome Cathedral Basilica is a historic and revered church located along the Marina Beach in Chennai, Tamil Nadu. It is built over the tomb of St. Thomas the Apostle, who is believed to have brought Christianity to India and was martyred in the 1st century AD. Originally constructed by Portuguese explorers in the 16th century, it was later rebuilt as a Gothic-style cathedral by the British in the 19th century and declared a Minor Basilica by the Vatican in 1956. The basilica is famous for its stunning neo-Gothic architecture, tall spire, stained glass windows, and peaceful interiors, making it a major pilgrimage site for Christians and a popular tourist attraction in Chennai. Every year, thousands of devotees and visitors come to offer prayers and admire its historical and spiritual significance. Its location near the Marina Beach adds to its accessibility and prominence as one of Chennai’s most important religious landmarks.
        </p>
        </center>
    </div>
    </body>
</html>
-------

Beach.html

{% load static %}
<html>
    <head>
        <title>Adyar Beach</title>
        <link rel="stylesheet" href="{% static 'CSS.css' %}">
        <link rel="icon" href="{% static 'beachicon.png' %}"
    </head>

    <body class="new-page beach1">
        <center>
            <h2 class="page-title">Edward Elliot's Beach, Adyar</h2>
            <img src="{% static 'eliot.jpg'%}" height="550" width="700">
            <div class="right-text">
        <p>
            Edward Elliot’s Beach, also known as Bessy, is a popular and picturesque beach in the Besant Nagar area of Chennai, Tamil Nadu. It is named after Edward Elliot, a former governor of Madras, and has become one of the city’s most serene seaside destinations. Unlike the crowded Marina Beach, Bessie offers a quieter and more peaceful environment, making it ideal for morning walks, jogging, meditation, or simply enjoying the sunset. The beach is lined with cafes, restaurants, and small shops, making it a hub for food lovers and families looking for leisure activities. Nearby landmarks include the Ashtalakshmi Temple, the Velankanni Church, and several cultural and recreational centers. Local residents and tourists alike come to relax, socialize, or take part in beach activities such as volleyball and kite flying. The beach is well-maintained and attracts visitors throughout the year, reflecting Chennai’s blend of urban life and coastal charm. Its accessibility from central Chennai and surrounding neighborhoods adds to its popularity as a must-visit destination for anyone exploring the city.
        </p>
        </center>
        </div>
    </body>
</html>
--------

CSS.css

body.main-page{
    background-color: rgb(0, 0, 0); 
    color: white;
    font-family: "Palatino Linotype"; 
    margin-left: auto;
    margin-right: auto;
    padding: 10px;
    text-align: center;
}

body.main-page img {
    height: 600px;         
    width: 1380px;            
    border: 4px solid rgb(203, 203, 203); 
    
}

body.new-page {
    background-color: black;
    color: white;
    font-family:"Lucida Calligraphy";
    margin-left: auto;
    margin-right: auto;
    padding: 10px;
}
body.mount1 h2.page-title {
    color: rgb(65, 65, 227);
}

body.flight1 h2.page-title{
    color: rgb(254, 190, 71);
}

body.shop1 h2.page-title{
    color: rgb(36, 155, 0);
}

body.church1 h2.page-title{
    color: rgb(255, 53, 53);
}

body.beach1 h2.page-title{
    color: rgb(254, 190, 71);
}

p{
    font-family:"Palatino Linotype";
    font-size: 23.5px;
}

.left-img {
    float: left;
    border: 2px solid gray;
    width: 50%;
    margin-right: 20px;
}

.right-text {
    float: right;
    width: 50%;
    text-align: left;
    color: white;
   
}
--------
urls.py 

from django.urls import path
from mapp_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mount', views.mount, name='mount'),
    path('flight', views.flight, name='flight'),
    path('shop', views.shop, name='shop'),
    path('church', views.church, name='church'),
    path('beach', views.beach, name='beach'),
]
------

views.py
from django.shortcuts import render

def home(request):
    return render(request,'map_image.html')

def mount(request):
    return render(request,'Mount.html')

def flight(request):
    return render(request,'Flight.html')

def shop(request):
    return render(request,'Shop.html')

def church(request):
    return render(request,'Church.html')

def beach(request):
    return render(request,'Beach.html')
-------


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# OUTPUT
~~~~~~~

mapout.png
mountout.png
airportout.png
tnagarout.png
santhomeout.png
beachout.png

~~~~~~~

# RESULT
The program for implementing image maps using HTML is executed successfully.
