define config.new_translate_order = True
define config.developer = True



image bathroom = "bathroom.png"
image office= "office.png"
image blank = "blank.png"
image park = "park.png"
image ok = "ok.png"
image ko = "ko.png"
image game_over = "game_over.png"
image desk both = "both_desks.png"
image desk left = "left_desk.png"
image desk right = "right_desk.png"
image irene naked = "irene_naked.png"
image marzio naked = "marzio_naked.png"
image irene dressed = "irene.png"
image marzio dressed = "marzio.png"
image irene_bijoux bathroom = "irene_bijoux.png"
image marzio_bijoux bathroom = "marzio_bijoux.png"
image irene_bijoux office = "irene_bijoux_office.png"
image marzio_bijoux office = "marzio_bijoux_office.png"
style monitor is text:
    font "fonts/telegrama_render.otf"
    text_align 0.0
style small_monitor:
    min_width 333
style left_small_monitor:
    xalign 0.15
style right_small_monitor:
    xalign 0.84
style big_monitor:
    xalign 0.5
    yalign 0.25
    min_width 400
image left_pc_text_0 = renpy.ParameterizedText(yalign=0.38, style='left_small_monitor') #UNUSED
image left_pc_text_1 = renpy.ParameterizedText(yalign=0.41, style='left_small_monitor') #UNUSED
image left_pc_text_2 = renpy.ParameterizedText(yalign=0.44, style='left_small_monitor') #UNUSED
image left_pc_text_3 = renpy.ParameterizedText(yalign=0.47, style='left_small_monitor')
image left_pc_text_4 = renpy.ParameterizedText(yalign=0.50, style='left_small_monitor')
image left_pc_text_5 = renpy.ParameterizedText(yalign=0.53, style='left_small_monitor')
image left_pc_text_6 = renpy.ParameterizedText(yalign=0.56, style='left_small_monitor')
image left_pc_text_7 = renpy.ParameterizedText(yalign=0.59, style='left_small_monitor')
image left_pc_text_8 = renpy.ParameterizedText(yalign=0.62, style='left_small_monitor')
image left_pc_text_9 = renpy.ParameterizedText(yalign=0.65, style='left_small_monitor')
image left_pc_text_10 = renpy.ParameterizedText(yalign=0.68, style='left_small_monitor')
image left_pc_text_11 = renpy.ParameterizedText(yalign=0.71, style='left_small_monitor')
image left_pc_text_12 = renpy.ParameterizedText(yalign=0.74, style='left_small_monitor')
image left_pc_text_last = renpy.ParameterizedText(yalign=0.77, style='left_small_monitor', slow_cps=20)
image right_pc_text_0 = renpy.ParameterizedText(yalign=0.38, style='right_small_monitor') #UNUSED
image right_pc_text_1 = renpy.ParameterizedText(yalign=0.41, style='right_small_monitor') #UNUSED
image right_pc_text_2 = renpy.ParameterizedText(yalign=0.44, style='right_small_monitor') #UNUSED
image right_pc_text_3 = renpy.ParameterizedText(yalign=0.47, style='right_small_monitor')
image right_pc_text_4 = renpy.ParameterizedText(yalign=0.50, style='right_small_monitor')
image right_pc_text_5 = renpy.ParameterizedText(yalign=0.53, style='right_small_monitor')
image right_pc_text_6 = renpy.ParameterizedText(yalign=0.56, style='right_small_monitor')
image right_pc_text_7 = renpy.ParameterizedText(yalign=0.59, style='right_small_monitor')
image right_pc_text_8 = renpy.ParameterizedText(yalign=0.62, style='right_small_monitor')
image right_pc_text_9 = renpy.ParameterizedText(yalign=0.65, style='right_small_monitor')
image right_pc_text_10 = renpy.ParameterizedText(yalign=0.68, style='right_small_monitor')
image right_pc_text_11 = renpy.ParameterizedText(yalign=0.71, style='right_small_monitor')
image right_pc_text_12 = renpy.ParameterizedText(yalign=0.74, style='right_small_monitor')
image right_pc_text_last = renpy.ParameterizedText(yalign=0.77, style='right_small_monitor', slow_cps=20)
image propaganda_display = "title.jpg"
image propaganda_text = renpy.ParameterizedText(style='big_monitor', slow_cps=50)
# Dichiara i personaggi usati in questo gioco
define irene = Character(_('Irene'), color='#ff8888')
define marzio = Character(_('Martin'), color='#8888ff')
define resp = Character(_('HR Recruiter'), color='#8888ff')
define segr = Character(_('Secretary'), color='#ff8888')

init:
    $ left_pc_text_content = ("", "", "", "", "", "", "", "", "", "", "", "", "", "")
    $ right_pc_text_content = ("", "", "", "", "", "", "", "", "", "", "", "", "", "")
    $ bijoux = False
    $ marzio_score = 6
    $ irene_score = 6
    $ renpy.music.register_channel(name='left_sfx', mixer=None, loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False)
    $ renpy.music.set_pan(pan=-1, delay=0, channel='left_sfx')
    $ renpy.music.register_channel(name='right_sfx', mixer=None, loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False)
    $ renpy.music.set_pan(pan=+1, delay=0, channel='right_sfx')

# Inizio del gioco
label start:    
    scene bathroom
    play music "audio/bathroom.ogg" loop fadeout 1.0 fadein 1.0
    #show blanket at left
    #show mirror at topright
    show marzio naked at left
    show irene naked at right
    pause 1.5
    marzio "Stay calm. Deep breaths. Be confident."
    irene "Stay calm. Deep breaths. Be confident."
    menu:
        "{i}I'll wear my jewellery...{/i}":
            jump use_bijoux
        "{i}...or I'd better not?{/i}":
            jump interview

label use_bijoux:
    $ bijoux = True
    show marzio_bijoux bathroom at left
    show irene_bijoux bathroom at right
    "{i}Ready to go.{/i}"
    jump interview

label interview:
    scene office
    queue music "audio/office.ogg" loop
    show marzio dressed at left
    show irene dressed at right
    if bijoux:
        show marzio_bijoux office at left
        show irene_bijoux office at right
    show desk both
    with dissolve

    call type_left(_("BUSINESS SERVICE Inc.{#m}")) from _call_type_left
    call type_left(_("====================={#m}")) from _call_type_left_1
    call type_left(_("{#m}")) from _call_type_left_2

    call type_right(_("STUDIO TEAM Ltd.{#f}")) from _call_type_right
    call type_right(_("****************{#f}")) from _call_type_right_1
    call type_right(_("{#f}")) from _call_type_right_2

    resp "Hello."

    call type_left(_("9am interview{#m}")) from _call_type_left_3
    call type_right(_("9am interview{#f}")) from _call_type_right_3

    pause 1.0
    resp "Right on time!"

    call type_left(_("On time{#m}")) from _call_type_left_4
    call type_right(_("On time{#f}")) from _call_type_right_4

    pause 1.0
    resp "Being on time for an interview is a quality I appreciate."

    call type_left(_("Martin Smith{#m}")) from _call_type_left_5
    call type_right(_("Irene Wilson{#f}")) from _call_type_right_5

    pause 1.0
    resp "I've read your CV carefully."

    if bijoux:
        call type_left_score(_("Weird look (gay?){#m}"), -1) from _call_type_left_6
        call type_right_score(_("Elegant, pretty{#f}"), +1) from _call_type_right_6
    else:
        call type_left_score(_("Good looks{#m}"), +1) from _call_type_left_7
        call type_right_score(_("Pretty but sloppy{#f}"), -1) from _call_type_right_7
    pause 1.0
    resp "Let's start the interview."

    menu:
        "Yes.":
            resp "How would you describe yourself?"
    menu:
        "As a competent, ambitious professional.":
            call type_left_score(_("Resolute{#m}"), +1) from _call_type_left_8
            call type_right(_("Arrogant{#f}")) from _call_type_right_8
            pause 1.0
            resp "Hm, fine."
        "A discreet and diligent person.":
            call type_right_score(_("Anxious{#f}"), -1) from _call_type_right_9
            pause 1.0
            resp "I see."
        "What do you mean? I don't get it.":
            call type_left_score(_("Fretful{#m}"), -1) from _call_type_left_9
            call type_right_score(_("Fretful{#f}"), -1) from _call_type_right_10
            pause 1.0
            resp "It doesn't matter, it was just a warm-up question."

    resp "Did you check on our website what our core business is?"
    menu:
        "Of course. Business intelligence and maintenance functions.":
            resp "Not exactly."
        "Of course. B2B and B2C consultancy.":
            resp "We do that as well. But it's not the whole story."
        "I did, but I didn't fully understand.":
            resp "I'll explain."
    resp "Our mission is total customer satisfaction through just-in-time delivery of full-stack support based on state-of-the-art technology."

    menu:
        "I see.":
            resp "Have you got the necessary skills for the job you applied for?"
    menu:
        "Absolutely.":
            call type_left(_("Skilled{#m}")) from _call_type_left_10
            call type_right(_("Skilled{#f}")) from _call_type_right_11
        "I think so.":
            call type_left(_("Skilled?{#m}")) from _call_type_left_11
            call type_right(_("Skilled?{#f}")) from _call_type_right_12
        "No way...":
            call type_left_score(_("NOT skilled{#m}"), -1) from _call_type_left_12
            call type_right_score(_("NOT skilled{#f}"), -1) from _call_type_right_13
    resp "Hm."
    if marzio_score <= 3 or irene_score <= 3:
        jump catastrophe

    resp "How do you see yourself in 20 years?"
    menu:
        "On a Caribbean beach with a drink!":
            call type_left_score(_("Lazy arse{#m}"), -1) from _call_type_left_13
            call type_right_score(_("Kept woman{#f}"), -1) from _call_type_right_14
            pause 1.0
            resp "Good luck."
        "With an established career and a family.":
            call type_left_score(_("Work ethic{#m}"), +1) from _call_type_left_14
            call type_right_score(_("Pregnancy alert{#f}"), -1) from _call_type_right_15
            pause 1.0
        "Focused on my goals.":
            pass
        "I don't know...":
            resp "Predicting what life has in store for us is never easy."
    resp "Hm."
    if marzio_score <= 3 or irene_score <= 3:
        jump catastrophe

    resp "May I ask what your marital status is?"
    menu:
        "I'm planning to move in with my partner, then we'll see.":
            call type_left(_("Unwed so far{#m}")) from _call_type_left_15
            call type_right_score(_("Plans to marry?{#f}"), -1) from _call_type_right_16
            pause 1.0
        "Not having a job prevents me from thinking about marriage.":
            call type_left_score(_("Whiny{#m}"), -1) from _call_type_left_16
            call type_right_score(_("Plans to marry{#f}"), -2) from _call_type_right_17
            pause 1.0
        "I enjoy being single!":
            call type_left_score(_("No children{#m}"), +1) from _call_type_left_17
            call type_right_score(_("Spinster{#f}"), +1) from _call_type_right_18
            pause 1.0
        "Isn't this question a bit off topic?":
            call type_left_score(_("Reserved{#m}"), -1) from _call_type_left_18
            call type_right_score(_("Bolshy{#f}"), -2) from _call_type_right_19
            pause 0.5
            resp "It's standard procedure. But we can skip it if you mind."
    resp "Hm."
    if marzio_score <= 3 or irene_score <= 3:
        jump catastrophe

    resp "What's the salary you expect to earn?"
    menu:
        "Gross annual income?":
            resp "Yes."
    menu:
        "Say 20,000.":
            call type_left(_("GAI: 20K{#m}")) from _call_type_left_19
            call type_left_score(_("Desperate?{#m}"), -1) from _call_type_left_20
            call type_right(_("GAI: 20K{#f}")) from _call_type_right_20
            if marzio_score > 3:
                resp "Definitely feasible."
        "Say 30,000.":
            call type_left(_("GAI: 30K{#m}")) from _call_type_left_21
            call type_right(_("GAI: 30K{#f}")) from _call_type_right_21
            call type_right_score(_("Asks for too much{#f}"), -1) from _call_type_right_22
    resp "Hm."
    if marzio_score <= 3 or irene_score <= 3:
        jump catastrophe

    resp "I'm being honest here: I'm not sure we're going to hire you, but we'll let you know."
    menu:
        "Thank you. See you soon, then, hopefully.":
            pass
        "I was thinking... Fancy a drink after work?":
            resp "Uhm. Thanks for your invitation, but I guess my wife expects me to be home for dinner pretty early."
            if bijoux:
                call type_left_score(_("GAY{#m}"), -2) from _call_type_left_22
            else:
                call type_left_score(_("Intrusive{#m}"), -1) from _call_type_left_23
            call type_right_score(_("Slut{#f}"), +1) from _call_type_right_23
            pause 0.5
    hide marzio
    hide marzio_bijoux
    hide irene
    hide irene_bijoux
    resp "Goodbye."
    jump scoring

label scoring:
    pause 1.0
    if marzio_score <4:
        call type_left(_("FINAL GRADE: F{#m}")) from _call_type_left_24
        pause 1.0
        call type_left_score(_("--DON'T HIRE--{#m}"), -0.1) from _call_type_left_25
    elif marzio_score <5:
        call type_left(_("FINAL GRADE: D{#m}")) from _call_type_left_26
        pause 1.0
        call type_left_score(_("--DON'T HIRE--{#m}"), -0.1) from _call_type_left_27
    elif marzio_score <6:
        call type_left(_("FINAL GRADE: D+{#m}")) from _call_type_left_28
        pause 1.0
        call type_left_score(_("--DON'T HIRE--{#m}"), -0.1) from _call_type_left_29
    elif marzio_score <7:
        call type_left(_("FINAL GRADE: C+{#m}")) from _call_type_left_30
        pause 1.0
        call type_left(_("--ON HOLD--{#m}")) from _call_type_left_31
    elif marzio_score <8:
        call type_left(_("FINAL GRADE: B{#m}")) from _call_type_left_32
        pause 1.0
        call type_left_score(_("--HIRE!--{#m}"), +0.1) from _call_type_left_33
    elif marzio_score <9:
        call type_left(_("FINAL GRADE: B+{#m}")) from _call_type_left_34
        pause 1.0
        call type_left_score(_("--HIRE!--{#m}"), +0.1) from _call_type_left_35
    elif marzio_score <10:
        call type_left(_("FINAL GRADE: A-{#m}")) from _call_type_left_36
        pause 1.0
        call type_left_score(_("--BRAVO! HIRE NOW--{#m}"), +0.1) from _call_type_left_37
    else:
        call type_left(_("FINAL GRADE: A{#m}")) from _call_type_left_38
        pause 1.0
        call type_left_score(_("--PERFECT! HIRE NOW--{#m}"), +0.1) from _call_type_left_39

    pause 1.0
    if irene_score <4:
        call type_right(_("FINAL GRADE: F{#f}")) from _call_type_right_24
        pause 1.0
        call type_right_score(_("--DON'T HIRE--{#f}"), -0.1) from _call_type_right_25
    elif irene_score <5:
        call type_right(_("FINAL GRADE: D-{#f}")) from _call_type_right_26
        pause 1.0
        call type_right_score(_("--DON'T HIRE--{#f}"), -0.1) from _call_type_right_27
    elif irene_score <6:
        call type_right(_("FINAL GRADE: D{#f}")) from _call_type_right_28
        pause 1.0
        call type_right_score(_("--DON'T HIRE--{#f}"), -0.1) from _call_type_right_29
    else:
        call type_right(_("FINAL GRADE: C-{#f}")) from _call_type_right_30
        pause 1.0
        call type_right_score(_("--DON'T HIRE--{#f}"), -0.1) from _call_type_right_31

    pause 1.0

    if marzio_score <6:
        resp "Miss Wong, please let the next candidate in."
        scene blank
        play music "audio/gameover.ogg" fadeout 1.0 fadein 1.0 noloop
        show game_over at center
        with dissolve
        segr "Certainly, Mr White."
        jump propaganda

    resp "Miss Wong, would you mind making a cup of tea?"
    segr "Certainly, Mr White."
    jump ending

label ending:
    scene park with dissolve
    play music "audio/park.ogg" fadeout 1.0 fadein 1.0 loop
    "{i}We have an appointment at the park.{/i}"
    if bijoux:
        #show irene dressed at right
        #show irene_bijoux at right
        #with dissolve
        #show marzio dressed at center
        #show marzio_bijoux at center
        #with dissolve
        marzio "You're wearing the earrings I gave you!"
    #else:
        #show irene dressed at right
        #with dissolve
        #show marzio dressed at center
        #with dissolve
    irene "Hello darling."
    marzio "Hi, babe."
    irene "How was your interview?"
    if marzio_score <7:
        marzio "Not great, but I reckon they'll still hire me."
    else:
        marzio "Good! I'm sure the job is mine!"
    marzio "And yours?"
    irene "Bad. They called me while I was coming here to tell me they're not taking me."
    marzio "..."
    marzio "I'm so sorry."
    irene "Me too."
    marzio "Never mind. You have me, I can work for both of us."
    show game_over at center with dissolve
    pause 1.0
    irene "Yeah. I have you."
    jump propaganda

label catastrophe:
    if marzio_score <=3:
        scene blank
        play music "audio/gameover.ogg" fadeout 1.0 fadein 1.0 noloop
        show marzio dressed at left
        if bijoux:
            show marzio_bijoux office at left
        show desk left
        call type_left_score(_("--SENT AWAY--{#m}"), -0.1) from _call_type_left_40
        pause 1.5
        resp "I think we can stop here. Thanks anyway."
        hide marzio
        hide marzio_bijoux
        show game_over at right with dissolve
    else:
        scene blank
        play music "audio/gameover.ogg" fadeout 1.0 fadein 1.0 noloop
        show irene dressed at right
        if bijoux:
            show irene_bijoux office at right
        show desk right
        call type_right_score(_("--SENT AWAY--{#f}"), -0.1) from _call_type_right_32
        pause 1.5
        resp "I think we can stop here. Thanks anyway."
        hide irene
        hide irene_bijoux
        show game_over at left with dissolve
    pause 1.0
    resp "Miss Wong, please let the next candidate in."
    segr "Certainly, Mr White."
    jump propaganda

label type_left(new_content):
    call type_left_score(new_content, 0)
    return

label type_left_score(new_content, marzio_score_change):
    $ left_pc_text_content = left_pc_text_content[1:] + (new_content,)
    # show left_pc_text_0 (left_pc_text_content[0])
    # show left_pc_text_1 (left_pc_text_content[1])
    # show left_pc_text_2 (left_pc_text_content[2])
    show left_pc_text_3 (left_pc_text_content[3])
    show left_pc_text_4 (left_pc_text_content[4])
    show left_pc_text_5 (left_pc_text_content[5])
    show left_pc_text_6 (left_pc_text_content[6])
    show left_pc_text_7 (left_pc_text_content[7])
    show left_pc_text_8 (left_pc_text_content[8])
    show left_pc_text_9 (left_pc_text_content[9])
    show left_pc_text_10 (left_pc_text_content[10])
    show left_pc_text_11 (left_pc_text_content[11])
    show left_pc_text_12 (left_pc_text_content[12])
    show left_pc_text_last ("[new_content!t]_")
    call score_left(marzio_score_change)
    return

label type_right(new_content):
    call type_right_score(new_content, 0)
    return

label type_right_score(new_content, irene_score_change):
    $ right_pc_text_content = right_pc_text_content[1:] + (new_content,)
    # show right_pc_text_0 (right_pc_text_content[0])
    # show right_pc_text_1 (right_pc_text_content[1])
    # show right_pc_text_2 (right_pc_text_content[2])
    show right_pc_text_3 (right_pc_text_content[3])
    show right_pc_text_4 (right_pc_text_content[4])
    show right_pc_text_5 (right_pc_text_content[5])
    show right_pc_text_6 (right_pc_text_content[6])
    show right_pc_text_7 (right_pc_text_content[7])
    show right_pc_text_8 (right_pc_text_content[8])
    show right_pc_text_9 (right_pc_text_content[9])
    show right_pc_text_10 (right_pc_text_content[10])
    show right_pc_text_11 (right_pc_text_content[11])
    show right_pc_text_12 (right_pc_text_content[12])
    show right_pc_text_last ("[new_content!t]_")
    call score_right(irene_score_change)
    return

label score_left(score_change):
    $ renpy.music.set_pan(pan=-0.8, delay=0, channel='left_sfx')
    $ marzio_score += score_change
    if score_change > 0:
        play left_sfx "audio/ok.wav" noloop
        show ok:
            xalign 0.1
            yalign 0.5
            linear 0.7 yalign 0.35
        hide ok with dissolve
    if score_change < 0:
        play left_sfx "audio/ko.wav" noloop
        show ko:
            xalign 0.1
            yalign 0.5
            linear 0.7 yalign 0.35
        hide ko with dissolve
    return


label score_right(score_change):
    $ renpy.music.set_pan(pan=+0.8, delay=0, channel='right_sfx')
    $ irene_score += score_change
    if score_change > 0:
        play right_sfx "audio/ok.wav" noloop
        show ok:
            xalign 0.9
            yalign 0.5
            linear 0.7 yalign 0.35
        hide ok with dissolve
    if score_change < 0:
        play right_sfx "audio/ko.wav" noloop
        show ko:
            xalign 0.9
            yalign 0.5
            linear 0.7 yalign 0.35
        hide ko with dissolve
    return

label stats:
    call propaganda
    menu:
        "Enough.":
            return
        "Tell me another random fact.":
            jump stats
        "I can't believe it! Give me your sources!":
            "Find them at {a=http://maurovanetti.itch.io/2i}maurovanetti.itch.io/2i{/a}, my friend."
            return

label propaganda:
    stop music fadeout 2.0
    play music "audio/stat.ogg" noloop
    scene propaganda_display with dissolve
    $ factoid = renpy.random.choice([
        _(
        "71% of entrepreneurs in Europe\n"
        "are men.\n\n"
        "(2012 data)"),
        _(
        "In average, in the USA women who\n"
        "work full-time are paid 21% less\n"
        "than men.\n\n"
        "(2014 data)"),
        _(
        "4/5 of EU workers work in\n"
        "segregated occupations, i.e.\n"
        "in which one sex has less than\n"
        "40% of the jobs and the other\n"
        "one more than 60%.\n\n"
        "(2014 data)"),
        _(
        "During her active lifetime, the\n"
        "average woman in the EU earns\n"
        "41% less than the average man.\n\n"
        "(2012 data)"),
        _(
        "On a world scale, the average\n"
        "annual earnings are $11,000 for\n"
        "women and $21,000 for men.\n\n"
        "(2015 data)"),
        _(
        "The employment rate in the EU is\n"
        "11% higher for men compared to\n"
        "women.\n\n"
        "(2013 data)"),
        _(
        "Gross earnings for each hour of\n"
        "work in the EU is 16% lower for\n"
        "women compared to men.\n\n"
        "(2013 data)"),
        _(
        "During their lifetime, 3.4% of\n"
        "women in Italy are checked for\n"
        "sexual availability at hiring\n"
        "time and the same amount are\n"
        "sexually blackmailed in the\n"
        "workplace.\n\n"
        "(2009 survey)"),
        _(
        "1 in 5 UK mothers felt harassed\n"
        "or criticised at work because of\n"
        "her pregnancy. 1 in 9 was forced\n"
        "to leave the job for being\n"
        "pregnant.\n\n"
        "(2015 survey)"),
        _(
        "1 in 5 UK mothers felt harassed\n"
        "or criticised at work because of\n"
        "her pregnancy. 1 in 9 was forced\n"
        "to leave the job for being\n"
        "pregnant.\n\n"
        "(2015 survey)"),
        _(
        "In most European countries,\n"
        "female workers employed in the\n"
        "public sector enjoy a narrower\n"
        "pay gap. The gender pay gap in\n"
        "the private sector is 6% wider\n"
        "in the UK, 9% wider in Italy,\n"
        "17% wider in Belgium.\n\n"
        "(2013 data)"),
        _(
        "At any level of education, US\n"
        "women earn less than their male\n"
        "counterparts. Education makes\n"
        "women earn more but does not\n"
        "fill the gender gap.\n\n"
        "(2014 data)"),
        _(
        "If the gender gap is not\n"
        "narrowed in the next years, the\n"
        "average US working woman would\n"
        "have lost over 430,000$\n"
        "compared to the average man\n"
        "when she is 65.\n\n"
        "(2012 data)")
        ])
    show propaganda_text (factoid)
    $ renpy.pause()
    return
