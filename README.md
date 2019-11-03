# DjangoRestApp
This is API for Amazon products.

## Prerequisites
```
pip install dj-database-url==0.5.0
pip install Django==2.2.6
pip install django-heroku==0.3.1
pip install djangorestframework==3.10.3
pip install gunicorn==19.9.0
pip install psycopg2==2.8.4
pip install pytz==2019.3
pip install sqlparse==0.3.0
pip install whitenoise==4.1.4
```

## How to use this API?

-Exapmple of basic usage in Django:

```
def home(request):
    response = requests.get('https://rest-project-amazon.herokuapp.com/products/')
    product = response.json()
    return render(request, 'main/index.html', {
        'results': product['results'],
        })
```

### JSON example of things you can access:
```
{
    "id": 50,
    "title": "Acer Aspire 5 Slim Laptop, 15.6\" Full HD IPS Display, AMD Ryzen 3 3200U, Vega 3 Graphics, 4GB DDR4, 128GB SSD, Backlit Keyboard, Windows 10 in S Mode, A515-43-R19L",
    "rating": "4.30",
    "review_num": 828,
    "price": 309.95,
    "owner": "Acer",
    "user": 1,
    "amazon_link": "https://www.amazon.com//Acer-Display-Graphics-Keyboard-A515-43-R19L/dp/B07RF1XD36/ref=sxin_4_af-pna-1_ffff313b8837e9dbab8675cb72b8efaee75ac48e?keywords=laptop&pd_rd_i=B07RF1XD36&pd_rd_r=de2ace02-32ef-4fc9-b26d-c02ea50a4783&pd_rd_w=KKixR&pd_rd_wg=70Kxt&pf_rd_p=3892bc23-5fa8-4a18-8855-22c23bd2e202&pf_rd_r=AVP8MCTY333XW8JHX2K9&qid=1572801116",
    "url": "https://rest-project-amazon.herokuapp.com/products/50/"
}
```

## Deployment
This project is currently deployed on Heroku. You can visit https://rest-project-amazon.herokuapp.com/products/

## Built with
- Django 2.2.6
- Djano REST Framework 3.10.3

