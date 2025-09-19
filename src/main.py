from nlp_preprocessing import preprocess_text
from sentiment_analysis import analyze_sentiment

def main():
    sample_text = "Python AI for NLP is amazing! I love learning new things about AI."
    
    print("Original Text:", sample_text)
    
    tokens = preprocess_text(sample_text)
    print("Preprocessed Tokens:", tokens)
    
    sentiment = analyze_sentiment(sample_text)
    print("Sentiment Analysis Result:", sentiment)

if __name__ == "__main__":
    main()
