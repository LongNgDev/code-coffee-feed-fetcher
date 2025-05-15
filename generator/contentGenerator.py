from generator.aiClient import AiClient
from articles.Article import Article

class ContentGenerator(AiClient):
    def __init__(self, model_name: str = "llma3"):
        super().__init__(model_name=model_name)
        self.article = Article()
        
    def generate_title(self, content:str = ""):
        title = ""
        
        PROMPT = f"""
            You are a professional tech journalist and SEO expert.

            Your task is to write a single, catchy, and SEO-optimised headline for a modern technology news article, based on the article below.

            Before writing, consider multiple headline options internally. Evaluate them based on:
            - Character length (under 70)
            - Clarity and news value
            - SEO strength for search visibility
            - Must include relevant keywords naturally
            - Must clearly express the article’s main topic or angle
            - Use strong action words or curiosity hooks if appropriate
            - Must be engaging, newsy, and journalistic in tone
            - Keep the tone informative, but slightly conversational to fit the Code&Coffee blog audience — friendly, smart, and chill
            - Prioritisation of any available statistics or figures (e.g. investment amounts, review dates)

            Return only the single, best headline as h1 component in HTML — no quotation marks, no explanation, and no extra formatting.
            
            [Strictly Follow the Rule above]

            Article:
            {content}

            [Title Only]

            """

        # Generate Title and return in HTML format
        try:
            title = self.generate(PROMPT) or ""

            if title == "":
                return None
            
            clean_title_html = self.clean_html_response(title)

            self.article.set_title(clean_title_html)

            return clean_title_html

        except Exception as e:
            print(f"❌ Error occured during generate Title: {e}")
        
        return title

    def generate_content(self, content:str = ""):
        """Generate content based on the provided pro mpt."""

        aiContent = ""
        
        PROMPT = f"""
            You are a professional tech journalist and SEO expert writing for Code&Coffee — a smart, cozy, and informative technology blog.

            Your task is to write clear, engaging, and SEO-optimised article body content in raw HTML format, ready to be embedded directly into a webpage. The article is based on the source material below.

            Before writing, internally consider multiple narrative flows. Select the most effective structure based on the following:

            - Total word count: approximately 700–900 words
            - Begin with a short, engaging introduction (<h2> followed by <p>) to set the context
            - Clearly explain the news angle, timeline of events, and involved parties
            - Naturally use strong, relevant keywords throughout (avoid keyword stuffing)
            - Prioritise and highlight key statistics, figures, or notable entities (e.g. funding amounts, companies, regulators)
            - Use short, clean paragraphs (<p> tags only) with smooth transitions
            - Maintain a journalistic tone with action verbs and clarity
            - Keep the writing smart, friendly, and slightly conversational to match Code&Coffee’s voice
            - End with a conclusion that reinforces the topic using terms like “AI startup”, “regulatory compliance”, or “tech investment”

            ⚠️ Output Format — Strict Instructions:
            - Return only valid, clean HTML body content
            - Begin with a single <h2> tag for the article subheading (do NOT repeat the original title)
            - Follow with one <p> tag per paragraph — do not skip or combine paragraphs
            - Do NOT use markdown syntax, triple backticks, or language identifiers
            - Do NOT include meta descriptions, comments, editor notes, or explanation
            - Do NOT output anything outside the HTML content

            [BEGIN ARTICLE SOURCE]
            {content}
            [END ARTICLE SOURCE]

            [Output: HTML Body Content Only — Begin with <h2>]
            """


        # Generate content and return in HTML format
        try:
            aiContent = self.generate(PROMPT) or ""

            # Clean up any markdown or newline artifacts from the output
            cleaned_content_html = self.clean_html_response(aiContent)

            self.article.set_content(cleaned_content_html)

        except Exception as e:
            print(f"❌ Error occured during generate Content: {e}")
        
        return cleaned_content_html
    
    def clean_html_response(self, raw:str = ""):
        if raw == "":
            return raw
        
        cleaned = raw.strip()

        # Step 1: Remove triple backticks + optional 'html' tag
        if cleaned.startswith("```html"):
            cleaned = cleaned[7:].strip()
        elif cleaned.startswith("```"):
            cleaned = cleaned[3:].strip()

        if cleaned.endswith("```"):
            cleaned = cleaned[:-3].strip()

        # Step 2: Replace literal \n with actual line breaks (only if needed)
        # Optional — for double-escaped LLM outputs
        cleaned = cleaned.replace('\\n', '')  # Unescape \n
        cleaned = cleaned.replace('\n\n', '')  # Clean up double newlines
        cleaned = cleaned.replace('\n', '')

        return cleaned.strip()
        
    def get_article(self):
        return self.article
        
      

if __name__ == "__main__":
    ARTICLE = """Manus AI is one of the hottest AI agent startups around, recently raising $75 million at a half-billion-dollar valuation in a round led by Benchmark.

    But two unnamed sources told Semafor that the investment is now under review by the U.S. Treasury Department over its compliance with 2023 restrictions on investing in Chinese companies.

    Benchmark’s lawyers cleared the investment because Manus isn’t technically developing its own AI models, but is instead a “wrapper” around existing ones, Semafor reported.

    Those lawyers also concluded Manus is not China-based since it’s incorporated in the Cayman Islands. (That’s a common structure used by Chinese companies, like Alibaba , to access foreign capital.)

    Benchmark has attracted criticism for its Manus investment from Founders Fund partner Delian Asparouhov, who posted on X “wow, actions have consequences?”.
    """

    
    client = ContentGenerator("phi4")

    content = client.generate_content(ARTICLE)
    print(client.get_article().to_dict())

    # print(content)
    client.close()