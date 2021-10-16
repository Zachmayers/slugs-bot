# Screenplay Reference

toc = '''I can answer some questions about screenplay formatting and writing! Just say `!guide (topic)` and I'll tell you what I know.

You can ask me about the following topics:

**Parentheticals**
'''

parenBase = '''**Parenthetical**

A parenthetical is a short description that modifies a line of dialogue in a screenplay. It is written in a dialogue block between a character name and the dialogue itself.

```
		JACOB
Sir, we have an opportunity that
we might never get again! I need
you to authorize my server time.

		HAYES
	(indifferent)
Server time is valuable, we can't
give it to everyone who asks. The
answer is no. Is there anything 
else?
```

Parentheticals can be used for many types of directions in a script that directly affect a single line of dialogue. These include:

1. Emotion / Delivery
2. Simultaneous action
3. Specifying who is being spoken to
4. Pauses and micro-actions
5. Language changes

Type `!guide parenthetical #` to view one of these sections.'''

paren1 = '''**1. Emotion and Delivery**

In general, you don't want to use parentheticals for this unless it is both *unclear or ambiguous* and *critical to the story*, because it is the actor's job to interpret the character and their feelings in the story through their delivery. If there is a case like this, though, a parenthetical is appropriate.

```
Nicole walks into the living room. Owen is sitting in his chair, watching a western on the television.

		NICOLE
Look at you. You made it a
whole month. I'm proud of
you, Owen.

Owen is quiet. He doesn't turn or react.

		NICOLE
Sweetie?

		OWEN
	(slurring)
I'm sorry, sweetie, I- I 
messsed up.
```'''

paren2 = '''**2. Simultaneous Action**

If there's an action that occurs simultaneously with, and connected to, a line of dialogue, it can be put into a parenthetical. In general, it's good practice to keep most actions in action lines, but, in some cases, a parenthetical can be used.

```
Dr. Calamity lays on the ground, finally bested. Heroman lands with a BOOM on the ground next to him. He stands and approaches Dr. Calamity, who flinches. Heroman extends a hand to help the evil Doctor up.

		HEROMAN
We have bigger things to worry
about than each other. Are you
ready to help me?

		DR. CALAMITY
It seems I'm left without much
choice, right?

		HEROMAN
It's either me or the giant
meteor. What do you pick?

		DR. CALAMITY
	(takes his hand)
As nice as the meteor sounds,
I suppose I'll help you.
```'''

paren3 = '''**3. Specifying Who is Being Spoken To**

If there's a large group of people in the scene, and you need to specify who is being spoken to by one of the characters in the scene, you can use a parenthetical.

```
		ELENA
I don't understand why you're
defending him! He's an asshole
and he's obviously the one who
left the seat up! It's his
fault!

		SHAWN
You just want to blame him
because it's convenient! Think 
about it! What evidence do you 
really have that he pissed in
that toilet at that time on
that night?

		JORDAN
	(to Maddi)
Yo, this is just like that
movie 12 ANGRY MEN.
```'''

paren4 = '''**4. Pauses and Micro-Actions**

You can add a pause or small action into a parenthetical to break up longer sections of dialogue. This helps with pacing how quickly your script will be read, and also helps to add or remove emphasis to the action.

```
		MYLES
I just - I need you to 
understand that this is hard
for me to talk about. I'm
not used to asking people
this, but I think you're worth
it, Sophie. I have to ask you.
	(beat)
Will you trade Yu-Gi-Oh cards 
with me?

		SOPHIE
Oh, Myles, sweetie, I was 
scared you would never ask! 
I've been waiting for so
long for you to ask!
	(hugs him)
Of course I'll trade Yu-
Gi-Oh cards with you!
```'''

paren5 = '''**5. Language Changes**

If a character switches between languages or is speaking in a different one from the last time they spoke, you can specify that with a parenthetical.

```
		BRANDON
Hey, your name is like that one
guy from Les Mis! Do you like
Les Mis? What's your favorite
line from Les Mis?

		JAVERT
	(in French)
I hate you with all of my being
and I hope you cry tonight and 
don't know why.

		BRANDON
Oh, awesome! What does that
mean?

		JAVERT
	(in English)
Uh, it means "oooh oh boy we're
French and we're revolting, down
with the aristocracy hahaha."
```'''

parentheticals = {
    "base": parenBase,
    "1": paren1,
    "2": paren2,
    "3": paren3,
    "4": paren4,
    "5": paren5,
}