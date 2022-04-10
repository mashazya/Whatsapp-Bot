from bot import WhatsappBot


def conv1 ():

	my_bot = WhatsappBot(language="en")  # Bot should re instantiated for each conversation

	my_bot.message("Yes, I would like to receive notifications", "newsletter")

	my_bot.message("My email is not_a_valid_email.com", "ask_for_email")

	my_bot.message("abc@email.com", "ask_for_email")  # valid email, bot inserts email and sends hangup

def conv2 ():

	my_bot = WhatsappBot(language="en")  # Bot should re instantiated for each conversation

	my_bot.message("No, I would hate to receive notifications", "newsletter")

def conv3 ():

	my_bot = WhatsappBot(language="en")  # Bot should re instantiated for each conversation

	my_bot.message("I'm not sure what is this about", "newsletter")

	my_bot.message("Yes", "newsletter")

	my_bot.message("not_a_valid_email.com", "ask_for_email")

	my_bot.message("abc@email.com", "ask_for_email")

	my_bot.message("Bye", "ask_for_email")

def conv4 ():

	my_bot = WhatsappBot(language="en")  # Bot should re instantiated for each conversation

	my_bot.message("What are you asking?", "newsletter")

	my_bot.message("Yes, i will give it a try", "newsletter")

	my_bot.message("not_a_valid_email.com", "ask_for_email")

	my_bot.message("I do not want no accept", "newsletter")

def conv5 ():

	my_bot = WhatsappBot(language="en")  # Bot should re instantiated for each conversation

	my_bot.message("Sure", "newsletter")

	my_bot.message("abc@email.com", "ask_for_email")

	my_bot.message("Okey", "ask_for_email")

