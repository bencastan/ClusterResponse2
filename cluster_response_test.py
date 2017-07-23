import json
import urllib
from colorama import Fore

URL_LIST = ['https://www.pinkfrosting.com.au', 'https://www.mcas.com.au',
            'https://www.theswag.com.au', 'http://www.susf.com.au',
            'http://www.racedeal.com.au', 'https://livingtextiles.com.au',
            'http://www.lepetitmarche.com.au', 'https://www.intoblinds.com.au',
            'https://giftwrapped.org.au', 'http://www.lollypotz.com.au',
            'https://www.sitesuite.com.au']


class PageSpeedOnLine:
    #Add sites here, this list is not a definativ elist


    # Gets ALL results for a given site
    # Returns a json object from google
    def GetSiteResults(self,target_url):
        params = {'url': target_url,
                    'key': 'AIzaSyA6pibr5UDIdt6Qxq1uoNOeiRbo_L3Kizw'}
        url = ('https://www.googleapis.com/pagespeedonline/v1/runPagespeed?' +
                urllib.urlencode(params))
        response = urllib.urlopen(url).read()
        return response

    # Gets the page speed for a single site
    # returns the score as a string as the json returnedby google is converted to a
    # python dictionary for easy manipulation
    def GetPageSpeedResults(self,target_url):
        site_speed = json.loads(self.GetSiteResults(target_url))
        return site_speed.get('score')

    def GetClusterAverage(self):
        total_cluster_speed = 0
        count = 1
        print (Fore.MAGENTA + 'Analysing Cluster speed')
        print (Fore.MAGENTA + 'Only returns Cluster Average')
        for TEST_URL in URL_LIST:
            site_speed = self.GetPageSpeedResults(TEST_URL)
            # display(TEST_URL + " ", site_speed)
            b = 'Averaging' + '.' * count
            print('\r'),
            print ('\r' + b),
            total_cluster_speed = (total_cluster_speed + site_speed)
            count = count + 1

        # print total_cluster_speed
        # print len(URL_LIST)
        average_cluster_speed = (int(total_cluster_speed)) / len(URL_LIST)
        print ""
        message = "Averaged Cluster Speed = "
        self.display(message, average_cluster_speed)

    def GetSiteAverage(self):
        total_cluster_speed = 0

        print (Fore.MAGENTA + 'Analysing Cluster speed')
        print (Fore.MAGENTA + 'Returns each site result and Cluster average')
        for TEST_URL in URL_LIST:
            site_speed = self.GetPageSpeedResults(TEST_URL)
            self.display(TEST_URL + " ", site_speed)
            # print TEST_URL + " Speed %s " % cluster_speed
            total_cluster_speed = total_cluster_speed + site_speed

        # print total_cluster_speed
        # print len(URL_LIST)
        average_cluster_speed = (int(total_cluster_speed)) / len(URL_LIST)
        message = "Averaged Cluster Speed = "
        self.display(message, average_cluster_speed)

    #A worker sub to display the results with colour.
    def display(self, message, speed):
        speedOk = 75
        speedHmm = 50
        speedBad = 35
        if speed < speedBad:
            print (Fore.RED + message + str(speed))
        elif speed >= speedHmm and speed < speedOk:
            print(Fore.YELLOW + message + str(speed))
        elif speed >= speedOk:
            print(Fore.GREEN + message + str(speed))
        #print (textColour +  message + str(speed))


if __name__ == '__main__':
    #Make an instance of the Class.
    psol = PageSpeedOnLine()
    psol.GetSiteAverage()
    #psol.GetClusterAverage()