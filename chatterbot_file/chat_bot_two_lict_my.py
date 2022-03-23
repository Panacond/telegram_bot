from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


'''
This is an example showing how to train a chat bot using the
ChatterBot ListTrainer.
'''

chatbot = ChatBot('Bot')

# Start by training our bot with the ChatterBot corpus data
trainer = ListTrainer(chatbot)

trainer.train([
    'Привет, как ты?',
    'Я отлично',
    'Хай, как ты?',
    'Неплохо',
    'Привет, чуляк',
    'Привет, привет',
])


# Now let's get a response to a greeting
response = chatbot.get_response('Привет, таркан')
print(response)