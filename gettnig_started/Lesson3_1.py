 
def initialize(context):
    
    context.aapl = sid(24)
    
    
def handle_data(context,data):
    
    order_target_percent( context.aapl, 1.0)