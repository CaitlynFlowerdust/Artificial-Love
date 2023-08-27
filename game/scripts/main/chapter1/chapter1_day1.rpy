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