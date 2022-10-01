
from imports import *





def update_answers_sheet(candidate_answers,destination_folder):

    print("Updating answers sheet")

    sheet = file.open("answers_sheet").sheet1


    sheet.update_acell("F3",str(candidate_answers['fb']))
    sheet.update_acell("G3",str(candidate_answers['linkedin']))
    sheet.update_acell("H3",str(candidate_answers['github']))
    sheet.update_acell("I3",str(candidate_answers['previous_work']))


    sheet.update_acell("C3:D3",str(candidate_answers['club_before']))
    sheet.update_acell("C4:D4",str(candidate_answers['details_club']))
    sheet.update_acell("C5:D5",str(candidate_answers['active_club']))
    sheet.update_acell("C6:D6",str(candidate_answers['club_name']))
    sheet.update_acell("C7:D7",str(candidate_answers['hackathon']))
    sheet.update_acell("C8:D8",str(candidate_answers['hackathon_name']))
    sheet.update_acell("C9:D9",str(candidate_answers['software']))
    sheet.update_acell("C10:D10",str(candidate_answers['designer_concern']))
    
    sheet.update_acell("C11:D11",str(candidate_answers['why_deepflow']))
    sheet.update_acell("C12:D12",str(candidate_answers['feedback']))


    copy_file(answers_sheet_id, destination_folder, candidate_info['name']+'_answers')


def update_eval_sheet(candidate_info, destination_folder):

    print("Updating Evaluation Sheet")

    sheet = file.open("evaluation_sheet").sheet1

    sheet.update_acell('C2:F2', candidate_info['name'])

    sheet.update_acell('A2', "-")

    sheet.update_acell(
        'B2', candidate_info['university']+" "+candidate_info['year']+" "+candidate_info['field'])

    sheet.update_acell('H6', candidate_info['cs_score'])
    sheet.update_acell('I6', candidate_info['python_score'])
    sheet.update_acell('J6', candidate_info['ai_score'])

    if candidate_info['comm'] == "Yes":
        sheet.update_acell('H14',candidate_info['comm_position'])
        for i in range(14, 18):
            sheet.update_acell('G'+str(i), 1)
    else:
        sheet.update_acell('H14',"")
        for i in range(14, 18):
            sheet.update_acell('G'+str(i), 0)


    if candidate_info['grp_members'] != []:
        sheet.update_acell('C3', candidate_info['grp_members'][0])
        sheet.update_acell('B21:C21', candidate_info['grp_members'][0])

        sheet.update_acell('D3', candidate_info['grp_members'][1])
        sheet.update_acell('D21:G21', candidate_info['grp_members'][1])

    copy_file(eval_sheet_id, destination_folder, candidate_info['name'])


def copy_file(file_id, destination_folder, filename, resume=False):

    if resume == True:
        print("Copying Resume")
        if file_id.find("id=") != -1:
            file_id = file_id.split("id=", 1)[1]
        elif file_id.find("/d") != -1:
            file_id = file_id.split("/d/", 1)[1].split("/")[0]
    else:
        print("Copying Sheet")

    file_metadata = {
        'name': filename,
        'parents': [destination_folder]
    }
    service.files().copy(
        fileId=file_id,
        body=file_metadata
    ).execute()


def create_folder(folder_name):
    print("\nCreating folder for: {0}".format(folder_name))
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [root_folder_id]
    }
    return service.files().create(body=file_metadata).execute()['id']


def progress_bar(candidate, nb_candidates):
    perc = round((candidate/nb_candidates)*100)
    os.system("cls")
    print("["+"="*round(perc/2)+" "*round((nb_candidates-perc)/2)+"]"+str(candidate)+"/"+str(nb_candidates))