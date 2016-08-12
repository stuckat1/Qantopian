def initialize(context):

    context.security_list = [sid(5061), sid(7792), sid(1941), sid(24556), sid(1746)]

    schedule_function(rebalance,
                      date_rules.week_start(days_offset=0),
                      time_rules.market_open())

    schedule_function(record_vars,
                      date_rules.every_day(),
                      time_rules.market_close())

def compute_weights(context, data):

    hist = data.history(context.security_list, 'price', 30, '1d')

    prices_10 = hist[-10:]
    prices_30 = hist

    sma_10 = prices_10.mean()
    sma_30 = prices_30.mean()

    raw_weights = (sma_30 - sma_10) / sma_30

    normalized_weights = raw_weights / raw_weights.abs().sum()
    
    return normalized_weights

def rebalance(context, data):

    weights = compute_weights(context, data)

    for security in context.security_list:
        if data.can_trade(security):
            order_target_percent(security, weights[security])

def record_vars(context, data):

    longs = shorts = 0
    for position in context.portfolio.positions.itervalues():
        if position.amount > 0:
            longs += 1
        elif position.amount < 0:
            shorts += 1

    record(leverage=context.account.leverage, long_count=longs, short_count=shorts)
