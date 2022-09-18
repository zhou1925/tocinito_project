# The extractors are charge of extract the data of the API endpoint
import json
from requests import get, post
from auth import *
from datetime import date, timedelta


token = get_token()
headers = {'Authorization': f'Bearer {token}'}

def get_all_orders():
    """ Return All the orders of the last 7 days """

    r = get(endpoint + "/orders/", headers=headers)
    return r.json()


def get_orders_by_date(date_before, date_after):
    """ 
    return orders by date:
    date_before: 2022-09-13
    date_after: 2022-09-10
    """

    query = f'/orders/?date_stamp_before={date_before}&date_stamp_after={date_after}'
    r = get(endpoint + query, headers=headers)
    return r.json()


def get_last_week_orders():
    """ return last week orders """

    today = date.today()
    last_week = today - timedelta(weeks=1)
    orders = get_orders_by_date(str(today), str(last_week))
    return orders

def get_today_orders():
    """ get the today orders """

    today = date.today()
    orders = get_orders_by_date(str(today), str(today))
    return orders
