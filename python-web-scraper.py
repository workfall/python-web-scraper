import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

mySkills = ['python', 'Node.js', 'angular', 'sql', 'git']

def jobSearch():
    htmlResponseSource = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Node.js&txtLocation=').text

    bSoup = BeautifulSoup(htmlResponseSource, 'lxml')
    allJobs = bSoup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    time_stamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    with open(f'Job_Posts.txt', 'a') as f:
        f.write(f"\n ========== {time_stamp} ========== \n\n")

        for job in allJobs:
            
            companyName = job.find('h3', class_='joblist-comp-name').text
            jobSkills = job.find('span', class_='srp-skills').text
            beautifiedJobSkills = jobSkills.strip().replace(' ', '').split(',')
            linkToApply = job.header.h2.a['href']
            jobPostLoction = job.find('span', class_='').text
            jobPostDay = job.find('span', class_='sim-posted').text

            skills_check = any(skill in mySkills for skill in beautifiedJobSkills)
            
            if skills_check is True:
                f.write(f'Company Name: {companyName.strip()} \n')
                f.write(f"Key Skills: {jobSkills.strip().replace(' ','')} \n")
                f.write(f'Apply Link: {linkToApply} \n')
                f.write(f'Job Post Location: {jobPostLoction.strip()} \n')
                f.write(f'Job Post Day: {jobPostDay.strip()} \n')
                f.write('\n')

if __name__ == '__main__':
    while True:
        jobSearch()
        time.sleep(700)

        
