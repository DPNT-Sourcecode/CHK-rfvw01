

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    print(skus)
    # price_table_and_offers = {
    #     "A": {"price": 50, "special_offers": (3, 130)},
    #     "B": {"price": 30, "special_offers": (2, 45)},
    #     "C": {"price": 20},
    #     "D": {"price": 15}
    # }

    # total_checkout_cost = 0
    # quantity = {}

    # for item, quantity in skus.items():
    #     if item in price_table_and_offers:
    #         item_info = price_table_and_offers[item]
    #         item_price = item_info["price"]

    #         if "special"









# define the pricings in dict
#loop through the skus - thing its just the items [A, B,A,C,D]
#if item is in the dict : - get the price
#  
# if item in dict AND theres a special offer - return the quantity and price - figure out if quantity is big enough for special offer (%)
#Add special offer price to total checkout cost and normal price on remainder
# Add items that doen't have special offers to the total 
#If item in cart isn't in the dict return -1