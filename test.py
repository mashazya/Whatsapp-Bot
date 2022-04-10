from unittest import TestCase, mock
from classifier import Classifier
import api
from api import BooklineAPI
import bot
from bot import WhatsappBot
import main as m

class TestMockValue(TestCase):
	
	@mock.patch.object(BooklineAPI, "insert_customer_email", autospec=True)
	@mock.patch.object(Classifier, "extract_intent")

	def test1(self, intent, insert):
		intent.return_value = "confirm"
		insert.return_value = True
		
		my_bot = WhatsappBot(language="en") 
		m.conv1()

	@mock.patch.object(BooklineAPI, "insert_customer_email", autospec=True)
	@mock.patch.object(Classifier, "extract_intent")

	def test2(self, intent, insert):
		intent.return_value = "reject"
		
		my_bot = WhatsappBot(language="en")
		m.conv2()

	@mock.patch.object(BooklineAPI, "insert_customer_email", autospec=True)
	@mock.patch.object(Classifier, "extract_intent", side_effect = ['other','confirm','confirm','confirm','confirm'])

	def test3(self, intent, insert):
		intent.return_value = "confirm"
		insert.return_value = True
		
		my_bot = WhatsappBot(language="en") 
		m.conv3()

	@mock.patch.object(BooklineAPI, "insert_customer_email", autospec=True)
	@mock.patch.object(Classifier, "extract_intent", side_effect = ['other','confirm','reject','reject'])

	def test4(self, intent, insert):
		intent.return_value = "reject"
		insert.return_value = True
		
		my_bot = WhatsappBot(language="en") 
		m.conv4()

	def exception (*args, **kwargs):
		raise api.InsertEmailError

	@mock.patch.object(BooklineAPI, "insert_customer_email", autospec=True,side_effect = exception)
	@mock.patch.object(Classifier, "extract_intent")

	def test5(self, intent, insert):
		intent.return_value = "confirm"
		
		my_bot = WhatsappBot(language="en") 
		m.conv5()


