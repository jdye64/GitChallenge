__author__ = 'jeremydyer'
import os
import fnmatch
import sys

gitdir = (os.getcwd() + "/.git").replace("//", "/")
worktree = os.getcwd()

#print "GitDir: ", gitdir
#print "WorkTree: ", worktree

cmd = "git --git-dir " + gitdir + " --work-tree " + worktree + " status --porcelain"
f = os.popen(cmd)
gitstatus = f.read()

challenges = []
for line in gitstatus.split("\n"):
    if len(line) > 0:
        line = line.strip()
        challenges.append(line.split(" ")[1])


#Build the list of challenge files from the .gitchallenge file
challengeFiles = open(worktree + "/.gitchallenge").read()
files = []

check = []
for f in challengeFiles.split("\n"):
    files.append(f)
    for m in fnmatch.filter(challenges, f):
        check.append(m)

if len(check) > 0:
    print "\nCancelling commit due to modified files:"
    for cfm in check:
        print "\t", cfm
else:
    print "Everything is clear. Allowing git command to continue"

    gitcmd = "git "
    first = True

    for arg in sys.argv:
        if first:
            first = False
        else:
            gitcmd += " " + arg

    print "Git CMD: ", gitcmd
    os.system(gitcmd)

