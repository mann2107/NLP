from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import smtplib

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		config = {"user_key": "c8a3ad4423bf00142b89eec1f9cc7c5f"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		cuisine = str(cuisine).lower()
		price = tracker.get_slot('price_range')

		price = str(price)

		if '300' in price and '700' in price:
			range = 'medium'
		elif '300' in price:
			range = 'low'
		else:
			range = 'high'


		if range == 'low':
			cost_low = 0
			cost_high = 300
		elif range == 'medium':
			cost_low = 300
			cost_high = 700
		elif range == 'high':
			cost_low = 700
			cost_high = 3000
		else:
			cost_low = 0
			cost_high = 3000
		

		res = []

		# get_location gets the lat-long coordinates of 'loc'
		location_detail = zomato.get_location(loc, 1)

		# store retrieved data as a dict
		d1 = json.loads(location_detail)

		# separate lat-long coordinates
		lat = d1["location_suggestions"][0]["latitude"]
		lon = d1["location_suggestions"][0]["longitude"]

		# cuisines code (used by zomatopy)
		cuisines_dict = {'chinese': 25, 'american': 1, 'italian': 55, 'mexican': 73, 'north indian': 50,
						 'south indian': 85}

		# fetch and print results
		results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		r = d['restaurants']
		for i in r:
			name = i['restaurant']['name']
			location = i['restaurant']['location']['locality']
			rating = i['restaurant']['user_rating']['aggregate_rating']
			cost = i['restaurant']['average_cost_for_two']
			if cost >= cost_low and cost <= cost_high:
				ld = {}
				ld['name'] = name
				ld['location'] = location
				ld['rating'] = rating
				ld['cost'] = cost
				res.append(ld)

		if len(res) == 0:
			response = "no results"
		else:
			response = 'Here is your search results - '
			for i in res:
				name = i['name']
				loc = i['location']
				rating = i['rating']
				cost = i['cost']
				response += '\n' + name + '\t\t' + loc + '\t\t' + str(cost) + '\t\t' + str(rating)
		dispatcher.utter_message("-----" + response)
		return [SlotSet('restaurant_details', res)]


class ActionSearchRestaurantValidity(Action):
	def name(self):
		return 'action_validity'
		
	def run(self, dispatcher, tracker, domain):
		city = tracker.get_slot('location')
		city = str(city)

		valid_cities = ['ahmedabad', 'bangalore', 'chennai', 'delhi', 'hyderabad', 'kolkata', 'mumbai', 'pune',
						'agra', 'ajmer', 'aligarh', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly',
						'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bokaro steel city',
						'chandigarh', 'coimbatore', 'cuttack', 'dehradun', 'dhanbad', 'durg-bhilai nagar', 'durgapur',
						'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gurgaon',
						'guwahati‚ gwalior', 'hubli-dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu',
						'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kannur', 'kanpur', 'kakinada', 'kochi',
						'kottayam',	'kolhapur', 'kollam', 'kota', 'kozhikode', 'kurnool', 'lucknow', 'ludhiana', 'madurai',
						'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik',
						'nellore', 'noida', 'palakkad', 'patna', 'pondicherry', 'prayagraj', 'raipur', 'rajkot', 'rajahmundry',
						'ranchi', 'rourkela', 'salem', 'sangli', 'siliguri', 'solapur', 'srinagar', 'sultanpur', 'surat',
						'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirunelveli', 'tiruppur', 'ujjain', 'bijapur', 'vadodara',
						'varanasi', 'vasai-virar city', 'vijayawada', 'visakhapatnam', 'warangal']

		if city.lower() in valid_cities:
			response = True
		else:
			response = False
		return [SlotSet('valid_res', response)]

class ActionSendEmail(Action):
	def name(self):
		return 'action_email'
		
	def run(self, dispatcher, tracker, domain):
		restaurant_details = tracker.get_slot('restaurant_details')
		to_email_id = tracker.get_slot('email_id')

		gmail_user = 'groupprojectupgrad@gmail.com'
		gmail_password = 'abcd@1234'

		sent_from = gmail_user
		subject = 'Restaurant Search Result'
		body = 'Hi ,\nHere is your search results - \nName -------------Location-------------Cost-------------Rating'
		for i in restaurant_details:
			name = i['name']
			loc = i['location']
			rating = i['rating']
			cost = i['cost']
			body += '\n' + name + '\t\t' + loc + '\t\t' + str(cost) + '\t\t' + str(rating)

		try:
			server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
			server.ehlo()
			server.login(gmail_user, gmail_password)
			server.sendmail(sent_from, to_email_id, body)
			server.sendmail
			server.close()

			dispatcher.utter_message("Details sent to " + to_email_id)
		except:
			dispatcher.utter_message("Something went wrong while sending email to " + to_email_id )

		return [SlotSet('restaurant_details',restaurant_details)]

