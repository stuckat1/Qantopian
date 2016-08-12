

def initialize(context):
#    context.sec = [sid(24), sid(8554), sid(50161)]
    context.sec = [sid(24), sid(8554)]
     

def handle_data(context,data):
    
    hist = data.history(context.sec, ['low','high'], 5, '1m')
    
    means = hist.mean()
    
    mean_lows = means['low']
    mean_highs = means['high']
    
    print '---low ----'
    print hist['low']
    print mean_lows
    
    print '---hi ----'
    print hist['low']
    print mean_highs
    