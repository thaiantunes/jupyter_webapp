from math import ceil

def food_calc(guests, veggie_guests, red, chicken, corn):
    num_tomato = ceil((guests-veggie_guests) + 1.5*veggie_guests)
    num_zucchini = ceil((guests-veggie_guests) + 1.2*veggie_guests)
    num_onions = ceil(((guests-veggie_guests) + 1.5*veggie_guests)*0.8)
    if corn=='Yes':
        num_corn = ceil((guests-veggie_guests) + 1.5*veggie_guests)
    else:
        num_corn = None
    if red=='Yes' and chicken=='No':
        num_red = (guests-veggie_guests) * 500
        num_chicken = None
    elif red=='No' and chicken=='No':
        num_red = None
        num_chicken = None
    elif red=='No' and chicken=='Yes':
        num_red = None
        num_chicken = (guests-veggie_guests) * 600
    else:
        num_red = (guests-veggie_guests) * 250
        num_chicken = (guests-veggie_guests) * 300
    return num_tomato, num_zucchini, num_onions, num_corn, num_red, num_chicken


