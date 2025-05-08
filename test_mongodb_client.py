from storage.mongodb_client import MongoDBClient
from datetime import datetime, timezone


def run_tests():
    # Initialize the MongoDB client
    client = MongoDBClient(db_name="code_and_coffee_test_db")
    test_collection = "test_articles"

    # Clear the test collection before starting
    client.clear(test_collection)

    # Test data
    article1 = {
        "guid": "article-001",
        "title": "Test Article 1",
        "content": "This is a test article.",
        "published_at": datetime.now(timezone.utc)
    }

    article2 = {
        "guid": "article-002",
        "title": "Test Article 2",
        "content": "This is another test article.",
        "published_at": datetime.now(timezone.utc)
    }

    # Test save()
    print("\n🔄 Testing save()...")
    client.save(article1, test_collection)
    client.save(article2, test_collection)

    # Test is_duplicate()
    print("\n🔄 Testing is_duplicate()...")
    assert client.is_duplicate(article1, test_collection), "❌ Duplicate check failed!"
    assert not client.is_duplicate({"guid": "article-003"}, test_collection), "❌ False positive on duplicate check!"

    # Test fetch()
    print("\n🔄 Testing fetch()...")
    fetched_articles = client.fetch({}, test_collection)
    print("Fetched Articles:", fetched_articles)
    assert len(fetched_articles) == 2, "❌ Fetch failed!"

    # Test update()
    print("\n🔄 Testing update()...")
    client.update({"guid": "article-001"}, {"title": "Updated Test Article 1"}, test_collection)
    updated_article = client.fetch({"guid": "article-001"}, test_collection)[0]
    print("Updated Article:", updated_article)
    assert updated_article["title"] == "Updated Test Article 1", "❌ Update failed!"

    # Test delete()
    print("\n🔄 Testing delete()...")
    client.delete({"guid": "article-001"}, test_collection)
    remaining_articles = client.fetch({}, test_collection)
    print("Remaining Articles After Delete:", remaining_articles)
    assert len(remaining_articles) == 1, "❌ Delete failed!"

    # Test get_all_collections()
    print("\n🔄 Testing get_all_collections()...")
    all_collections = client.get_all_collections()
    print("All Collections:", all_collections)
    assert test_collection in all_collections, "❌ get_all_collections failed!"

    # Test clear()
    print("\n🔄 Testing clear()...")
    client.clear(test_collection)
    assert len(client.fetch({}, test_collection)) == 0, "❌ Clear failed!"
    print("✅ Clear test passed!")

    # Disconnect when done
    client.disconnect()
    print("\n🎉 All tests passed!")


if __name__ == "__main__":
    run_tests()
