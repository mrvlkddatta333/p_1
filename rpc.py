from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
import nltk
nlkt.download("punkt")

from nltk.sentiment import SentimentAnalyzer

sa = SentimentAnalyzer()

def check_sentiment(text):
    sentiment = sa.polarity_scores(text)
    compound = sentiment['compound']

    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"
    

def main():
    server = SimpleJSONRPCServer(('localhost', 7000))
    print("Listening on port 7000...")
    server.register_function(check_sentiment, 'check_sentiment')
    server.serve_forever()

if __name__ == "__main__":
    main()


from jsonrpclib import Server

text  = "I love programming in Python!"

def main():
    server = Server('http://localhost:7000')
    sentiment = server.check_sentiment(text)
    print(f"The sentiment of the text is: {sentiment}")

if __name__ == "__main__":
    main()