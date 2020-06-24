import os

from django.conf import settings


class ProjetcRule:

    def __init__(self, request):
        self.request = request

    def __execute_git_clone(self, homologation):
        command = 'cd {0} && git clone {1} {2}'.format(settings.REPOSITORIES_FOLDER,
                                                       homologation.git_repository_url,
                                                       homologation.project_folder)

        os.system(command)
        command = 'ls -lah {0}{1}'.format(settings.REPOSITORIES_FOLDER, homologation.project_folder)
        return os.popen(command).read()

    def clone_project(self, homologation):

        if not os.path.isdir(settings.REPOSITORIES_FOLDER + homologation.project_folder):
            return self.__execute_git_clone(homologation)

        return 'Diretório não está vazio'

    def reclone_project(self, homologation):

        command = 'rm -rdf {0}{1}'.format(settings.REPOSITORIES_FOLDER, homologation.project_folder.replace('/', ''))
        os.system(command)

        if not os.path.isdir(settings.REPOSITORIES_FOLDER + homologation.project_folder):
            return self.__execute_git_clone(homologation)
