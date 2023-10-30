

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

#     +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+
#special offer (quantity of item, price/another item?)
    price_table_and_offers = {
        "A": {"price": 50, "special_offers": [(3, 130), (5,200)]},
        "B": {"price": 30, "special_offer": (2, 45)},
        "C": {"price": 20},
        "D": {"price": 15},
        "E": {"price": 40, "special_offer": (2, "B")}
    }

    total_checkout_cost = 0
    quantity_count = {}
    # special_offer_items = {}

    for item in skus:
        if item in price_table_and_offers:
            if item in quantity_count:
                quantity_count[item] += 1
            else:
                quantity_count[item] = 1
        else:
            return -1

    for item, quantity in quantity_count.items():
        if item in price_table_and_offers:
            item_info = price_table_and_offers[item]
            item_price = item_info["price"]

            if "special_offers" in item_info:
                for special_quant, special_deal in item_info["special_offers"]:
                    special_count = quantity // special_quant
                    total_checkout_cost += special_count * special_deal
                    special_remainder_count = quantity % special_quant
            elif "special_offer" in item_info:
                special_quant, special_deal = item_info["special_offers"]
                special_count = quantity // special_quant
                total_checkout_cost += special_count * special_deal
                special_remainder_count = quantity % special_quant

            total_checkout_cost += special_remainder_count * item_price
                # if special_quant == 2 and special_deal == "B":
                #     special_offer_items["E"] = special_offer_items.get("E", 0)+1
                # else:
                #     special_quant, special_deal = item_info["special_offers"]
                #     special_offer_items[item] = special_offer_items.get(item, 0)+1


            # special_count = quantity // special_quant
            # special_remainder_count = quantity % special_quant

            # total_checkout_cost += special_count * special_price
            # total_checkout_cost += special_remainder_count * item_price
        
        else:
            return -1
        
    if "E" in quantity_count and "B" in quantity_count:
        b_count = quantity_count["E"]
        e_count = quantity_count["B"]
        free_bs = e_count // 2
        
        if free_bs <= b_count:
            total_checkout_cost -= (free_bs * price_table_and_offers["B"]["price"])
    
    return total_checkout_cost

    # for item, quantity in special_offer_items.items():
    #     item_info = price_table_and_offers[item]
    #     special_quant, special_deal = item_info["special_offers"]
    #     if special_quant == 2 and special_deal == "B":
    #         item_price = item_info["price"]
    #         b_count = special_offer_items.get("B", 0)
    #         e_count = quantity // 2
    #         free_bs = min(b_count,e_count)
    #         total_checkout_cost += (quantity - free_bs) * item_price

    
    # return total_checkout_cost


