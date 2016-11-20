# Author: Jiali Huang

import os
import sys
import re




def get_coverage(url,cite_package):
	coverage_list = []
	os.chdir(url)
	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	for f in files:
		if f.startswith('test') and f.endswith('.py'):

			os.system("nosetests --with-coverage -s -v --cover-erase --cover-package="+ cite_package + "  " + f + " > coverage.txt 2>&1")
			file = open("coverage.txt")
			for line in file.readlines():
				x = line.split()
				if len(x) >= 4:
					if x[0].startswith(cite_package):
						if x[3] != '0%':
							if x[1] != '0':
								a = [f] + x
								coverage_list = coverage_list + [a]

	return coverage_list

def get_diff(url):
	diff_list = []
	os.chdir(url)
	cmd = "git diff --name-only  > diff.txt"
	os.system(cmd)
	file = open("diff.txt")
	for file_name in file:
		comand = file_name[:-1]
		cmd = "git blame "+ comand + " | grep -n '^0\{8\} ' | cut -f1 -d: > diff_out.txt"
		os.system(cmd)
		
		diff_file = open("diff_out.txt")
		num_list = []
		for line in diff_file.readlines():
			num_list = num_list + [line[:-1]]
		if len(num_list) != 0:
			a = [comand] + num_list
			diff_list = diff_list + [a]
	os.system('rm diff_out.txt')
	return diff_list

if __name__ == "__main__":
	diff_list = get_diff('/Users/Admin/scipy')
	coverage_list = get_coverage('/Users/Admin/scikit-learn/sklearn/tests','scipy')
	
	in_the_list = 0
	for each_diff_list in diff_list:
		print "----------------------"
		print each_diff_list 
		for each_coverage_list in coverage_list:
			in_the_list = 0
			if each_coverage_list[1].endswith(each_diff_list[0]):
				if each_coverage_list[4] == '100%':
					print each_coverage_list
				else:
					for i in range(1,len(each_diff_list)):
						if in_the_list == 0:
							for x in range(2,len(each_coverage_list)):
								matchObj = re.match( r'(.*)-(.*)', each_coverage_list[x], re.M|re.I)
								if matchObj:
									matchObj1 = int(matchObj.group(1).replace(',',""))
									matchObj2 = int(matchObj.group(2).replace(',',""))							
									if matchObj1 <= int(each_diff_list[i]) and matchObj2 >= int(each_diff_list[i]):
										in_the_list = 1
										break
								else:
									if each_diff_list[i] == each_coverage_list[x]:
										in_the_list = 1
										break
					if in_the_list == 0:
						print each_coverage_list

		print "-----------------------"
		print "\n"						
		