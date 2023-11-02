## Not working (To be debugged)

The static message queue is created in `store_messages.py`. For some reason when flask reloads with chages in debug, CPU hits 100% and program is stuck. Haven't debugged this further but it works as long as the program is restarted and there haven't been change on running program. Unfamiliar with flash reload mechanism ATM.