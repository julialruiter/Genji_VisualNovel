##FULL SCRIPT

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image dining_hall = "dininghall.jpg"
image dorm_night = "dorm_night.jpg"
image outside_dorm = "outside_dorm.jpg"
image picnic = "picnic.jpg"
image lantern_path = "lantern_path.jpg"
image park = "park.jpg"
image black = "black.jpg"
image classroom = "class.jpg"


image Jim = "Jim.png"
image Rokujo = "Lady_Rokujo.png"
image Murasaki = "Murasaki.png"
image Yugao = "Yugao.png"
image Utsusemi = "Utsusemi.png"
image Suetsumuhana = "Suetsumuhana.png"
image Tamakazura = "Tamakazura.png"
image Oborozukiyo = "Oborozukiyo.png"
image Fujitsubo = "Fujitsubo.png"
image Aoi = "Ukifune.png"
image Genji = "Genji.png"
image Ghost = "Ghost.png"
image Narrator = "Narrator.png"

# Declare characters used by this game.
define G = Character('Genji', color="#faeede")
define F = Character('Fujitsubo', color="#faeede")
define Y = Character('Yugao', color="#faeede")
define S = Character('Suetsumuhana', color="#faeede")
define M = Character('Murasaki', color="#faeede")
define T = Character('Tamakazura', color="#faeede")
define O = Character('Oborozukiyo', color="#faeede")
define A = Character('Aoi', color="#faeede")
define U = Character('Utsusemii', color="#faeede")
define J = Character('Jim', color="#faeede")
define R = Character('Rokujo', color="#faeede")
define Ghost = Character('Ghost', color="#faeede")
define Narrator = Character('Narrator', color="#faeede")

# the game starts here
label start:
    scene black
show Murasaki
M "My name is Murasaki and this is the tale of my good friend Genji"
"Genji is the resident playboy of CMC. He’s good-looking (and knows it), well-connected, and is overall the most desirable guy on campus. And he’s only a junior!"
"Although he technically has a girlfriend, Aoi, she’s going to school in Connecticut, so Genji doesn’t really worry about her."
"As long as I’ve known Genji at the Claremont Colleges, he’s had one goal in mind…"
"The Five C Challenge."
"...The goal of every aspiring playboy"
"If he’s able to date a girl from all of the five colleges, Genji will be cemented in CMC legend."
"Here begins his story…"
scene lantern_path
show Genji
with dissolve
"The start of a new semester…"
"Finally I can begin new classes, and with new classes come new girls!"
"I hope To no Chujo was right with his recommendations… This gender and sexuality studies class had better be full of proper prospects!"
"I need to get this 5C challenge done this year… no one has completed it before senior year before."
"If anyone can do it, I can…"
"In any case, I had better get to class and see what goods have been provided!"
jump room

label room:
scene classroom
with fade

"Excellent… plenty of beautiful women, all for me to talk to."
"I’ve seen some of these girls before, but thankfully there’s also some new faces for me to explore"
"There’s no time like the present to get started towards my goal!"
"Let’s see… who all is in this class…"
show Utsusemi
"Utsusemi… she’s a slippery girl alright. I can hardly count how many times she’s slipped through my fingers."
"Definitely a smart girl though… If I remember correctly she goes to Pomona"
hide Utsusemi
show Yugao
"Yugao, a Scripps student… She’s very shy but there’s just something about her that I can’t resist!"
"And her roommate…"
hide Yugao
show Rokujo
"Rokujo, also a Scripps student. A little scary but I kind of like that."
"I hear she’s pretty jealous though, I would have to be careful with her."
hide Rokujo
show Suetsumuhana
"I think that girl goes to Mudd… maybe her name is Suetsumuhana?."
"I hear that no one ever even sees her outside of class."
"She’s supposedly a pretty big deal in her hometown, but no one even seems to realize she exists here."
hide Suetsumuhana
show Tamakazura
"That’s Tamakazura. Another Scripps student."
"I’ve never really been able to hold her attention the way I do with other girls…"
"A challenge if there ever was one"
hide Tamakazura
show Oborozukiyo
"And there’s Oborozukiyo, a Pitzer student"
"Apparently she’s pretty fascinated by the moon, but beyond that I don’t really know that much about her"
hide Oborozukiyo
"I wonder who I should talk to today?"

menu:
    "…Utsusemi":
        jump Utsusemi
    "…Yugao":
        jump Yugao
    "…Rokujo":
        jump Rokujo
    "…Suetsumuhana":
        jump Suetsumuhana
    "…Tamakazura":
        jump Tamakazura
    "… Oborozukiyo":
        jump Oborozukiyo
    "No one, I'm Genji—I'll wait for the girls to talk to me":
        jump Fujitsubo


label Utsusemi:
   show Utsusemi
   with dissolve

"She was the girl that got away..."
"Ever since freshman year Utsusemi has been ignoring my advances"
"This is not a normal occurrence for me"
"If I am to be assured of my greatness in the world of love I must have her!"
"Besides, Utsusemi is the only girl from Pomona that is worth my attention right now…"
"So, since I know she secretly finds me attractive"
"Today I decided"
menu:
    "... to talk to her after class":
        jump rightaway
    "... to leave her alone today, no doubt wanting more.":
        jump later


label rightaway:
    scene classroom
    show Utsusemi 
    "It’s important that I talk to her today, I can’t just let her slip away again"
    U "Oh, Genji, it’s you again."
    G "Of course! You’ve been avoiding me again Utsusemi...."
    "I saw her grimace and wondered what I could do to convince her of her love for me"
    U "…so did you want something? Because I need to get back to south Pomona, so if you’re just going to leer at me like an idiot I’m leaving"
    G "Come on ‘Semi, don’t be like that, all I want is for"

    menu:
        "…Us to be friends":
            jump friends
        "…you to finally admit your love for me!":
            jump love

label later:

   scene park
   with dissolve


   "And so I decided to ask her later."
   "But I was indecisive."
   "what if my hesitation costs me my one shot at Utsusemi?"
   "I head back to CMC with a heavy heart, pondering my bad luck in love."
   "My phone buzzes with a text"
   A "Genji! I know you just got out of class, were you thinking of me the whole time?"
   "I really dislike how much Aoi talks to me… Does she not understand that without her here I need to find other women?"
   "The thought of Aoi is not enough for me… I must complete the 5C challenge to truly prove that no one is greater than Genji"
   jump Nextday1

label Nextday1:
    scene dining_hall
    with dissolve

    "Entering the dining hall the next day I was still hung up on the cold exterior of Utsusemi"
    "To my good fortune I spot Utsusemi sitting across the room!"
    "I wonder who the handsome young man next to her is…I cannot have competition, I will destroy him…"
    "Walking over I greet Utsusemi"
    G "’Semi, how charming to see you here…I didn’t get a chance to talk to you yesterday after class"
    show Utsusemi at left
    show Jim at right
    U "Whatever Genji, could you shove off please? My brother Jim just finished his first week here at Pomona and I don’t want to be dealing with you while we’re having lunch together."
    G "Now now ‘Semi, no need to get heated… I would never dream of taking up too much of your time when your delightful brother is around!"
    "I can’t help but notice the innocent beauty in Jim’s eyes… His beauty may even surpass that of his sister"
    "But don’t I have the 5C challenge to complete?"
    hide Jim
    "I should"

    menu:
        "…Try to get Utsusemi alone to ask her out":
            jump alone
        "…Focus on the beautiful man in front of me":
            jump Jim

label alone:
    scene dining_hall

    "I should focus and talk to Utsusemi…Jim is just a distraction"
    G "But seriously ‘Semi, I do have a question about the homework for class."
    show Utsusemi
    U "Well? Why don’t you ask me your question and leave then?"

    G "I don’t want to bother Jim while he’s eating, why don’t we go discuss this alone for a few minutes?"
    show Utsusemi
    U "Whatever will finally get you off my back…"
    "We walk over to a secluded corner of Frary, with no one standing between us anymore"
    G "Listen ‘Semi, we’ve been dancing around the sexual tension for too long…"
    G "Why don’t you just admit that you’re attracted to me, and we can make your dreams a reality?"
    U "…"
    G "So, what do you say? You, me, candles, up on the roof of Kravis? Saturday night?"
    U "I don’t know about that…"
    G "Just give me a chance…"
    U "I guess one date couldn’t hurt"
    "Finally the chance I need to get Utsusemi"
    "She’s denied me for too long… this date can change everything!"
    hide Utsusemi
    scene black with fade
    jump Saturdaynight 


label Jim:
    show Jim at right
    "In the end I can’t ignore perfection when it’s staring me in the face"
    "Besides, Jim can still work to fulfill Pomona in the 5C challenge!"
    "Although he was not my initial target, he’s clearly more friendly and open to me than Utsusemi is…"
    G "Anyway ‘Semi, if you don’t want to be bothered that’s fine by me"
    G "And since it is your brother’s first week here, I would be remiss not to offer him my services should he need anything at all" 
    U "I’m sure Jim…"
    J "I can speak for myself thanks Utsusemi."
    J "Actually Genji I would love to hang out sometime. I haven’t really met anyone from CMC yet."
    J "In fact I’m free later tonight…"
    "This is my chance to really get to know Jim"
    "Should I"
    menu:
        "…Immediately invite Jim to hang out tonight":
            jump Immediately
        
        "…Play it cool":
            jump Playitcool


label Immediately:

"I decide to act immediately…I can’t let a prize like Jim slip from my fingertips!"
G "Well it’s your lucky day then… I’m free as well!"
G "What do you say I show you around my home turf?"
J "Wow! Thanks Genji!"
G "It’s my pleasure Jim. There’s nothing I would rather do…"
hide Jim
hide Utsusemi
scene black with fade
jump jimnight

label Playitcool:
"I decide to play it cool…hopefully that will leave him wanting more"
G "Well Jim I’ll be sure to let you know when I have the time."
G "I was planning to hang out with To no Chujo tonight anyway."
J "Oh…"
"I can’t help but notice that Jim seems disheartened"
"It seems like I have hurt his feelings"
"I should have taken my chance when I had it…"
hide Jim
scene black with fade

jump TonoChujo

label TonoChujo:
scene dorm_night
 
"That night I ended up visiting To no Chujo just as I had promised Jim"
"I feel as though I have missed a great opportunity…"
"Although I have known To no Chujo a very long time his company is not what I want."
"All he does is remind me of Aoi"
"I don’t want to think of her right now"
"Instead I busy my mind with thoughts of Jim…"
"I’ve messed everything up…"
"Here I am, alone on a Saturday night with To no Chujo!"
"How far the mighty Genji has fallen to have me stuck here with Aoi’s brother and no hope of any action!"
"Somewhere I went terribly wrong… I should"

menu:
    "Accept a life of loneliness and sleep through the rest of my college years":
        jump lonelyend
    "Go back to class tomorrow and try to get back on track…":
        jump room

label lonelyend:
    scene black

"There is no point anymore…"
"Goodbye social life… Goodbye conquests… I’m off to study and sleep forever…"
".: BAD END:."
return



label Saturdaynight:
scene dorm_night
"Tonight I finally have a chance to show Utsusemi what she’s been missing!"
"Everything is all set up. I brought candles, a blanket, and refreshments"
"Now all that’s left is for Utsusemi to arrive so that we can watch the stars and for her to fall madly in love with me!"
show Utsusemi
U "Genji? Are you here?"
G "’Semi! I must say you look positively ravishing tonight!"
U "Oh, um, thank you Genji."
U "I don’t know how you managed it but here we are. On a date. I can hardly believe it."
G "Well believe it ‘Semi!"
G "Get ready for the best night of your entire life!"
G "As you can see I’m all set up. What do you say we get to know one another?"
U "Oh, um, ok then."
U "This actually is quite beautiful… I’ve never been on the roof of the Kravis Center"
G "Just one of the many things I can offer you if you agree to go out with me again!"
G "You may not realize it yet, but I think we have a lot to offer each other."
G "I think that deep down you realize that we’re meant for each other!"
"…"
"…"
"That’s pretty forward of you to say Genji…"
G "Well I just want you to understand my feelings"
G "It just seems like you’re running away from this relationship and I want to know why!"
G "I can’t think of any reason why you wouldn’t want to be with me, and I know I want to be with you, so I guess I just don’t understand what the issue is."
U "Genji I just don’t know you that well…"
G "What better way to get to know me than through a relationship?"
"I don’t understand why she has to be so hesitant…"
"I need to find a way to break into her shell"
"I wonder what the best way to do that is though…"
"I should"

menu:
    "…Go in for the kiss. What better way to make her accept her feelings":
        jump quickkiss
    "…Give her some time to figure out what she wants.":
        jump slowtime

label quickkiss:
    scene dorm_night

"There’s nothing better than action to realize emotion…"
"I close my eyes and lean in for a kiss…"
hide Utsusemi
"…"
"My lips meet air"
"I fall over as Utsusemi is no longer where she once was"
"What is this feeling?"
"I open my eyes to see my sleeve ablaze with the fire from the candles I lit earlier"
"This is not the end to the night I imagined at all"
"As a furiously attempt to put out my burning sleeve I see Utsusemi fleeing the building…"
"I have failed…"
"I’ll have to try again with someone else I suppose…"
".: BAD END :."
jump room

label slowtime:
scene dorm_night
"In the end I cannot force her to immediately realize her feelings…"
G "I understand if you need some time ‘Semi. This is just the first date after all…"
U "That’s surprisingly mature of you Genji…"
U "You know every time I feel like you are about to become a total creep you end up acting ok?"
U "Maybe there’s hope for you after all."
U "I don’t hate you or anything Genji… All I want is to take this a little slow."
U "If I’m going to be with someone I need to trust them. Can you give me the time I need?"

menu:
    "I think I can ‘Semi. You’re worth any amount of time!":
        jump worthit
    "…I don’t know about that ‘Semi. A man has needs you know…":
        jump manneeds

label worthit:
    scene dorm_night
    show Utsusemi
U "Congratulations Genji. You have passed my test!"
U "For some reason I thought that you might not be ok with that…"
U "All I really wanted to know is that you’re a man who can wait."
U "Since you have shown me that you have at least some virtue in that mind of yours I feel that you have earned a reward."
U "I’m ready Genji…"
scene black
jump happyutsusemi

label happyutsusemi:
scene park

"I have managed to check Pomona off my list."
"That was quite the experience…"
"Utsusemi sure is a slippery one… but now I’ve experienced the whole package with her."
"Now on to new adventures…"
".: GOOD END :."
jump room

label manneeds:
scene dorm_night
show Utsusemi
"…"
"…"
U "I thought you were better than this Genji…"
"Oh dear. There she goes running into the night…"
"I can’t help but feel like I let her slip through my fingers."
"In any case, I wish I could have had her at some point…"
jump default1


label jimnight:
scene dorm_night

"I’m actually a little nervous about hanging out with Jim tonight!"
"I so rarely get nervous… I mean I’m Genji!"
"And Jim did seem excited to hang out tonight…"
"…"
"I wonder when he’ll get here?"
show Jim
J "Genji? Are you here?"
G "Jim! You came! I wasn’t sure when you would arrive!"
"He looks perfect… why is he perfect?"
"Why can’t this be just like the other women?"
"In any case I can’t just stand here like an idiot!!"
G "So… um, Jim?" 
G "I was thinking that maybe you want to…"

menu:
    "Take a walk in the moonlight with me?":
        jump moonlight
    "Hang out in my dorm room with me?":
        jump dormnight

label moonlight:
J "Oh in the moonlight? That would be so beautiful! I’ve never walked around CMC at night!"
G "Well let me show you my world…"
G "I know the perfect place that we can go to…"
"I’ve heard that the roof of the Athenaeum is perfect at night. I think I’ll show my little boy the starts tonight!"
G "Follow me up here Jim. From here you can see the whole sky!"
J "Wow Genji! This is really amazing!"
J "How did you find out about this place?"
G "You learn a few things after spending a few years here…"
G "There’s a lot of things I could teach you Jim…If you would only let me"
J "What kind of things Genji?"
"This is my chance"
"He’s so beautifully innocent…I will make him mine tonight…"
G "What kind of things you ask? Well for starters I can teach you what real passion feels like…"
scene black with fade
jump Jimend

label dormnight:
scene dorm_night

G "So, um, this is my dorm room!"
G "It’s a single so luckily we can have some privacy tonight…"
show Jim
J "This is such a cool room Genji!"
J "Hey why do you have a checklist with the five colleges listed on it?"
"Crap! That’s my 5C challenge checklist!"
G "Oh, um, don’t worry about that…"
G "That’s… um… not nearly as interesting as some other things all the way on the other side of the room!"
J "Ok! What’s over there!?"
J "Wow you have a couch?"
J "Genji you’re so cool!!!"
"That was close…"
G "Anyway Jim, why don’t we hang out on the couch? Get a little more…comfortable?"
J "Sure Genji!"
J "So what do we do now?"
G "Oh I can think of a lot of things we could do…"
G "Since we have all night I think we might even get to try them all…"
"I can’t help but think that I’ll be able to add a checkmark to that list after tonight…"
hide Jim
scene black
jump Jimend

label Jimend:
scene park
show Jim
J "Genji I’m so glad I met you..."
J "I didn’t really know what to expect coming to college but you’ve shown me how to live my best life here"
G "I’m glad that I could service *ahem provide that service for you"
G "You know Jim, you’re a really special guy…"
G "It’s the funniest thing…I originally wanted to ask your sister out…"
G "I have to admit that I’m glad that I spent time with you instead!"
G "I wouldn’t trade anything we’ve done for the world!"
"These days with Jim have been some of the best of my whole time at Claremont.."
"Who would have thought that Jim was who I was looking for all along?"
".: GOOD END :."
return

label friends:
scene classroom
"I decided that it was best to play it slow with Utsusemi…"
"She’s a tricky one, if I’m not careful I might just scare her away."
show Utsusemi
U "Wow Genji… You know maybe I underestimated you. Here I thought that all you wanted was to sleep with me."
U "I guess you’re not as much of a scumbag as I thought!"
G "As much as? You wound me ‘Semi. You know I just want you to be happy…"
U "We’ll see Genji…We’ll see…"
hide Utsusemi
scene black
 
jump Nextday2

label Nextday2:
scene dining_hall

"It seems like Utsusemi might actually trust me a bit after yesterday!"
"Which makes it the perfect time to take advantage of that!"
"Today I will make Utsusemi mine…"
"And just my luck that she’s here in the dining hall!"
G "Hey! ‘Semi! Fancy seeing you here!"
"And I wonder who that dreamboat next to her is…"
G "And just who might this be?"
show Utsusemi at left
show Jim at right
U "Oh. This is my brother Jim. He’s a freshman this year. It’s pretty great that we both get to go to Pomona"
G "Indeed. Who would have thought that the school was lucky enough to have both of you under one roof?"
G "What a stunning family…"
"I can’t help but notice Jim’s innocent beauty"
"This changes things… I want them both if I’m being honest… but right now I should"
menu:
    "…focus on Utsusemi":
        jump alone
    "…accept the beauty of Jim and focus on him.":
        jump Jim

label love:
scene classroom

"I decide that it’s been long enough. It’s time for Utsusemi to admit her true feelings!"
G "So ‘Semi. Don’t you have something to say? Maybe about your undying love?"
show Utsusemi
U "…"
U "…"
U "…"
G "Why are you just staring at me? Are you too overcome with feelings to talk?"
G "I understand ‘Semi… I’m also just so overwhelmed with my feelings for you!"
G "Perhaps a kiss from the majestic Genji will bring you back to earth."
G "Or is might just blow you out of this world!"
"I lean in to finally capture my Utsusemi in a kiss when suddenly…"
show Utsusemi
U "No! I will not!"
"…"
"…"
"She ran away from me?"
"I thought we were meant to be…"
jump default1

label default1:
scene black with fade
scene lantern_path

"Well that could have gone better…"
"Oh well…"
"Here comes Murasaki! She’ll know what to do to soothe my broken heart!"
show Murasaki
M "Genji… Alone again I see."
M "When will you learn to treat the women you like better?"
M "Who would willingly take you when you treat them like that?"
G "Well I was thinking you would…"
M "Haha you got me. You may be an idiot but I just can’t resist!"
G "Oh Murasaki, why do I even try with these girls that don’t understand me?"
M "I’ll never know Genji…"
"Should I try again?"
menu:
    "I can’t give up on the challenge now!":
        jump room
    "What’s the point when I already have the perfect woman in Murasaki?":
        jump defaultend

label defaultend:
"In the end Murasaki is a great girl."
"I know we can be truly happy together…"
".: TRUE END :."

return


label Utsusemi:
   show Utsusemi
   with dissolve

"She was the girl that got away..."
"Ever since freshman year Utsusemi has been ignoring my advances"
"This is not a normal occurrence for me"
"If I am to be assured of my greatness in the world of love I must have her!"
"Besides, Utsusemi is the only girl from Pomona that is worth my attention right now…"
"So, since I know she secretly finds me attractive"
"Today I decided"
menu:
    "... to talk to her after class":
        jump rightaway
    "... to leave her alone today, no doubt wanting more.":
        jump later


label rightaway:
scene classroom
show Utsusemi 
"It’s important that I talk to her today, I can’t just let her slip away again"
U "Oh, Genji, it’s you again."
G "Of course! You’ve been avoiding me again Utsusemi...."
"I saw her grimace and wondered what I could do to convince her of her love for me"
U "…so did you want something? Because I need to get back to south Pomona, so if you’re just going to leer at me like an idiot I’m leaving"
G "Come on ‘Semi, don’t be like that, all I want is for"
menu:
    "…Us to be friends":
        jump friends
    "…you to finally admit your love for me!":
        jump love

label later:

scene park
with dissolve


"And so I decided to ask her later."
"But I was indecisive."
"what if my hesitation costs me my one shot at Utsusemi?"
"I head back to CMC with a heavy heart, pondering my bad luck in love."
"My phone buzzes with a text"
A "Genji! I know you just got out of class, were you thinking of me the whole time?"
"I really dislike how much Aoi talks to me… Does she not understand that without her here I need to find other women?"
"The thought of Aoi is not enough for me… I must complete the 5C challenge to truly prove that no one is greater than Genji"
jump Nextday1

label Nextday1:
scene dining_hall
with dissolve

"Entering the dining hall the next day I was still hung up on the cold exterior of Utsusemi"
"To my good fortune I spot Utsusemi sitting across the room!"
"I wonder who the handsome young man next to her is…I cannot have competition, I will destroy him…"
"Walking over I greet Utsusemi"
G "’Semi, how charming to see you here…I didn’t get a chance to talk to you yesterday after class"
show Utsusemi at left
show Jim at right
U "Whatever Genji, could you shove off please? My brother Jim just finished his first week here at Pomona and I don’t want to be dealing with you while we’re having lunch together."
G "Now now ‘Semi, no need to get heated… I would never dream of taking up too much of your time when your delightful brother is around!"
"I can’t help but notice the innocent beauty in Jim’s eyes… His beauty may even surpass that of his sister"
"But don’t I have the 5C challenge to complete?"
hide Ji
"I should"
menu:
    "…Try to get Utsusemi alone to ask her out":
        jump alone
    "…Focus on the beautiful man in front of me":
        jump Jim

label alone:
scene dining_hall

"I should focus and talk to Utsusemi…Jim is just a distraction"
G "But seriously ‘Semi, I do have a question about the homework for class."
show Utsusemi
U "Well? Why don’t you ask me your question and leave then?"

G "I don’t want to bother Jim while he’s eating, why don’t we go discuss this alone for a few minutes?"
show Utsusemi
U "Whatever will finally get you off my back…"
"We walk over to a secluded corner of Frary, with no one standing between us anymore"
G "Listen ‘Semi, we’ve been dancing around the sexual tension for too long…"
G "Why don’t you just admit that you’re attracted to me, and we can make your dreams a reality?"
U "…"
G "So, what do you say? You, me, candles, up on the roof of Kravis? Saturday night?"
U "I don’t know about that…"
G "Just give me a chance…"
U "I guess one date couldn’t hurt"
"Finally the chance I need to get Utsusemi"
"She’s denied me for too long… this date can change everything!"
hide Utsusemi
scene black with fade
jump Saturdaynight 


label Jim:
show Jim at right
"In the end I can’t ignore perfection when it’s staring me in the face"
"Besides, Jim can still work to fulfill Pomona in the 5C challenge!"
"Although he was not my initial target, he’s clearly more friendly and open to me than Utsusemi is…"
G "Anyway ‘Semi, if you don’t want to be bothered that’s fine by me"
G "And since it is your brother’s first week here, I would be remiss not to offer him my services should he need anything at all" 
U "I’m sure Jim…"
J "I can speak for myself thanks Utsusemi."
J "Actually Genji I would love to hang out sometime. I haven’t really met anyone from CMC yet."
J "In fact I’m free later tonight…"

"This is my chance to really get to know Jim"
"Should I"
menu:
    "…Immediately invite Jim to hang out tonight":
        jump Immediately
    "…Play it cool":
        jump Playitcool


label Immediately:

"I decide to act immediately…I can’t let a prize like Jim slip from my fingertips!"
G "Well it’s your lucky day then… I’m free as well!"
G "What do you say I show you around my home turf?"
J "Wow! Thanks Genji!"
G "It’s my pleasure Jim. There’s nothing I would rather do…"
hide Jim
hide Utsusemi
scene black with fade
jump jimnight

label Playitcool:
"I decide to play it cool…hopefully that will leave him wanting more"
G "Well Jim I’ll be sure to let you know when I have the time."
G "I was planning to hang out with To no Chujo tonight anyway."
J "Oh…"
"I can’t help but notice that Jim seems disheartened"
"It seems like I have hurt his feelings"
"I should have taken my chance when I had it…"
hide Jim
scene black with fade

jump TonoChujo

label TonoChujo:
scene dorm_night
 
"That night I ended up visiting To no Chujo just as I had promised Jim"
"I feel as though I have missed a great opportunity…"
"Although I have known To no Chujo a very long time his company is not what I want."
"All he does is remind me of Aoi"
"I don’t want to think of her right now"
"Instead I busy my mind with thoughts of Jim…"
"I’ve messed everything up…"
"Here I am, alone on a Saturday night with To no Chujo!"
"How far the mighty Genji has fallen to have me stuck here with Aoi’s brother and no hope of any action!"
"Somewhere I went terribly wrong… I should"
menu:
    "Accept a life of loneliness and sleep through the rest of my college years":
        jump lonelyend
    "Go back to class tomorrow and try to get back on track…":
        jump room

label lonelyend:
scene black

"There is no point anymore…"
"Goodbye social life… Goodbye conquests… I’m off to study and sleep forever…"
".: BAD END:."
return



label Saturdaynight:
scene dorm_night
"Tonight I finally have a chance to show Utsusemi what she’s been missing!"
"Everything is all set up. I brought candles, a blanket, and refreshments"
"Now all that’s left is for Utsusemi to arrive so that we can watch the stars and for her to fall madly in love with me!"
show Utsusemi
U "Genji? Are you here?"
G "’Semi! I must say you look positively ravishing tonight!"
U "Oh, um, thank you Genji."
U "I don’t know how you managed it but here we are. On a date. I can hardly believe it."
G "Well believe it ‘Semi!"
G "Get ready for the best night of your entire life!"
G "As you can see I’m all set up. What do you say we get to know one another?"
U "Oh, um, ok then."
U "This actually is quite beautiful… I’ve never been on the roof of the Kravis Center"
G "Just one of the many things I can offer you if you agree to go out with me again!"
G "You may not realize it yet, but I think we have a lot to offer each other."
G "I think that deep down you realize that we’re meant for each other!"
"…"
"…"
"That’s pretty forward of you to say Genji…"
G "Well I just want you to understand my feelings"
G "It just seems like you’re running away from this relationship and I want to know why!"
G "I can’t think of any reason why you wouldn’t want to be with me, and I know I want to be with you, so I guess I just don’t understand what the issue is."
U "Genji I just don’t know you that well…"
G "What better way to get to know me than through a relationship?"
"I don’t understand why she has to be so hesitant…"
"I need to find a way to break into her shell"
"I wonder what the best way to do that is though…"
"I should"
menu:
    "…Go in for the kiss. What better way to make her accept her feelings":
        jump quickkiss
    "…Give her some time to figure out what she wants":
        jump slowtime

label quickkiss:
scene dorm_night

"There’s nothing better than action to realize emotion…"
"I close my eyes and lean in for a kiss…"
hide Utsusemi
"…"
"My lips meet air"
"I fall over as Utsusemi is no longer where she once was"
"What is this feeling?"
"I open my eyes to see my sleeve ablaze with the fire from the candles I lit earlier"
"This is not the end to the night I imagined at all"
"As a furiously attempt to put out my burning sleeve I see Utsusemi fleeing the building…"
"I have failed…"
"I’ll have to try again with someone else I suppose…"
".: BAD END :."
jump room

label slowtime:
scene dorm_night
"In the end I cannot force her to immediately realize her feelings…"
G "I understand if you need some time ‘Semi. This is just the first date after all…"
U "That’s surprisingly mature of you Genji…"
U "You know every time I feel like you are about to become a total creep you end up acting ok?"
U "Maybe there’s hope for you after all."
U "I don’t hate you or anything Genji… All I want is to take this a little slow."
U "If I’m going to be with someone I need to trust them. Can you give me the time I need?"
menu:
    "I think I can ‘Semi. You’re worth any amount of time!":
        jump worthit
    "…I don’t know about that ‘Semi. A man has needs you know…":
        jump manneeds

label worthit:
scene dorm_night
show Utsusemi
U "Congratulations Genji. You have passed my test!"
U "For some reason I thought that you might not be ok with that…"
U "All I really wanted to know is that you’re a man who can wait."
U "Since you have shown me that you have at least some virtue in that mind of yours I feel that you have earned a reward."
U "I’m ready Genji…"
scene black
jump happyutsusemi

label happyutsusemi:
scene park

"I have managed to check Pomona off my list."
"That was quite the experience…"
"Utsusemi sure is a slippery one… but now I’ve experienced the whole package with her."
"Now on to new adventures…"
".: GOOD END :."
jump room

label manneeds:
scene dorm_night
show Utsusemi
"…"
"…"
U "I thought you were better than this Genji…"
"Oh dear. There she goes running into the night…"
"I can’t help but feel like I let her slip through my fingers."
"In any case, I wish I could have had her at some point…"
jump default1


label jimnight:
scene dorm_night

"I’m actually a little nervous about hanging out with Jim tonight!"
"I so rarely get nervous… I mean I’m Genji!"
"And Jim did seem excited to hang out tonight…"
"…"
"I wonder when he’ll get here?"
show Jim
J "Genji? Are you here?"
G "Jim! You came! I wasn’t sure when you would arrive!"
"He looks perfect… why is he perfect?"
"Why can’t this be just like the other women?"
"In any case I can’t just stand here like an idiot!!"
G "So… um, Jim?" 
G "I was thinking that maybe you want to…"
menu:
    "Take a walk in the moonlight with me?":
        jump moonlight
    "Hang out in my dorm room with me?":
        jump dormnight

label moonlight:
J "Oh in the moonlight? That would be so beautiful! I’ve never walked around CMC at night!"
G "Well let me show you my world…"
G "I know the perfect place that we can go to…"
"I’ve heard that the roof of the Athenaeum is perfect at night. I think I’ll show my little boy the starts tonight!"
G "Follow me up here Jim. From here you can see the whole sky!"
J "Wow Genji! This is really amazing!"
J "How did you find out about this place?"
G "You learn a few things after spending a few years here…"
G "There’s a lot of things I could teach you Jim…If you would only let me"
J "What kind of things Genji?"
"This is my chance"
"He’s so beautifully innocent…I will make him mine tonight…"
G "What kind of things you ask? Well for starters I can teach you what real passion feels like…"
scene black with fade
jump Jimend

label dormnight:
scene dorm_night

G "So, um, this is my dorm room!"
G "It’s a single so luckily we can have some privacy tonight…"
show Jim
J "This is such a cool room Genji!"
J "Hey why do you have a checklist with the five colleges listed on it?"
"Crap! That’s my 5C challenge checklist!"
G "Oh, um, don’t worry about that…"
G "That’s… um… not nearly as interesting as some other things all the way on the other side of the room!"
J "Ok! What’s over there!?"
J "Wow you have a couch?"
J "Genji you’re so cool!!!"
"That was close…"
G "Anyway Jim, why don’t we hang out on the couch? Get a little more…comfortable?"
J "Sure Genji!"
J "So what do we do now?"
G "Oh I can think of a lot of things we could do…"
G "Since we have all night I think we might even get to try them all…"
"I can’t help but think that I’ll be able to add a checkmark to that list after tonight…"
hide Jim
scene black
jump Jimend

label Jimend:
scene park
show Jim
J "Genji I’m so glad I met you..."
J "I didn’t really know what to expect coming to college but you’ve shown me how to live my best life here"
G "I’m glad that I could service *ahem provide that service for you"
G "You know Jim, you’re a really special guy…"
G "It’s the funniest thing…I originally wanted to ask your sister out…"
G "I have to admit that I’m glad that I spent time with you instead!"
G "I wouldn’t trade anything we’ve done for the world!"
"These days with Jim have been some of the best of my whole time at Claremont.."
"Who would have thought that Jim was who I was looking for all along?"
".: GOOD END :."
return

label friends:
scene room
"I decided that it was best to play it slow with Utsusemi…"
"She’s a tricky one, if I’m not careful I might just scare her away."
show Utsusemi
U "Wow Genji… You know maybe I underestimated you. Here I thought that all you wanted was to sleep with me."
U "I guess you’re not as much of a scumbag as I thought!"
G "As much as? You wound me ‘Semi. You know I just want you to be happy…"
U "We’ll see Genji…We’ll see…"
hide Utsusemi
scene black
 
jump Nextday2

label Nextday2:
scene dining_hall

"It seems like Utsusemi might actually trust me a bit after yesterday!"
"Which makes it the perfect time to take advantage of that!"
"Today I will make Utsusemi mine…"
"And just my luck that she’s here in the dining hall!"
G "Hey! ‘Semi! Fancy seeing you here!"
"And I wonder who that dreamboat next to her is…"
G "And just who might this be?"
show Utsusemi at left
show Jim at right
U "Oh. This is my brother Jim. He’s a freshman this year. It’s pretty great that we both get to go to Pomona"
G "Indeed. Who would have thought that the school was lucky enough to have both of you under one roof?"
G "What a stunning family…"
"I can’t help but notice Jim’s innocent beauty"
"This changes things… I want them both if I’m being honest… but right now I should"
menu:
    "…focus on Utsusemi":
        jump alone
    "…accept the beauty of Jim and focus on him.":
        jump Jim

label love:
scene classroom

"I decide that it’s been long enough. It’s time for Utsusemi to admit her true feelings!"
G "So ‘Semi. Don’t you have something to say? Maybe about your undying love?"
show Utsusemi
U "…"
U "…"
U "…"
G "Why are you just staring at me? Are you too overcome with feelings to talk?"
G "I understand ‘Semi… I’m also just so overwhelmed with my feelings for you!"
G "Perhaps a kiss from the majestic Genji will bring you back to earth."
G "Or is might just blow you out of this world!"
"I lean in to finally capture my Utsusemi in a kiss when suddenly…"
show Utsusemi
U "No! I will not!"
"…"
"…"
"She ran away from me?"
"I thought we were meant to be…"
jump default1

return

label Tamakazura:

"Challenge Accepted"
"But how should I approach her?  I’m a little afraid she might be one of those man-hating Scrippsies….or maybe a lesbian"
"Wait, what the heck am I talking about.  I’m Genji—that means all the ladies must love me."
"She may not pay attention to me now, but I’ll change that"
"Still…."
"If this goes badly, I swear this is the last time I’ll take To no Chujo’s advice..."
"…"
"Aw, shit, class is about to start, I’ll catch her after."
scene black with fade

scene classroom
G "Tamakazura!"
"…"
"Is she ignoring me??"
G "Tamakazura!"
show Tamakazura
T "Oh!  Sorry, I was lost in thought.  What do you want?"
menu:
    "you":
        jump feisty
    "just to talk to you":
        jump chattyG
    "complement you":
        jump chattyG

label feisty:
G "You."
T "Excuse me?"
G "Uhh, I want you to go on a date with me?"
T "…"
"Why does this girl put me on edge?  Why won't my good looks and guiles work on her"
"..I guess that wasn't particularly sly, but still…"
T "Why this, why now?"
G "I'm looking out for you"
T "I don't need you looking out for me."
G "But I—"
T "What a creep…."
hide Tamakazura
"I have the feeling that could have gone better.  I'll try again Wednesday."
jump room

label chattyG:
"Okay Genji, you don't want to scare her, try the shy tactic"
G "I keep seeing you around, but we haven't really talked.  I just wanted to tell you that you look beautiful today."
"I think that did the trick, I'm such a great actor."
T "Wow, that out of character for the notorious Genji."
"WHAT?! She saw through that??  But  I have to keep it up or I'll lose my chance."
G "I know I have a, uhm, reputation as a womanizer, but can't a man change his ways?"
T "I don't know, can a leopard change its spots?—"
"Aw man, the sarcasm just makes her more irresistible."
G "Paint."
T "…paint?"
"Smooth one, Genji, you dolt."
G "Yeah….anyways I've changed.  I'll prove it to you if you just go on a date with me."
T "Sorry, busy."
G "Please, Tamakazura."
G "Wait, you play harp in the orchestra don't you?"
G "So I have a better idea"
G "I've been working on a flute piece and need an accompanist."
G "Could you please?"
"I can see her smiling a bit now, I think I've found her sweet spot.  Seems she has a thing for music."
T "Okaaaay…"
T "Meet me at the practice rooms tonight.  8pm sharp.  As I said, I'm busy."
"She took it, hook, line, and sink."
"But there's a slight problem….well, besides the fact I haven't played flute since I was ten."
menu:
    "tell Tamakazura I can't get into the practice rooms":
        jump nopractice
    "agree regardless":
        jump gopractice

label nopractice:
G "Slight problem, that's a Scripps building and I don't think I can get in.  Can we meet at my dorm instead?"
T "Slight problem, that's a CMC building and I don't think I can get in."
"Damn, she's sharp.  I might just have become more attracted to her"
G "Come on, top floor of the towers.  Haven't you wanted to see them?"
T "…"
"Come on…..please just give in to my gorgeous, alluring looks already."
T "See you later."
hide Tamakazura
"Wait, was that a yes or a no?"
"She'll show up, I'm Genji, after all."
scene black with fade
jump Tnight

label Tnight:
scene dorm_night
"….it's 8:30 and she hasn't showed up yet."
"I couldn't have…scared her, could I have?"
"Oh!  Wait!  I just got a text."
"it says:  Sorry I'm late, how about we meet for a run tomorrow morning instead?"
"…on one hand it's running…."
"…but it's also an excuse to be shirtless and show off my gains…"
"I should respond…"
menu:
    "Sure, no problem, 7":
        jump run7
    "eh, no thanks":
        jump loseinterest

label run7:
"mmm hot and sweaty Scrippsie.  Might just have to take a shower together afterwards."
"I think tomorrow will start wonderfully."
scene black with fade
scene park
"7:15, where is she?"
"For someone who was so insistent yesterday about being punctual, she sure is a hypocrite"
"For all this waiting, I deserve some nice shower sex"
"…"
"Do I hear footsteps?"
Narrator "(Genji turned around, only to find no one there.  Suddenly, he felt a heavy dull thud on the small of his back, quickly followed by a harder blow to the head.  Genji fell, temporarily crippled by pain.  He barely managed to turn his head around and look at the attacker.)"

show Tamakazura
with dissolve
T "You are such a liar"
T "And a creep"
T "You thought I would fall for one of your pathetic little scemes?"
T "What would you have done if I showed up last night?"
Narrator "(Genji felt another heavy kick, this time to his left side.)"
T "I told you I don't like creeps.  You deserve this, and more.  For all the poor women you've conned."
hide Tamakazura
G "…Ow…"
"…Definitely a man-hater."
"This is what I get for cheating on Aoi.  I can see the sad look on her face if she could see me now."
"I'm glad she can't….I'm such a mess.  Such a failure."
"How could the mighty Genji fail so miserably?."
"I should never have pursued Tamakazura."
"At least….there are other Scrippsies…"
".: BAD END :."
jump room

label loseinterest:
"Why am I wasting my time on her, there are other Scripps students that I can use to fulfil the 5C challenge."
"In fact, I can start on another tomorrow."
".: UNFULFILING END :."
jump room

label gopractice:
G "Sure.  Could you meet me by the entrance though to let me in?"
T "*sigh*  Fine."
hide Tamakazura
scene black with fade
"…"
show Tamakazura
Narrator "Tamakazura was already there, looking impatient and taking long drags from a cigarette.  Upon seeing Genji, she began stubbing it out."
T "What took you so long?  You're four minutes late."
T "…"
T "And where is your flute?"
G "…"
G "I was hoping that we would find…a different use for those private, soundproof practice rooms."
T "Typical CMC fuckboy, only one thing one the brain."
G "Is that a yes?"
T "ARE YOU FUCKING DENSE?"
T "NO."
T "I came here to play harp, and play harp only."
T "I'll bet you don't even own a flute."
T "You're a filthy lair."
hide Tamakazura
Narrator "Tamakazura flung her still smoldering cigarette butt at Genji, narrowly missing his face by mere centimeters.  She sharply turned away and stalked off in obvious anger."
G "…ouch"

jump default1


label Rokujo:
"Scary can be good"
R "Hey, you there."
"…!!"
show Rokujo
R "I see you staring at me."
G "How could I help but admire your beauty?  I—"
R "You think flattery will get you anything you want?"
G "You look and act tough, but I can show you why you need a man."
R "We'll see."
"Did I just see a slimmer of a smile?  I think she's flirting with me."
"Pshh, this will be a piece of cake."
hide Rokujo
scene black with fade
jump lunchRY


label Yugao:

"I still need a Scrippsie and Yugao seems like the least intimidating option here"
"Besides, I've talked to her in class before and she seems genuinely kind.  Almost makes me feel bad using her to complete the challenge."
"…Almost, not quite."
"And besides, such a sweet, pretty girl like her would just be ecstatic if someone like me so much as looked her way, it would make her day."
"Well in that case, I'm about to make her whole semester."
"Here goes…."

show Yugao at left
G "Hey there, Yugao.  How are you doing today?"
"I can see her beginning to smile already.  This is too easy."
Y "Great!  Thank you!  How are you?"
show Rokujo at right
R "Yugao, hurry up we're going to be late."
Y "Oh!  Right!  Talk to you later, Genji!."
hide Yugao
R "…"
hide Rokujo
"…did I just imagine Rokujo glaring at me?"
"Scary..."
"Anyways, Yugao is even friendlier than I hoped.  She'll be a nice break from…my last."
"I just need to figure out how to get time alone with her."
scene black with fade
jump lunchRY

label lunchRY:
scene dining_hall
show Rokujo
G "Oh!  Imagine running into you here!"
"I didn't follow her here, I don't know what you're talking about."
R "I told you I was in a hurry—unless you want to join our feminist meeting, I'll see you later."
"F—feminist meeting?  Ugh."
"Then again….sitting at a table full of pretty women…."
"*shudders*"
"If they're all like Rokujo, I don't think I want to piss them off."
show Yugao
Y "Hi Genji!  Here for the meeting?"
"Those two girls are inseparable.  How am I ever going to get one of them alone?"
"…"
"Genji, you idiot, respond fast or they'll know you're lost in threesome fantasyland."
G "I think…"
menu:
    "Sure.":
        jump mansplain
    "I think I'll pass":
        jump ithoughtso

label ithoughtso:
show Rokujo
R "Huh.  Thought so."
"…"
"She doesn't even seem sad to lose the grace of my presence."
"Well, I squeaked out of that one."
hide Rokujo
scene black with fade
jump rokodorm

label mansplain:
Y "Really?  Okay, follow me."
show Rokujo
R "Remember your privilege.  Don't interrupt, don't talk, don't excuse your kind."
"… oh no…"
"what have I gotten myself into…?"
hide Rokujo
scene black with fade
"…"
"Everyone keeps shooting daggers at me."
"I wonder why?"
"Well…maybe because a few of them, erm, know about my reputation."
"Still though…This is miserable"
"This has just been an hour of me feeling bullied and scrutinized."
"Can I leave yet?"
jump rokodorm


label rokodorm:
scene dorm_night
"Ah, good to finally be back in the comfort of my dorm."
"Time for Netflix…unfortunately no chill."
"…"
"Was that a knock on my door?"
"Who does that?"
menu:
    "Answer it already":
        jump answerr
    "Stay quiet and ignore it.  I've earned this Netflix.":
        jump boringg

label boringg:
"…"
"I think they've left."
"Huh, wonder who that was…."
"Anyways, time to binge watch tv."
scene black with fade
jump room

label answerr:
G "Hello?"
show Rokujo
"How does she know where I live?"
"But…a pretty girl coming right to my door—I can't complain."
R "I told you I'd see you later."
R "Now where did we leave off…?"
"Really?!  Sweet!"
"I'm not going to pinch myself, this is too good."
hide Rokujo 
scene black with fade
"That quickly went from just Netflix to just chill."
"…"
"Hmm?  Where did she go?"
"…?"
"Odd…I guess I'll just go back to sleep."
jump nextday42

label nextday42:
scene classroom
"Rokujo isn't in class today.  I wonder what's happened to her.  Maybe Yugao will know."
show Yugao
G "Hey Yugao, where's you roommate?"
Y "Oh…she's a little sick…"
"Am I just imagining it, or does she look sad?  I didn't even do anything!"
"…oh…"
"I should…"
menu:
    "Quickly try to repair the situation.":
        jump hauntedhouse
    "Not worry about it.":
        jump asshat

label asshat:
"Besides, I've already gotten Scripps checked off, so what does it matter?"
"Hmmm, that night was nice though, I wonder when I can see her again…"
"I've got it—two sparrows with one stone!"
G "Oh it's nothing, just tell her she left"
"I feel bad making such a nice girl upset.  But hey, she should have seen this coming--that`s what you get when you crush on a playboy, right?"
hide Yugao
scene black with fade

scene dorm_night
"I hope Rokujo takes the hint and comes back."
"…"
"… …"
"Oh!  There`s the knock!"
G "Come in!"
"I think I could be happy with Rokujo."
".: GOOD END :."

label hauntedhouse:
G "Nonono don`t worry about it."
"…she doesn`t look convinced."
G "I was just asking because you two are inseparable and I wanted a moment alone to ask you a question."
G "There's a haunted house at my dorm this weekend and I was hoping you would go to it with me."
"There we go, Genji you sly fox.  You can have them both."
Y "Oh!  That…wasn't what I was expecting…but that sounds like fun!"
Y "…Although I get scared pretty easily…"
"heh, that's the point, you'll be clinging to me and see me as your hero and just be so enamored that anything could happen."
G "That's alright—that's why you'll have me to hold on to."
Y "Thank you Genji, you're so kind!"
hide Yugao
"I think that's one of the best ideas I've ever had."
scene black with fade
"…"
"It's the night of the haunted house."
"It's pretty quiet, I don't see anyone here beside Yugao and myself."
G "Ready?"
show Yugao
Y "Uhm…..okaaay….Yes, sure, you'll keep me safe!"
"Thank goodness she brightened up a little, I was beginning to think this was a bad idea…"
Ghost "WELCOME TO THE HOUSE OF DOOOOOOM"
Y "AUGHH"
"…it hasn't even started yet…"
Ghost "I WILL BE YOUR GHOST, ERM, HOST TONIGHT.  WILL YOU MAKE IT OUT ALIVE?"
G "Wow that's pretty corny."
Y "Y-yeah…"
"She seems was more scared than she should.  What's up with her?"
Ghost "AH FRESH YOUNG LIFE.  IT SHALL BE MINE!  MINE!  MIIIIIIIIIIIIIIIIIINE."
"…I'm having a hard time trying not to laugh."
"Yugao seems really into it though, judging by how sore my arm is already."
"Youch, I don't know if I'll make it out of here with my arm still alive."
"hehe oh well"
Narrator "(The ghost charged in, wielding a not-so-menacing tin foil sword.  Somehow, though, the ghost still managed to frighten, fueled on by an intensity of hatred and…jealousy?  Yugao screamed then passed out from freight.)"
hide Yugao
with fade
G "YUGAO!"
"Oh my god, she isn't dead, she can't be dead, oh my god what have I done, why did I do this, why couldn't I have just been direct in my intentions."
"…"
"…I think I feel a pulse still, but I'm no doctor…"
Ghost "AHAHAHAHAHAHAHAAAA"
G "Hey!  This is no time to laugh!  A girl has just passed out!  Shouldn't we take her to the hospital or something."
Narrator "(When the ghost made no inclination to help, Genji lashed out, yanking the sheet from the student worker.)"
show Rokujo
"…"
G "Wha-...Why…?"
R "My how quickly you break your promises."
G "Promises?  What promises?  And help me get your roommate to the hospital!  How can you be so cold!"
R "Me?  Cold?  You're the one that gets a girls hopes up then leaves her to the wolves in favor of her ROOMMATE nonetheless."
G "Rokujo, no, that's not—"
R "Not what you meant?  Of course it's what you meant.  You're a heartless playboy to the core.  No one is ever good enough for you—used once then tossed aside like a broken toy."
R "I can't believe I thought you were better than this."
G "But we never said we were exclusive."
R "Typical CMCer.  Fine.  Be that way.  I'll see to it that the rest of your college life is miserable."
hide Rokujo
"…"
"And she didn't even help me carry out Yugao…"
"What a mess I've gotten myself into."
"I must be losing my charm…."
"Without that, what else to I have?"
"…certainly not my dignity…lost it at toga last week…"
"Anyways….but, Yugao…."
"I think she's still alive."
"She had better be alive."
"…"
G "HELP!"
"…"
".: DESPAIR END :."
return

label Fujitsubo:

"…"
"Somehow I'm the last one left in the classroom…"
"Well, today sure was uneventful—it's almost as if I've lost my girl magnet powers.  I'm beginning to question To no Chujo's advice to take this class."
"Huh….I guess I'll head back to my dorm."
scene black with fade
jump RArunin

label RArunin:
scene outside_dorm
with fade
show Fujitsubo
with fade
"Oh!  That's my RA, Fujitsubo." 
"I've never paid much attention to her because she's a year older than me."
"But now that I see her here, and in broad daylight….she's actually pretty attractive"
"…actually, no, make that VERY hot"
"I wonder what she's doing here, shouldn't she be busy working on RA things?"
"I mean, it's not like I'm not glad to run into her and her perfect figure…."
"…alright, time to do my best and make sure I've still got it after today's earlier fiasco."
"I'll…"

menu:
    "complement her":
        jump charmRA
    "ask about the hall meeting":
        jump hallnoob
    "catcall her":
        jump asshole


label charmRA:

G "Fujitsuboi!  Damn that dress looks great on you"
F "Are you going to finish the pickup line?"
"mmm direct, I like it."
G "It would definitely look better on my floor, though?"
F "Let's test that, shall we?"
" Just when I thought I had run out of luck—Genji scores again."
"I'm good, really good, really suave."
"I can't believe this is going so well so quickly, it's like we were destined to be together."
"…normally I'd think I've gone crazy for and laugh for thinking up such a cliché romantic thing as destiny."
"…but this isn't normal.  This is alluringly taboo."
"I think my CMC checkmark will be the most exciting one yet."
scene black with fade
jump class2


label hallnoob:
G "Oh! Fujitsubo!  I'm so glad I ran into you.  I'm sorry I missed the hall meeting."
F "…that's all you wanted to say?"
G "Well, no, but…"
F "Go ahead…RAs are  required to have an amnesty policy, so say what you really want to."
"Was my lust so visible?"
"Or was this pure, unadulterated luck?"
"I might as well give it a shot…"
G "Say, why don't you take me back to your dorm and get me…caught up?"
F "That's better."
"Success!  Who knew CMC would be that easy?"
scene black with fade
jump class2


label asshole:
G "Sexy legs, baby."
"that should do the trick"
F "Fuck off, Genji."
hide Fujitsubo
"What did I do wrong?"
"And how could being cursed at be so arousing?"
G "Wait!  No!  Don't go!"
"Since when did I go begging after girls?"
"This isn't right…"
"Shit."
jump default1

label class2:
scene classroom
with fade
"I can't stop thinking about yesterday afternoon"
"She was not lying when she said the dress would look better off."
"Fujitsubo is just….perfect….there are no other words to describe her."
"There are plenty of beautiful women in this class for me to talk to, but..."
"They all pale in comparison."
show Utsusemi
"Utsusemi… she’s a slippery girl alright. But, that doesn't seem to matter anymore."
show Yugao
"Yugao, a Scripps student… She’s very shy but there’s just something about her that I can’t resist!"
"…actually…"
"She's lost her appeal, too."
"What's wrong with me?  ME, GENJI, THE NOTORIOUS PLAYBOY OF THE 5CS."
"They all just seem…so boring."
show Rokujo
"Rokujo, also a Scripps student. A little scary but I don't mind that—I don't need her anymore."
"I hear she’s pretty jealous, but with Fujitsubo she'd have every right to be."
"What am I saying, I couldn't do that to Fujitsubo."
show Suetsumuhana
"I think that girl goes to Mudd… maybe her name is Suetsumuhana?."
"I hear that no one ever even sees her outside of class.  Eh."
show Tamakazura
"That’s Tamakazura. Another Scripps student."
"A challenge if there ever was one"
show Oborozukiyo
"And there’s Oborozukiyo, a Pitzer loony I guess."
hide Oborozukiyo
"I think I've gone mad.  I've never been this infatuated with anyone before, not even Aoi."
"I need to see Fujitsubo again."
"No, NOW!"
scene black with fade

scene outside_dorm
with fade
show Fujitsubo
with fade
G "Fujitsubo, I need you."
F "Need?  Since when are you so clingy."
F "Grow up a little."
F "We only slept together once.  That doesn't mean we're exclusive."
F "And you of all people should realize that."
G "…"
F "You know, I thought you seemed like a pretty chill guy, but apparently I was wrong."
F "Thanks for reminding me why RAs should never get involved with their students."
hide Fujitsubo
scene black with fade

"I shouldn't be so worked up over this."
"She's right, we never were in a relationship."
"But I can't help but feel that a part of me is missing."
"How the mighty have fallen…."
"…"
"I think…"
"To spite her, I'll complete the 5C challenge as fast as possible."
".: BAD END :."
jump room



label Oborozukiyo:
"I haven't really talked to many Pitzer students before, they're always just a bit…strange."
"But this one looks like she actually takes showers."
"Plus I'm intrigued—what's her deal with the moon?"
G "Oborozuk—"
show Oborozukiyo
O "…"
O "… …"
G "—iyo…"
O "…"
"How did she even get to class, she's so spacey?"
"Heh, spacey, I'm funny."
"Maybe that's her lunacy.."
"Getting baked off space cakes."
"I think I'll:"
menu:
    "Leave her be, she's too stoned to function.":
        jump RArunin
    "Treat her munchies":
        jump munchies

label munchies:
G "You hungry?  Want to stop by the hub for a snack?"
O "… …"
O "Hmmm?  Food?  Oh, yes please."
"She responds to food, but not her own name??"
"Anyways, don't look a gift horse in the mouth, right?  She should be a quiche."
"…I mean quickie…"
hide Oborozukiyo
scene black with fade

scene black
"…"
"…I can't believe we did it outside…"
"But what I'm most ashamed of is that she seems to be paying more attention to the night sky than to me."
"…"
"Well….Pitzer, check."
".: A HAZY END :."
jump room

label Suetsumuhana:
scene classroom
with dissolve

"It’s a brand new day and I’m ready for a new extracurricular project for my class"
"I think Suetsumuhana is just the girl for that!"
"The mystery surrounding her is intriguing…"
"I’ll make sure to catch her after class and introduce myself. No one better than Genji to bring Suetsumuhana into the light!"
jump afterclass2

label afterclass2:
scene classroom
"After class…"

G "Hey! You there! Suetsumuhana?"
show Suetsumuhana
S "!!!"
S "Me?"
G "Yes, you!. Allow me to introduce myself. As you probably already know, my name is Genji."
G "Sitting in class today, I found myself distracted. I could sense someone’s intoxicating perfume behind me…"
G "Do you know whose perfume that was?"
S "Um…. No?"
G "Yours, my little yellow blossom."
G "Your sweet flowery scent washed over me and I knew whose it was immediately."
G "There have been stories of the girl who smells of safflower. People say she’s from New York, and that her father was a big CEO out there…"
G "I don’t suppose you could be that girl?"
S "Well I am from New York… What kinds of stories have you heard?"
G "You can’t expect me to give up all of my secrets right when I meet you!"
G "It’s probably for the best that we meet again… Outside of class?"
S "A-a-again?"
S "I don’t know… Can’t we just meet in class tomorrow?"

"I wonder what it is that she does outside of class…"
"Yet another mystery surrounding this girl…"
"I should"
menu:
    "…Agree to meet her in class. There are more important goals than finding out about her social life.":
        jump notcurious
    "…Insist that we meet tonight. I must uncover where she goes at night!":
        jump curious

label notcurious:
scene classroom
"This matter is not worth pressing. Meeting her tomorrow in class will be a good start at gaining her trust…"
G "Sure thing little blossom. I wouldn’t want to make you uncomfortable or anything… Let’s meet tomorrow."
G "Besides, more likely than not you’ll be begging to hang out after class with me in due time…"
S "Thanks Genji…"
hide Suetsumuhana
jump nextclass2

label nextclass2:
scene classroom
"It’s a fresh day. Today I WILL get Suetsumuhana to go out with me tonight."
"I’ve caved to her wishes once… It’s about time I learned what she’s up to."
"And just my luck, there’s Suetsumuhana!"
G "Oh my little blossom, did you miss me dearly last night?"
show Suetsumuhana
S "Oh! Genji... You startled me!"
S "So… um… A-are you going to tell me the stories you’ve heard about me today?"
G "Why my little blossom! This is hardly the time or place to be sharing such information!"
G "What do you say we instead find a nice little place to talk tonight?"
S "Oh… Um… I suppose that would be fine…"
G "Excellent. Then I’ll be seeing you tonight my little blossom!"
hide Suetsumuhana
scene black with fade

jump Suetnight

label curious:
scene classroom
"In the end I am just too curious about her. Meeting her tonight will help clear things up. Plus no one can resist Genji at night!"
G "My little blossom!"
G "Why are you trying to blow me off?"
G "All I want is for us to have a little chat later… A classroom is no place to discuss important matters."
S "If you insist Genji…"
G "I absolutely do. Besides, this will give me the chance to really get to know you better my little yellow blossom!"
G "I shall see you later…"
hide Suetsumuhana
scene black with fade

jump Suetnight

label Suetnight:
scene picnic
"Finally the time has come for me to really understand my Suetsumuhana!"
"I’ve noticed To no Chujo lurking around her as well; it seems that her mystery is not only intoxicating to me."
"But To no Chujo does not really stand a chance. Not when I, the irresistible Genji, am also pursuing her"
G "Ah, my flower! I’m so glad you came to this little spot with me!"
show Suetsumuhana
S "Did I really have a choice Genji?"
S "You apparently know of all my secrets and have been threatening me with them ever since I met you!"
G "Is that really what you think of me my blossom?"
G "A man willing to threaten an innocent girl just to spend time with her?"
G "I’m frankly insulted!"
S "Is that not what you’re doing?"
G "Not at all my flower! I just want to get to know the real you! And I think we all know that I don’t need to resort to threats to get a woman on a date with me!"
G "Is it so foreign to you to think that I might just be interested in getting to know the real Suetsumuhana?"
S "I suppose not… It’s just that men don’t normally want to get to know me…"
G "My sweet sweet Suetsumuhana… That is all I want. So what do you say we start over? Just get to know one another as we are now?"
show Suetsumuhana
S "I would like that a lot Genji…"
G "Excellent. So tell me about yourself…"

jump laterconvo

label laterconvo:
scene picnic
"We ended up talking for hours. And yet she still felt guarded…"
G "You are truly a delight my little blossom!"
"I think she finally trusts me… I should"
menu:
    "…ask about her past":
        jump pastlife
    "…ask her out on a proper date tomorrow night":
        jump properdate

label pastlife:
scene picnic
"Now is my chance to understand Suetsumuhana and all of this mystery surrounding her past life!"
G "So tell me my blossom… what circumstances caused you to leave the east coast? It’s so far from home…"
S "Well after my father passed away I fell on some bad…. Wait… I thought you agreed not to pry into my past!"
S "Is that all you want from me Genji?"
S "I thought you actually cared about me…"
S "Not the controversy surrounding me!"
S "You know what? I’m done with this…"
hide Suetsumuhana
"…"
"…"
"She left me…"
"Wait a moment!"
"She’s walking over to To no Chujo!"
"How have I let this happen…"
"I never should have broken my promise…"
".: BAD END :."
jump default1


label properdate:
scene picnic
"I’ve had such a wonderful time with Suetsumuhana today, I really think we could have a proper relationship!"
G "Anyway my flower… I’ve enjoyed this talk so much. It’s amazing how much we really have in common when you think about it."
G "What do you say that we have a proper date tomorrow night?"
G "I want to show you a real good time!"
S "I would really like that Genji…"
hide Suetsumuhana
scene black
jump datenight

label datenight:
scene dorm_night
"Tonight’s the night that I take Suetsumuhana out! I never thought that I would actually date a Mudd girl."
G "And there’s the door!"
G "My yellow blossom I must say you look amazing tonight!"
show Suetsumuhana
S "Thank you Genji…"
S "You know I never thought that you would even be interested in me…"
S "Everyone always told me that you were such a player, and that you could have any girl that you wanted."
S "I guess I never thought that I would be that girl!"
G "Well think again my blossom."
G "I’ve yet to meet a more intriguing girl than you."
G "So shall we get going? I have quite the night planned!"
G "I’m taking you out to the village for dinner!"
S "That sounds wonderful Genji…"
hide Suetsumuhana
scene black
jump villagedate

label villagedate:
scene picnic
"As we get seated at an outdoor table I can’t help but notice that this is the happiest I have ever seen Suetsumuhana"
G "My dear little blossom, you don’t even understand how long I have waited to take you out like this."
show Suetsumuhana
S "Genji we literally met just a few days ago!"
G "With you, time is not even a concept. An hour with you is equivalent to a lifetime of happiness!"
G "I only wish that I do get the pleasure of more time in your company…"
S "Genji I wish for that too…"
S "But before you agree to that I think there’s something you should know…"
S "I haven’t trusted anyone here with my past… But I think it’s about time that I let my guard down."
"I can’t believe it! Does this mean I am the first that gets to unravel the mystery of Suetsumuhana?"
"To no Chujo is going to lose his mind out of jealousy…"
show Suetsumuhana
S "You see, before my father passed away I was at the height of society."
S "If you can believe it I spent most of my life attending parties and other social functions. That was my entire life."
S "But then my father died, leaving me alone with no connections left."
S "I must admit I went a little crazy…"
S "I locked myself in the apartment for two years and refused to speak to anyone."
S "Coming to Mudd was an incredibly difficult decision for me. Fact of the matter is I forgot how to socialize entirely."
S "So I focused on my studies. But I never quite got back to the way I once was. I’m still a girl who literally locked herself up for years."
S "So yes. I have a bit of a reputation for being crazy. I hope you don’t judge me too harshly for it."
"So this is her big secret?"
"That just makes her all the more interesting!"
"This means that I, Genji, am the first man to take her interest in years!"
"Yes… This is very interesting…"
G "My little yellow blossom do you honestly think that I would feel any differently about you?"
G "I’ve just learned more about you and that was my goal after all, wasn’t it?"
"I realize that Suetsumuhana is a very complex girl. But she’s a girl I just keep wanting to figure out…"
"I know that this date is just the beginning of something wonderful…"
"I believe that this counts as a successful courtship of Suetsumuhana."
"The real question is whether I still wish to complete my challenge or if I am happy enough to keep unraveling the mystery that is Suetsumuhana…"
hide Suetsumuhana
scene black
".: GOOD END :."

jump room




