MOVIES RECOMMENDER SYSTEM

# 🎬 Movie Recommender using Machine Learning

This project is a simple **content-based movie recommendation system** built using Python and scikit-learn. It leverages movie overviews to compute similarities and suggest titles that are thematically close to the user’s input.

---

## 🚀 Features

- Content-based filtering using movie overviews
- Text vectorization with `CountVectorizer`
- Cosine similarity for recommendation logic
- Minimal dependencies and beginner-friendly
- CLI-based interaction (easy to extend into a web app)

---

## 🧠 How It Works

The system generates a textual 'tag' for each movie by combining the title and overview. These tags are vectorized into numerical representations using the bag-of-words approach. Then, cosine similarity is computed to find the most similar movies.

---

## datset

I got the datset from::https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/data
