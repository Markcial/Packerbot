from subprocess import Popen, PIPE

class Git(object):
    def __call(self, cmd, *args):
        command = ['git', cmd] + [arg for arg in args]
        process = Popen(command, shell=False, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        out, err = process.communicate()
        success = process.returncode is None

        return out, err, success

    def ping(self, repo):
        out, err, status = self.__call('ls-remote', '--exit-code', repo)

        return status is None

    def help(self):
        out, err, status = self.__call('help')

        return out, err, status


class Repository(object):
    url = None
    def __init__(self, repo=None):
        self.repo = repo

    def ping(self):
        pass



def ping(repo):
    if type(repo) is not Repository:
        repo = Repository(repo)
    repo.ping()
