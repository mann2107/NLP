## Generated Story -3538672859105080118
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validity
    - slot{"valid_res": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"price_range": "rs. 300 to 700"}
    - slot{"price_range": "rs. 300 to 700"}
    - action_restaurant
    - slot{"restaurant_details": [{"name": "Saravana Bhavan", "location": "Connaught Place", "rating": "4.3", "cost": 500}, {"name": "Saravana Bhavan", "location": "Janpath", "rating": "4.3", "cost": 500}, {"name": "Andhra Bhavan", "location": "Feroze Shah Road", "rating": "4.1", "cost": 300}]}
    - utter_affirm
* restaurant_search{"email_id": "manish.kumar2107@gmail.com"}
    - slot{"email_id": "manish.kumar2107@gmail.com"}
    - action_email
    - slot{"restaurant_details": [{"name": "Saravana Bhavan", "location": "Connaught Place", "rating": "4.3", "cost": 500}, {"name": "Saravana Bhavan", "location": "Janpath", "rating": "4.3", "cost": 500}, {"name": "Andhra Bhavan", "location": "Feroze Shah Road", "rating": "4.1", "cost": 300}]}
    - utter_mail_sent
* affirm
    - utter_goodbye
    - export

## Generated Story 4688443156950502818
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "cafe"}
    - slot{"location": "cafe"}
    - action_validity
    - slot{"valid_res": false}
    - utter_deny
* goodbye
    - utter_goodbye
    - export

## Generated Story 5776761009378784578
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_validity
    - slot{"valid_res": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price_range
* restaurant_search{"price_range": "700"}
    - slot{"price_range": "700"}
    - action_restaurant
    - slot{"restaurant_details": [{"name": "Earthen Oven", "location": "Candolim", "rating": "4.1", "cost": 1200}, {"name": "The Yellow Chilli", "location": "Penha de Franca", "rating": "4.3", "cost": 1000}, {"name": "Sher E Punjab", "location": "Panaji", "rating": "3.7", "cost": 1300}, {"name": "Cherry Tomato", "location": "Margao", "rating": "3.8", "cost": 1000}, {"name": "Chulha - Grand Hyatt", "location": "Grand Hyatt, Bambolim", "rating": "4.1", "cost": 2500}]}
    - utter_affirm
* goodbye
    - utter_goodbye
    - export

## Generated Story 6890868003473045379
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "delhi"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "delhi"}
    - action_validity
    - slot{"valid_res": true}
    - utter_ask_price_range
* restaurant_search
    - utter_repeat
* 
    - utter_ask_price_range
* restaurant_search{"price_range": "300"}
    - slot{"price_range": "300"}
    - action_restaurant
    - slot{"restaurant_details": [{"name": "Anna Ka Dosa", "location": "Kalkaji", "rating": "3.9", "cost": 200}, {"name": "Andhra Bhavan", "location": "Feroze Shah Road", "rating": "4.1", "cost": 300}]}
    - utter_affirm
* deny
    - utter_goodbye
    - export



## Generated Story -8417560050544373599
* greet
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "asansol"}
    - slot{"location": "asansol"}
    - action_validity
    - slot{"valid_res": true}
    - utter_ask_price_range
* restaurant_search{"price_range": ">700"}
    - slot{"price_range": ">700"}
    - action_restaurant
    - slot{"restaurant_details": [{"name": "American Food House", "location": "Bodakdev", "rating": "3.7", "cost": 900}, {"name": "Cellad Eatery", "location": "Gulbai Tekra", "rating": "4.0", "cost": 800}, {"name": "American Food House", "location": "Bopal", "rating": "3.3", "cost": 900}]}
    - utter_affirm
* affirm
    - utter_ask_email_id
* send_email{"email_id": "manish.kumar2107@gmail.com"}
    - slot{"email_id": "manish.kumar2107@gmail.com"}
    - action_email
    - slot{"restaurant_details": [{"name": "American Food House", "location": "Bodakdev", "rating": "3.7", "cost": 900}, {"name": "Cellad Eatery", "location": "Gulbai Tekra", "rating": "4.0", "cost": 800}, {"name": "American Food House", "location": "Bopal", "rating": "3.3", "cost": 900}]}
    - utter_mail_sent
* affirm
    - utter_goodbye
    - export

## Generated Story -8779036160979671308
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "18328"}
    - slot{"location": "18328"}
    - action_validity
    - slot{"valid_res": false}
    - utter_deny
* deny
    - utter_goodbye
    - export

## Generated Story 5845981793056761060
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_validity
    - slot{"valid_res": true}
    - utter_ask_price_range
* restaurant_search
    - utter_repeat
    - utter_ask_price_range
* restaurant_search{"price_range": "rs. 300 to 700"}
    - slot{"price_range": "rs. 300 to 700"}
    - action_restaurant
    - slot{"restaurant_details": [{"name": "Tortilla's", "location": "Panjagutta", "rating": "3.4", "cost": 500}, {"name": "Rooster", "location": "Madhapur", "rating": "3.4", "cost": 450}]}
    - utter_affirm
* goodbye
    - utter_goodbye
    - export

## Generated Story -5245651431740489544
* greet
    - utter_greet
* restaurant_search{"location": "amritsar"}
    - slot{"location": "amritsar"}
    - action_validity
    - slot{"valid_res": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price_range
* restaurant_search{"price_range": "300 to 700"}
    - slot{"price_range": "300 to 700"}
    - action_restaurant
    - slot{"restaurant_details": [{"name": "Pizza Italia", "location": "Lawrence Road", "rating": "4.1", "cost": 600}, {"name": "Pizza Italia", "location": "Ranjit Avenue", "rating": "4.0", "cost": 500}, {"name": "Italian Pizza", "location": "Hathi Gate", "rating": "3.6", "cost": 600}, {"name": "Deep Pizzeria", "location": "Mohan Nagar", "rating": "3.5", "cost": 600}, {"name": "Crown's Pizza", "location": "Hathi Gate", "rating": "3.1", "cost": 400}]}
    - utter_affirm
* goodbye
    - utter_goodbye
    - export

## Generated Story 7014658787428235043
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "meerut"}
    - slot{"cuisine": "italian"}
    - slot{"location": "meerut"}
    - action_validity
    - slot{"valid_res": true}
    - utter_ask_price_range
* restaurant_search{"price_range": "300 - 700"}
    - slot{"price_range": "300 - 700"}
    - action_restaurant
    - slot{"restaurant_details": [{"name": "Pizza By The Way", "location": "Sadar Bazaar", "rating": "3.2", "cost": 400}, {"name": "Domino's Pizza", "location": "Shastri Nagar", "rating": "3.4", "cost": 400}, {"name": "Domino's", "location": "Shastri Nagar", "rating": "3.4", "cost": 400}, {"name": "Domino's", "location": "Shopprix Mall, Mohkam Pur", "rating": "3.3", "cost": 400}]}
    - utter_affirm
* goodbye
    - utter_goodbye
    - export

## Generated Story 8750227000761782830
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "price_range": "300 - 700"}
    - slot{"cuisine": "american"}
    - slot{"price_range": "300 - 700"}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validity
    - slot{"valid_res": true}
    - action_restaurant
    - slot{"restaurant_details": [{"name": "The Burger House", "location": "Koregaon Park", "rating": "3.8", "cost": 400}, {"name": "The Burger Barn Cafe", "location": "Shivaji Nagar", "rating": "3.9", "cost": 700}, {"name": "CP7 - The BBQ Heaven", "location": "Baner", "rating": "3.9", "cost": 700}]}
    - utter_affirm
* goodbye
    - utter_goodbye
    - export

## Generated Story 4096752685780357722
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "pune", "price_range": "300 - 700"}
    - slot{"cuisine": "american"}
    - slot{"location": "pune"}
    - slot{"price_range": "300 - 700"}
    - action_validity
    - slot{"valid_res": true}
    - action_restaurant
    - slot{"restaurant_details": [{"name": "The Burger House", "location": "Koregaon Park", "rating": "3.8", "cost": 400}, {"name": "The Burger Barn Cafe", "location": "Shivaji Nagar", "rating": "3.9", "cost": 700}, {"name": "CP7 - The BBQ Heaven", "location": "Baner", "rating": "3.9", "cost": 700}]}
    - utter_affirm
* affirm
    - utter_ask_email_id
* send_email{"email_id": "manish.kumar2107@gmail.com"}
    - slot{"email_id": "manish.kumar2107@gmail.com"}
    - action_email
    - slot{"restaurant_details": [{"name": "The Burger House", "location": "Koregaon Park", "rating": "3.8", "cost": 400}, {"name": "The Burger Barn Cafe", "location": "Shivaji Nagar", "rating": "3.9", "cost": 700}, {"name": "CP7 - The BBQ Heaven", "location": "Baner", "rating": "3.9", "cost": 700}]}
    - utter_mail_sent
    - export

