#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sqlite3
import sys


con = sqlite3.connect('pets.db')
c = con.cursor()

def query_pets():

    search = input('\nPlease enter the ID number of the person you wish to view or enter -1 to exit: ')

    if search == '-1':
        sys.exit()

    else:
        try:
            c.execute('\
                SELECT \
                    first_name, \
                    last_name, \
                    age \
                FROM \
                    person \
                WHERE \
                    id = ?', search)
            
            person_info = c.fetchall()

            c.execute('\
                SELECT pet_id \
                FROM person_pet \
                WHERE person_id = ?', search)
            
            pet_owner = c.fetchall()


            pets = []
            count = 0

            for item in pet_owner:
                c.execute('\
                    SELECT \
                        name, \
                        breed, \
                        age, \
                        dead \
                    FROM pet \
                    WHERE id = ?', pet_owner[count])
                
                count += 1
                pets.append(c.fetchall())

            print ('\n{} {}, {} years old:'.format(person_info[0][0], person_info[0][1], person_info[0][2]))
            count = 0

            while count < len(pets):
                
                for item in pets:
                    
                    if pets[count][0][3] == 0:
                        text = item[0][1]
                      
                        if (item[0][2] == 1):
                            if text.startswith('A') == True:
                                print ('\t{} {} owns {}, an {} who is {} year old.'.format(person_info[0][0], person_info[0][1], item[0][0], item[0][1], item[0][2]))
                            else:
                                print ('\t{} {} owns {}, a {} who is {} year old.'.format(person_info[0][0], person_info[0][1], item[0][0], item[0][1], item[0][2]))
                                
                        if (item[0][2] > 1):
                            if text.startswith('A') == True:
                                print ('\t{} {} owns {}, an {} who is {} years old.'.format(person_info[0][0], person_info[0][1], item[0][0], item[0][1], item[0][2]))
                            else:
                                print ('\t{} {} owns {}, a {} who is {} years old.'.format(person_info[0][0], person_info[0][1], item[0][0], item[0][1], item[0][2]))
                            
                    if pets[count][0][3] == 1:
                        text = str(item[0][1])

                        if (item[0][2] == 1):
                            if text.startswith('A') == True:
                                print ('\t{} {} owned {}, an {} that was {} year old.'.format(person_info[0][0], person_info[0][1], item[0][0], item[0][1], item[0][2]))
                            else:
                                print ('\t{} {} owned {}, a {} that was {} year old.'.format(person_info[0][0], person_info[0][1], item[0][0], item[0][1], item[0][2]))
                                
                        if (item[0][2] > 1):
                            if text.startswith('A') == True:
                                print ('\t{} {} owned {}, an {} that was {} years old.'.format(person_info[0][0], person_info[0][1], item[0][0], item[0][1], item[0][2]))
                            else:
                                print ('\t{} {} owned {}, a {} that was {} years old.'.format(person_info[0][0], person_info[0][1], item[0][0], item[0][1], item[0][2]))
                                
                    count += 1

            query_pets()

        except IndexError:
            print ('\nPlease enter a valid ID number')
            query_pets()


if __name__ == "__main__":
    query_pets()
