def initialize(context):
    
    context.security = sid(40768)
    
    
def handle_data(context,data):
    
    order_target_percent(context.security, 1.00)
    
    print 'Cash: %.2f' % context.portfolio.cash