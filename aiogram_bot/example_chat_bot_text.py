import re
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def Cha():
    bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train("chatterbot.corpus.english")
    # trainer.train("chatterbot.corpus.russian")
    return bot


if __name__ == "__main__":
    bot = Cha()
    print('Type something to begin...')
    while True:
        try:
            user_input = input()

            bot_response = bot.get_response(user_input)

            print(bot_response)

        # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break