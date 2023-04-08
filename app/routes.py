from flask import render_template, flash, redirect, url_for
from app import app
import os
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
from googleapiclient.discovery import build
from app.models import Orders
from app import db
import requests
import xml.etree.ElementTree as ET

def get_service_sacc():
    creds_json = os.path.dirname(__file__) + "/creds/sacc1.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)

def ord_rub(dt):
    pass
    resp = requests.post(f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={dt}')
    root = ET.fromstring(resp.text)
    for valuteid in root.findall('Valute'):  # /Value'):
        if valuteid.attrib['ID'] == 'R01235':
            for value in valuteid.findall('Value'):
                dig = float(value.text.replace(',', '.'))
                return dig

def google():
    service = get_service_sacc()
    sheet = service.spreadsheets()
    sheet_id = "1fqmR2r3vap2Zf_b0pJ2IdJDZ5tt_rdDConlrj3jRaQ0"
    resp = sheet.values().get(spreadsheetId=sheet_id, range="Лист1").execute()
    resp2 = resp['values']
    resp2.pop(0)
    return resp2

@app.route('/')
@app.route('/index')
def index():
    resp=google()
    for r in resp:
        pass
        ord_s=float(r[2])
        date=r[3].replace('.','/')
        ord_r=ord_rub(date)
        ord = Orders(num=int(r[0]),num_ord=int(r[1]),cost_s=ord_s,date=date,cost_r=round(ord_s*ord_r,2))
        db.session.add(ord)
    ords=Orders.query.all()
    return render_template('index.html', ords=ords)
