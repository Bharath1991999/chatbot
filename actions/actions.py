# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
import logging

logger = logging.getLogger(__name__)

meaning = {
    "annotations" : "Data annotation is the process of adding metadata to a dataset. This metadata usually takes the form of tags, which can be added to any type of data, including text, images, and video",
    "annotation" : "Data annotation is the process of adding metadata to a dataset. This metadata usually takes the form of tags, which can be added to any type of data, including text, images, and video",
    "rpa" : "Robotic process automation (RPA) is the term used for software tools that partially or fully automate human activities that are manual, rule-based, and repetitive.",
    "textrecognition" : "OCR (optical character recognition) is the use of technology to distinguish printed or handwritten text characters inside digital images of physical documents, such as a scanned paper document. ... OCR is sometimes also referred to as text recognition",
    "hyperautomation" : "Hyperautomation refers to the use of advanced technologies, like artificial intelligence (AI), machine learning (ML), and robotic process automation (RPA), to automate tasks that were once completed by humans",
    "on-prem" : "On-premises software (also incorrectly referred to as on-premise, and alternatively abbreviated on-prem) is installed and runs on computers on the premises of the person or organization using the software, rather than at a remote facility such as a server farm or cloud.",
    "onprem" : "On-premises software (also incorrectly referred to as on-premise, and alternatively abbreviated on-prem) is installed and runs on computers on the premises of the person or organization using the software, rather than at a remote facility such as a server farm or cloud.",
    "on-premises" : "On-premises software (also incorrectly referred to as on-premise, and alternatively abbreviated on-prem) is installed and runs on computers on the premises of the person or organization using the software, rather than at a remote facility such as a server farm or cloud.",
    "onpremises" : "On-premises software (also incorrectly referred to as on-premise, and alternatively abbreviated on-prem) is installed and runs on computers on the premises of the person or organization using the software, rather than at a remote facility such as a server farm or cloud.",
    "speechrecognition" : "The process of enabling a computer to identify and respond to the sounds produced in human speech",
    "ai":"Artificial intelligence (AI), the ability of a digital computer or computer-controlled robot to perform tasks commonly associated with intelligent beings",
    "artificialintelligence":"Artificial intelligence (AI), the ability of a digital computer or computer-controlled robot to perform tasks commonly associated with intelligent beings",
    "machinelearning":"The use and development of computer systems that are able to learn and adapt without following explicit instructions, by using algorithms and statistical models to analyse and draw inferences from patterns in data",
    "ml":"The use and development of computer systems that are able to learn and adapt without following explicit instructions, by using algorithms and statistical models to analyse and draw inferences from patterns in data",
    "dl":"Deep Learning is a subfield of machine learning concerned with algorithms inspired by the structure and function of the brain called artificial neural networks",
    "deeplearning":"Deep Learning is a subfield of machine learning concerned with algorithms inspired by the structure and function of the brain called artificial neural networks",
    "cnn" : "A convolutional neural network (CNN) is a type of artificial neural network used in image recognition and processing that is specifically designed to process pixel data. ... A neural network is a system of hardware and/or software patterned after the operation of neurons in the human brain",
    "convolutionalneuralnetwork": "A convolutional neural network (CNN) is a type of artificial neural network used in image recognition and processing that is specifically designed to process pixel data. ... A neural network is a system of hardware and/or software patterned after the operation of neurons in the human brain",
    "rnn" : "A recurrent neural network (RNN) is a class of artificial neural networks where connections between nodes form a directed graph along a temporal sequence",
    "recurrentneuralnetwork": "A recurrent neural network (RNN) is a class of artificial neural networks where connections between nodes form a directed graph along a temporal sequence",
    "nlp" : "Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data",
    "accelerating" : "In SARA accelerating means compliment screen level integrations with API level integrations,Implementing RPA for processes requiring interaction with disparate legacy systems as well .\n"
}

NEXT_FORM_NAME = {
    "project_info": "project_info_form",
    "project_features": "project_features_form",
    "project_benefits": "project_benefits_form",
}

FORM_DESCRIPTION = {
    "project_info_form": "Information about a project",
    "project_features_form": "Features of a project",
    "project_benefits_form": "Benefits of a project",
}

Projects_Form_List = ["Info", "Benefits", "Features"]

class ActionIntro(Action):

    def name(self) -> Text:
        return "action_intro"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text="Hey..!!\nWe The SandLogic - Adding Intelligence are an Indian deep-tech startup, providing - disruptive, cohesive solutions & services across industries & overseas. In 2018, we introduced our unique products to the market. Our purpose was to raise awareness about the significance and value of hyper automation & AI. Please drop me mail to get in touch (mailto:info@sandlogic.com) & discuss things over coffee. Coffee is on me.ðŸ˜ƒ"
        prev = tracker.get_slot('prev_project')
        buttons = None
        con = tracker.get_slot('continue')
        if prev and con==None:
            previous_form_list = tracker.get_slot('previous_form_list')
            if previous_form_list:
                if len(previous_form_list)<3:
                    text = text + "\n Do you want to know more about the project" + prev
                if len(previous_form_list)==3:
                    text = text + "\n Are you interested to know more projects other than" + prev
                buttons = [
                    {"payload": "Yes", "title": "Yes"},
                    {"payload": "No", "title": "No"},
                ]
        if buttons:
            dispatcher.utter_message(text=text, buttons=buttons)
        else:
            dispatcher.utter_message(text=text)
        return []

class ActionknowPerson(Action):

    def name(self) -> Text:
        return "action_know_person"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        text = ""
        for e in entities:
            if e['entity'] == 'person':
                name = e['value']
            if name == 'founder':
                text = text + "Meet Our CEO - KAMALAKAR DEVAKI\nHe is techpreneur at heart, with a zeal to build solutions for global market.\nhe have technical leadership & Solution Architecture, with high-level management experience in the IT industry\n"
            if name == 'mentor':
                text = text + "I am glad to introduce you to Our Mentor - RAJ NERAVATI\nTechnology Entrepreneur and accomplished leader with experience in growing and managing business operations.\nvalues Served:- Head of Technology at Titan Company Limited, Chief Operating Officer, Senior Vice President – Delivery, VP – Sales & Account Management, AVP – Solutions & Client Services.\nDomains:- IoT, Financial Services, Insurance, Airline Industry, Health Care\n"


        if text != "":
            prev = tracker.get_slot('prev_project')
            buttons = None
            con = tracker.get_slot('continue')
            if prev and con == None:
                previous_form_list = tracker.get_slot('previous_form_list')
                if previous_form_list:
                    if len(previous_form_list) < 3:
                        text = text + "\n Do you want to know more about the project" + prev
                    if len(previous_form_list) == 3:
                        text = text + "\n Are you interested to know more projects other than" + prev
                    buttons = [
                        {"payload": "Yes", "title": "Yes"},
                        {"payload": "No", "title": "No"},
                    ]
            if buttons:
                dispatcher.utter_message(text=text, buttons=buttons)
            else:
                dispatcher.utter_message(text=text)
        if text == "":
            dispatcher.utter_message(
                text="Could you please rephrase the question. Do you want to know about our CEO or founder or mentor")
        return []


class address(Action):

    def name(self) -> Text:
        return "action_address"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        text = ""
        for e in entities:
            if e['entity'] == 'location':
                name = e['value']
            if name == 'India':
                text = text + "🇮🇳:-\nSandLogic Technologies Pvt. Ltd.\n#113, 2nd floor, 100 Feet Ring Road.\n5th Block, 3rd Phase, Banashankari 3rd Stage\nBengaluru, Karnataka 560085. India.\n📍https://g.page/SandLogic?share"
            if name == 'USA':
                text = text + "🇱🇷 Office :\nSandLogic Labs Corp.\n2300, McDermott Dr, Ste 200-368\nPlano, Texas, 75025. USA."

        if text == "":
            text = "🇮🇳:-\nSandLogic Technologies Pvt. Ltd.\n#113, 2nd floor, 100 Feet Ring Road.\n5th Block, 3rd Phase, Banashankari 3rd Stage\nBengaluru, Karnataka 560085. India.\n📍https://g.page/SandLogic?share \n 🇱🇷 Office :\nSandLogic Labs Corp.\n2300, McDermott Dr, Ste 200-368\nPlano, Texas, 75025. USA."

        prev = tracker.get_slot('prev_project')
        buttons = None
        con = tracker.get_slot('continue')
        if prev and con == None:
            previous_form_list = tracker.get_slot('previous_form_list')
            if previous_form_list:
                if len(previous_form_list) < 3:
                    text = text + "\n Do you want to know more about the project" + prev
                if len(previous_form_list) == 3:
                    text = text + "\n Are you interested to know more projects other than" + prev
                buttons = [
                    {"payload": "Yes", "title": "Yes"},
                    {"payload": "No", "title": "No"},
                ]
        if buttons:
            dispatcher.utter_message(text=text, buttons=buttons)
        else:
            dispatcher.utter_message(text=text)
        return []


class ActionMeaning(Action):

    def name(self) -> Text:
        return "action_meaning"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text="Hey! Glad that you asked.\nSAND + LOGIC = Silica which is the basis of any semiconductor and hardware + foundation of any software or digital solution.\nOur logo is ⌛ \nThe fire brick red color reflects our passion, intensity and energy.\nThe slate blue color reflects innovation, our integrity, knowledge and ambition."
        prev = tracker.get_slot('prev_project')
        buttons = None
        con = tracker.get_slot('continue')
        if prev and con == None:
            previous_form_list = tracker.get_slot('previous_form_list')
            if previous_form_list:
                if len(previous_form_list) < 3:
                    text = text + "\n Do you want to know more about the project" + prev
                if len(previous_form_list) == 3:
                    text = text + "\n Are you interested to know more projects other than" + prev
                buttons = [
                    {"payload": "Yes", "title": "Yes"},
                    {"payload": "No", "title": "No"},
                ]
        if buttons:
            dispatcher.utter_message(text=text, buttons=buttons)
        else:
            dispatcher.utter_message(text=text)
        return []


class contact(Action):

    def name(self) -> Text:
        return "action_contact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        text = ""
        for e in entities:
            if e['entity'] == 'contact':
                name = e['value']
                if name == 'mobile':
                    text = text + "☎️ :- +91 8800810207\n"
                if name == 'mail':
                    text = text + "📧 :- info@sandlogic.com\n"
                if name == 'linkedin':
                    text = text + "Our linkedin Pages : https://www.linkedin.com/company/sandlogic/\n"

        if text == "":
            text = "☎️ :- +91 8800810207\n📧 :- (info@sandlogic.com)\n📍 :- SandLogic Technologies Pvt. Ltd.\n#113, 2nd floor, 100 Feet Ring Road, 5th Block,\n3rd Phase, Banashankari 3rd Stage, Bengaluru,\nKarnataka 560085. India.\nhttps://g.page/SandLogic?share"
        prev = tracker.get_slot('prev_project')
        buttons = None
        con = tracker.get_slot('continue')
        if prev and con == None:
            previous_form_list = tracker.get_slot('previous_form_list')
            if previous_form_list:
                if len(previous_form_list) < 3:
                    text = text + "\n Do you want to know more about the project" + prev
                if len(previous_form_list) == 3:
                    text = text + "\n Are you interested to know more projects other than" + prev
                buttons = [
                    {"payload": "Yes", "title": "Yes"},
                    {"payload": "No", "title": "No"},
                ]
        if buttons:
            dispatcher.utter_message(text=text, buttons=buttons)
        else:
            dispatcher.utter_message(text=text)
        return []


class visionMission(Action):

    def name(self) -> Text:
        return "action_vision_mission"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        text = ""
        for e in entities:
            if e['entity'] == 'statement':
                name = e['value']
            if name == 'vision':
                text = text + "OUR VISION - Design and implementation of top-notch solutions and unique products for businesses, delighting our customers and keep the graphs of our growth rising.\n"
            if name == 'mission':
                text = text + "OUR MISSION - To enlighten AI with the world’s potential brainpower and tap new possibilities. Be one of the 5 prime companies in AI & Robotics by 2022.\n"

        if text != "":
            prev = tracker.get_slot('prev_project')
            buttons = None
            con = tracker.get_slot('continue')
            if prev and con == None:
                previous_form_list = tracker.get_slot('previous_form_list')
                if previous_form_list:
                    if len(previous_form_list) < 3:
                        text = text + "\n Do you want to know more about the project" + prev
                    if len(previous_form_list) == 3:
                        text = text + "\n Are you interested to know more projects other than" + prev
                    buttons = [
                        {"payload": "Yes", "title": "Yes"},
                        {"payload": "No", "title": "No"},
                    ]
            if buttons:
                dispatcher.utter_message(text=text, buttons=buttons)
            else:
                dispatcher.utter_message(text=text)
        else:
            dispatcher.utter_message(
                "Could you please rephrase the question. Do you want to know about vision or mission")
            return []


class ActionWorkFlow(Action):

    def name(self) -> Text:
        return "action_workflow"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text="Using our end to end solution and a suitable strategic approach, we turn your plan/project into reality:\n1)AI SURVEY :- Doing research with latest insights & trends to embrace innovation to drive new value to your project to give you tangible outcomes.\n2)MAKE PLAN :- Preparation of a plan, suitable to your business needs, together with customized strategy to embrace AI.\n3)DATA COLLECTION AND PREPROCESSING :- One of the main task is to manage data according to requirements. We help our client in seamless data management for AI projects, reducing the efforts involved.\n4)START YOUR PROJECT :- Good foundations lead to strong & fruitful results. If you're done with all the essential process required to start a project."
        prev = tracker.get_slot('prev_project')
        buttons = None
        con = tracker.get_slot('continue')
        if prev and con == None:
            previous_form_list = tracker.get_slot('previous_form_list')
            if previous_form_list:
                if len(previous_form_list) < 3:
                    text = text + "\n Do you want to know more about the project" + prev
                if len(previous_form_list) == 3:
                    text = text + "\n Are you interested to know more projects other than" + prev
                buttons = [
                    {"payload": "Yes", "title": "Yes"},
                    {"payload": "No", "title": "No"},
                ]
        if buttons:
            dispatcher.utter_message(text=text, buttons=buttons)
        else:
            dispatcher.utter_message(text=text)
        return []


class ActionWhySandLogic(Action):

    def name(self) -> Text:
        return "action_why_sandlogic"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text="Few of the advantage working with us\n- Implement advanced AI technology into the customerâ€™s systems, products and services.\n- Provide complete and true customisations and IPs.\n- Create solutions that fit every business model like a glove.\n- Assist companies to derive meaningful information from the data that improve business efficiency and workflows.\n- Help businesses in utilising the superpower of AI with end to end solutions for Healthcare, Retail, Manufacturing Insurance, and Finance industries."
        prev = tracker.get_slot('prev_project')
        buttons = None
        con = tracker.get_slot('continue')
        if prev and con == None:
            previous_form_list = tracker.get_slot('previous_form_list')
            if previous_form_list:
                if len(previous_form_list) < 3:
                    text = text + "\n Do you want to know more about the project" + prev
                if len(previous_form_list) == 3:
                    text = text + "\n Are you interested to know more projects other than" + prev
                buttons = [
                    {"payload": "Yes", "title": "Yes"},
                    {"payload": "No", "title": "No"},
                ]
        if buttons:
            dispatcher.utter_message(text=text, buttons=buttons)
        else:
            dispatcher.utter_message(text=text)
        return []


class ActionTiming(Action):

    def name(self) -> Text:
        return "action_office_timing"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text="Let's have conversation over â˜• from Monday-Friday\nðŸ•°ï¸ 10:30 AM - 7:00 PM.\nOtherwise you are always welcome to drop ðŸ“§ (mailto:info@sandlogic)"
        prev = tracker.get_slot('prev_project')
        buttons = None
        con = tracker.get_slot('continue')
        if prev and con == None:
            previous_form_list = tracker.get_slot('previous_form_list')
            if previous_form_list:
                if len(previous_form_list) < 3:
                    text = text + "\n Do you want to know more about the project" + prev
                if len(previous_form_list) == 3:
                    text = text + "\n Are you interested to know more projects other than" + prev
                buttons = [
                    {"payload": "Yes", "title": "Yes"},
                    {"payload": "No", "title": "No"},
                ]
        if buttons:
            dispatcher.utter_message(text=text, buttons=buttons)
        else:
            dispatcher.utter_message(text=text)
        return []


class ActionHirings(Action):

    def name(self) -> Text:
        return "action_hirings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text="Hey, Thanks for your interest in working with us..!!\n Please Drop your Resume at (mailto:people@sandlogic.com)"
        prev = tracker.get_slot('prev_project')
        buttons = None
        con = tracker.get_slot('continue')
        if prev and con == None:
            previous_form_list = tracker.get_slot('previous_form_list')
            if previous_form_list:
                if len(previous_form_list) < 3:
                    text = text + "\n Do you want to know more about the project" + prev
                if len(previous_form_list) == 3:
                    text = text + "\n Are you interested to know more projects other than" + prev
                buttons = [
                    {"payload": "Yes", "title": "Yes"},
                    {"payload": "No", "title": "No"},
                ]
        if buttons:
            dispatcher.utter_message(text=text, buttons=buttons)
        else:
            dispatcher.utter_message(text=text)
        return []


class ActionIndustries(Action):

    def name(self) -> Text:
        return "action_company_industries"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text="Hey, we can support you with Asset Tracking, Predictive Maintence, Inventory Management, Automating the Cognitive tasks, Warehouse automation , & many more. I would reccommend you to check out our 1 stop solution for your warehouse automation need - Warehouz.AI. For further assist please contact our expert at ðŸ“§ (mailto:info@sandlogic.com)"
        prev = tracker.get_slot('prev_project')
        buttons = None
        con = tracker.get_slot('continue')
        if prev and con == None:
            previous_form_list = tracker.get_slot('previous_form_list')
            if previous_form_list:
                if len(previous_form_list) < 3:
                    text = text + "\n Do you want to know more about the project" + prev
                if len(previous_form_list) == 3:
                    text = text + "\n Are you interested to know more projects other than" + prev
                buttons = [
                    {"payload": "Yes", "title": "Yes"},
                    {"payload": "No", "title": "No"},
                ]
        if buttons:
            dispatcher.utter_message(text=text, buttons=buttons)
        else:
            dispatcher.utter_message(text=text)
        return []


class ActionSectors(Action):

    def name(self) -> Text:
        return "action_company_sectors"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text="Hey, As of now our expertise lies in following domain :-\nBFSI, IT & Telecom, Manufacturing, Logistics, Energy & Utility, Pharma & Healthcare last but not least Warehouse Industry.\nWorking towards expanding our wingsðŸ¦‹. Please feel free to contact at ðŸ“§ info@sandlogic.com "
        prev = tracker.get_slot('prev_project')
        buttons = None
        con = tracker.get_slot('continue')
        if prev and con == None:
            previous_form_list = tracker.get_slot('previous_form_list')
            if previous_form_list:
                if len(previous_form_list) < 3:
                    text = text + "\n Do you want to know more about the project" + prev
                if len(previous_form_list) == 3:
                    text = text + "\n Are you interested to know more projects other than" + prev
                buttons = [
                    {"payload": "Yes", "title": "Yes"},
                    {"payload": "No", "title": "No"},
                ]
        if buttons:
            dispatcher.utter_message(text=text, buttons=buttons)
        else:
            dispatcher.utter_message(text=text)
        return []


class ActionUsecases(Action):

    def name(self) -> Text:
        return "action_use_cases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        text = ""
        if len(entities) != 0:
            for e in entities:
                if e['entity'] == 'use_case':
                    name = e['value']
                    name = name.lower()
                    if 'face' in name:
                        text = text + "Yes..!!We do work in facial recognition system.\n" \
                                      "Few of areas, we cover are:-" \
                                      "â€¢ FaceDetection" \
                                      "â€¢ FaceRegistration" \
                                      "â€¢ FaceRecognition" \
                                      "â€¢ FaceVerification" \
                                      "â€¢ Emotion Recognition" \
                                      "â€¢ Person Re-ID and Tracking\n" \
                                      "For further assist please contact our expert at ðŸ“§ (mailto:info@sandlogic.com)."
                    if 'ocr' in name:
                        text = text + "Yes..!!We do work in Optical character recognition.\n" \
                                      "Few of areas, we cover are:-" \
                                      "â€¢ Generic OCR" \
                                      "â€¢ Pan Card Reader" \
                                      "â€¢ LPNR (License Plate Number Recognition)" \
                                      "â€¢ Document Digitization" \
                                      "â€¢ Local Language Support\n" \
                                      "For further assist please contact our expert at ðŸ“§ (mailto:info@sandlogic.com)."
                    if 'visual' in name:
                        text = text + "Yes..!!We do work in Visual Intelligence System\n" \
                                      "Few of areas, we cover are:-" \
                                      "â€¢ Query Images for the visual features" \
                                      "â€¢ Human Action Recognition" \
                                      "â€¢ Custom object detection & Tracking" \
                                      "â€¢ Action Time Intelligence" \
                                      "â€¢ Action Sequence Intelligence\n" \
                                      "For further assist please contact our expert at ðŸ“§ (mailto:info@sandlogic.com)."
                    if 'logistics' in name:
                        text = text + "Yes..!!We do work to Automate the warehouse.\n" \
                                      "â€¢ Automation of Warehouse activities like" \
                                      "â€¢ Palette sorting" \
                                      "â€¢ Label reading" \
                                      "â€¢ Updating inventory" \
                                      "â€¢ Catch-weight.\n" \
                                      "For further assist please contact our expert at ðŸ“§ (mailto:info@sandlogic.com).\n"
                    if 'agrinet' in name:
                        text = text + "Yes..!!We do work in Agriculture field \n" \
                                      "Few of areas, we cover are:-" \
                                      "â€¢ Plant classification" \
                                      "â€¢ Plant disease detection" \
                                      "â€¢ Plant disease classification\n" \
                                      "For further assist please contact our expert at ðŸ“§ (mailto:info@sandlogic.com)."
                    if 'medical' in name:
                        text = text + "Yes..!!We do work in Healthcare field \n" \
                                      "Few of areas, we cover are:-" \
                                      "â€¢ TuberculosisDetection" \
                                      "â€¢ Alzheimer'sDetection" \
                                      "â€¢ Covid-19Detection" \
                                      "â€¢ Skin Cancer, lesion detection & Classification\n" \
                                      "For further assist please contact our expert at ðŸ“§ (mailto:info@sandlogic.com).\n"
                    if 'audio' in name:
                        text = text + "Yes..!!We do work in Audio Intelligence field \n" \
                                      "Few of areas, we cover are :-" \
                                      "â€¢ Speaker Diarization" \
                                      "â€¢ Speaker Recognition" \
                                      "â€¢ Speech Emotion Recognition" \
                                      "â€¢ Audio Classification" \
                                      "â€¢ ASR\n" \
                                      "For further assist please contact our expert at ðŸ“§ (mailto:info@sandlogic.com)."

                    if 'pattern' in name:
                        text = text + "Yes..!!We do work in Pattern & Materials Field \n" \
                                      "Few of areas, we cover are:-" \
                                      "â€¢ Pattern matching" \
                                      "â€¢ Similarity Scoring" \
                                      "â€¢ Surface defect detection" \
                                      "â€¢ Point Cloud based rendering" \
                                      "â€¢ 2D-3D rendering\n" \
                                      "For further assist please contact our expert at ðŸ“§ (mailto:info@sandlogic.com)."
                    if 'nlp' in name:
                        text = text + "Yes..!!We do work in NLP(Natural Language Processing )\n" \
                                      "Few of areas, we cover are:-" \
                                      "â€¢ Conversational AI" \
                                      "â€¢ Text Summarization" \
                                      "â€¢ Abstractive" \
                                      "â€¢ Extractive\n" \
                                      "For further assist please contact our expert at ðŸ“§ (mailto:info@sandlogic.com)."
                    if 'safety' in name:
                        text = text + "Yes..!!We do work for Work place Safety\n" \
                                      "Few of areas, we cover are:-" \
                                      "â€¢ Hardhat" \
                                      "â€¢ SafetyJacket" \
                                      "â€¢ Helmet" \
                                      "â€¢ Gloves" \
                                      "â€¢ Shoes" \
                                      "â€¢ Unauthorized Action Recognition\n" \
                                      "For further assist please contact our expert at ðŸ“§ (mailto:info@sandlogic.com)."
            dispatcher.utter_message(text=text)

        if text == "" or len(entities) == 0:
            dispatcher.utter_message(
                text="I dont have much info about this. Please contact our expert for details ðŸ“§ (mailto:info@sandlogic.com). If you want to know about our work in deep face, OCR, Deep vision, warehouse, agriculture, medical, Audio NLP, Pattern and Materials, NLP and workplace security. Please be free to ask")
            return []


class askProductService(Action):

    def name(self) -> Text:
        return "action_product_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        text = ""
        name = tracker.get_slot("project_type")
        if len(entities) == 1:
            for e in entities:
                if e['entity'] == 'project_type':
                    name = e['value']
                if name == 'products':
                    text = text + "Great, Let me give you tour about our Products.\n"
                    buttons = [
                        {"payload": "AUVI", "title": "AUVI"},
                        {"payload": "SARA", "title": "SARA"},
                        {"payload": "TXTR", "title": "TXTR"},
                        {"payload": "WareHouz", "title": "Warehouz"},
                        {"payload": "EdgeMatrix", "title": "EdgeMatrix"},
                        {"payload": "AudioNLP", "title": "Audio NLP"},
                        {"payload": "ContagionManagement", "title": "Contagion Management"},
                        {"payload": "workspace", "title": "WorkPlace solutions"},
                    ]
                    text = text + "Click on option to know more about them"

                if name == 'services':
                    text = text + "Great, Let me give you tour about our services.\n"
                    buttons = [
                        {"payload": "CORE", "title": "CORE"},
                        {"payload": "CV", "title": "CV based Models"},
                        {"payload": "R&D", "title": "R&D-AS-A-SERVICE"},
                        {"payload": "Domain", "title": "Domain Specific Models"},
                        {"payload": "CustomModels", "title": "Custom Models"},
                    ]
                    text = text + "Click on option to know more about them"

        if text != "":
            dispatcher.utter_message(text=text, buttons=buttons)
            return [SlotSet("project_type", name)]
        else:
            text = "Well what would you like to know about our products or services."
            buttons = [
                {"payload": "products", "title": "Products"},
                {"payload": "services", "title": "Services"},
            ]
            text = text + " Click on option to know about them"
            dispatcher.utter_message(text=text, buttons=buttons)
        return []


class askProductServiceInfo(Action):

    def name(self) -> Text:
        return "action_product_service_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = ""
        name = tracker.get_slot("project")
        if name == 'AUVI':
            text = text + "Auvi is AI framework for end to end design, development, annotation, and testing, of a neural net & anything in AI. It’s also a project management tool which reduces your project cycle time by over 30% and save on costs.\n"
        if name == 'SARA':
            text = text + "In-house developed tool for automating daily routine cognitive tasks. This tool is based on Intelligent RPA, Hyper Automation, & AI.\n" \
                          "It’s low cost & extremely advanced in comparison to market.\n" \
                          "Also, incorporated with AI & OCR enabled bots to extract & analyze the information in real time."
        if name == 'TXTR':
            text = text + "Pioneered with Optical Character Recognition (OCR) & Intelligent Character Recognition (ICR), this tool Identifies, Classify, Categorize, Capture the text statements from any image file.\n" \
                          "Then, Stores it into desired editable text files (or other formats)."
        if name == 'WareHouz':
            text = text + "A single tool to automate almost 60% process (manually done) in any largescale warehouse – be it at a Inbound stage, Outbound stage, Storage stage, or Retrieval stage.\n" \
                          "This tool is occupied with the power of Deep Learning, CV, Image Processing, ML, & custom neural network models."
        if name == 'EdgeMatrix':
            text = text + "A H/W enabler tool, which help organizations to unleased the power for Edge based Analytics.\n" \
                          "With this tool you can deploy & run any DL or ML model on any hardware (GPU or Memory based) or FPGA."
        if name == 'ContagionManagement':
            text = text + "An end-to-end solution to monitor the compliance and to ensure the maximum effectiveness of the preventive measures by providing the alerts to concerned team.\n" \
                          "Solution is a combination of CV, along with AI & ML."
        if name == 'AudioNLP':
            text = text + "A futuristic product to analyze & classify the various types of sounds by combining the power of NLP, CNN, & MFCCs features.\n"

        if name == 'workplace':
            text = text + "A robust solution for you workspace – it secure your people & premises, also, mark their attendances using facial recognition\n"

        if name == 'CORE':
            text = text + "Creation, training of NN models are easier on high end configuration VMs on cloud or high end computer desktops on premises. With the decrease in cost of hardware, controllers, GPUs and increase in computational power, smart devices and hardware are available on which AI models can be deployed."
        if name == 'R&D':
            text = text + "With R&D services, we don't limit ourself.Give us a your idea/program, we plan & do research accordingly & tries to give to tangible results.Changing your plan to reality."
        if name == 'custommodel':
            text = text + "Custom models provide the customers with the freedom required to meet their specific requirements from a model under constraints and limitations.\n" \
                          "There are several benefits of the custom model which are difficult to ignore, for building commercial solutions and products as part of the business portfolio."

        if text != "":
            list = tracker.get_slot("previous_form_list")
            if list:
                prev_project = tracker.get_slot("prev_project")
                if prev_project:
                    if prev_project == name:
                        list.append("Info")
                        rem_list = [i for i in list + Projects_Form_List if i not in list or i not in Projects_Form_List]

                    else:
                        list = []
                        list.append("Info")
                        rem_list = ["Features", "Benefits"]
                else:
                    list = []
                    list.append("Info")
                    rem_list = ["Features", "Benefits"]

            else:
                list = ['Info']
                rem_list = ["Features", "Benefits"]
            buttons = []
            for i in rem_list:
                buttons.append({"payload": i, "title": i})
            dispatcher.utter_message(text=text, buttons=buttons)
            return [SlotSet("prev_project", name),
                    SlotSet("previous_form_list",list),
                    SlotSet("continue",None)]

        else:
            text = "I didn't quite understood the product or service you are asking. Please click on one of the options to know about the product or service."
            buttons = [
                {"payload": "AUVI", "title": "AUVI"},
                {"payload": "SARA", "title": "SARA"},
                {"payload": "TXTR", "title": "TXTR"},
                {"payload": "WareHouz", "title": "Warehouz"},
                {"payload": "EdgeMatrix", "title": "EdgeMatrix"},
                {"payload": "AudioNLP", "title": "Audio NLP"},
                {"payload": "ContagionManagement", "title": "Contagion Management"},
                {"payload": "workspace", "title": "WorkPlace solutions"},
                {"payload": "CORE", "title": "CORE"},
                {"payload": "CV", "title": "CV based Models"},
                {"payload": "R&D", "title": "R&D-AS-A-SERVICE"},
                {"payload": "Domain", "title": "Domain Specific Models"},
                {"payload": "CustomModels", "title": "Custom Models"}
            ]
            dispatcher.utter_message(text=text, buttons=buttons)
            return [SlotSet("continue",None)]


class askProductServiceBenefits(Action):

    def name(self) -> Text:
        return "action_product_service_benefits"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = ""
        name = tracker.get_slot("project")
        if name == 'AUVI':
            text = text + "benefits of AUVI\n"
        if name == 'SARA':
            text = text + "benefits of SARA\n"
        if name == 'TXTR':
            text = text + "benefits of txtr"
        if name == 'WareHouz':
            text = text + "benefits of warehouz\n"
        if name == 'EdgeMatrix':
            text = text + "benefits of edgematrix\n"
        if name == 'ContagionManagement':
            text = text + "benefits of contagion management\n"
        if name == 'AudioNLP':
            text = text + "benefits of Audion NLP\n"
        if name == 'workplace':
            text = text + "benefits of ws s & s\n"
        if name == 'CORE':
            text = text + "benefits of core\n"
        if name == 'R&D':
            text = text + "benefits of r&d\n"
        if name == 'custommodel':
            text = text + "benefits of cm\n"

        if text != "":
            list = tracker.get_slot("previous_form_list")
            if list:
                prev_project = tracker.get_slot("prev_project")
                if prev_project:
                    if prev_project == name:
                        list.append("Benefits")
                        rem_list = [i for i in list + Projects_Form_List if i not in list]
                    else:
                        list = []
                        list.append("Benefits")
                        rem_list = ['Info', 'Features']
                else:
                    list = []
                    list.append("Benefits")
                    rem_list = ['Info', 'Features']

            else:
                list = ['Benefits']
                rem_list = ['Info', 'Features']
            buttons = []
            for i in rem_list:
                buttons.append({"payload": i, "title": i})
            dispatcher.utter_message(text=text, buttons=buttons)
            return [SlotSet("prev_project", name),
                    SlotSet("previous_form_list", list),
                    SlotSet("continue",None)]
        else:
            text = "I didn't quite understood the product or service you are asking. Please click on one of the options to know about the product or service."
            buttons = [
                {"payload": "AUVI", "title": "AUVI"},
                {"payload": "SARA", "title": "SARA"},
                {"payload": "TXTR", "title": "TXTR"},
                {"payload": "WareHouz", "title": "Warehouz"},
                {"payload": "EdgeMatrix", "title": "EdgeMatrix"},
                {"payload": "AudioNLP", "title": "Audio NLP"},
                {"payload": "ContagionManagement", "title": "Contagion Management"},
                {"payload": "workspace", "title": "WorkPlace solutions"},
                {"payload": "CORE", "title": "CORE"},
                {"payload": "CV", "title": "CV based Models"},
                {"payload": "R&D", "title": "R&D-AS-A-SERVICE"},
                {"payload": "Domain", "title": "Domain Specific Models"},
                {"payload": "CustomModels", "title": "Custom Models"}
            ]
            dispatcher.utter_message(text=text, buttons=buttons)
            return []


class askProductServiceFeatures(Action):

    def name(self) -> Text:
        return "action_product_service_features"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = ""

        name = tracker.get_slot("project")
        if name == 'AUVI':
            text = text + "Hey..Glad you asked.!!\n" \
                          "AuVi.io framework helps in the creation of the dataset, annotation and labelling, visualization and verification of the annotations and output format for the annotations as required by the neural net for training, and the trained neural nets can be plugged into SARA.\n" \
                          "I would suggest to look feature of SARA.ai, which is solution many.\n" \
                          "Please contact our expert for further details ðŸ“§ (mailto:info@sandlogic.com)\n"
        if name == 'SARA':
            text = text + "Hey..Thanks for your interest..!!\n" \
                          "Sara is framework where the intelligence of AI blends with the automation of RPA to provide capabilities beyond the horizons of traditional RPA and automation systems.\n" \
                          "Few main feature to mention are :-\n" \
                          "-> Accelerating :- Compliment screen level integrations with API level integrations,Implementing RPA for processes requiring interaction with disparate legacy systems as well .\n" \
                          "-> OCR & HTR ENABLED BOTS :- Document data extraction of printed and handwritten text & analysis of information in real time, Integrate OCR engines communication within Bots for scanned text driven context switching.\n" \
                          "-> Audio Visual Intelligence enabled bots :- Bring in Visual and Audio inputs to your workflows, derive those critical inputs required your flows from Images, Videos and Audio.\n" \
                          "-> Automate across heterogeneous applications :- Author workflows across any web browsers, thick clients developed using any tech stack.\n" \
                          "-> Cloud & On-Prem Deployment\n" \
                          "Please contact our expert for further details ðŸ“§ (mailto:info@sandlogic.com)\n"
        if name == 'TXTR':
            text = text + "Pioneered with Optical Character Recognition (OCR) & Intelligent Character Recognition (ICR), this tool Identifies, Classify, Categorize, Capture the text statements from any image file.\n" \
                          "Then, Stores it into desired editable text files (or other formats)."
        if name == 'WareHouz':
            text = text + "Hey..Thanks for your interest..!!\n" \
                          "Our WareHouz is solution to many question. Let me give you a briefing about the feature\n" \
                          "-> Pallet label Detection/Classification/Identification.\n" \
                          "-> Bar/QR Code detection & decoding.\n" \
                          "-> Pallet box counting.\n" \
                          "-> Automated Storage rack detection.\n" \
                          "-> Automated retrieval of pallet.\n" \
                          "-> Automated pallet profile check.\n" \
                          "-> Interface warehouse management system.\n" \
                          "This are just few, I could mention. Please contact our expert for further details ðŸ“§ (mailto:info@sandlogic.com)\n"
        if name == 'EdgeMatrix':
            text = text + "A H/W enabler tool, which help organizations to unleased the power for Edge based Analytics.\n" \
                          "With this tool you can deploy & run any DL or ML model on any hardware (GPU or Memory based) or FPGA."
        if name == 'ContagionManagement':
            text = text + "An end-to-end solution to monitor the compliance and to ensure the maximum effectiveness of the preventive measures by providing the alerts to concerned team.\n" \
                          "Solution is a combination of CV, along with AI & ML."
        if name == 'AudioNLP':
            text = text + "A futuristic product to analyze & classify the various types of sounds by combining the power of NLP, CNN, & MFCCs features.\n"

        #if name == 'Workspace Safety & Security':
        if name == 'workplace':
            text = text + "A robust solution for you workspace – it secure your people & premises, also, mark their attendances using facial recognition\n"

        if name == 'CORE':
            text = text + "Creation, training of NN models are easier on high end configuration VMs on cloud or high end computer desktops on premises. With the decrease in cost of hardware, controllers, GPUs and increase in computational power, smart devices and hardware are available on which AI models can be deployed."
        if name == 'R&D':
            text = text + "With R&D services, we don't limit ourself.Give us a your idea/program, we plan & do research accordingly & tries to give to tangible results.Changing your plan to reality."
        if name == 'CustomModel':
            text = text + "Custom models provide the customers with the freedom required to meet their specific requirements from a model under constraints and limitations.\n" \
                          "There are several benefits of the custom model which are difficult to ignore, for building commercial solutions and products as part of the business portfolio."


        if text != "":
            list = tracker.get_slot("previous_form_list")
            if list:
                prev_project = tracker.get_slot("prev_project")
                if prev_project:
                    if prev_project == name:
                        list.append("Features")
                        rem_list = [i for i in list + Projects_Form_List if i not in list]
                    else:
                        list = []
                        list.append("Features")
                        rem_list = ['Info', 'Benefits']
                else:
                    list = []
                    list.append("Features")
                    rem_list = ['Info', 'Benefits']

            else:
                list = ['Features']
                rem_list = ['Info', 'Benefits']
            buttons = []
            for i in rem_list:
                buttons.append({"payload": i, "title": i})
            dispatcher.utter_message(text=text, buttons=buttons)
            return [SlotSet("prev_project", name),
                    SlotSet("previous_form_list", list),
                    SlotSet("continue",None)]
        else:
            text = "I didn't quite understood the product or service you are asking. Please click on one of the options to know about the product or service."
            buttons = [
                {"payload": "AUVI", "title": "AUVI"},
                {"payload": "SARA", "title": "SARA"},
                {"payload": "TXTR", "title": "TXTR"},
                {"payload": "WareHouz", "title": "Warehouz"},
                {"payload": "EdgeMatrix", "title": "EdgeMatrix"},
                {"payload": "AudioNLP", "title": "Audio NLP"},
                {"payload": "ContagionManagement", "title": "Contagion Management"},
                {"payload": "workspace", "title": "WorkPlace solutions"},
                {"payload": "CORE", "title": "CORE"},
                {"payload": "CV", "title": "CV based Models"},
                {"payload": "R&D", "title": "R&D-AS-A-SERVICE"},
                {"payload": "Domain", "title": "Domain Specific Models"},
                {"payload": "CustomModels", "title": "Custom Models"}
            ]
            dispatcher.utter_message(text=text, buttons=buttons)
            return []


class askProductServiceTechnologies(Action):

    def name(self) -> Text:
        return "action_product_service_technologies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text="We as AI company use a different methodology, to bringing thoughts from ideas to reality. Mainly, we work on different frameworks & Models.\nAs industry experts in deep-tech development, we possess the following skill sets in AI, ML, EdgeAI, Deep Learning, Computer Vision, Machine Vision, Warehouse Automation, Intelligent Automation, hyper automation, OCR, ICR, Data Labelling, NLP, and Speech Recognition.\nThat being said, we keep upgrading with time.ðŸ¤“"
        prev = tracker.get_slot('prev_project')
        buttons = None
        con = tracker.get_slot('continue')
        if prev and con == None:
            previous_form_list = tracker.get_slot('previous_form_list')
            if previous_form_list:
                if len(previous_form_list) < 3:
                    text = text + "\n Do you want to know more about the project" + prev
                if len(previous_form_list) == 3:
                    text = text + "\n Are you interested to know more projects other than" + prev
                buttons = [
                    {"payload": "Yes", "title": "Yes"},
                    {"payload": "No", "title": "No"},
                ]
        if buttons:
            dispatcher.utter_message(text=text, buttons=buttons)
        else:
            dispatcher.utter_message(text=text)
        return []


'''
class askProductServiceSectors(Action):

    def name(self) -> Text:
        return "action_product_service_sectors"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        text = ""
        if len(entities)!=0:
            project = []
            for e in entities:
                if e['entity'] == 'product':
                    name = e['value']
                    if name == 'AUVI':
                        project.append('AUVI')
                        text = text + "sectors of AUVI\n"
                    if name == 'SARA':
                        project.append('SARA')
                        text = text + "sectors of SARA\n"
                    if name == 'TXTR':
                        project.append('TXTR')
                        text = text + "sectors of txtr"
                    if name == 'WareHouz':
                        project.append('wareHouz')
                        text = text + "sectors of warehouz\n"
                    if name == 'EdgeMatrix':
                        project.append('EdgeMatrix')
                        text = text + "sectors of edgematrix\n"
                    if name == 'ContagionManagement':
                        project.append('Contagion Management')
                        text = text + "sectors of contagion management\n"
                    if name == 'AudioNLP':
                        project.append('Audio NLP')
                        text = text + "sectors of Audion NLP\n"

                if e['entity'] == 'service':
                    name = e['value']
                    if name == 'Workspace Safety & Security':
                        project.append('Workspace Safety & Security')
                        text = text + "sectors of ws s & s\n"
                    if name == 'CORE':
                        project.append('CORE')
                        text = text + "sectors of core\n"
                    if name == 'R&D':
                        project.append('R&D')
                        text = text + "sectors of r&d\n"
                    if name == 'CustomModel':
                        project.append('Custom Model')
                        text = text + "sectors of cm\n"

            dispatcher.utter_message(text=text)
            return [SlotSet("project",project)]
        if text=="":
            project = tracker.get_slot("project")
            for name in project:
                if name == 'AUVI':
                    text = text + "sectors of AUVI\n"
                if name == 'SARA':
                    text = text + "sectors of SARA\n"
                if name == 'TXTR':
                    text = text + "sectors of txtr"
                if name == 'WareHouz':
                    text = text + "sectors of warehouz\n"
                if name == 'EdgeMatrix':
                    text = text + "sectors of edgematrix\n"
                if name == 'ContagionManagement':
                    text = text + "sectors of contagion management\n"
                if name == 'AudioNLP':
                    text = text + "sectors of Audion NLP\n"

                if name == 'Workspace Safety & Security':
                    text = text + "sectors of ws s & s\n"
                if name == 'CORE':
                    text = text + "sectors of core\n"
                if name == 'R&D':
                    text = text + "sectors of r&d\n"
                if name == 'CustomModel':
                    text = text + "sectors of cm\n"

            dispatcher.utter_message(text=text)
            return [SlotSet("project", project)]

'''


class ActionCost(Action):

    def name(self) -> Text:
        return "action_cost"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text="Hey!! We work on custom business models, as per our customer's comfort & also as per the solution you are looking for.\nPlease reach out to our expert to know more at ðŸ“§ info@sandlogic.com. Happy to help"
        prev = tracker.get_slot('prev_project')
        buttons = None
        con = tracker.get_slot('continue')
        if prev and con == None:
            previous_form_list = tracker.get_slot('previous_form_list')
            if previous_form_list:
                if len(previous_form_list) < 3:
                    text = text + "\n Do you want to know more about the project" + prev
                if len(previous_form_list) == 3:
                    text = text + "\n Are you interested to know more projects other than" + prev
                buttons = [
                    {"payload": "Yes", "title": "Yes"},
                    {"payload": "No", "title": "No"},
                ]
        if buttons:
            dispatcher.utter_message(text=text, buttons=buttons)
        else:
            dispatcher.utter_message(text=text)
        return []

class ActionAffirm(Action):

    def name(self) -> Text:
        return "action_affirm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        previous_form_list = tracker.get_slot("previous_form_list")
        project = tracker.get_slot('prev_project')
        buttons = []
        text = ""
        if len(previous_form_list)<3:
            text = text + "Please select one of the options to know about" + project
            rem_list = [i for i in Projects_Form_List if i not in previous_form_list]
            for i in rem_list:
                buttons.append({"payload":i,"title":i})
        if len(previous_form_list) == 3:
            text = text + "Please select one of the product or service you want to know"
            buttons = [
                {"payload": "AUVI", "title": "AUVI"},
                {"payload": "SARA", "title": "SARA"},
                {"payload": "TXTR", "title": "TXTR"},
                {"payload": "WareHouz", "title": "Warehouz"},
                {"payload": "EdgeMatrix", "title": "EdgeMatrix"},
                {"payload": "AudioNLP", "title": "Audio NLP"},
                {"payload": "ContagionManagement", "title": "Contagion Management"},
                {"payload": "workspace", "title": "WorkPlace solutions"},
                {"payload": "CORE", "title": "CORE"},
                {"payload": "CV", "title": "CV based Models"},
                {"payload": "R&D", "title": "R&D-AS-A-SERVICE"},
                {"payload": "Domain", "title": "Domain Specific Models"},
                {"payload": "CustomModels", "title": "Custom Models"}
            ]
        dispatcher.utter_message(text=text,buttons=buttons)

class ActionDeny(Action):

    def name(self) -> Text:
        return "action_deny"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Feel free to ask if you're interested")
        return[SlotSet("continue","No")]

class ActionWordMeaning(Action):

    def name(self) -> Text:
        return "action_word_meaning"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        text = ""
        for e in entities:
            if e['entity']=='word':
                name = e['value']
                name = name.lower()
                w = ""
                for i in name.split():
                    w = w+i
                for x in meaning:
                    if w == x:
                        text = text + meaning[w]
        if text!="":
            dispatcher.utter_message(text=text)
        else:
            dispatcher.utter_message(text="We dont have info about this.")



        return []

# class ActionSwitchFormsAsk(Action):
#     """Asks to switch forms"""
#
#     def name(self) -> Text:
#         return "action_switch_forms_ask"
#
#     async def run(
#             self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         """Executes the custom action"""
#         active_form_name = tracker.active_form.get("name")
#         intent_name = tracker.latest_message["intent"]["name"]
#         next_form_name = NEXT_FORM_NAME.get(intent_name)
#
#         if (
#                 active_form_name not in FORM_DESCRIPTION.keys()
#                 or next_form_name not in FORM_DESCRIPTION.keys()
#         ):
#             logger.debug(
#                 f"Cannot create text for `active_form_name={active_form_name}` & "
#                 f"`next_form_name={next_form_name}`"
#             )
#             next_form_name = None
#         else:
#             text = (
#                 f"We haven't completed to tell {FORM_DESCRIPTION[active_form_name]} yet. "
#                 f"Are you sure you want to switch to {FORM_DESCRIPTION[next_form_name]}?"
#             )
#             buttons = [
#                 {"payload": "yes", "title": "yes"},
#                 {"payload": "no", "title": "no"},
#             ]
#             dispatcher.utter_message(text=text, buttons=buttons)
#
#         return [SlotSet("next_form_name", next_form_name)]
#
#
# class ActionSwitchFormsAffirm(Action):
#     """Switches forms"""
#
#     def name(self) -> Text:
#         return "action_switch_forms_affirm"
#
#     async def run(
#             self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         """Executes the custom action"""
#         active_form_name = tracker.active_form.get("name")
#         next_form_name = tracker.get_slot("next_form_name")
#
#         if (
#                 active_form_name not in FORM_DESCRIPTION.keys()
#                 or next_form_name not in FORM_DESCRIPTION.keys()
#         ):
#             logger.debug(
#                 f"Cannot create text for `active_form_name={active_form_name}` & "
#                 f"`next_form_name={next_form_name}`"
#             )
#         else:
#             text = (
#                 f"Great. Lets discuss about {FORM_DESCRIPTION[active_form_name]} "
#                 f"Once it is completed, we will discuss about {FORM_DESCRIPTION[next_form_name]}."
#             )
#             dispatcher.utter_message(text=text)
#
#         return [
#             SlotSet("previous_form_name", active_form_name),
#             SlotSet("next_form_name", None),
#         ]
#
#
# class ActionSwitchBackAsk(Action):
#     """Asks to switch back to previous form"""
#
#     def name(self) -> Text:
#         return "action_switch_back_ask"
#
#     async def run(
#             self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         """Executes the custom action"""
#         previous_form_name = tracker.get_slot("previous_form_name")
#
#         if previous_form_name not in FORM_DESCRIPTION.keys():
#             logger.debug(
#                 f"Cannot create text for `previous_form_name={previous_form_name}`"
#             )
#             previous_form_name = None
#         else:
#             text = (
#                 f"Would you like to go back to know about "
#                 f"{FORM_DESCRIPTION[previous_form_name]} now?."
#             )
#             buttons = [
#                 {"payload": "yes", "title": "yes"},
#                 {"payload": "no", "title": "no"},
#             ]
#             dispatcher.utter_message(text=text, buttons=buttons)
#
#         return [SlotSet("previous_form_name", None)]
#
#
# class ActionSwitchFormsDeny(Action):
#     """Does not switch forms"""
#
#     def name(self) -> Text:
#         return "action_switch_forms_deny"
#
#     async def run(
#             self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         """Executes the custom action"""
#         active_form_name = tracker.active_form.get("name")
#
#         if active_form_name not in FORM_DESCRIPTION.keys():
#             logger.debug(
#                 f"Cannot create text for `active_form_name={active_form_name}`."
#             )
#         else:
#             text = f"Ok, let's continue with the {FORM_DESCRIPTION[active_form_name]}."
#             dispatcher.utter_message(text=text)
#
#         return [SlotSet("next_form_name", None)]
