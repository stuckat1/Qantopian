def initialize(context) :
    context.list = [sid(5061),sid(24)]
    
def handle_data(context,data):
    
    df = data.current( context.list, ['high','lo'])
                    

    print "hi = ", df['high']
    print "lo = ", df['lo']
    
    print data.can_trade(context.list)
    print data.is_stale(context.list)