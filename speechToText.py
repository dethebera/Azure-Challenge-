#inside speechtotext.py, enter the following code to create two variables and a speech_config object. The first line imports the necessary package for the speech sdk.
import azure.cognitiveservices.speech as speechsdk
speech_key, service_region = "YourSubscriptionKey", "YourServiceRegion"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

