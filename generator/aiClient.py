import subprocess
import re
import time

class AiClient:
    def __init__(self, model_name:str ="llama3"):
        self.model_name = model_name
        self.process = self._initialize_process()
        print(f"🚀 Persistent {model_name} process started!")

    def _initialize_process(self):
        try:
            return subprocess.Popen(
                ["ollama", "run", self.model_name],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                bufsize=1  # Line-buffered for better real-time response
            )
        except Exception as e:
            print(f"❌ Failed to start {self.model_name} subprocess: {e}")
            return None

    
    def generate(self, prompt):
        try:
            result = subprocess.run(
                ["ollama", "run", self.model_name],
                input=prompt + "\n",
                text=True,
                capture_output=True,
                encoding="utf-8",
                timeout=300
            )

            if result.stderr:
                print(f"⚠️ stderr: {result.stderr.strip()}")

            print(f"stdout: {result.stdout}")

            return result.stdout.strip()

        except Exception as e:
            print(f"❌ Error during subprocess run: {e}")
            return None

    def close(self):
        try:
            self.process.stdin.close()
            self.process.stdout.close()
            self.process.stderr.close()
            self.process.terminate()
            print(f"🛑 Persistent {self.model_name} process terminated.")
        except Exception as e:
            print(f"❌ Error closing subprocess: {e}")


    # 🎀 Context manager support
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

if __name__ == "__main__":

    for model in [ "mistral"]:
        start_time = time.time()
        client = AiClient(model_name=model)
        print(f"\nTesting {model}...")
        prompt = f"""
        Extract only the most relevant, concise keywords or tags that best describe the content of the following tech-focused article. Focus on technology-related terms, industry keywords, and company names. Return the tags as a single, comma-separated list with no explanations, no formatting, and no introductory text.
        """

        response = client.generate(prompt)
        tags = [tag.strip() for tag in response.split(",") if tag.strip()]
        print(f"{type(tags)}")
        end_time = time.time()
        print(f"Response ({model}): {tags}")
        client.close()
        print(f"Time taken: {end_time - start_time:.2f} seconds")
        print("=========================================")

