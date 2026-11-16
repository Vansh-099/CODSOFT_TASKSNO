import random
import re 

intents = {
    "greetings":{
        "patterns":["hi", "hello", "hey", "howdy", "hola"],
        "responses":["Hello!", "Hi there!", "Hey!", "howdy","hi, how can i help you?"]
    },
    "college_timing": {
        "patterns": ["when does college start", "college timings", "when are classes"],
        "responses": [
            "Check your timetable for the exact class timings.",
            "Your class schedule should have the college timings.",
            "You can confirm the timing with your class teacher."
        ]
    },
    "assignment_help": {
        "patterns": ["how to complete an assignment", "assignment deadline", "help with assignment","assignment"],
        "responses": [
            "Read the instructions first and divide the work into smaller tasks.",
            "Check the submission date and start with the important questions.",
            "Try completing one part at a time instead of doing everything together."
        ]
    },
    "exam_prep": {
        "patterns": ["how to prepare for exams", "exam tips", "how should I revise"],
        "responses": [
            "Revise your notes and practise important questions.",
            "Start with difficult topics and then revise the easier ones.",
            "Make a short revision sheet for important definitions and formulas."
        ]
    },
    "python_help": {
        "patterns": ["what is a dictionary", "python list example", "explain nested dictionary"],
        "responses": [
            "A dictionary stores data in key-value pairs.",
            "A list stores multiple items in a single variable.",
            "A nested dictionary is a dictionary inside another dictionary."
        ]
    },
    "project_ideas": {
        "patterns": ["suggest a Python project", "beginner coding project", "simple chatbot project"],
        "responses": [
            "You can build a quiz application using Python.",
            "Try making a student record management system.",
            "A rule-based chatbot is a good beginner project."
        ]
    },
    "goodbyes": {
        "patterns": ["bye", "goodbye", "see you", "later"],
        "responses":["Goodbye!", "See you later!", "Take care!"]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "appreciate it"],
        "responses":["You're welcome!", "No problem!", "Happy to help!", "Anytime! bro"]
    },
    "questions": {
       "how are you": ["I'm fine, thank you!", "Doing great, what about you?"],
       "what's your name": ["I'm your friend. What's your name?"],
       "what can you do": ["I can chat with you, help answer questions, and even solve math problems!"]
    }
}

def match_intent(user_input):
    for intent, intent_data in intents.items():
        if isinstance(intent_data, dict) and "patterns" in intent_data:
            for pattern in intent_data["patterns"]:  
                if re.search(pattern, user_input, re.IGNORECASE):
                    return random.choice(intent_data["responses"])
    for question, responses in intents["questions"].items():
        if question in user_input.lower():
            return random.choice(responses)
    return None

def get_response(user_input):
    matched_intent = match_intent(user_input)
    if matched_intent:
        return matched_intent
    else:
        return "I didn't understand what you said, can you please rephrase it?"

def chatbot():
    print("Aniimo_Bot: Hello, how can I help you?")
    while True:
        user_input = input("You: ")

        if "bye" in user_input.lower():
            print("Goodbye!")
            break

        response = get_response(user_input)
        print("Aniimo_Bot:", response)

chatbot()