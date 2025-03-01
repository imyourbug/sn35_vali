import random
import os
from dotenv import load_dotenv

load_dotenv()


def model_selector(model_rotation_pool):

    # Return the selected model details
    return "gpt-4o-mini", "https://api.openai.com/v1", os.getenv("OPENAI_API_KEY")
