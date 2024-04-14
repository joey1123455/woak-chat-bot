# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import List, Dict, Text, Any
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import Action
from rasa_sdk.events import SlotSet

class FeedbackForm(Action):
    def name(self) -> Text:
        return "action_feedback_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["name", "email", "feedback"]
    
    @staticmethod
    def send_email(self, config):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        # SMTP server configuration
        smtp_server = "smtp.gmail.com"
        port = 587
        # TODO: change to proper email
        username = "sascente00@gmail.com"
        password = "kbgi ssed nwlf txmr"

        # Email content
        sender_email = username
        receiver_email = config['sascente00@gmail.coms']
        subject = "Hello"
        body = f"Hello, this feedback from {config['name']}: " + config['feedback']

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message['From'] = config['email']
        message['To'] = receiver_email
        message['Subject'] = subject

        # Add body to email
        message.attach(MIMEText(body, 'html'))

        # Establish a secure connection with server
        with smtplib.SMTP(smtp_server, port) as server:
            server.login(username, password)
            server.send_message(message)

        print('Email sent successfully!')


    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Process or store the collected feedback (e.g., log the feedback)
        name = tracker.get_slot("name")
        email = tracker.get_slot("email")
        feedback = tracker.get_slot("feedback")

        # You can customize this part based on your use case (e.g., store feedback in a database)
        # For demonstration purposes, we'll just print the feedback
        print(f"name: {name}, email: {email} feedback: {feedback}")

        self.send_email({'name': name, 'email': email, 'feedback': feedback})

        dispatcher.utter_message("Thank you for your feedback!")
        return [SlotSet("name", None), SlotSet("email", None), SlotSet("feedback", None)]

