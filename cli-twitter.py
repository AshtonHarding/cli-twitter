#!/usr/bin/env python2
#-*- coding: utf-8 -*-

__version__='0.03'
__author__='Ashton "Kashire" Harding'

"""
This program is for running Twitter account(s) via the command-line
exclusively. It will require (unless I figure out how to get around this)
you to log into your account via a browser at first. But afterwards, you
shouldn't need to do this anymore.
"""

## Imports
import os
import sys

import urlparse
import json
import oauth2 as oauth
import webbrowser

from twitter import *

class string_handler():
    """This class is for holding static strings for this program.
    I'm hoping this will make it easier to edit. I suppose time
    will tell."""
    def printer(self,x):
        """This function just prints what it's given."""
        print(x)



    def clear(self):
        """This function clears the screen, to make it cleaner."""
        os.system('clear')


    def text(self, arg):
        """This simply handles the text to be displayed."""
        if arg == 'main menu':
            a='Account'
            subject = '\n0. Add %s \n1. Select %s \n2. Remove %s \n3. Quit \n' % (a,a,a)
        elif arg == 'account menu':
            subject = '\n0. Post \n1. Check DM \n2. Notifications \n3. Read TL \n4. Logout \n'
        elif arg == 'border':
            subject = '~' * 80
        elif arg == 'header':
            subject = ''+\
                         '\t       _  _         _              _  _    _              \n'+\
                         '\t  ___ | |(_)       | |_ __      __(_)| |_ | |_   ___  _ __ \n'+\
                         '\t / __|| || | _____ | __|\ \ /\ / /| || __|| __| / _ \| \'__|\n'+\
                         '\t| (__ | || ||_____|| |_  \ V  V / | || |_ | |_ |  __/| |   \n'+\
                         '\t \___||_||_|        \__|  \_/\_/  |_| \__| \__| \___||_|\n'
        elif arg == 'select user':
            subject = '\t(Please select the nickname of the account you want to control.)\n'
        else:
            subject = 'FUCKING'
        self.printer(subject)



class account_operation():
    string = string_handler()
    """This class handles"""
    ## Handle the main variables
    def login(self, consumer_key, consumer_secret, username):
        """Logs in as the user."""
        # Open file, get two auth keys.
        with open(username.rstrip('\n'), 'r') as grabbing_name:
            self.z = []
            for line in grabbing_name:
                self.z.append(line)
            self.oauth_token = self.z[0]
            self.oauth_secret= self.z[1]
        ## rstrip from oauth_token because it comes with a newline. 
        self.twitter = Twitter(auth=OAuth(self.oauth_token.rstrip('\n'), self.oauth_secret,
                                          consumer_key, consumer_secret))

        



    def poster(self, post_type):
        """Posting"""
        if post_type == 'text-only':
            pass
        elif post_type == 'image+text':
            pass
        else:
            print('ERROR')


    def post_text_only(self, twitter, TEXT_TO_POST):
        twitter.statuses.update(status=TEXT_TO_POST)



    def post_image(self):
        pass



    def notifications(self):
        """Display all unread notifications."""
        pass



    def timeline(self, consumer_key, consumer_secret, username):
        """Display timeline. (Is this even possible??)"""
        self.login(consumer_key, consumer_secret, username)
        timeline = self.twitter.statuses.home_timeline(count=200, exclude_replies=True)
        tl_time = True # Stays in here until done.
        ## Variables:
        print('#' * 80) # Just aesthetic. Probably will remove.
        self.page = 0 #default front page.
        while tl_time:
            self.high = (self.page * 4) + 4
            self.low = (self.high - 4)
            self.timeline_picking(timeline, self.low, self.high)
            print('PAGE NUMBER: '+str(self.page))
            try:
                print('Select one: [PREV] [MENU] [NEXT] :\n')
                self.select = raw_input(' ').lower()
            except:
                print('BAD INPUT. TRY AGAIN.')
            else:
                if self.select == 'PREV'.lower():
                    if self.page > 0:
                        self.page = self.page - 1
                    elif self.page == 0:
                        pass
                elif self.select == 'MENU'.lower():
                    tl_time = False
                elif self.select == 'NEXT'.lower():
                    if self.page < 20:
                        self.page = self.page + 1
                    else:
                        pass
                else:
                    print('BAD INPUT.')
        print('\n')



    def timeline_picking(self, timeline, low, high):
        self.string.clear()
        self.string.text('border')
        self.string.text('header')
        self.string.text('border')
        for x in range(low, high):
            tl_name = timeline[x]['user']['name']
            tl_username = timeline[x]['user']['screen_name']
            tl_text = timeline[x]['text']
            tl_post_id = timeline[x]['id']
            try:
                tl_media = timeline[x]['extended_entities']['media'][0]['media_url']
            except:
                tl_media = 'N/A'
            else:
                pass
            tl_datetime = timeline[x]['created_at']
            ## Printing a test.
            print('User: %s (%s) - Time Posted: %s (UTC)' % (tl_name, tl_username, tl_datetime))
            print('MESSAGE: %s' % (tl_text))
            print('media: %s' % (tl_media))
            print('-' * 80)


    def handler_of_operations(self, consumer_key, consumer_secret, username, TEXT_TO_POST, post_type, image_to_post):
        """Essentially the "main" of this class."""
        # Open file, get two auth keys.
        self.login(consumer_key, consumer_secret, username)
        if post_type == 'text-only':
            # Check size AT OR LESS THAN 140 CHARACTERS.
            if len(TEXT_TO_POST) < 141:
                self.twitter.statuses.update(status=TEXT_TO_POST)
            else:
                print('Your text is too long, post 140 characters or less.')
                sys.exit()
        elif post_type == 'text & image':
            if len(TEXT_TO_POST) > 116:
                print('Your text is too long, post 116 characters or less with images.')
                sys.exit()
            else:
                if os.path.isfile(image_to_post):
                    with open(image_to_post, "rb") as imagefile:
                        imagedata = imagefile.read()
                        self.imagedata = imagefile.read()
                        self.t_upload = Twitter(domain='upload.twitter.com',
                                                auth=OAuth(self.oauth_token.rstrip('\n'), self.oauth_secret,
                                                           consumer_key, consumer_secret))
                        self.id_img = self.t_upload.media.upload(media=imagedata)["media_id_string"]
                        self.twitter.statuses.update(status=TEXT_TO_POST, media_ids=",".join([self.id_img]))
                else:
                    print('DIRECTORY EITHER DOES NOT EXIST OR WAS INPUT INCORRECTLY.')
                    sys.exit()
        else:
            print('ERROR - line 135')
            sys.exit()
            


class cli_twitter():
    """This class is for actually handling Twitter in the command line."""
    string = string_handler()
    account_operations = account_operation()
    menu_state = 0
    ### CLI-TWITTER aesthetics & user input ###
    def display(self):
        """Displays the program name constantly!"""
        self.string.text('border')
        self.string.text('header')
        self.string.text('border')



    ### Main menu stuff.
    def main_menu(self):
        """Handles displaying the main menu."""
        self.display()
        self.main_menu_options()



    def main_menu_options(self):
        """Handles the user inputs for the main menu."""
        try:
            self.string.text('main menu')
            selector = input()
        except:
            print('BAD SELECTION')
            pass
        else:
            if selector == 0:
                self.oauth_function()
            elif selector == 1:
                self.menu_state = 1
            elif selector == 2:
                print('\n SELECT ACCOUNT TO DELETE')
            elif selector == 3:
                print('\nQUITTING.')
                sys.exit()
            else:
                print('wew')



    def oauth_function(self):
        """For authentication of each user account."""
        ## secret app keys.
        global consumer_key, consumer_secret
        self.consumer_key='12Xd3uIG4ZJQKeaZBWNdHSRML'
        self.consumer_secret='BxT0GWzXuID7ElshtWN1J9w2oweFfNZrQeCWbMp9y3ifOcHEE8'

        ## Websites needed for authorization.
        self.request_token='https://api.twitter.com/oauth/request_token'
        self.access_token='https://api.twitter.com/oauth/access_token'
        self.authorize_url='https://api.twitter.com/oauth/authorize'

        ## Makes the app easier to work with.
        self.consumer = oauth.Consumer(self.consumer_key, self.consumer_secret)
        self.client = oauth.Client(self.consumer)

        ## Grabs the temp. request token.
        self.resp, self.content = self.client.request(self.request_token, 'GET')

        ## Does a check to see if this is functioning properly.
        if self.resp['status'] != '200':
            raise Exception("Invalid response %s." % self.resp['status'])

        self.request_token = dict(urlparse.parse_qsl(self.content))

        ## Asks user to authorize physically.
        webbrowser.open('%s?oauth_token=%s' % (self.authorize_url,
                                               self.request_token['oauth_token']))
        ## Asks user for the pin.
        self.apple = 'n'
        while self.apple.lower() == 'n':
            self.apple = raw_input('Done authorizing? (Keep the pin ready) [y / n] : ')
        self.oauth_verify = raw_input('What is the pin?\n')

        ## Compiling token data together
        self.token = oauth.Token(self.request_token['oauth_token'],
                                 self.request_token['oauth_token_secret'])
        self.token.set_verifier(self.oauth_verify)
        self.client = oauth.Client(self.consumer, self.token)
        self.resp, self.content = self.client.request(self.access_token, "POST")
        self.access_token = dict(urlparse.parse_qsl(self.content))

        ## Saves user token data
        self.username = raw_input('Nickname this account: ')
        self.user_data_file = open(self.username,'w')
        self.user_data_file.write('%s\n%s' % (self.access_token['oauth_token'],
                                              self.access_token['oauth_token_secret']))
        self.user_data_file.close()

        ## Saves user to the db.
        if os.path.isfile('users.txt'):
            pass
        else:
            os.system('touch users.txt')
        self.f = open('users.txt','a')
        self.f.write('%s\n' % (self.username))
        self.f.close()



    def select_user_check(self):
        if not os.path.isfile('users.txt'):
            print('NO ACCOUNTS')
            sys.exit()
        else:
            self.f = open('users.txt', 'r')
            self.amount_of_lines = sum(1 for _ in self.f)
            if self.amount_of_lines == 0:
                print("EMPTY USERS.TXT")
                sys.exit()
            self.f.close()
            self.select_user(self.amount_of_lines)



    ### Select account.
    def select_user(self, amount_of_users):
        """Display registered users, asks to select one:"""
        self.display()
        self.string.text('select user')

        ## Display list of users to select from.
        self.f = open('users.txt', 'r')
        self.username = []
        for line in self.f:
            self.username.append(line)
        for x in range(0, amount_of_users):
            print('%s %s' % ( amount_of_users, self.username[x].rstrip('\n') ))
        self.f.close()

        ## Grabs user selection
        try:
            selector = input()
        except:
            print('BAD SELECTION.')
            sys.exit()
        else:
            print('selected.')
        
        ## Selects proper account, if exists.
        with open('users.txt', 'r') as fire:
            for i, line in enumerate(fire):
                if i == (selector-1):
                    try:
                        self.selected_username = line
                    except:
                        print('Account does not exist')
                    else:
                        self.account_menu(self.selected_username.rstrip('\n'))



    ### Handles the selected account.
    def account_menu(self, selected_username):
        self.string.clear()
        self.display()
        print('Hello, %s!' % (selected_username) )
        self.account_menu_options()



    def account_menu_options(self):
        self.consumer_key='12Xd3uIG4ZJQKeaZBWNdHSRML'
        self.consumer_secret='BxT0GWzXuID7ElshtWN1J9w2oweFfNZrQeCWbMp9y3ifOcHEE8'
        try:
            self.string.text('account menu')
            selector = input()
        except:
            print('BAD SELECTION')
            pass
        else:
            if selector == 0:
                self.TEXT_TO_POST = raw_input('(TEXT-ONLY) What would you like to post? : ')
                self.IMAGE_TO_POST = raw_input('(LEAVE BLANK IF NO) /DIR/TO/IMAGE : ')
                if self.IMAGE_TO_POST:
                    self.MESSAGE_TYPE = 'text & image'
                elif not self.IMAGE_TO_POST:
                    self.MESSAGE_TYPE = 'text-only'
                self.account_operations.handler_of_operations(self.consumer_key, self.consumer_secret,
                                                                  self.selected_username, self.TEXT_TO_POST,
                                                                  self.MESSAGE_TYPE, self.IMAGE_TO_POST)
            elif selector == 1:
                print('CHECKING DM')
            elif selector == 2:
                print('NOTIFICATIONS')
            elif selector == 3:
                print('READING TIMELINE')
                self.account_operations.timeline(self.consumer_key, self.consumer_secret, self.selected_username)
            elif selector == 4:
                print('\nLOGGING OUT.')
                self.menu_state = 0
                self.menu_handler()




    ### Handles all the menu crap.
    def menu_handler(self):
        """This directs state traffic"""
        while True:
            self.string.clear()
            if self.menu_state == 0:
                self.main_menu()
            elif self.menu_state  == 1:
                self.select_user_check()
                #self.account_menu()
            else:
                print('ERROR. STATE DOES NOT EXIST. EXITING.')
                sys.exit()



if __name__=='__main__':
    cli = cli_twitter()
    cli.menu_handler()
