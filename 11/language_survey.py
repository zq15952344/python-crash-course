from surey import AnonymousSurvey

question = 'what is the first language you learned'

my_survey = AnonymousSurvey(question)

my_survey.show_question()
print 'q for quit'

while 1:
	response = raw_input('input the langugage: ')
	if response == 'q':
		break
	my_survey.store_response(response)

my_survey.show_results()