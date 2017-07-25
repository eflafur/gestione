from django.contrib.auth import authenticate

class Credentials:
    def GetCredentials(self,line):
        self.row=line
        user = authenticate(username=self.row['a1'], password=self.row['a2'])
        if user is not None:
            return 1
        else:
            return 0