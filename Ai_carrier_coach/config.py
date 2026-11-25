"""
Configuration module
Loads environment variables used across the projects 
"""

import os
from dotenv import load_dotenv

class Config:
    """
    central configuration class
    """

    GEMINI_API_KEY: str=os.getenv("GEMINI_API_KEY")

    MODEL_NAME: str = os.getenv("MODEL_NAME","gemini-2.5-flash")


    @staticmethod
    def validate():
       
        
       """validate mandatory configuration
       """

       if not Config.GEMINI_API_KEY:
         raise ValueError(
           "GEMINI_API_KEY is missing.please check your .env file"
         )
         
