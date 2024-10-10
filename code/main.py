from transformers import pipeline
import yake

# NOTE: This updated approach is roughly 4.64 times slower than the 
# original approach and the runtime has increased by about 364.58%.

def analyze_sentiment(review: str) -> dict:
    # added the default model as distilbert to ensure consistency in the sentiment scoring
    sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    result = sentiment_analyzer(review)
    return result[0]

def extract_keywords(text: str, num_keywords: int = 5) -> list[str]:
    custom_kw_extractor = yake.KeywordExtractor(
        lan="en",
        n=num_keywords,
        dedupLim=0.9,
        top=num_keywords,
        features=None
    )
    keywords = [kw for kw, score in custom_kw_extractor.extract_keywords(text)]
    return keywords

def extract_issues(text: str) -> list[str]:
    issues = []
    # added crash a category as well as I saw it often  
    keywords = ["bug", "problem", "issue", "crash"]
    for keyword in keywords:
        if keyword in text.lower():
            issues.append(keyword)
    return issues

def context_aware_sentiment_classification(text: str, keywords: list[str]) -> tuple[set[str], set[str]]:
    positive_aspects = set()
    negative_aspects = set()

    for keyword in keywords:
        sentiment_result = analyze_sentiment(keyword)
        sentiment = sentiment_result['label']

        if sentiment == 'POSITIVE':
            positive_aspects.add(keyword)
        elif sentiment == 'NEGATIVE':
            negative_aspects.add(keyword)

    return positive_aspects, negative_aspects

def extract_insights(reviews: list[str]) -> tuple[list[str], list[str], list[str]]:
    positive_aspects = set()
    negative_aspects = set()
    issues = set()

    for review in reviews:
        keywords = extract_keywords(review)
        # NOTE: We used context awareness to improve the accuracy of sentiment categorization. 
        # Context-aware sentiment analysis considers the surrounding context of keywords, 
        # leading to more accurate classification of sentiments. This approach helps reduce misclassification by 
        # understanding the sentiment in relation to the entire text, not just isolated words.
        pos_aspects, neg_aspects = context_aware_sentiment_classification(review, keywords)

        positive_aspects.update(pos_aspects)
        negative_aspects.update(neg_aspects)
        issues.update(extract_issues(review))

    return list(positive_aspects), list(negative_aspects), list(issues)

reviews = [
    "I love this product! It's amazing!",
    "The quality is top-notch, but the price is too high.",
    "The instructions are unclear and confusing.",
    "Great features, but it crashes frequently.",
    "Not satisfied with the customer service.",
    "Excellent product, worth every penny!",
    "The design is sleek and modern, but the battery life is disappointing.",
    "Easy to use and setup, but lacks some advanced features.",
    "Disappointed with the shipping time. It took longer than expected.",
    "This product exceeded my expectations. Highly recommended!",
    "The customer support team was helpful and resolved my issue promptly.",
    "The user interface is intuitive, making it user-friendly.",
    "Received a damaged product. Poor packaging.",
    "The price is reasonable considering the features it offers.",
    "I encountered a software bug that needs immediate attention.",
    "The sound quality is excellent, but the device heats up quickly.",
    "The product is durable and built to last. Impressed with the build quality.",
    "Terrible experience with the return process. It was a hassle.",
    "Average product. Nothing extraordinary, but it gets the job done.",
    "The user manual is comprehensive and easy to follow.",
    "Not recommended. Numerous issues with functionality.",
    "The product arrived earlier than expected. Pleasant surprise!",
    "The interface is outdated and could use a modern redesign.",
    "Fantastic customer service. They went above and beyond to assist me.",
    "The product is versatile and can be used for various applications.",
    "Not happy with the performance. Laggy and slow.",
    "Great value for the money. Affordable and high-quality.",
    "The product is a game-changer. I can't imagine life without it.",
    "The packaging was eco-friendly, which is a plus for me.",
    "Too many unnecessary features. It complicates the user experience.",
    "Responsive touchscreen, but the battery drains quickly.",
]

positive_aspects, negative_aspects, issues = extract_insights(reviews)
print("Positive Aspects:", positive_aspects)
print("Negative Aspects:", negative_aspects)
print("Issues:", issues)