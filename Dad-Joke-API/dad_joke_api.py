
# Fun with APIs

# imports
import requests as rq

# fetching the dad joke
# icanhazdadjoke => API Instruction: https://icanhazdadjoke.com/api
dad_joke_url = "https://icanhazdadjoke.com/"
dad_joke_param = {'Accept': 'text/plain'}

# dad_joke_content=rq.get(dad_joke_url, headers=dad_joke_param)		# fetches data in plain text format

# User interaction and show the joke
user_interaction_initiate = print('''
Hey there!!
Do you wanna hear a dad joke?
'''
)
user_interaction_asking = input('Hit "y" for the fun, else press any other key.\nYour selection : ')

while True:
    if user_interaction_asking.lower() != 'y':
        print('\nCiao. See you soon.')
        break
    else:
        dad_joke_content=rq.get(dad_joke_url, headers=dad_joke_param).text	# fetches data in plain text format
        print(f'<<< {dad_joke_content} >>>\n')
        user_interaction_asking = input('''
Are you game for another one?
Hit "y" to continue the fun, else press any other key.
Your selection : ''')


