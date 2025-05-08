from abc import ABC, abstractmethod


class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        """Establish a connection to the database."""
        pass

    @abstractmethod
    def disconnect(self):
        """Close the connection to the database."""
        pass
  
    @abstractmethod
    def save(self, data: dict):
        """Save data to the database."""
        pass
    
    @abstractmethod
    def fetch(self, query: dict):
        """Fetch data from the database."""
        pass
    
    @abstractmethod
    def delete(self, query: dict):
        """Delete data from the database."""
        pass
    
    @abstractmethod
    def update(self, query: dict, update_data: dict):
        """Update data in the database."""
        pass
    
    @abstractmethod
    def clear(self):
        """Clear the database."""
        pass
    
    @abstractmethod
    def is_duplicate(self, query: dict) -> bool:
        """Check if data already exists in the database."""
        pass
    
    @abstractmethod
    def get_collection(self, collection_name: str):
        """Get a specific collection from the database."""
        pass
    
    @abstractmethod
    def get_all_collections(self):
        """Get all collections in the database."""
        pass
    
    