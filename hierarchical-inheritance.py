class Software :
    def setSoftware(self):
        self.company = 'microwsoft'
    def getSoftware(self):
        print(f'Company - {self.company}')

class SystemSoftware(Software):
    def setSystemSoftware(self):
        self.use = 'Operating the computer devics'
    def getSystemSoftware(self):
        print(f'USE - {self.use}')

class ApplicationSoftware(Software):
    def setApplicationSoftware(self):
        self.use = 'Working on variosu day to day functional operations'
    def getApplicationSoftware(self):
        print(f'USE - {self.use}')  

class Windows(SystemSoftware):
    def setWindows(self):
        self.version = 11
        self.feature = 'To provide best ever user-interfacet the user' 
    def getWindows(self):
        print(f'Version - {self.version}')
        print(f'Feature - {self.feature}')

class WebApp(ApplicationSoftware):
    def setWebApp(self):
        self.version = 20
        self.feature = 'To provide web bassed functionality to user on internet'
    def getWebApp(self):
        print(f'Version - {self.version}')
        print(f'Feature - {self.feature}')

class MobileApp(ApplicationSoftware):
    def setMobileApp(self):
        self.version =11
        self.feature = 'To provide mobile features on  the fingertips of the user'
    def getMboliApp(self):
        print(f'Verstion - {self.version}')
        print(f'Feature - {self.feature}')


w = Windows()
w.setSoftware()
w.setSystemSoftware()
w.setWindows()

wb = WebApp()
wb.setSoftware()
wb.setApplicationSoftware()
wb.setWebApp()

mb = MobileApp()
mb.setSoftware()
mb.setApplicationSoftware()
mb.setMobileApp()

print('Informtion about system software windows')
w.getSoftware()
w.getSystemSoftware()
w.getWindows()
print('___________________________________')

print('Information about App liction software web app')
wb.getSoftware()
wb.getApplicationSoftware()
wb.getWebApp()
print("___________________________________")

print('Information about application software mobile apps')
mb.getSoftware()
mb.getApplicationSoftware()
mb.getMboliApp()
print("__________________________")