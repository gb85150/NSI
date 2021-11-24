import requests
import json
def get_classroom_credentials_json():
    """
    Get the classroom credentials in json format
    """
    url = 'https://accounts.google.com/o/oauth2/v2/auth'
    params = {
        'client_id': '',
        'response_type': 'code',
        'redirect_uri': '',
        'scope': 'https://www.googleapis.com/auth/classroom.courses.readonly',
        'access_type': 'offline',
        'include_granted_scopes': 'true',
        'state': '',
        'login_hint': '',
        'prompt': 'select_account'
    }
    response = requests.get(url, params=params)
    print(response.url)
    print(response.text)
    print(response.status_code)
    return response.text

def get_classroom_assignments(course_id: str, page_token: str):
    """
    Get all the assignments and put it in a json string
    """
    url = 'https://classroom.googleapis.com/v1/courses/'
    params = {
        'courseId': course_id,
        'pageSize': '100',
        'pageToken': page_token,
        'orderBy': 'dueDate',
        'assignmentStates': 'ALL'
    }
    response = requests.get(url, params=params)
    print(response.url)
    print(response.text)
    print(response.status_code)
    return response.text

def list_courses(credentials_json: str):
    """
    List all the courses
    """
    url = 'https://classroom.googleapis.com/v1/courses'
    headers = {
        'Authorization': 'Bearer ' + credentials_json
    }
    response = requests.get(url, headers=headers)
    print(response.url)
    print(response.text)
    print(response.status_code)
    return response.text

if __name__ == '__main__':
    get_classroom_credentials_json()
    get_classroom_assignments('', '')
    list_courses('')