from app import getTotalJiraIssue,getJiraIssue,insertData,insertAllData,statusChange,titleChange,descriptionChange
from app import jiraEmailAddr,jiraApiKey,jiraProjectName,jiraUrl,mySqlHost,mySqlUser,mySqlPassword,mySqlDatabase

# test case for fecthing total issue in Jira
def test1_getTotalJiraIssue():
    totalJiraIssue = 33
    response = getTotalJiraIssue(jiraUrl,jiraEmailAddr,jiraApiKey, jiraProjectName)
    assert response == totalJiraIssue
    pass

# test case for fecthing data from jira for page-1
def test2_getJiraIssue():
    pageNumber = 1
    perPageLimit = 10;
    response = getJiraIssue(jiraUrl,jiraEmailAddr,jiraApiKey,jiraProjectName,pageNumber, perPageLimit)
    assert len(response) == perPageLimit
    pass

#test case for fecthing data from jira for page-2
def test3_getJiraIssue():
    pageNumber = 2
    perPageLimit = 10;
    response = getJiraIssue(jiraUrl,jiraEmailAddr,jiraApiKey, jiraProjectName,pageNumber, perPageLimit)
    assert len(response) == perPageLimit
    pass

#test case for fecthing data from jira for page-3
def test4_getJiraIssue():
    pageNumber = 3
    perPageLimit = 10;
    response = getJiraIssue(jiraUrl,jiraEmailAddr,jiraApiKey, jiraProjectName,pageNumber, perPageLimit)
    assert len(response) == perPageLimit
    pass

#test case for fecthing data from jira for page-4
def test5_getJiraIssue():
    pageNumber = 4
    perPageLimit = 3;
    response = getJiraIssue(jiraUrl,jiraEmailAddr,jiraApiKey, jiraProjectName,pageNumber, perPageLimit)
    assert len(response) == perPageLimit
    pass

#test case for fecthing data and inserting into database using page number and limit
def test6_insertData():
    pageNumber = 1
    perPageLimit = 10;
    data = getJiraIssue(jiraUrl,jiraEmailAddr,jiraApiKey, jiraProjectName,pageNumber, perPageLimit)
    count_data_insert = insertData(mySqlHost, mySqlUser, mySqlPassword, mySqlDatabase, data)
    assert len(data) == count_data_insert
    pass

#test case for fecthing data and inserting all data into database
def test7_insertAllData():
    total_data_in_database = 33
    response = insertAllData(mySqlHost, mySqlUser, mySqlPassword, mySqlDatabase)
    assert total_data_in_database == response
    pass

#test case for changing status
def test8_statusChange():
    flag = False
    response = statusChange(jiraUrl,jiraEmailAddr,jiraApiKey,mySqlHost, mySqlUser, mySqlPassword, mySqlDatabase, 10019, "To Do")
    if(response):
        flag = True
    assert flag == True
    pass

#test case for changing title
def test9_titleChange():
    flag = False
    response = titleChange(jiraUrl,jiraEmailAddr,jiraApiKey,mySqlHost, mySqlUser, mySqlPassword, mySqlDatabase, 10019, "rock and Roll")
    if(response):
        flag = True
    assert flag == True
    pass

#test case for changing description
def test10_descriptionChange():
    flag = False
    response = descriptionChange(jiraUrl,jiraEmailAddr,jiraApiKey,mySqlHost, mySqlUser, mySqlPassword, mySqlDatabase, 10019, "work on movie")
    if(response):
        flag = True
    assert flag == True
    pass