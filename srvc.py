'''
srvc.py
base class to the ervice

'''

import socket
import win32serviceutil as util
import win32service as winserve
import servicemanager
import win32event

class WindowsService(util.ServiceFramework):
    ''' inheritate from the win32 service util and define base class to service'''

    '''Instance variables'''
    _svc_name_ = 'pyService'
    _svc_description_ = 'Generic description to override'
    _svc_display_name_ = 'py Service'

    
    def __init__(self, args):
        '''
            Constructor
        '''
        util.ServiceFramework.__init__(self, args)
        '''creating waitable event if we want to stop the service'''
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    @classmethod
    def handle_cmd(cls):
        '''handling command line'''
        util.HandleCommandLine(cls)

    def stop(self):
        '''
            reserve for adding commands before stopping the service
        '''
        pass

    def SvcStop(self):
        '''
            call to stop service
        '''
        self.stop()
        self.ReportServiceStatus(winserve.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def start(self):
        '''
            reserve for adding commands before starting the service
        '''
        pass

    def SvcDoRun(self):
        '''
            call to start service
        '''
        self.start()
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()
    

    def main(self):
        '''
            reserve to add logic
        '''
        pass

    
if __name__ == '__main__':
    WindowsService.handle_cmd()