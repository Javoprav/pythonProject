from data_manager.manager import load_data

def get_statistics():

    data = load_data()

    return len(data)