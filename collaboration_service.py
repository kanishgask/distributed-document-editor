class CollaborationService:

    def __init__(self):
        self.active_users = {}

    def join_document(self, doc_id, user):

        if doc_id not in self.active_users:
            self.active_users[doc_id] = []

        self.active_users[doc_id].append(user)

    def leave_document(self, doc_id, user):

        if doc_id in self.active_users:
            self.active_users[doc_id].remove(user)

    def get_active_users(self, doc_id):

        return self.active_users.get(doc_id, [])
