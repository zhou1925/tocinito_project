from extractors import get_last_week_orders
from transformers import orders_to_df, generate_report
from loaders import upload_file
  
  
def lambda_handler(event, context):

    orders_json = get_last_week_orders()
    orders_df = orders_to_df(orders_json)

    report_txt = generate_report(orders_df)
    upload_file(report_txt,'jobs-api-zhou')

