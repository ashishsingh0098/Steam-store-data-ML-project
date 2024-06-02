import sys
import pandas as pd

from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = ("/home/ashish/VScode files/Python files/projects/ML project/Loan-Approval-ML-project/artifacts/model.pkl")
            preprocessor_path = ('/home/ashish/VScode files/Python files/projects/ML project/Loan-Approval-ML-project/artifacts/preprocessor.pkl')
            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self, Income: int, Age: int, Experience: int, CURRENT_JOB_YRS: int, CURRENT_HOUSE_YRS: int, Marital_Status: str, House_Ownership: str, Car_Ownership: str, Profession: str, CITY: str, STATE: str):
        self.Income = Income
        self.Age = Age
        self.Experience = Experience
        self.CURRENT_JOB_YRS = CURRENT_JOB_YRS
        self.CURRENT_HOUSE_YRS = CURRENT_HOUSE_YRS
        self.Marital_Status = Marital_Status
        self.House_Ownership = House_Ownership
        self.Car_Ownership = Car_Ownership
        self.Profession = Profession
        self.CITY = CITY
        self.STATE = STATE

    
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Income": [self.Income],
                "Age": [self.Age],
                "Experience": [self.Experience],
                "CURRENT_JOB_YRS": [self.CURRENT_JOB_YRS],
                "CURRENT_HOUSE_YRS": [self.CURRENT_HOUSE_YRS],
                "Marital_Status": [self.Marital_Status],
                "House_Ownership": [self.House_Ownership],
                "Car_Ownership": [self.Car_Ownership],
                "Profession": [self.Profession],
                "CITY": [self.CITY],
                "STATE": [self.STATE],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)