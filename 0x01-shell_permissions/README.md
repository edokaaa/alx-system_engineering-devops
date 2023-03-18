# 0x01. Shell, permissions
This project focuses on permissions (owner, group and others) of files and directories in a unix system.

# Learning Objectives
    Usages of chmod, sudo, su, chown, chgrp
    Linux file permissions
    Representing the three sets of permissions (owner, group, and other) as a single digit
    How to change permissions, owner and group of a file
    Why can’t a normal user chown a file
    How to run a command with root privileges
    How to change user ID or become superuser
    How to create/view a user & group

# Files
Below are the overview on all the files of this project:
File name	|	Description
---------------	|------------------
0-iambetty |	switches the current user to the user betty.
1-who_am_i    |   prints the effective username of the current user.
2-groups 	| prints all the groups the current user is part of.
3-new_owner |  changes the owner of the file hello to the user betty.
4-empty |   creates an empty file called hello.
5-execute    |   adds execute permission to the owner of the file hello.
6-multiple_permissions    |   adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
7-everybody  |  adds execution permission to the owner, the group owner and the other users, to the file hello
8-James_Bond   |  sets the permission to the file hello
9-John_Doe  |   sets the mode of the file hello
10-mirror_permissions |   sets the mode of the file hello the same as olleh’s mode.
11-directories_permissions    |   adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.
12-directory_permissions    |   creates a directory called my_dir with permissions 751 in the working directory.
13-change_group    |   changes the group owner to school for the file hello
100-change_owner_and_group    |   changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.
101-symbolic_link_permissions   |   changes the owner and the group owner of _hello to vincent and staff respectively.
102-if_only |   changes the owner of the file hello to betty only if it is owned by the user guillaume.
103-Star_Wars    |   will play the StarWars IV episode in the terminal.
