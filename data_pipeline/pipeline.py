from functools import reduce
import json

################# FP DATA PIPELINE #################

################# DATA CLEANUP FUNCTIONS #################

def clean_usernames(users):

    return list(map(lambda user: {**user, "name": user['name'].strip().capitalize()}, users))
        


def clean_emails(users):

    return list(map(lambda user: {**user, "email": user.get('email', '').lower()}, users))



def filter_valid_emails(users):
    
    return list(filter(lambda user: "@" in user['email'], users))



def filter_active_users(users):

    return list(filter(lambda user: user.get('active', False), users))


################# PIPELINE ENGINE #################

def run_pipeline(data, functions):

    return reduce(lambda acc, func: func(acc), functions, data)


################# MAIN #################

def main():

    cleaned_user_data_functions = [
        clean_usernames,
        clean_emails,
        filter_valid_emails,
        filter_active_users
]  
    # Open dirty data
    with open("dirty_data.json", "r") as file:
        retrieve_data = json.load(file)

    print("---------------Dirty Data----------------")
    for u in retrieve_data: print(u)

    cleaned_up_data = run_pipeline(retrieve_data, cleaned_user_data_functions)

    print("---------------Cleaned Data----------------")
    for u in cleaned_up_data: print(u)

    with open("clean_data.json", "w") as file:
        json.dump(cleaned_up_data, file, indent=4, ensure_ascii=False)



if __name__ == "__main__":
    main()