import datetime
import pandas as pd

class BeautyInsider: 
    def __init__(self, name, points, birthday,
                 purchasetoday=0, redeemedpoints=0, rinvitation='No', rmonthlygift='No',
                 rbirthdaygift='No'):
        self.name = name
        self.points = points
        self.birthday = birthday
        self.purchasetoday = purchasetoday
        self.redeemedpoints = redeemedpoints
        self.rinvitattion = rinvitation
        self.rmonthlygift = rmonthlygift
        self.rbirthdaygift = rbirthdaygift
    
    def add_points(self):
        self.points = self.points + self.purchasetoday - self.redeemedpoints
        return self.points
        
    def get_birthday(self):
        if self.birthday == datetime.datetime.now().month\
        and self.rbirthdaygift == 'No':
            self.rbirthdaygift = 'Yes'
            return "Say 'Happy Birthday, {}' and give birthday gift".format(self.name)
        else:
            return 'Do not send birthday gift to {}'.format(self.name)
    
    def monthly_gift(self):
        if self.points >= 350 and self.rmonthlygift == 'No':
            self.rmonthlygift = 'Yes'
            return 'Send monthly gift'
        else:
            return "Do not send monthly gift"
    
    def invitation(self):
        if self.points >= 1000 and self.rinvitattion == 'No':
            self.rbirthdaygift = 'Yes'
            return 'Send invitation'
        else:
            return 'Do not send invitation'
        
        
    def print_summary(self):
        summary = pd.DataFrame({'Benefits':['Total points', 'Birthday gift',
                                            'Monthly gift', 'Invitation'],
                                'Instructions': [self.add_points(), self.get_birthday(),
                                                 self.monthly_gift(), self.invitation()]})
        return summary
        
        