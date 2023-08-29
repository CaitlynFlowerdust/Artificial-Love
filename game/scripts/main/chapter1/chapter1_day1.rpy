label chapter1_start:
    scene white
    play music music_intrareality loop fadein 1.0
    with dissolve
    centered "{color=#000}Welcome to IntraReality!{/color}"
    centered "{color=#000}We are the leading company in Artificial Intelligence development.{/color}"
    centered "{color=#000}Ever since our founding in 3015, we've been working hard to produce the greatest breakthroughs in the industry.{/color}"
    centered "{color=#000}And guess what? We got one!{/color}"
    centered "{color=#000}In 3063, we created a new system called Axelium.{/color}"
    centered "{color=#000}This system essentially made our androids capable of doing anything.{/color}"
    centered "{color=#000}However, we put dampeners on any models with Axelium installed. If we didn't do that, the possibility of sentience would be possible.{/color}"
    centered "{color=#000}Indeed, being capable of \"anything\" comes with a price.{/color}"
    centered "{color=#000}Anyways!{/color}"
    centered "{color=#000}I am sure you're excited for your first day at IntraReality. We have so much in store for you.{/color}"
    centered "{color=#000}Your job? You'll find out soon enough.{/color}"
    centered "{color=#000}Not everyone gets hired here, you know. So enjoy it!{/color}"
    centered "{color=#000}Good luck, [mc_name], and see you soon!{/color}"

    scene black
    stop music fadeout 1.0
    with fade
    pause 1.5
    play sound [sfx_alarm_beep, "<silence 1.0>"] loop
    "Ugh..."
    "What's that noise...?"
    "I slowly awaken."
    scene bg bedroom_day with dissolve
    "I'm in my bedroom. Of course."
    mc "Array, turn off the alarm!"
    stop sound
    "The beeping finally stopped."
    array "Good morning, [mc_name]!"
    "The bubbly voice of Array rings out."
    mc "Mm... Morning..."
    array "Not so happy to be awake?"
    mc "Well yea... I have school..."
    array "You'll do great!"
    mc "Sigh..."
    "I sat up, stretching."
    mc "Thanks, Array."
    "With that, I forced myself out of bed and headed to the bathroom."
    scene bg bathroom
    with fade
    play sound sfx_fillbathtub noloop
    "I ran the bath and began getting undressed."
    "Staring at the person in the mirror..."
    "I haven't felt like {i}myself{/i} for days now."
    "Sometimes I wonder..."
    "What would it be like to have a new life..."
    stop sound fadeout 1.0
    "With the bath filled, I step in."
    "Allowing myself to relax a little."
    "The warm water laps around me, and it does feel nice."
    play sound sfx_notif1
    "I hear my phone beep."
    "What now...?"
    mc "Array, read the message!"
    array "You have: 1 new message."
    mc "Yea, yea, I said read it!"
    "Honestly..."
    array "New message. From: Unknown."
    "Oh God..."
    "A sense of dread stirs within me."
    array "The message reads as follows:"
    unk """
    Oi, [mc_name]. I want ya to listen very carefully to what I'm about to say.
    Do NOT go to IntraReality.
    I may sound crazy but, hear me out, {i}please{/i}.
    There's been an incident. A bad one.
    It's not safe t-{nw}
    """
    mc "Array, stop."
    array "Would you like me to discard the message?"
    mc "Yes please."
    array "Message discarded."
    "I groan, laying back down in the bath."
    "What a nuisance..."
    "Everyone's always like, \"Oh, don't go to IntraReality! Oh, it's dangerous!\""
    "Honestly, what bullshit..."
    array "I'm sorry but, it's almost time to leave, [mc_name]."
    "Oh, shit..."
    mc "Alright, alright."
    "I reluctantly exit the bath."
    play sound sfx_drainbathtub
    "Getting dressed into my new uniform, and tidying my hair, I look back to the mirror."
    "I look professional."
    mc "Alright. Let's do this."
    stop sound fadeout 1.5
    scene bg bedroom_day
    with fade
    mc "Array?"
    array "Yes?"
    mc "I'm leaving now. Make sure to lock the apartment when I go. And tidy up if you can."
    array "Yes, will do."
    mc "Goodbye."
    array "Have a nice day!"
    scene black
    with fade
    play sound sfx_newday
    centered "{b}{u}Day 1 - Monday 1st May"
    scene bg office_day
    with fade
    play music music_mc_office loop
    "I push open the office door."
    mc "Phew, made it..."
    "I take a look around. The room is clean and neatly decorated."
    "My eyes land on a solitary figure standing by the window."
    show AM1RA still_eyeclose_neutral at left
    with dissolve
    "I approach."
    mc "Uhm, excuse me?"
    show AM1RA still_neutral
    with dissolve
    "She looks at me."
    unk "Yes?"
    "Her stare is cold. It makes me nervous."
    mc "U-Um-"
    unk "You're the new employee, correct?"
    mc "Y-Yes..."
    unk "Good."
    unk "Welcome to IntraReality."
    mc "Thank you..."
    "I don't know why she makes me feel so jittery."
    "I just couldn't help it."
    "She doesn't look... alive..."
    show AM1RA at center with move
    unk "Allow me to introduce myself."
    am "My name is AM1RA."
    mc "AM1RA?"
    am "Yes."
    am "Arbitrary Model 1 Response Android."
    mc "O-Oh..."
    "So she's an android..."
    "That explains the lack of emotion."
    "And why I felt so damn powerless."
    mc "So, uhm, they have androids working inside the company too?"
    am "Correct."
    mc "Wow..."
    show AM1RA still_eyeclose_neutral
    am "You weren't told anything, were you."
    mc "U-Uhm, no..."
    am "What a nuisance..."
    mc "I-I-I'm so sorry!!!"
    show AM1RA still_neutral
    am "I didn't mean you."
    am "We're the ones at fault for not properly informing you."
    mc "O-Oh..."
    "This is... so awkward..."
    "What do I do...?"
    stop music
    scene black
    with vpunch
    "Suddenly, everything went dark."
    mc "A-AM1RA?!"
    am "I'm here."
    "I hear shuffling."
    am "It appears there has been a power outage."
    mc "Y-Yeah, I can see that..."
    "As if things couldn't get any worse..."
    # need an electric flash and sfx here
    "A sudden flash of light blinded me for a moment."
    "The smell of smoke filled the air."
    mc "{i}Oh shit...{/i}"