from src.logger import logging
from src.exception import CustomeException
import os,sys
import pickle

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok= True)

        with open(file_path, 'WB') as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomeException(e.sys)