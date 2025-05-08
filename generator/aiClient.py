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
            # Use communicate for a single-shot prompt-response cycle
            stdout, stderr = self.process.communicate(input=prompt + "\n", timeout=300)
            # Clean up the ANSI escape sequences (if any)
            clean_output = re.sub(r'\x1b\[[0-9;]*[a-zA-Z]', '', stdout).strip()
            if stderr:
                print(f"⚠️ Subprocess stderr: {stderr.strip()}")
            return clean_output
        except Exception as e:
            print(f"❌ Subprocess error: {e}")
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

if __name__ == "__main__":
    ARTICLE = """Tesla’s attempt to trademark the term “Robotaxi” in reference to its vehicles has been refused by the U.S. Patent and Trademark Office for being too generic, according to a new filing. Another application by Tesla to trademark the term “Robotaxi” for its upcoming ride-hailing service is still under examination by the office.In addition, applications from Tesla for the trademark on the term “Cybercab” have been halted due to other companies pursuing similar “Cyber” trademarks. That includes one company that has applied for numerous trademarks related to aftermarket Cybertruck accessories. The USPTO issued Tuesday what’s known as a “nonfinal office action” on the “Robotaxi” trademark application, which means Tesla has three months to file a response or the office will abandon the application. A trademark lawyer representing Tesla did not immediately respond to a request for comment.

    Tesla applied for the trademarks in October 2024 on the same day that it revealed the Cybercab, the purpose-built electric car that it hopes to one day use in its planned autonomous ride-hailing service. Tesla also submitted two similar trademark applications October 10 for the term “Robobus,” which are still under examination.

    The trademark that was refused was assigned to a USPTO examiner on April 14. Tesla said it would use the word in reference to “[l]and vehicles; electric vehicles, namely automobiles; automobiles; and structural parts therefor,” according to the original application.

    While the USPTO examiner found there were no conflicting trademarks in existence, it refused the application because it was “merely descriptive.” The examiner wrote that the term “Robotaxi” is “used to describe similar goods and services by other companies.”

    “[S]uch wording appears to be generic in the context of applicant’s goods and/or services,” the examiner wrote.

    Tesla will be allowed to submit evidence and arguments to support its argument in favor of the trademark. If it does, the USPTO wants Tesla to provide “[f]act sheets, instruction manuals, brochures, advertisements and pertinent screenshots of applicant’s website as it relates to the goods and/or services in the application, including any materials using the terms in the applied-for mark.”

    In other words, Tesla needs to give the agency specific plans for how and why it deserves the “Robotaxi” trademark.

    The examiner also wrote that Tesla will need to tell the USPTO if “competitors” use the terms “ROBO, ROBOT, or ROBOTIC to advertise similar goods and/or services.”

    Tesla’s other application for the “Robotaxi” trademark would cover the use of the word when offering transportation services, including “coordinating travel arrangements for individuals and for groups,” “arranging time-based ridesharing services,” and offering vehicle sharing or rentals. That application was also assigned to a USPTO examiner on April 14, but no decision has been filed.

    This story has been updated to include information about the “Cybercab” trademark applications."""


    for model in [ "mistral"]:
        start_time = time.time()
        client = AiClient(model_name=model)
        print(f"\nTesting {model}...")
        prompt = f"""
        Analyze the following article and provide a list of relevant keywords or tags that best describe its content. The tags should be concise, relevant, and suitable for a tech-focused blog.

            Article: {ARTICLE}

            Return a list of tags only, no other text, no explanations, no formatting.
        """

        response = client.generate(prompt)
        tags = [tag.strip() for tag in response.split(",") if tag.strip()]
        print(f"{type(tags)}")
        end_time = time.time()
        print(f"Response ({model}): {tags}")
        client.close()
        print(f"Time taken: {end_time - start_time:.2f} seconds")
        print("=========================================")

