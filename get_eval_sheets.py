from functions import *

if __name__=="__main__":
    query = f"parents = '{root_folder_id}'"
    eval_sheets = []
    metadata = service.files().list(q = query).execute()

    folders = [(file['id'],file['name']) for file in metadata['files']]
    for folder in folders:
        query = f"parents = '{folder[0]}' and name='{folder[1]}'"
        file_metadata = service.files().list(q = query).execute()     
        print(file_metadata)
        eval_sheets.append({"id":file_metadata['files'][0]['id'],"name":file_metadata['files'][0]['name']})


    with open('eval_sheets.json', 'w') as fout:
        json.dump(eval_sheets , fout)