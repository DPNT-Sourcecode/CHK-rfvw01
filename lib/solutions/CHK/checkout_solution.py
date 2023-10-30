

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_table_and_offers = {
        "A": {"price": 50, "special_offers": (3, 130)},
        "B": {"price": 30, "special_offers": (2, 45)},
        "C": {"price": 20},
        "D": {"price": 15}
    }

    total_checkout_cost = 0
    quantity = {}

    for item in skus:
        if item in price_table_and_offers:
            if item in quantity:
                quantity[item] += 1
            else:
                quantity[item] = 1
        else:
            return -1

    for item, quantity in quantity.items():
        item_info = price_table_and_offers[item]
        item_price = item_info["price"]

        if "special_offers" in item_info:
            special_quant, special_price = item_info["special_offers"]
            special_count = quantity // special_quant
            special_remainder_count = quantity % special_quant

            total_checkout_cost += special_count * special_price
            total_checkout_cost += special_remainder_count * item_price
        
        else:
            total_checkout_cost += quantity * item_price
    
    return total_checkout_cost
