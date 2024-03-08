from typing import TypeVar
import requests

CLIENT_DATA: dict = {}
URL: str = ""
VAR_NAME = TypeVar("VAR_NAME")
VAR_TYPE = TypeVar("VAR_TYPE")
VAR_VALUE = TypeVar("VAR_VALUE")

class Login:
    def __init__(self, username, token, url):
        global URL

        self.url = url
        URL += url
        CLIENT_DATA['user_name'] = username
        CLIENT_DATA['user_token'] = token

class Multi:
    def __init__(self, var: VAR_NAME, type: VAR_TYPE, value: VAR_VALUE):
        self.var = var
        self.type = type
        self.value = value

    def Var(self):
        CLIENT_DATA['var_name'] = self.var
        CLIENT_DATA['var_type'] = self.type
        CLIENT_DATA['var_value'] = self.value

class Var:
    def __init__(self, var: VAR_NAME, type: VAR_TYPE, value: VAR_VALUE) -> None:
        self.var_name = var
        self.var_type = type
        self.var_value = value

    def creat(self):
        CLIENT_DATA['var_name'] = self.var_name
        CLIENT_DATA['var_type'] = self.var_type
        CLIENT_DATA['var_value'] = self.var_value
        return put_request(URL + "/API-CREAT", data=CLIENT_DATA)

    def multi_var(self):
        CLIENT_DATA['var_name'] = self.var_name
        CLIENT_DATA['var_type'] = self.var_type
        CLIENT_DATA['var_value'] = self.var_value
        return put_request(URL + "/API-CREAT-Multi", data=CLIENT_DATA)

    @staticmethod
    def delete(Var_ID:str):
        CLIENT_DATA['id'] = Var_ID
        return delete_request(URL + "/API-DEL",data=CLIENT_DATA)
    
    @staticmethod
    def clear_all():
        return clear_request(URL + "/API-CLEAR",data=CLIENT_DATA)
    
    @staticmethod
    def total_var():
        return total_request(URL + "/API-TOTALVAR",data=CLIENT_DATA)

    @staticmethod
    def get(VAR_ID: str):
        CLIENT_DATA["id"] = VAR_ID
        return get_request(URL + "/API-GET", data=CLIENT_DATA)

    @staticmethod
    def update(OLD_VAR: VAR_NAME, NEW_VAR: VAR_NAME, TYPE: VAR_TYPE, VALUE: VAR_VALUE):
        CLIENT_DATA["var_name"] = OLD_VAR
        CLIENT_DATA["new_name"] = NEW_VAR
        CLIENT_DATA["new_type"] = TYPE
        CLIENT_DATA["new_value"] = VALUE
        return put_request(URL + "/API-UPDATE", data=CLIENT_DATA)

def put_request(url: str, data: dict):
    try:
        http = requests.put(url,json=data)
        return http.text
    except ConnectionRefusedError as e:
        print(f"Error http: {e}")

def delete_request(url:str,data:dict):
    try:
        http = requests.delete(url,json=data)
        return http.text
    except ConnectionRefusedError as e:
        print(e)

def clear_request(url:str,data:dict):
    try:
        http = requests.delete(url,json=data)
        return http.text
    except ConnectionRefusedError as e:
        print(e)

def total_request(url: str, data: dict):
    try:
        http = requests.get(url,json=data)
        return http.text
    except ConnectionRefusedError as e:
        print(f"Error http: {e}")


def get_request(url: str, data: dict):
    try:
        http = requests.get(url,json=data)
        return http.text
    except ConnectionRefusedError as e:
        print(f"Error http: {e}")

