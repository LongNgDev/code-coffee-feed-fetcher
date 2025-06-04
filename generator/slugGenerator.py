from slugify import slugify


class SlugGenerator:
  def __init__(self, raw_title: str, model_name:str = "mistral"):
    self.raw_title = raw_title
    self.slug = None
    
  def generate_slug(self):
    try:
      self.slug = slugify(self.raw_title)
      
    except Exception as e:
      print(f"❌ Error during slug generating: {e}")

    finally:  
      return None
    
  def get_slug(self):
    return self.slug