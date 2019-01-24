## Generated Story -1655879515623881333
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validity
    - slot{"valid_res": "False"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search
    - action_restaurant
    - slot{"restaurant_details": "Found Pa Pa Ya in Dome, Level 4, Select Citywalk, A-3, District Centre, Saket, New Delhi\nFound Berco's in 104, Hazipur, Sector 104, Near Sector 110, Noida\nFound Orient Heritage in Shop 90/61B, Malviya Nagar Market, Malviya Nagar, New Delhi\nFound Berco's in GA-06, Metro Walk Mall, Rohini, New Delhi\nFound Boa Village in 13, Alipur Road, Civil Lines, New Delhi\n"}
    - utter_affirm
* affirm
* restaurant_search
    - utter_goodbye
    - export

