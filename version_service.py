class VersionService:

    def __init__(self):
        self.versions = {}

    def save_version(self, doc_id, content):

        if doc_id not in self.versions:
            self.versions[doc_id] = []

        version_number = len(self.versions[doc_id]) + 1

        version = {
            "version": version_number,
            "content": content
        }

        self.versions[doc_id].append(version)

    def get_versions(self, doc_id):

        return self.versions.get(doc_id, [])
