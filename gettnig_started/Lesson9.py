def initialize(context) :
    
    context.aapl = sid(24)
    
    schedule_function( rebalance, date_rules.every_day(), time_rules.market_open())
    
    set_slippage(slippage.VolumeShareSlippage(volume_limit=0.025, price_impact=0.1))
    set_commission(commission.PerShare(cost=0.0075, min_trade_cost=1.00))
    
def rebalance(context,data):

    order_target_percent( context.aapl, 1.0)