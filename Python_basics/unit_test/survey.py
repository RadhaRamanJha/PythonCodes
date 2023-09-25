class AnonymusSurvey:
    """Collect Anonymus answer to Survey question"""
    def __init__(self,question):
        self.question = question
        self.responses = []
    def show_question(self):
        """Show the survey question"""
        print(self.question)
    def store_response(self,new_response):
        """Store a new response to survey"""
        self.responses.append(new_response)
    def show_responses(self):
        """Show all the responses of survey """
        for response in self.responses:
            print(f"- {response}")    