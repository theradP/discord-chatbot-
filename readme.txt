bot invite url - https://discordapp.com/api/oauth2/authorize?client_id=688291982849736738&permissions=806090806&scope=bot
bot name - emitrr_bot

Pre-requisites-
- Python 3.7 
- Discord account

Overview of system -
- This particular chat bot can handle replies to a greeting from a user on the discord server 
- User can search for a keyword or phrase on google directly from the discord chat using '!google' as a prefix to it.
- User can search the history for all recent searches with the given keyword or phrase using '!recent' as prefix to it.
- The program uses a sqlite database to store data which helps in retaining data even when the server is restarted.

Getting started -
- Copy and paste the bot invite url to a browser window and select the server of your choosing from the menu displayed.
- Create a virtual environment using conda or virtualenv 
- Run the command 'pip install -r requirements.txt' to install all the dependencies in the virtual environment.
- Run the command 'python chatbot.py' after traversing to the respective directory and once the message 'We have logged in as emitrr_bot#2587' is displayed on the terminal our bot is ready for work.
- Now you can greet and search the web using the bot directly from your discord chat .