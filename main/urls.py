"""TutorialsWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homePage, name='home'),path('home/', views.homePage, name='homePage'),
    # Machine Learning
    path('machine-learning-tutorials/', views.machinelearningtutorials, name='machineLearning'),
    path('deep-learning-neural-networks/', views.deeplearningneuralnetworks, name='deepLearningNeuralNetwork'),
    path('cloud-gpus/', views.cloudgpus, name='cloud GPUs'),
    path('reinforcement-learning/', views.reinforcementlearning, name='reinforcementLearning'),
    path('self-driving-cars/', views.selfdrivingcars, name='selfDrivingCars'),
    path('deep-learning-with-tensorflow-keras/', views.deeplearningwithtensorflowkeras, name='deepLearningWithTensorflowKeras'),
    path('practical-machine-learning/', views.practicalmachinelearning, name='practicalMachineLearning'),
    path('gta-v/', views.gtav, name='gtav'),
    path('starcraft-ii-ai/', views.starcraftiiai, name='starcraftiiAI'),
    path('chatbot-with-deep-learning/', views.chatbotwithdeeplearning, name='chatbotWithDeepLearning'),
    path('unconventional-neural-networks/', views.unconventionalneuralnetworks, name='unconventionalNeuralNetworks'),
    path('tensorflowjs/', views.tensorflowjs, name='tensorflowJs'),
    path('tensorflow-object-detection/', views.tensorflowobjectdetection, name='tensorflowObjectDetection'),
    path('support-vector-machines/', views.supportvectormachines, name='supportVectorMachines'),
    path('learn-about-clustering/', views.learnaboutclustering, name='learnAboutClustering'),
    path('image-recognition/', views.imagerecognition, name='imageRecognition'),
    path('halite-ii-artificial-intelligence/', views.haliteiiartificialintelligence, name=' haliteiiArtificialIntelligence'),
    # Data Analysis
    path('data-analysis-tutorials/', views.dataanalysistutorials, name='dataAnalysis'),
    path('machine-learning/', views.machinelearning, name='machineLearning'),
    path('data-analysis-with-pandas/', views.dataanalysiswithpandas, name='dataAnalysisWithPandas'),
    path('data-visualization-with-dash-and-python/', views.datavisualizationwithdashandpython, name='dataVisualizationWithDash'),
    path('data-visualization/', views.datavisualization, name='dataVisualization'),
        #Finance
    path('finance/', views.finance, name='finance'),
    path('getting-stock-prices/', views.stockprices, name='gettingStockPrices'),
    path('sklearn-intro/', views.sklearnintro, name='sklearnIntro'),
    path('google-cloud/', views.googlecloud, name='googleCloud'),
    path('images-and-video-analysis/', views.imagesandvideoanalysis, name='imagesAndVideoAnalysis'),
    path('distributed-computing/', views.distributedcomputing, name='distributedComputing'),
    path('natural-language-processing/', views.naturallanguageprocessing, name='naturalLanguageProcessing'),
    #Quantum Programming
    path('quantum-programming-tutorials/', views.quantumprogrammingtutorials, name='quantumProgramming'),
    path('game-development-tutorials/', views.gamedevelopmenttutorials, name='gameDevelopment'),
    #Python
    path('python-fundamental-tutorials/', views.pythonfundamentaltutorials, name='pythonFundamentals'),
    path('python-basics/', views.pythonbasics, name='pythonBasics'),
    path('python-intermediate/', views.pythonintermediate, name='pythonIntermediate'),
    path('sockets-tutorial/', views.socketstutorial, name='socketsTutorial'),
    # Web Development
    path('web-development-tutorials/', views.webdevelopmenttutorials, name='webDevelopment'),
    path('django-web-development/', views.djangowebdevelopment, name='djangoWebDevelopment'),
    path('flask/', views.flask, name='flask'),
    # Bots and AI
    path('bot-tutorials/', views.bottutorials, name='botandai'),
    path('gta-v/', views.gtav, name='gtav'),
    path('reddit-api-wrapper/', views.redditapiwrapper, name='redditApiWrapper'),
    path('self-driving-cars/', views.selfdrivingcars, name='selfDrivingCars'),
    path('discord-bots/', views.discordbots, name='discordbBots'),
    path('beautiful-soup-tutorial/', views.beautifulsouptutorial, name='beautifulSoupTutorial'),
    path('starcraft-ii-ai/', views.starcraftiiai, name='starcraftiiAI'),
    path('halite-ii-ai-coding/', views.haliteiiartificialintelligence, name=' haliteiiArtificialIntelligence'),
    path('halite-iii-ai-coding/', views.haliteiiiartificialintelligence, name=' haliteiiiArtificialIntelligence'),
    path('alexa-skills/', views.alexaskills, name='alexaSkills'),
    path('twitter-api/', views.twitterapi, name='twitterApi'),
    #RaspberryPI
    path('raspberry-pi/', views.raspberrypi, name='raspberryPi'),
    path('robotics-raspberry-pi/', views.roboticsraspberrypi, name='roboticsRaspberryPi'),
    path('building-quadcopter/', views.buildingquadcopter, name='buildingQuadcopter'),
    path('robotics-tutorials/', views.roboticstutorials, name='robotics'),
    #GUI
    path('gui-development-tutorials/', views.guitutorials, name='gui'),
    path('basic-gui-pyqt/', views.pyqt, name='pyqt'),
    path('tkinter/', views.tkinter, name='tkinter'),
    path('kivy-application/', views.kivy, name='kivy'),
    #GoLang
    path('golang-tutorials/', views.golangtutorials, name='golang'),
    path('syntax-go-language/', views.syntaxgolanguage, name='syntax-golang'),
    path('golang-types/', views.golangtypes, name='golang-types'),
    
]


