import logging
import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import mail
import datetime

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
from userRights import UserRights


class OpenInvites(ndb.Expando):

    strOrganizationID = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strSecurityCode = ndb.StringProperty()
    strDateSent = ndb.DateProperty(auto_now_add=True)
    strTimeSent = ndb.TimeProperty(auto_now_add=True)
    strAccepted = ndb.BooleanProperty(default=False)

    def writeOrganizationID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strOrganizationID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCell(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False
    def writeEmail(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strEmail = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSecurityCode(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strSecurityCode = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateSent(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateSent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeSent(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strTimeSent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAccepted(self,strinput):
        try:
            if strinput in [True,False]:
                self.strAccepted = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateSecurityCode(self):
        import random,string
        try:
            strSecurityCode = ""
            for i in range(6):
                strSecurityCode += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strSecurityCode
        except:
            return None

class Accounts(ndb.Expando):

    strUserID = ndb.StringProperty()
    strOrganizationID = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strTel = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strWebsite = ndb.StringProperty()
    strVerified = ndb.BooleanProperty(default=False)
    strVerificationCode = ndb.StringProperty()
    strSuspended = ndb.BooleanProperty(default=False)

    strPhotoURL = ndb.StringProperty()
    strProviderData = ndb.StringProperty()
    strAccessToken = ndb.StringProperty()

    strLastSignInDate = ndb.DateProperty()
    strLastSignInTime = ndb.TimeProperty()

    def writeLastSignInDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strLastSignInDate = strinput
                return True
            else:
                return False
        except:
            return False

    def writeLastSignInTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strLastSignInTime = strinput
                return True
            else:
                return False
        except:
            return False

    def writePhotoURL(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strPhotoURL = strinput
                return True
            else:
                return False
        except:
            return False

    def writeProviderData(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strProviderData = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAccessToken(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strAccessToken = strinput
                return True
            else:
                return False
        except:
            return False

    def writeVerified(self,strinput):
        try:
            if strinput in [True,False]:
                self.strVerified = strinput
                return True
            else:
                return False

        except:
            return False
    def writeVerificationCode(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strVerificationCode = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateVerificationCode(self):
        import random, string
        try:
            strVerificationCode = ""
            for i in range(6):
                strVerificationCode += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strVerificationCode
        except:
            return None
    def writeUserID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOrganizationID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strOrganizationID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNames(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strNames = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurname(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strSurname = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCell(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTel(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strTel = strinput
                return True
            else:
                return False
        except:
            return False
    def writeEmail(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strEmail = strinput
                return True
            else:
                return False
        except:
            return False
    def writeWebsite(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strWebsite = strinput
                return True
            else:
                return False
        except:
            return False

class Organization(ndb.Expando):

    strUserID = ndb.StringProperty()
    strOrganizationID = ndb.StringProperty()
    strOrganizationName = ndb.StringProperty()
    strDescription = ndb.StringProperty()
    strRegistration = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strTel = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strWebsite = ndb.StringProperty()

    strRegisteringLink = ndb.StringProperty()
    strVerificationCode = ndb.StringProperty()
    strVerified = ndb.BooleanProperty(default=False)

    strSuspended = ndb.BooleanProperty(default=False)

    def writeRegisteringLink(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strRegisteringLink = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateRegisteringLink(self):
        import random,string
        try:
            strRegLink = ""
            for i in range(255):
                strRegLink += random.SystemRandom().choice(string.digits + string.ascii_uppercase + string.digits + string.ascii_lowercase)
            return strRegLink
        except:
            return None
    def writeVerificationCode(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strVerificationCode = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateVerificiationCode(self):
        import random,string
        try:
            strVerificationCode = ""
            for i in range(8):
                strVerificationCode += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strVerificationCode
        except:
            return None
    def writeVerified(self,strinput):
        try:
            if strinput in [True,False]:
                self.strVerified = strinput
                return True
            else:
                return False
        except:
            return False

    def writeUserID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOrganizationID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strOrganizationID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOrganizationName(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strOrganizationName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDescription(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strDescription = strinput
                return True
            else:
                return False
        except:
            return False
    def writeRegistration(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strRegistration = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCell(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTel(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strTel = strinput
                return True
            else:
                return False
        except:
            return False
    def writeEmail(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strEmail = strinput
                return True
            else:
                return False
        except:
            return False
    def writeWebsite(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strWebsite = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateOrgID(self):
        import random,string
        try:
            strOrganizationID = ""
            for i in range(256):
                strOrganizationID += random.SystemRandom().choice(string.digits + string.ascii_lowercase)

            return strOrganizationID
        except:
            return None


    def writeSuspended(self,strinput):
        try:
            if strinput in [True,False]:
                self.strSuspended = strinput
                return True
            else:
                return False
        except:
            return False

class BankAccountDetails(ndb.Expando):
    strUserID = ndb.StringProperty()
    strOrganizationID = ndb.StringProperty()
    strAccountHolder = ndb.StringProperty()
    strAccountNumber = ndb.StringProperty()
    strAccountType = ndb.StringProperty()
    strBankName = ndb.StringProperty()
    strBranchName = ndb.StringProperty()
    strBranchCode = ndb.StringProperty()


    def writeUserID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOrganizationID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strOrganizationID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAccountHolder(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strAccountHolder = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAccountNumber(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strAccountNumber = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAccountType(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strAccountType = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBankName(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strBankName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBranchName(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strBranchName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBranchCode(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strBranchCode = strinput
                return True
            else:
                return False
        except:
            return False

class Payments(ndb.Expando):
    strUserID = ndb.StringProperty()
    strOrganizationID = ndb.StringProperty()
    strReference = ndb.StringProperty()


    def writeUserID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOrganizationID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strOrganizationID = strinput
                return True
            else:
                return False
        except:
            return False

class AccountsHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/account/accounts.html')
        context = {}
        self.response.write(template.render(context))


app = webapp2.WSGIApplication([
    ('/accounts', AccountsHandler)



], debug=True)
