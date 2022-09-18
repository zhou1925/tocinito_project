from pandas import json_normalize
from datetime import date
import pandas as pd

def normalize_orders_df(orders_df):
    """ normalize dataframe and convert datatypes """

    df = orders_df.explode('product')  
    df['date'] = pd.to_datetime(df['date'])
    df['time'] = pd.to_timedelta(df['time'])
    df['Hour'] = df['time'].dt.components['hours']
    return df

def orders_to_df(data):
    """ get orders json data and return a df """
    order_items_list = []
    order_ids = []
    order_date_list = []
    order_time_list = []

    # 1: get order ids
    for order in data:
        order_ids.append(order['id'])
    
    # 2 get items of each order
    order_items = []
    for order in data:
        order_date_list.append(order['date_stamp'])
        order_time_list.append(order['time_stamp'])

        for item in order['items']:
            order_item = item['product']['title']
            order_items.append(order_item)
        order_items_list.append(order_items)
        order_items = []

    orders_data = {'order_id': order_ids, 'product': order_items_list, 'date': order_date_list, 'time':order_time_list}
    
    df = pd.DataFrame(orders_data) # create dataframe
    df = normalize_orders_df(df) # normalize dataframe
    return df

def count_products(df):
    """ count products from data frame """
    product_group = df['product'].value_counts()
    product_group = product_group.to_dict().items()
    return dict(product_group)

def orders_by_hour(df):
    """ return products sell by hour """

    df = df.groupby(['Hour']).count()
    data = df.to_dict()['order_id']
    return data

def create_txt_file():
    filename = str(date.today()) + "-report" + ".txt"
    file = open(filename,"w+")
    return file

def generate_report(orders_df):
    """ generate report from orders dataframe """
    count_products_report = count_products(orders_df)
    orders_by_hour_report = orders_by_hour(orders_df)
    file = create_txt_file()
    file.write(f"====== REPORT {str(date.today())} ======")
    file.write("\n#PRODUCTS FREQUENCY")
    for product, quantity in count_products_report.items():
        file.write(f"\nProducto: {product}: {quantity}")
    file.write("\n-------------------")
    file.write("\n#PRODUCTS SELL BY HOUR")
    for hour, quantity in orders_by_hour_report.items():
        file.write(f"\nHora: {hour} Cantidad: {quantity}")
    file.write("\n")
    file.close()
    return file
