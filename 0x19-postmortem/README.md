# Sever Requests Failure Report
Last Month, it was reported that all the request made to our sever is returning 500 Error, all our services were down.
The root cause was from one of the configuration file of our server web_stack_debugging_1.

## Timeline
The error was realized 25th of May 2:00 pm(GMT).
When pager notify one of our teams.
Our engineering team On-call quickly login to the server for further analysis and to get to the root of the problem.
The problem was solved later by 25th may 3:00 pm (GMT).

## Root Cause and Resolution
The server stopped working because the config of software(Nginx) serving the sever pages is seen to be a directory instead of a symoblic link to another config file
The config file(sites-enabled) was quickly deleted
The config file(sites-enabled) is then made a symbolic link to the original config file(sites-available)
The server was restarted.
100% of traffic is back.

## Prevention against such problm in future
- Always test and thoroughly check the config files brfore deployment
- ALways keep an eye on servers to ensure proper running of them
- Always have backup severs to prevent all of our services being down during an isuue
