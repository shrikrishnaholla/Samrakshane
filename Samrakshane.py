#!/usr/bin/python
# backup7.py

print """A program that backs up a list of files/folders into a zip/tar archive"""

import os
import time

source_dir=[]

cwd=raw_input('Enter the directory where the files/folders to backup are present\n(Ignore if on the present working directory): ')
try:
	os.chdir(cwd)   # Changes the working directory to the source's so that explicit declaration of directory not needed
except:
	os.chdir(os.getcwd())   # If on present directory and the user doesn't give any input,
	cwd=os.getcwd()         # natively assign cwd to the current directory itself
print 'The list of files/folders present in',os.getcwd()

direct=os.listdir(cwd)
os.system('ls')       # Gives the list of all files/folders so that user need not use a separate filemanager to know which
                      # files/folders to backup

ch=raw_input('Do you want to specify any specific kind of file (Extension) ? [yes/no] ')
if ch == 'yes' :
	ext_xt=raw_input('And that would be??\n(Ex "exe","py","txt" etc): ')
	flag=0                          # I am taking a flag to know whether the user has given the correct extension
	dor=[]                          # I am creating an empty list where I'm going to append the files that have the
	for ory in direct:              #   user's required extension
		if ext_xt in ory:
			dor.append(ory)
			flag = 1
	if flag == 0:
		print 'Sorry!! No file with the specified extension exists. I will now allow you to select from all the files/folders in this directory'
		os.system('ls')  
	else:                     # If flag is not 0, means it's 1 and that means the list 'dor' is not empty. 
		direct = dor [:]  # which means it contains the list of filenames that end with the req extension
                print 'Files with the extension %s are:' % ext_xt         # So the list 'dor' is copied to direct
		for di in direct:
			print di,'\t',
		print

s=raw_input('Enter the name of the folders/files to back up (type "all" to select all): ')
if s == 'all':
	d=direct[:]
        strng=''
        for fold in d:                        # Let the list of all files/folders in the directory be backed up
                strng = strng + ' ' + fold
        source_dir.append(strng)
	
else:
	source_dir.append(s)       # Only the files/folders specified by the user are backed up

 
target_dir=raw_input('Enter the directory where you want to create the archive backup file\n(leave field blank if you want the program to generate a directory for backups): ')  # If you want, tell me where I should create your backup.
                                                    # If you are a novice, sit back and I'll handle everything for you

if len(target_dir) == 0:  # If the user has opted for me to generate a backup directory, I hav to create a target directory
        target_dir='/home/'+os.getlogin()+'/backup/' # Go to the user's home and create a folder for backups
	if not os.path.exists(target_dir):           # (If it doesnt exist already)
		os.mkdir(target_dir)
        today=target_dir+time.strftime('%Y%m%d')
        if not os.path.exists(today):               # Create a subfolder for backups created today
                os.mkdir(today)                     # I'm assuming that you may back up more than one a day
                print 'Backup folder created successfully @ %s' % today
        now=today+os.sep+time.strftime('%H%M%S')
	
	arch=raw_input('Do you want your backup archive to be a zip file or a tar file? ')

        comment=raw_input('Enter a comment to easily identify what this backup is for (optional): ')
        if len(comment) == 0:
		if arch=='zip':
                	target=now+'.zip'
		else:
			target=now+'.tar'
        else:
                if arch=='zip':    # Appending user's comments to the backup file
			target=now+'_'+comment.replace(' ', '_')+'.zip'
		else:
			 target=now+'_'+comment.replace(' ', '_')+'.tar'
else:
        arch=raw_input('Do you want your backup archive to be a zip file or a tar file? ')

	comment=raw_input('Enter a comment to easily identify what this backup is for (optional): ')
        if len(comment) == 0:
		if arch=='zip':
                	target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'
		else:
			target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.tar'
        else:
                if arch=='zip':
			target=target_dir+time.strftime('%Y%m%d%H%M%S')+'_'+comment.replace(' ', '_')+'.zip'
		else:
			target=target_dir+time.strftime('%Y%m%d%H%M%S')+'_'+comment.replace(' ', '_')+'.tar'

print 'Backing up...'

if arch=='zip':
	zip_command = "zip -qr '%s' %s" % (target, ' '.join(source_dir))
	if os.system(zip_command) == 0: # Running a terminal command via a program
        	print 'Backup Successful!! :)'
		print 'Your backup file is @ %s' % target

	else:
		print 'Backup Failed :('
		err=os.system(zip_command)
	        print 'Error: ',err # Not particularly useful, just returns the error number. Added it just for fun

else:
	tar_command = "tar -czf %s %s" % (target, ' '.join(source_dir))
        if os.system(tar_command) == 0:
                print 'Backup Successful!! :)'
		print 'Your backup file is @ %s' % target

        else:
                print 'Backup Failed :('
                err=os.system(tar_command)
                print 'Error: ',err

