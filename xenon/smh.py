
# Import internal modules
from xenon.helpers import convert_iso_to_dt
from xenon.models import GetRequest

# Import external modules
import datetime



#* ====================================================================================================================================================================================================



class _Urls():
    """ Class object which holds all the api urls """

    TODOS_URL = 'https://api.satchelone.com/api/todos'
    ASSIGNMENT_URL = 'https://api.satchelone.com/api/homeworks/'
    ATTACHMENT_URL = 'https://api.satchelone.com/api/attachments'

def _header() -> dict:
    """ Holds the default header for all smh requests. """

    return {
        'authority': 'api.satchelone.com',
        'accept': 'application/smhw.v2021.5+json',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'authorization': 'Bearer !--- AUTHORIZATION CODE ---!',
        'origin': 'https://www.satchelone.com',
        'referer': 'https://www.satchelone.com/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'x-platform': 'web'
    }



#* ====================================================================================================================================================================================================



class Assignment():
    def __init__(self, data: dict) -> None:
        self._data = data
    
    def get_data(self) -> dict:
        """ Returns the whole data package of the object. """
        return self._data

    def _get_assignment_data(self) -> dict:
        """ Returns data purely about the assignment. """
        return self.get_data()['homework']

    def _get_lesson_occurrences(self) -> dict:
        """ Returns data purely about the lesson occurrence. """
        return self.get_data()['lesson_occurrences']

    @property
    def assignment_id(self) -> int:
        """ Returns the id of the assignment. """
        return self._get_assignment_data()['id']
    
    @property
    def teacher(self) -> int:
        """ Returns the name of the teacher who set the assignment. """
        return self._get_assignment_data['teacher_name']

    @property
    def title(self) -> str:
        """ Returns the title of the assignment. """
        return self._get_assignment_data()['title']

    @property
    def subject(self) -> str:
        """ Returns the subject name given to the assignment. """
        return self._get_assignment_data()['subject']

    @property
    def due_datetime(self) -> datetime.datetime:
        """ Returns just the datetime of when the assignment is due. """

        dl_id = self.due_lesson_id

        for lo in self._get_lesson_occurrences():
            if lo['id'] == dl_id:
                return lo['starts_at']
            
        return convert_iso_to_dt(self._get_assignment_data()['due_on'])

    @property
    def issue_datetime(self) -> datetime.datetime:
        """ Returns just the datetime of when the assignment was issued. """
        return convert_iso_to_dt(self._get_assignment_data()['issued_at'])

    @property
    def last_updated_datetime(self) -> datetime.datetime:
        """ Returns the datetime of when the assignment was last modified. """
        return self._get_assignment_data()['updated_at']

    @property
    def class_name(self) -> str:
        """ Returns the name of the class allocated to the assignment. """
        return self._get_assignment_data()['class_group_name']

    @property
    def class_id(self) -> int:
        """ Returns the id of the class allocated to the assignment. """
        return self._get_assignment_data()['class_group_id']

    @property
    def description(self) -> str:
        """ Returns the description of the assignment. """
        return self._get_assignment_data()['description']

    @property
    def duration(self) -> tuple:
        """ Returns a tuple of the expected duration of the task. `self.duration[0]` is the number; `self.duration[1]` is the units. """
        return (self._get_assignment_data()['duration'], self._get_assignment_data()['duration_units'])

    @property
    def attachment_ids(self) -> list:
        """ Returns a list of the attachment ids used in this assignment. Use `smh.AttachmentRequest()` to obtain more information about the attachments. """
        return self._get_assignment_data()['attachment_ids']

    @property
    def web_links(self) -> list:
        """ Returns a list of any web links associated with the assignment. """
        return self._get_assignment_data()['web_links']

    @property
    def issue_lesson_id(self) -> None | int:
        """ Returns the id of the lesson which it was issued. This is an int. If it does not exist then it defaults to `None`. """
        return self._get_assignment_data()['issued_on_lesson_occurrence_id']

    @property
    def due_lesson_id(self) -> None | int:
        """ Returns the id of the lesson which it is due. This is an int. If it does not exist then it defaults to `None`. """
        return self._get_assignment_data()['due_on_lesson_occurrence_id']

class Attachment():
    def __init__(self, data: dict) -> None:
        self._data = data

    def get_data(self) -> dict:
        """ Returns the whole data package of the object. """
        return self._data

    @property
    def assignment_id(self) -> int:
        """ Returns the id of the attachment. """
        return self.get_data()['id']

    @property
    def content_type(self) -> str:
        """ Returns the original media type of the attachment resource. """
        return self.get_data()['content_type']

    @property
    def filename(self) -> str:
        """ Returns the name of the attachment file. """
        return self.get_data()['filename']

    @property
    def file_size(self) -> int:
        """ Returns the size of the file in megabytes. """
        return self.get_data()['file_size']

    @property
    def file_url(self) -> str:
        """ Returns the url of the file. This can be downloaded. """
        return self.get_data()['file_url']

    @property
    def creation_datetime(self) -> datetime.datetime:
        """ Returns an iso type `datetime.datetime` of when the attachment was created. """
        return convert_iso_to_dt(self.get_data()['created_at'])

    @property
    def last_updated_datetime(self) -> datetime.datetime:
        """ Returns an iso type `datetime.datetime` of when the attachment was last updated. """
        return convert_iso_to_dt(self.get_data()['updated_at'])



#* ====================================================================================================================================================================================================



class TodosRequest(GetRequest):
    def __init__(self, start_dt: datetime.datetime, end_dt: datetime.datetime) -> None:
        super().__init__()

        self.api_url = _Urls.TODOS_URL
        self.api_params = {
            'add_dateless': 'true',
            'from': start_dt.date(),
            'to': end_dt.date()
        }
        self.api_headers = _header()

    def get_all(self) -> list:
        """ Returns a list with all the ids on the todo list. """
        all_list = []
        for todo_a in self.get_data():
            all_list.append(todo_a['class_task_id'])

        return all_list

    def get_all_completed(self) -> list:
        """ Returns a list with all the ids of assignments that are deemed completed. """
        completed_list = []
        for todo_a in self.get_data():
            if todo_a['completed']:
                completed_list.append(todo_a)
        
        return completed_list

    def get_all_todo(self) -> list:
        """ Returns a list with all the ids of assignments that are deemed todo. """
        todos_list = []
        for todos_a in self.get_data():
            if not todos_a['completed']:
                todos_list.append(todos_a)

        return todos_list

class AssignmentRequest(GetRequest):
    def __init__(self, assignment_id: int) -> None:
        super().__init__()

        self.api_url = f"{_Urls.ASSIGNMENT_URL}{str(assignment_id)}" 
        self.api_params = {}
        self.api_headers = _header()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data gathered from the request api. This essentially removes any unnecessary data. """

        remove_list = ['teacher_id', 'published_at', 'created_at', 'class_year', 'submission_status', 'submission_ids', 'school_id', 'school_name', 'school_logo_url', 'submission_method_id', 'for_partial_group', 'partial_group_of_student_ids', 'source_id', 'marking_scheme_id', 'submission_type', 'community_resource_item_id', 'bookstore_content_ids', 'period_id']

        h_data = self.get_data()['homework']
        for key in list(h_data.keys()):
            if key in remove_list:
                h_data.pop(key)

        lo_data = self.get_data()['lesson_occurrences']
        for i, lo in enumerate(lo_data):
            for key in list(lo.keys()):
                if key in remove_list:
                    lo.pop(key)
                    lo_data[i] = lo

        self._data['homework'] = h_data
        self._data['lesson_occurrences'] = lo_data
    
    @property
    def assignment(self):
        """ Returns the data as a `smh.Assignment()` object. """
        return Assignment(self.get_data())

class AttachmentRequest(GetRequest):
    def __init__(self, attachment_id: int) -> None:
        super().__init__()

        self.api_url = _Urls.ATTACHMENT_URL
        self.api_params = {
            'ids': attachment_id
        }
        self.api_headers = _header()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data gathered from the request api. This essentially removes any unnecessary data. """

        remove_list = ['user_id', 'preview_url', 'third_party_provider', 'third_party_shared_link', 'is_previewable']

        new_data = self.get_data()['attachments'][0]
        for key in list(new_data.keys()):
            if key in remove_list:
                new_data.pop(key)
        
        self._data = new_data

    @property
    def attachment(self):
        """ Returns the data as a `smh.Attachment()` object. """
        return Attachment(self.get_data())