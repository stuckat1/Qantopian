


def initialize(context):
    
    context.spy = sid(8554)
    
    schedule_function( open_position, date_rules.week_start(), time_rules.market_open())
    schedule_function( close_position, date_rules.week_end(), time_rules.market_close(minutes=30))
    
    
def open_position(context, data):
    print 'Opening'
    order_target_percent(context.spy, 0.10)
    

def close_position(context,data):
    print 'Closing'
    order_target_percent(context.spy, 0)