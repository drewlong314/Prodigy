screen point_and_click():
    imagebutton:
        idle "left_box.png"
        xalign 0.3
        yalign 0.5
        action Jump("left_box")
    imagebutton:
        idle "right_box.png"
        xalign 0.8
        yalign 0.5
        action Jump('right_box')


transform shake(rate=0.090):
    linear rate xoffset 2 yoffset -6
    linear rate xoffset -2.8 yoffset -2
    linear rate xoffset 2.8 yoffset -2
    linear rate xoffset -2 yoffset -6
    linear rate xoffset +0 yoffset +0
    repeat


transform middle:
    xalign 0.5
    yalign 0.5

define j = Character("June")

label start:

    # Scene 1

    scene black
    queue music "audio/Prodigy OST Loop.ogg" loop volume 0.1

    "{i}Ah, another day of classes has finally come to an end.{/i}"
    "{i}Now time to go home and{/i}"
    "{i}Oops!{/i}"
    "{i}I forgot my Student ID in the art studio!{/i}"
    "{i}No biggie, as long as I grab it real quick, no one will notice.{/i}"

    scene bg main
    show june neutral

    "{i}Oh! There's someone here!{/i}"
    "{i}Oh. She's here.{/i}"

    show june surprised

    j "...hello."
    "{i}June Goldeen. Objectively the best artist in class, rumored to have been a child prodigy. She barely talks outside of critique, and when she does-it's brutal. Looks like she's painting, I better get out of here as soon as possible before she decides to dig into me.{/i}"

    menu:

        "…hi.":
            jump find_id

        "hello…have you seen an ID card around here?":
            jump ask_for_id

    # CHOICE 1
    label find_id:
        show june neutral
        "{i}She turns away and continues working. I really have to find that ID!{/i}"
        "{i}Let's see, I was sitting over there, so maybe it's…{/i}"
        hide june
        
        # Point and Click
        call screen point_and_click
        label left_box:
            "Let's see…No, not here"
            call screen point_and_click
        label right_box:
            show prodigy card at middle
        "{i}Yes!! I'd be dead if I lost this!{/i}"
        hide prodigy card
        jump scene_2

    # CHOICE 2
    label ask_for_id:
        show june shocked
        j "You lost your ID? Is it this one?"
        hide june
        # Little ID card appears on screen w/ sparkly sound effect
        show prodigy card at middle
        "Whew! Thanks, June."
        hide prodigy
        show june content
        jump scene_2

    label scene_2:
        show june neutral
        "{i}I really want to leave…but critique is tomorrow, and I want to see what she's busy with. Maybe I can give her a taste of her own medicine if I get extra time to think about it.{/i}"
        j "You're in my class, right?"
        "Yeah, I sit right next to you"
        "{i}Has she really not noticed me the entire semester?! That's just cruel!{/i}"
        "{i}Yeah, this critique is a long time coming.{/i}"
        show june nervous
        j "Oh"
        j "I'm sorry, I don't always pay attention to what's going on around me. Or, the people around me. That's my mistake, please don't take it personally. "
        "{i}She seems…weirdly genuine. It's almost like she actually feels bad about not recognizing me.{/i}"
        "So, what are you up to?"
        show june neutral
        j "Just some finishing touches. Critique is tomorrow and I haven't finished my piece."

        # Scene 2
        show june nervous
        j "Don't tell anyone, but this assignment is giving me a headache."

        menu:

            "Hm? I thought The Amazing June didn't struggle with stuff like this.":
                jump first_ending

            "Now I have to tell everyone":
                jump second_ending

        # CHOICE 3
        label first_ending:

            show june neutral
            j "Normally I don't. "
            j "but, this is different"
            "Different how?"
            j "I don't know. It's like I'll never finish this piece! I can't decide when enough is enough, and now I don't know if it looks presentable"
            "Can I see?"
            "{i}If I can just see what she's doing, then maybe I'll be able to really give it to her right now!{/i}"
            show june shocked
            j "..."
            show june worried
            j "..."
            show june neutral
            j "Fine, here it is. Just remember, I'm trusting you with this, okay? Artist to Artist"
            show june neutral at left
            "{i}It's.{/i}"
            "{i}Wow.{/i}"
            "{i}Incredible, typical.{/i}"
            "{i}It's an abstract piece, full of paint splatters and organic shape. I'd never say it outloud, but her work always finds a way of entrancing me. Her linework, the techniques, even the movement of her art is so well encapsulated that each piece is its own world.{/i}"
            "{i}I try to find something to critique, anything that would give me a leg up tomorrow, but my jealousy is starting to fizzle out into-what is this?{/i}"
            "{i}Adoration? Ew.{/i}"
            show june nervous
            j "Are you…okay? You've been quiet for a while"
            j "I know it's not my best work, I've done better. I can do better."

            menu:

                "What are you talking about? This is great!":
                    jump this_is_great

                "Well, there is one little thing":
                    jump one_little_thing

            label this_is_great:
                show june neutral
                j "Yeah, but is it good, though?"
                "What do you mean?"
                j "Maybe you were the wrong person to ask about this."
                show june shocked
                j "Oh! Was that rude? I'm sorry-I just mean that I need actual feedback. Telling me it's great doesn't fix the problem, remember?"
                show june neutral
                j "I know there's a problem with it, but she won't tell me what it is"
                "She?"
                jump finish_first

            label one_little_thing:
                j "Go on"
                "This is an abstract piece, so why are you worrying about it so much?"
                "Abstraction is about, I don't know, fleeting emotions and just doing what feels right in the moment."
                "You're overthinking it"
                show june sad
                j "Thank you. I really appreciate your feedback. Though, I do have good reason to be 'over thinking'. "
                jump finish_first

            label finish_first:
                j "…My mom is an art collector, so of course she looks at all my paintings. I brought this one to her yesterday after class,"
                show june sad
                j "but she keeps saying there's something missing…and that if I can't figure it out, maybe all my paintings are 'missing something'."
                "That's a kind of messed up thing for your mom to say"
                j "Well, she's my mom, and she's the whole reason I was a child prodigy. If she says my art isn't good enough,"
                show june nervous
                j "…"
                show june worried
                j "I…um…If my art isn't good enough, then"
                show june tearing up
                "Hey, hey, are you okay?"
                j "I, yeah, I'm just having a hard time with this p-painting, but I shouldn't be! I'm June Goldeen! The prodigy! And if I can't even do this simple assignment, then!"
                "{i}Crap, now I really feel about trying to bring her down. June clearly has had a lot on her plate, for probably way longer than I can imagine.{/i}"
                "Woah, let's breathe, okay?"
                "{i}I place my hand on hers, and she's trembling. She takes in a shaky breath, and I feel the tension lessen with each frightened exhale.{/i}"
                show june worried
                "{i}Seeing her like this drains me of all malice, all jealousy. Without warning, something comes over me, and it's like I'm seeing her for the first time again.{/i}"
                "June, I'm going to say this…because I get the feeling your mom hasn't told you, but"
                "You can struggle."
                "You can be a good artist and still have a hard time."
                "You're a human person, with limits and needs, not just a prodigy. You're allowed to take breaks, and you're allowed to just…be. You don't have to be the best."
                show june nervous
                j "Thank you, that's sweet, really."
                show june content at center
                j "You know what? I think it's finished."
                return
                # Ending 1 Complete

        label second_ending:

            show june worried
            j "I can't tell if you're joking"
            "Maybe. Maybe not."
            show june shocked
            j "No, please!"
            show june shocked at shake, center
            j "If everyone knew… that I couldn't handle this, my reputation would be…"
            show june sad at center
            j "Please. Keep this a secret, you have no idea what's at stake! I shouldn't have told you."
            "Relax, I was just kidding! I'm not going to ruin the illusion for everybody."
            show june shocked
            j "What…'The illusion'? I'm not lying to people by trying hard! I'm a good artist! I…I think…this is just a difficult assignment. I'll be able to finish it!"
            show june mad
            j "I really shouldn't have said anything."
            j "If you have nothing else to do but waste my time, get out."

    return
