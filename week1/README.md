# Week 1 learning

For week1, you will be introduced to a few new topics. The first that you'll have noticed right away is the concept of branching in git.

 - Branching is a way to organize work in git repositories so that while we are developing, we are not interfering with production code!
 - Branching seems weird, because when we switch to a new branch, all the files in our repository are updated to reflect the current branch.
 - Some things we shouldn't do:
   - work directly in the main branch (also referred to as the master branch, this is a very recent change due to the negative connotations of master)
   - Switch to a new branch if we have uncommitted work (in fact, git will complain about this)
   
 - Below are some common branching commands:
   - see all branches as well as the one you are currently on: `git branch`
   - create and switch to a new branch: `git checkout -b <branchname>`
   - switch to a new branch that already exists: `git checkout <branchname>`
   - There are many more, but these should suffice for this week's work

## Work for week 1

Git has the concept of a remote and local state. The local state in our case is what is on the server in your home directory. Making changes to the local state does not make changes to the remote state unless you commit them and push them (which you have had some practice with in the README).

In my local copy, I have created a branch called `week1` by doing the following from inside the `Learning_2_Code` directory:
  - `git checkout -b week1`

- From the above, we know this both created and changed to the week1 branch. Immediately when we change, it will be "even" with the state of the main branch.
- When we make any change (add a new file, change an existing file, delete a file), the state of our new branch will be different than our main branch.
- We then commit these changes, and push them to the remote respository on github.
- This is how 2 people can work on projects at the same time. In this example, I am committing changes that you do not have, so you will have `pull` them to your local copy:

Exercise 1 (GIT fundamentals):

1. You first need to fetch my changes to your local copy:
  - The name of our remote repository is "origin" because we have set it up that way when you did:
    - `git remote add origin https://github.com/dp2909/Learning_2_Code.git`
  - From main: `git fetch origin`
    - This will `fetch` all the changes that have been made to the remote and bring them to your local copy
  - Then, change to the branch:
    - `git checkout week1`
  - You should now be on the week1 branch (check with `git branch`)

2. Change to the GIT directory:
  - `cd` is the linux "change directory" command. It is how we will navigate our directory structure
  - `ls` is the linux "list" command. It will list all files and directories in the current directory
  - Change to the week1 directory:
    - `cd week1`
    - `ls`
    - `cd GIT`
  - You are now in the `git directory

3. Practicing some emacs and git fundamentals

  ### Emacs quick introduction
  - emacs (text editor) introduction:
  - To modify the file, you will need to use a linux text editor. Common choices are emacs and vim. I use emacs, so that is what I will teach you.
  - To open a file for modification, you simply type `emacs test.txt`
  - You can't click with your mouse to move around linux files, you have to use keyboard shortcuts. Some useful shortcuts to get started:
    - "+" denotes that you need to be holding the first key while you press the second key
    - move to the beginning of a line: `ctrl+a`
    - move to the end of a line: `ctrl+e`
    - move to the bottom of the file: `esc+shift+.`
    - move to the top of the file: `esc+shift+,
    - you can move up a line with the up arrow, down with the down arrow, and left and right with the left and right arrows
    - search for a keyword: `ctrl+s` which will open a typing box at the bottom of the terminal. so in this file if I wanted to search for the word "terminal", I'd do:
      - `ctrl+s`, then type the word terminal, then hit enter
      - This will highlight all the occurrences of terminal in the file
      - To jump to the next occurence of terminal after you have executed the search command, simply press `ctrl+s` again. Once you make it to the last occurrence, it will jump back to the top
    - to "cut" a whole line (to paste later, or not):
      - go to the start of the line you want to delete
      - `ctrl+spacebar` sets a marker, then pressing the <down> arrow key should highlight the whole line in blue, then `ctrl+w` cuts the line
      - to paste the line you just cut back press `ctrl+y`. As long as this is the last line you cut, you can continually paste this repeatedly by pressing `ctrl+y` as many times as you want.
  - To save a file that has been modified:
    - `ctrl+x+s`
  - To close the saved file:
    - `ctrl+x+c`
  - To close a file without saving it:
    - `ctrl+x+c`
      - This will prompt a dialogue box asking if you want to save your changes. type "n"
      - This will prompt a second dialogue box saying "Modified buffers exist; exit anyway?" for which you will have to type "yes" and hit enter

Work:

Part1:
- Open the test.txt file with `emacs test.txt`
- Add the string "Dev was here" as the second line of the file, followed by enter (you should have a blank line at the end of the file)
- use the commands above to `cut` the "Dev was here" line, and then paste it 4 more times (5 total lines containing "Dev was here"
- save the file and close it.
- add the changes to git: `git add test.txt`
- commit the changes: `git commit -m "updated test.txt"`
- push the changes to the remote branch: `git push origin week1`

Part2:
- delete the file named "deleteme.txt" with `git rm deleteme.txt`, this deletes the file and stages it for commit
- commit it: git commit -m "deletd file deleteme.txt"
- push it to the remote branch: `git push origin week1`

## This is the end of the GIT lecture. I will add a python specific lecture as soon as you complete this exercise

