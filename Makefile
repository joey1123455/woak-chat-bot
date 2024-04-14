tt:
	rasa data validate 
	rasa train
	rasa shell

action:
	rasa run actions

activate:
	source venv/bin/activate

valid:
	rasa data validate 