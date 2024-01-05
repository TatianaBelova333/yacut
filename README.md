# Yacut Service

## Description

The web version of this application allows any users to get a short version of long urls.
Users may create their own versions of short urls containing up to sixteen characters (ascii letters and digits only). If a user doesn't provide a short url, the short url will be generated automatically (6 characters).
![Yacut index_page](/yacut/static/img/readme/yacut_index.png "Yacut index_page")

The API version has two endpoints that allow to create a short link and get the original link by a short id.


## Installation

Clone the repository

```
git clone https://github.com/TatianaBelova333/yacut.git
```

```
cd yacut
```

Create and activate a virtual environement

```
python3 -m venv venv
```

* For Linux/macOS

    ```
    source venv/bin/activate
    ```

* For Windows

    ```
    source venv/scripts/activate
    ```

Install all dependencies from requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

## SOME REST API EXAMPLES

Full documentation is available in openapi.yml.

#### Get the original url by a valid short_id

`GET /api/id/{short_id}/`

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "url": "string"
}
```
#### Get the original url by a non-existent short_id
```
HTTP/1.1 404 Not Found
Content-Type: application/json

{
    "message": "Указанный id не найден."
}
```

#### Create a short url

`POST /api/id/`

```
Request body

{
  "url": "string",
  "custom_id": "string"
}
```

```
HTTP/1.1 201 OK
Content-Type: application/json
{
  "url": "string",
  "short_link": "string"
}
```

#### Attempt to create an invalid short url
```
Request body

{
  "url": "string",
  "custom_id": ".....f/"
}
```

```
HTTP/1.1 400 Bad request
Content-Type: application/json
{
  "message": "Указано недопустимое имя для короткой ссылки"
}
```

### Authors
[Tatiana Belova](https://github.com/TatianaBelova333)