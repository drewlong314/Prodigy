define j = Character("June")

label start:

    # Scene 1
    
    scene black

    "Ah, another day of classes has finally come to an end."
    "Now time to go home and"
    "Oops!"
    "I forgot my Student ID in the art studio!"
    "No biggie, as long as I grab it real quick, no one will notice."

    # Main background + June in center of screen. June neutral sprite.


    "Oh! There's someone here!"
    "Oh. She's here."

    # June surprised sprite

    j "...hello."
    "June Goldeen. Objectively the best artist in class, rumored to have been a child prodigy. She barely talks outside of critique, and when she does-it's brutal. Looks like she's painting, I better get out of here as soon as possible before she decides to dig into me."

    menu:

        "…hi.":
            jump find_id

        "hello…have you seen an ID card around here?":
            jump ask_for_id

    # CHOICE 1
    label find_id:
        # June neutral expression
        "She turns away and continues working. I really have to find that ID!"
        "Let's see, I was sitting over there, so maybe it's…"

            # CHOICE 2/ Point and Click
            # Box 1:Let's see…No, not here
            # Box 2:Little ID card appears on screen w/ sparkly sound effect
        "Yes!! I'd be dead if I lost this!"

    # CHOICE 2
    label ask_for_id:
        # June shocked sprite
        j "You lost your ID? Is it this one?"
        # Little ID card appears on screen w/ sparkly sound effect
        "Whew! Thanks, June."
        # June content sprite

    "I really want to leave…but critique is tomorrow, and I want to see what she's busy with. Maybe I can give her a taste of her own medicine if I get extra time to think about it."
    j "You're in my class, right?"
    "Yeah, I sit right next to you"
    "Has she really not noticed me the entire semester?! That's just cruel!"
    "Yeah, this critique is a long time coming."
    # June nervous sprite
    j "Oh"
    j "I'm sorry, I don't always pay attention to what's going on around me. Or, the people around me. That's my mistake, please don't take it personally. "
    "She seems…weirdly genuine. It's almost like she actually feels bad about not recognizing me."
    "So, what are you up to?"
    # June neutral sprite
    j "Just some finishing touches. Critique is tomorrow and I haven't finished my piece."

    # Scene 2
    # June nervous sprite
    j "Don't tell anyone, but this assignment is giving me a headache."

    menu:

        "Hm? I thought The Amazing June didn't struggle with stuff like this.":
            jump first_ending

        "Now I have to tell everyone":
            jump second_ending

    # CHOICE 3
    label first_ending:

        # June neutral sprite
        j "Normally I don't. "
        j "but, this is different"
        "Different how?"
        j "I don't know. It's like I'll never finish this piece! I can't decide when enough is enough, and now I don't know if it looks presentable"
        "Can I see?"
        "If I can just see what she's doing, then maybe I'll be able to really give it to her right now!"
        # June shocked sprite
        j "..."
        # June  worried sprite
        j "..."
        # June neutral
        j "Fine, here it is. Just remember, I'm trusting you with this, okay? Artist to Artist"
        # June's sprite moves from center to left side
        "It's."
        "Wow."
        "Incredible, typical."
        "It's an abstract piece, full of paint splatters and organic shape. I'd never say it outloud, but her work always finds a way of entrancing me. Her linework, the techniques, even the movement of her art is so well encapsulated that each piece is its own world."
        "I try to find something to critique, anything that would give me a leg up tomorrow, but my jealousy is starting to fizzle out into-what is this?"
        "Adoration? Ew."
        # June nervous sprite
        j "Are you…okay? You've been quiet for a while"
        j "I know it's not my best work, I've done better. I can do better."

        menu:

            "What are you talking about? This is great!":
                jump this_is_great

            "Well, there is one little thing":
                jump one_little_thing

        label this_is_great:
            "What are you talking about? This is great!"
            # June neutral sprite
            j "Yeah, but is it good, though?"
            "What do you mean?"
            j "Maybe you were the wrong person to ask about this."
            # June shocked sprite
            j "Oh! Was that rude? I'm sorry-I just mean that I need actual feedback. Telling me it's great doesn't fix the problem, remember?"
            # June neutral sprite
            j "I know there's a problem with it, but she won't tell me what it is"
            "She?"
            jump finish_first

        label one_little_thing:
            "Well, there is one little thing"
            j "Go on"
            "This is an abstract piece, so why are you worrying about it so much?"
            "Abstraction is about, I don't know, fleeting emotions and just doing what feels right in the moment."
            "You're overthinking it"
            # June sad sprite
            j "Thank you. I really appreciate your feedback. Though, I do have good reason to be 'over thinking'. "
            jump finish_first

        label finish_first:
            j "…My mom is an art collector, so of course she looks at all my paintings. I brought this one to her yesterday after class,"
            # June sad sprite
            j "but she keeps saying there's something missing…and that if I can't figure it out, maybe all my paintings are 'missing something'."
            "That's a kind of messed up thing for your mom to say"
            j "Well, she's my mom, and she's the whole reason I was a child prodigy. If she says my art isn't good enough,"
            # June nervous sprite
            j "…"
            # June worried sprite
            j "I…um…If my art isn't good enough, then"
            # June tearing up sprite
            "Hey, hey, are you okay?"
            j "I, yeah, I'm just having a hard time with this p-painting, but I shouldn't be! I'm June Goldeen! The prodigy! And if I can't even do this simple assignment, then!"
            "Crap, now I really feel about trying to bring her down. June clearly has had a lot on her plate, for probably way longer than I can imagine."
            "Woah, let's breathe, okay?"
            "I place my hand on hers, and she's trembling. She takes in a shaky breath, and I feel the tension lessen with each frightened exhale."
            # June worried sprite
            "Seeing her like this drains me of all malice, all jealousy. Without warning, something comes over me, and it's like I'm seeing her for the first time again."
            "June, I'm going to say this…because I get the feeling your mom hasn't told you, but"
            "You can struggle."
            "You can be a good artist and still have a hard time."
            "You're a human person, with limits and needs, not just a prodigy. You're allowed to take breaks, and you're allowed to just…be. You don't have to be the best."
            # June nervous sprite
            j "Thank you, that's sweet, really."
            # June sprite moves to middle of screen
            # June content sprite
            j "You know what? I think it's finished."
            return
            # Ending 1 Complete

    label second_ending:

        # June worried sprite
        j "I can't tell if you're joking"
        "Maybe. Maybe not."
        # June shocked sprite
        j "No, please!"
        # June's sprite shakes a little bit
        j "If everyone knew… that I couldn't handle this, my reputation would be…"
        # June sad sprite, no more shaking
        j "Please. Keep this a secret, you have no idea what's at stake! I shouldn't have told you."
        "Relax, I was just kidding! I'm not going to ruin the illusion for everybody."
        # June shocked sprite
        j "What…'The illusion'? I'm not lying to people by trying hard! I'm a good artist! I…I think…this is just a difficult assignment. I'll be able to finish it!"
        # June mad sprite
        j "I really shouldn't have said anything."
        j "If you have nothing else to do but waste my time, get out."

    return
