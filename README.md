# MSPazaryeri
in development
colosus.pythonanywhere.com

Usage
```
pip install -r requirements.txt 
python manage.py makemigrations
python manage.py migrate
ceate and add secret key for settings
python manage.py runserver
```
```
PUT /musteriler
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 1
  },
  "mappings": {
    "properties": {
      "ad": {
        "type": "text"
      },
      "soyad": {
        "type": "text"
      },
      "yas": {
        "type": "integer"
      },
      "email": {
        "type": "keyword"
      },
      "adres": {
        "type": "text"
      }
    }
  }
}
```
