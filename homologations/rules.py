import os

from django.conf import settings

from homologations.models import Homologations


class HomologationsRule:

    def __init__(self, request):
        self.request = request

    def get_homologations_list(self):
        homologations = Homologations.objects.all()

        homologations_list = []
        for homologation in homologations:
            project_absolute_folder = os.path.join(settings.REPOSITORIES_FOLDER, homologation.project_folder),
            homologation_data = {
                'pk': homologation.pk,
                'project_name': homologation.project_name,
                'project_folder': homologation.project_folder,
                'project_absolute_folder': project_absolute_folder[0],
                'git_repository_url': homologation.git_repository_url,
                'docker_folder': homologation.docker_folder_normalized,
                'container_name': homologation.container_name_normalized,
                'container_port': homologation.container_port_normalized,
                'settings_file': homologation.settings_file_normalized,
                'project_description': homologation.project_description_normalized,
                'responsible': '{0} {1}'.format(homologation.user.first_name, homologation.user.last_name),
                'user': homologation.user,
                'file_exists': os.path.isdir(project_absolute_folder[0]),
            }

            homologations_list.append(homologation_data)

        return homologations_list


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

    def clone_project(self, kwargs):
        homologation = Homologations.objects.get(pk=kwargs['pk'])

        if not os.path.isdir(settings.REPOSITORIES_FOLDER + homologation.project_folder):
            return self.__execute_git_clone(homologation)

        return 'Diretório não está vazio'

    def reclone_project(self, kwargs):
        homologation = Homologations.objects.get(pk=kwargs['pk'])

        command = 'rm -rdf {0}{1}'.format(settings.REPOSITORIES_FOLDER, homologation.project_folder.replace('/', ''))
        os.system(command)

        if not os.path.isdir(settings.REPOSITORIES_FOLDER + homologation.project_folder):
            return self.__execute_git_clone(homologation)
