# 17/07/2021
Continued work on the Magic Handler by adding some basic methods.

# 17/07/2021
Began work on the Magic Handler. I like keeping the features largely 
compartmentalised in it's own files, so that's what I'm doing.

I've made the skeleton set up:
-I have a basic magic list. I will need to fill this in with each entry having
a dictionary with more details. I should also consider replacing it with a
database.
-I've created the Character Mixin which sets up the Handler and dictionary.
-I've set up the Handler. Will need to fill in the methodds as required.

# 16/07/2021
Picking up the delayed exit contrib. I want to add custom messages sitting on
the exit object. First I'll need to look at the default message system, then 
make the relevant changes.

Turns out the contrib does exactly what I want. I don't need to change it. 

It uses a ndb at the beginning of the delay, and checks it at call back to see
if the move should still happen. When I start combining features for them to
interplay, I'll have to decide whether I should use the pose instead.

# 13/07/2021
Picked up the old half finished pose system and finished that.
The pose, pose/reset and pose/default lead to some trickyness defining the 
target. Wasn't as neat as I would like it to be but it should work. Will do
a testing phase later which may encourage me to refactor it with fresh eyes.

Next I want to work on delayed exits to rely on the pose system.

# 13/07/2021
Picking this back up after the last time I put it down.

On first review:
-The ambience system seems to be functional and connected up to rooms only.
 Will need to connect up to objects and characters in future
-The detail system seems to be functional and connected up to rooms and 
 commands.
-Everything else does not to be in a complete state. Will review as needed.

The next thing I'm going to work on is a pose/emote system.
 