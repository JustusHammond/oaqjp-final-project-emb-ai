''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
# Import the emotion_analyzer function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Analyzer")

@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion analysis over it using emotion_detection()
        function. The output returned shows the emotion and its rating
        for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the emotions and rank from response
    emotions = response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)
    # Return the formatted string with the emotion and rank
    return (
       f"For the given statement, the system response is {emotions} ",
    {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion,
    },
       f"The dominant emotion is {dominant_emotion}" 
    )
