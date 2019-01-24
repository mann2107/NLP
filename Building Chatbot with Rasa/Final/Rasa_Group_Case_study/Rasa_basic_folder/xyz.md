## Generated Story 3127653402550674617
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_validity
    - slot{"valid_res": true}
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_price_range
* restaurant_search{"price_range": "300"}
    - slot{"price_range": "300"}
    - action_restaurant
    - slot{"restaurant_details": []}
    - utter_affirm
    - export

