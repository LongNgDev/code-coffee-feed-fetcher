from base.storage.mongodb_client import MongoDBClient
from generator.slugGenerator import SlugGenerator


def main():
    db = MongoDBClient("news_articles")
    collection = db.get_collection()
    article = db.fetch({"title": "One week left to spotlight your brand with a Side Event at TechCrunch All Stage"})
    all_article = list(collection.find({"slug" : {"$exists": False}}))

    for article in all_article:
        if not article:
            continue
        
        slugGenerator = SlugGenerator(article.get("title"))
        slugGenerator.generate_slug()
        slug = slugGenerator.get_slug()
        
        print(slug)

        db.update({"_id": article.get("_id")},{"slug": slug})

    print(f"Article fetched from MongoDB:\n{article[0].get('slug', 'Untitled')}")
    


if __name__ == "__main__":
    main()
