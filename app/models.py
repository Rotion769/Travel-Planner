from transformers import pipeline


# NOTE: these models are relatively large. If you want to avoid loading them in dev,
# guard with environment variables or lazy-init functions.


summarizer = pipeline("summarization", model="facebook/bart-large-cnn", tokenizer="facebook/bart-large-cnn")
mode_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", tokenizer="facebook/bart-large-mnli")