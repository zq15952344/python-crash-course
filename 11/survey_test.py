import unittest
from surey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
	def setUp(self):
		question = 'what language did you first learn to speak?'
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['dfs', 'sfd', 'sfd']
	
	def test_store_single_response(self):
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)
	
	def test_store_mutil_response(self):
		for response in self.responses:
			self.my_survey.store_response(response)
		
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)
	
	"""
	def test_store_single_response(self):
		question = 'what language did you first learn to speak?'
		my_survey = AnonymousSurvey(question)
		my_survey.store_response('English')
		
		self.assertIn('English', my_survey.responses)

	def test_store_mutil_response(self):
		question = 'what language did you first learn to speak?'
		
		my_survey = AnonymousSurvey(question)
		responses = ['python', 'swift', 'English','Chinese']
		for response in responses:
			my_survey.store_response(response)
		
		for response in responses:
			self.assertIn(response, my_survey.responses)
	"""

	
unittest.main()
