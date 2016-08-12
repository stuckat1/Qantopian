def initialize(context):
    
    context.aapl = sid(24)
    context.spy = sid(8554)
    context.msci = sid(35078)
    
    schedule_function( rebalance, date_rules.every_day(), time_rules.market_open())
    schedule_function( record_vars, date_rules.every_day(), time_rules.market_close())
    
def rebalance(context,data):

    order_target_percent( context.aapl, 0.10)
    order_target_percent( context.spy, -0.50)
    order_target_percent( context.msci, -0.40)
    
    
def record_vars(context,data):

    positions = context.portfolio.positions
    
    long_count = 0
    short_count = 0
    
    for security, position in positions.items():
        if position.amount > 0 :
            long_count += 1
        else :
            short_count += 1
            
    record(num_long = long_count, num_short = short_count)