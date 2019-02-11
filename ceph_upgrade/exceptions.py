
class SuperUserError(Exception):

    def __str__(self):
        return 'This command needs to be executed with sudo or as root'
