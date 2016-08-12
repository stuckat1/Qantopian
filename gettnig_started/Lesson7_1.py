def initialize(context):
    
    context.spy = sid(24)
    
    schedule_function(check_mean, date_rules.every_day(), time_rules.market_close(minutes=30))
                      
def check_mean(context,data):
     print get_datetime('US/Eastern')
     print data.history(context.spy,'price',10,'1m').mean()
                      