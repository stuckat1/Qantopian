def initialize(context):
    
    context.aapl = sid(24)
    context.spy = sid(8554)
    
    schedule_function( rebalance, date_rules.every_day(), time_rules.market_open())
    schedule_function( record_vars, date_rules.every_day(), time_rules.market_close())
    
def rebalance(context,data):

    order_target_percent( context.aapl, 0.50)
    order_target_percent( context.spy, -0.50)
    
    
def record_vars(context,data):

    positions = context.portfolio.positions
    
    print positions.keys()
    