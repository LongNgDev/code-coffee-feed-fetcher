from storage.mongodb_client import MongoDBClient


def main():
    db = MongoDBClient()
    collection = db.get_collection("news_articles")
    print(f"Collection: {collection}")
    article = db.fetch({"title": "Scaling startups in the European market"}, "news_articles" )

    print(f"Article fetched from MongoDB:\n{article[0].get('_id', 'Untitled')}")
    


if __name__ == "__main__":
    main()
