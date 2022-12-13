
from functions import *

if __name__ == '__main__':
    df = pd.read_csv('accepted.csv')
    nb_candidates = df.shape[0]



    grps = {
        "1": ["Jihed", "Rayen"],
        "2": ["Dhia", "Omar"],
        "3": ["Rima", "Semah"],
        "4": ["Abdessalem", "Youssef"]
    }

    for index, candidate in df.iterrows():

        print("Sleeping")
        time.sleep(30)

        logging.basicConfig(filename="log.txt", level=logging.DEBUG)
        logging.debug(str(index))

        progress_bar(index+1,nb_candidates)
        if candidate['name'] == NULL:
            break
        candidate_info = {
            "name": candidate['name'],
            "university": candidate['university'],
            "year": candidate['year'],
            "field": candidate['field'],
            "cs_score": candidate['cs_score'],
            "python_score": candidate['python_score'],
            "ai_score": candidate['ai_score'],
            "day_time": candidate['day_time'],
            "group": candidate['group'],
            "comm": candidate['comm'],
            "comm_position": candidate['comm_position'],
            "resume_link": candidate['CV']
        }

        candidate_answers={
            "fb":candidate.iloc[11],
            "linkedin":candidate.iloc[12],
            "github":candidate.iloc[13],
            "club_before":candidate.iloc[15],
            "details_club":candidate.iloc[16],
            "active_club":candidate.iloc[17],
            "club_name":candidate.iloc[18],
            "hackathon":candidate.iloc[19],
            "hackathon_name":candidate.iloc[20],
            "software":candidate.iloc[26],
            "designer_concern":candidate.iloc[27],
            "previous_work":candidate.iloc[28],
            "why_deepflow":candidate.iloc[29],
            "feedback":candidate.iloc[30]
        }

        if "grp" in str(candidate['group']):
            candidate_info['grp_members'] = grps[candidate['group'][0]]
        else:
            candidate_info['grp_members'] = []

        folder_id = create_folder(candidate_info['name'])
        if (candidate_info['resume_link'] != '' and type(candidate_info['resume_link']) != float):
            copy_file(candidate_info['resume_link'], folder_id,
                      candidate_info['name']+"_resume", resume=True)

        update_eval_sheet(candidate_info, folder_id)
        update_answers_sheet(candidate_answers,folder_id)

    print("You're welcome, Rima u_u!")
