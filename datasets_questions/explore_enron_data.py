#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "number of persons: {}".format(len(enron_data))
print "number of features per person: {}".format(len(enron_data['METTS MARK']))
print enron_data['METTS MARK']['poi']

persons_of_interest = [person for person in enron_data.values() if person['poi'] is True]
print "number of poi: {}".format(len(persons_of_interest))

print "total value of stock belonging to James Prentice: {}".format(enron_data['PRENTICE JAMES']['total_stock_value'])

print "number of emails from Wesley Colwell to poi: {}".format(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

print "value of exercised stocks belonging to Jeffrey Skilling: {}".format(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

print "total payments of Jeffery Skilling: {}".format(enron_data['SKILLING JEFFREY K']['total_payments'])
print "total payments of Kenneth Lay: {}".format(enron_data['LAY KENNETH L']['total_payments'])
print "total payments of Andrew Fastow: {}".format(enron_data['FASTOW ANDREW S']['total_payments'])

persons_with_salary = [person for person in enron_data.values() if person['salary'] != 'NaN']
print "persons in dataset with a quantified salary: {}".format(len(persons_with_salary))

persons_with_email = [person for person in enron_data.values() if person['email_address'] != 'NaN']
print "persons in dataset with an email address: {}".format(len(persons_with_email))

persons_without_total_payments = [person for person in enron_data.values() if person['total_payments'] == 'NaN']
print "persons without total payments: {}".format(len(persons_without_total_payments))
print "percentage of people without total payments: {0:.2f}".format(float( len(persons_without_total_payments) ) / len(enron_data.values()))

poi_without_total_payments = [poi for poi in persons_of_interest if poi['total_payments'] == 'NaN']
print "poi without total payments: {}".format(len(poi_without_total_payments))
print "percentage of poi without total payments: {0:.2f}".format(float( len(poi_without_total_payments) ) / len(persons_of_interest))
