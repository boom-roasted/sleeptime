import sys
import os
import datetime
import time

from termcolor import cprint 
from pyfiglet import figlet_format
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected

    
def time_in_range(start, end, x):
    '''
    return true if x is in the range [start, end]
    '''
    if start <= end:
        # not crossing midnight
        return start <= x <= end
    else:
        # crossing midnight
        return start <= x or x <= end
        
        
class Countdown:
    def __init__(self, title='Starting Countdown', start_at=10, interval=1):
        '''
        counts down in the console in big font
        '''
        self.title = title
        self.max = start_at
        self.interval = interval
        
        self.run_sequence()
        
        
    def bigprint(self, message):
        '''
        prints a message to the console in big font
        '''
        cprint(
               figlet_format(str(message), font='big', justify='right', width=150),
               'yellow', 'on_red', attrs=['bold'])
               
               
    def run_sequence(self):
        '''
        run the countdown sequence
        '''
        self.bigprint(self.title)
        
        for i in range(self.max, 0, -1):
            time.sleep(self.interval)
            self.bigprint(i)
        
        
        
class SleepManager:
    def __init__(self, bedtime, wakeuptime):
        '''
        manages the users sleep schedule and doesn't let
        them mess around on their computer when they should be sleeping
        '''
        self.bedtime = bedtime
        self.wakeuptime = wakeuptime
        
        self.checktime()
        
        
    @property
    def should_be_asleep(self):
        return time_in_range(self.bedtime,
                             self.wakeuptime,
                             datetime.datetime.now().time())
        
        
    def checktime(self):
        '''
        checks whether or not the user should be asleep
        '''
        if self.should_be_asleep:
            self.warnuser()
            self.countdown()
            self.shutdown()
        else:
            print('crisis averted')
            
            
    def countdown(self):
        '''
        counts down for the user, letting them know that
        their machine will be shut off soon
        '''
        Countdown('Shutdown will commence in...', 10, 1)
        
        
    def shutdown(self):
        '''
        shuts of the computer
        '''
        self.bigprint('Shutting down')
        os.system('shutdown /s /t 10')
            
            
    def bigprint(self, message):
        '''
        prints a message to the console in big font
        '''
        cprint(
               figlet_format(message, font='starwars', justify='right', width=150),
               'yellow', 'on_blue', attrs=['bold'])
            
            
    def warnuser(self):
        '''
        warns the user that they should be alseep
        '''
        self.bigprint('Go to bed')
        
        
def main():
    '''
    checks the time to see if you should be asleep
    if you should be asleep, then it warns you and then shuts off your computer
    '''
    bedtime = datetime.time(23,0,0)
    wakeuptime = datetime.time(5,0,0)
    SleepManager(bedtime, wakeuptime)
    
    
def test():
    ''' run the tests '''
    print('testing when user is awake ...')
    test_awake()
    
    print('testing when user is asleep ...')
    test_asleep()
    
    
def test_awake():
    bedtime = datetime.time(23,0,0)
    wakeuptime = datetime.time(5,0,0)
    SleepManager(bedtime, wakeuptime)
    
    
def test_asleep():
    bedtime = datetime.time(5,0,0)
    wakeuptime = datetime.time(23,0,0)
    SleepManager(bedtime, wakeuptime)
    
    
    
        
if __name__ == '__main__':
    #test()
    main()