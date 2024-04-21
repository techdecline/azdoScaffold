class GitCreateException(Exception):
    pass 

from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from azure.devops.v7_1.git.models import GitRepositoryCreateOptions, GitImportRequestParameters

class AzureDevOps:
    def __init__(self, personal_access_token, organization_url):
        self.credentials = BasicAuthentication('PAT', personal_access_token)
        self.connection = Connection(base_url=organization_url, creds=self.credentials)

    def create_repository(self, repository_name, project_name):
        # Get a Git client
        git_client = self.connection.clients_v7_1.get_git_client()
        
        # Create a new Git repository
        repository_options = GitRepositoryCreateOptions(name=repository_name)
        try:
            git_client.create_repository(repository_options, project_name)
        except Exception as Error:
            print(Error)
            return False
        return True
    
    def import_repository(self, repository_name, project_name, source_repo_url):
        # Get a Git client
        git_client = self.connection.clients_v7_1.get_git_client()
        
        newRepoResult = self.create_repository(repository_name, project_name)

        if newRepoResult == True:
            import_params = GitImportRequestParameters(
                git_source={"url": source_repo_url},
                tfvc_source=None,
                repository_name=repository_name
            )
            import_status = git_client.begin_import_repository(import_params, project_name)
            while not import_status.finished:
                import_status.refresh()
            
        else:
            return False