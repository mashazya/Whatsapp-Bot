# Whatsapp-Bot
This repository is created to present the results of the implementation of five full-conversation tests for a WhatsApp bot. The repository contains the bot implementation with some unimplemented methods. The `test.py` file contains all the tests that simulate the interaction with an arbitrary user. The user's input is contained in the `main.py`file.
## Conversation scripts
To obtain high code coverage of the `bot.py` five user-bot conversations were modeled.
### Conversation 1:
This conversation models a confirmation of the newsletter, but a typo in the email message
  - B: Please confirm that you wish to receive additional info via subscription to our newsletter.
  - U: Yes, I would like to receive notifications
  - B: Great! Please, let me know your e-mail
  - U: My email is not_a_valid_email.com
  - B: It seems that this e-mail is not valid. Please make sure it's correct
  - U: abc@email.com
  - B: Perfect, we've stored your e-mail! Enjoy the experience at the restaurant
### Conversation 2:
This conversation models a rejection of the newsletter
  - B: Please confirm that you wish to receive additional info via subscription to our newsletter.
  - U: No, I would hate to receive notifications
  - B: Okay, I hope you enjoy the experience at the restaurant

### Conversation 3:
This conversation models a first unclear response by the user and a later confirmation of the newsletter
  - B: Please confirm that you wish to receive additional info via subscription to our newsletter.
  - U: I'm not sure what is this about
  - B: Please, let me know if you agree or not
  - U: Yes
  - B: Great! Please, let me know your e-mail
  - U: not_a_valid_email.com
  - B: It seems that this e-mail is not valid. Please make sure it's correct
  - U: abc@email.com
  - B: Perfect, we've stored your e-mail! Enjoy the experience at the restaurant
  - U: Bye
  - B: Thanks for reaching out. I can't help you with anything else yet but if you want to make a reservation you can call the restaurant again

### Conversation 4:
This conversation models a first unclear response by the user and a first confirmation of the newsletter and a later rejection of the newsletter
  - B: Please confirm that you wish to receive additional info via subscription to our newsletter.
  - U: What are you asking?
  - B: Please, let me know if you agree or not
  - U: Yes, i will give it a try
  - B: Great! Please, let me know your e-mail
  - U: not_a_valid_email.com
  - B: It seems that this e-mail is not valid. Please make sure it's correct
  - U: I do not want no accept
  - B: Okay, I hope you enjoy the experience at the restaurant

### Conversation 5:
This conversation models an error in saving the email address per part of the bot
  - B: Please confirm that you wish to receive additional info via subscription to our newsletter.
  - U: Sure
  - B: Great! Please, let me know your e-mail
  - U: abc@email.com
  - B: There has been an error. Please try again later.
  - U: Okey
  - B: Thanks for reaching out. I can't help you with anything else yet but if you want to make a reservation you can call the restaurant again
## Testing
  1. Install `mock`library with the following command:
 
     `$ pip install mock`
     
  2. Execute the test file in the terminal with the following command:
  
     `$ python -m unittest test.py`
     
     The output should indicate that the test ran correctly.
 ## Suggested improvements
 Some minor suggestions can be made to make the interaction with the bot easier:
 1. The else clause in the private `newsletter_flow` function of the `bot.py` file accesed through the conditional `self.conversation_status == "start"` should contain an additional line of 
 
  `self.conversation_status = "expectingEmail"`
  
  2. Add possibility of rejecting after accepting as in the example conversation 4 with the `ask_for_email` intention instead of the `newsletter` intention

