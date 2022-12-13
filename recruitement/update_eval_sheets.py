from urllib import request, response
from functions import *
from googleapiclient import discovery

if __name__ == "__main__":
    with open('eval_sheets.json', 'r') as f:
        eval_sheets = list(map(json.loads, f))

    service = discovery.build('sheets', 'v4', credentials=cred)
    index = 1

    for eval_sheet in eval_sheets[0][6:]:
        progress_bar(index+1,len(eval_sheets[0]))
        index = index +1
        print("Sleeping")
        time.sleep(30)
        print("Updating {0}'s evaluation sheet".format(eval_sheet['name']))
        for _ in [0, 1]:
            request_body = {
                "requests": [

                    {
                        "insertDimension": {
                            "range": {
                                "sheetId": '0',
                                "dimension": "ROWS",
                                "startIndex": 13,
                                "endIndex": 14
                            },
                            "inheritFromBefore": True
                        }
                    },
                    {
                        "mergeCells": {
                            "range": {
                                "sheetId": '0',
                                "startRowIndex": 13,
                                "endRowIndex": 14,
                                "startColumnIndex": 4,
                                "endColumnIndex": 6
                            },
                            "mergeType": "MERGE_ALL"
                        }
                    },


                ],
            }

            response = service.spreadsheets().batchUpdate(
                spreadsheetId=eval_sheet['id'],
                body=request_body
            ).execute()

            sheet = file.open(eval_sheet['name']).sheet1

            sheet.update_acell("G14", "1")
            sheet.update_acell("C3", "interviewer_1")
            sheet.update_acell("D3", "interviewer_2")
            sheet.update_acell("E14:F14", "=ARRONDI((C14+D14)/2) * G14")

        data =[
            ["Can you provide me with examples of ensemble methods?"],
            ["Can you define the difference between Bagging and Boosting?"],
            ["How can we handle unbalanced dataset?"]

        ]

        sheet = service.spreadsheets()
        result = sheet.values().append(spreadsheetId=eval_sheet['id'],
                                    range='Questions!B16:B16', valueInputOption="USER_ENTERED",insertDataOption="INSERT_ROWS", body={
            "values":data
        }).execute()

    

        
