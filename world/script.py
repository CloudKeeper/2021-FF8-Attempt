# 
from evennia import create_script
test = create_script("features.ambience_system.AmbientScript", 
               key="Ambience", persistent=True, obj=None, interval=10)
test.at_repeat()