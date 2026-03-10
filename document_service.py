class DocumentService:

    def __init__(self):
        self.documents = {}
        self.current_id = 0

    def create_document(self, title, owner):

        self.current_id += 1

        document = {
            "id": self.current_id,
            "title": title,
            "owner": owner,
            "content": ""
        }

        self.documents[self.current_id] = document

        return document

    def get_document(self, doc_id):

        return self.documents.get(doc_id)

    def update_document(self, doc_id, content):

        if doc_id in self.documents:
            self.documents[doc_id]["content"] = content
            return True

        return False
