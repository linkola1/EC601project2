# Imports the Google Cloud client library
GOOGLE_APPLICATION_CREDENTIALS="D:\lin\EC601\project2\Phase1b\goolge-stroage-879f9abb00de.json"
from google.cloud import language_v1

# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = "Hello,this is Lexiao Lin"
document = language_v1.Document(
    content=text, type_=language_v1.Document.Type.PLAIN_TEXT
)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))