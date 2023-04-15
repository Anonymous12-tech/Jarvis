import openai
import speech_recognition as sr
import pyttsx3

# set up OpenAI API
openai.api_key = "YOU API KEY"

# set up speech recognition
r = sr.Recognizer()
mic = sr.Microphone()

# set up text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 200)  # set the speaking rate to 150 words per minute

while True:
    with mic as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        # recognize speech using Google Speech Recognition
        query = r.recognize_google(audio)

        # use OpenAI API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=query,
            temperature=0.5,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response_text = response.choices[0].text.strip()

        # use pyttsx3 to speak the response
        engine.say(response_text)
        engine.runAndWait()

        print("Response: ", response_text)
        

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    except Exception as e:
        print("An error occurred: {0}".format(e))
