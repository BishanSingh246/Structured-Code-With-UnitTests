import os
from dotenv import load_dotenv

load_dotenv()
# Jira
jiraEmailAddr = os.getenv("jiraEmailAddr")
jiraApiKey = os.getenv("jiraApiKey")
jiraProjectName = os.getenv("jiraProjectName")
jiraUrl = os.getenv("jiraUrl")
# Database
mySqlHost = os.getenv("mySqlHost")
mySqlUser = os.getenv("mySqlUser")
mySqlPassword = os.getenv("mySqlPassword")
mySqlDatabase = os.getenv("mySqlDatabase")



# For fetching Total issues in Jira
def getTotalJiraIssue(jiraUrl,jiraEmail,jiraApiKey, jiraProjectName):
    # Add your code here and return the total issue. 
            
getTotalJiraIssue(jiraUrl,jiraEmailAddr,jiraApiKey, jiraProjectName)

# For fetching Jira issues details by page number and per page limit
def getJiraIssue(jiraUrl,jiraEmailAddr,jiraApiKey, jiraProjectName, pageNumber, perPageLimit):
    # Add your code here and return the array.         

data = getJiraIssue(jiraUrl,jiraEmailAddr,jiraApiKey, jiraProjectName, 1, 10)

# For inserting data into database using return value of get_jira_issue function  
def insertData(mySqlHost, mySqlUser, mySqlPassword, mySqlDatabaseName, data):
    # Add your code here and return the count how many data you inserted or updated into database.       

insertData(mySqlHost, mySqlUser, mySqlPassword, mySqlDatabase, data)

# For Inserting all data into database 
def insertAllData(mySqlHost, mySqlUser, mySqlPassword, mySqlDatabaseName):
    # Add your code here and return count of row from database after inserting or updating all data into database.

insertAllData(mySqlHost, mySqlUser, mySqlPassword, mySqlDatabase)

#  For changing status of the single jira issue using issue Key
def statusChange(jiraUrl,jiraEmail,jiraApiKey,mySqlHost, mySqlUser, mySqlPassword, mySqlDatabaseName,jiraIssueIdOrKey,newStatus):
    # Add your code here and return the response.

statusChange(jiraUrl,jiraEmailAddr,jiraApiKey,mySqlHost, mySqlUser, mySqlPassword, mySqlDatabase,10019,"In Progress")

# For changing title of the single jira issue using issue Key
def titleChange(jiraUrl,jiraEmail,jiraApiKey,mySqlHost, mySqlUser, mySqlPassword, mySqlDatabaseName,jiraIssueIdOrKey,newTitle):
    # Add your code here and return the response.

titleChange(jiraUrl,jiraEmailAddr,jiraApiKey,mySqlHost, mySqlUser, mySqlPassword, mySqlDatabase,10019, "rock and Roll")

# For changing description of the single jira issue using issue Key
def descriptionChange(jiraUrl,jiraEmail,jiraApiKey,mySqlHost, mySqlUser, mySqlPassword, mySqlDatabaseName,jiraIssueIdOrKey,newDescription):
    # Add your code here and return the response.

descriptionChange(jiraUrl,jiraEmailAddr,jiraApiKey,mySqlHost, mySqlUser, mySqlPassword, mySqlDatabase,10019,"work on movie")