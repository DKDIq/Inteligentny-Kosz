import random

from fastapi import FastAPI, Request, Form, Depends, HTTPException,Cookie,Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi import FastAPI, WebSocket, WebSocketDisconnect,Response

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

waiting_clients = []
templates = Jinja2Templates(directory="templates")

import pymysql


def check_cookie(request: Request, cookie_name: str):
    return request.cookies.get(cookie_name)





def set_login_cookie(response: Response, username: str):
    token = str(random.randint(10000, 200000)) #wiem ze jest szansa na wygenerowanie dla 2 uzytkownikow takiego samego pliku cookie co spowoduje blad jednak to jedynie prototyp wiec postanowilem zajac sie najwazniejszymi sprawami najpierw
    connection = get_db_connection()

    try:
        with connection.cursor() as cursor:
            sql = "UPDATE uzy SET cookie = %s WHERE nick = %s"
            cursor.execute(sql, (token, username))
            connection.commit()
            print("Token zapisany w bazie danych dla użytkownika:", username)

    except pymysql.MySQLError as e:
        print(f"Nie udało się zapisać tokena w bazie danych: {e}")

    finally:
        connection.close()

    response.set_cookie(
        key="auth_token",
        value=token,
        max_age=3600,
        httponly=True,
        secure=False,
        samesite="Strict",
        path="/"
    )

    return token
def get_db_connection():
    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            user="TOMASZ",
            password="root",
            database="kosz",
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Połączono z bazą danych MySQL")
        return conn

    except pymysql.MySQLError as e:
        print(f"Nie udało się połączyć z bazą danych: {e}")
        return None




@app.get("/")
def read_root(request: Request):
    if check_cookie(request,"auth_token"):
        return RedirectResponse(url="/dashboard/", status_code=302)
    return RedirectResponse(url="/register/", status_code=302)


@app.get("/login/")
def login(request: Request):
    if check_cookie(request,"auth_token"):
        print("test")
        return RedirectResponse(url="/dashboard/", status_code=302)
    template_response = templates.TemplateResponse("login.html", {"request": request})
    return template_response

@app.get("/register/")
def register(request: Request):
    if check_cookie(request,"auth_token"):
        print("test")
        return RedirectResponse(url="/dashboard/", status_code=302)
    return templates.TemplateResponse("register.html", {"request": request, "error": ""})

@app.get("/dashboard/")
def dashboard(request:Request,response: Response):
    cookie=check_cookie(request,"auth_token")
    conn = get_db_connection()
    if conn is None:
        return RedirectResponse(url="/register/", status_code=302)
    print("SDADADAD")

    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM uzy WHERE cookie = %s', (cookie,))
        existing_user = cursor.fetchone()
        print("SDADADAD")

        if not existing_user:
            print("ASDDA")
            response = RedirectResponse(url="/register/", status_code=302)
            response.delete_cookie(key="auth_token")
            return response
        print("SDADADAD")
        conn.close()

    print("DSDAd")
    data = {
        "account": existing_user["nick"],
        "device_id": existing_user["id"],
        "categories": [
            {"name": "Plastik", "progress": existing_user["pl"], "count": existing_user["pl1"]},
            {"name": "Papier", "progress": existing_user["pap"], "count": existing_user["pap1"]},
            {"name": "Szkło", "progress": existing_user["szkl"], "count": existing_user["szkl1"]},
            {"name": "Mieszane", "progress": existing_user["miesz"], "count": existing_user["miesz1"]},
        ],
        "announcements": [
            "SEGREGUJ SMIECI!",
            "SEGREGUJ SMIECI",
            "SEGREGUJ SMIECI",
            "Śledź aktualizacje i nowe funkcje aplikacji!"
        ]
    }

    return templates.TemplateResponse("dashboard.html", {"request": request, "data": data})





@app.post("/login/")
def login_przycisk(response:Response,request: Request, username: str = Form(...), password: str = Form(...)):
    print(username,password)
    print("DDADADADADAD")
    conn = get_db_connection()
    if conn is None:
        error_message = "We having trouble with servers please try again later"
        return templates.TemplateResponse("login.html", {"request": request, "error": error_message})
    print("DDADADADADAD")

    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM uzy WHERE nick = %s', (username,))
        user = cursor.fetchone()
        print("DDADADADADAD")
        if user is None:
            error_message = "We did not found account with this nickname"
            return templates.TemplateResponse("login.html", {"request": request, "error": error_message})
        print("DDADADADADAD")

        if user['haslo'] != password:
            error_message = "Incorrect Password!"
            return templates.TemplateResponse("login.html", {"request": request, "error": error_message})
        print("DDADADADADAD")

    conn.close()

    set_login_cookie(response,username)

    redirect_response = RedirectResponse(url="/dashboard/", status_code=302)

    for header, value in response.headers.items():
        redirect_response.headers[header] = value

    return redirect_response

@app.post("/register/")
def register_przycisk(response:Response,request: Request, username: str = Form(...), password: str = Form(...),
                      password1: str = Form(...), deviceId: str = Form(...)):
    print(f"USERNAME: {username}, PASSWORD: {password}, PASSWORD1: {password1}, id: {deviceId}")



    conn = get_db_connection()
    if conn is None:
        error_message = "We having trouble with servers please try again later"
        return templates.TemplateResponse("register.html", {"request": request, "error": error_message})
    print("SDADADAD")

    with conn.cursor() as cursor:

        cursor.execute('SELECT * FROM uzy WHERE nick = %s', (username,))
        existing_user = cursor.fetchone()
        print("SDADADAD")

        if existing_user:
            error_message = "Account with that nickname is already exist"
            return templates.TemplateResponse("register.html", {"request": request, "error": error_message})
        print("SDADADAD")
        cookie = str(random.randint(10000, 200000))
        response.set_cookie(key="auth_token", value=cookie, httponly=True)
        cursor.execute('INSERT INTO uzy (nick, haslo,id,cookie) VALUES (%s, %s, %s, %s)',
                       (username, password, deviceId, cookie))
        conn.commit()
        conn.close()


        print("SDADADAD")


    redirect_response = RedirectResponse(url="/dashboard/", status_code=302)

    for header, value in response.headers.items():
        redirect_response.headers[header] = value

    return redirect_response


