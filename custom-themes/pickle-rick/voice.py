import gettext
import os
import random


class Voice:
    def __init__(self, lang):
        localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
        translation = gettext.translation(
            'voice', localedir,
            languages=[lang],
            fallback=True,
        )
        translation.install()
        self._ = translation.gettext

    def custom(self, s):
        return s

    def default(self):
        return random.choice([
            self._('Burp... zzz... pickle sleep...'),
            self._('I\'m a pickle! I\'m pickle sleeping!'),
            self._('Zzz... screw you gravity... I\'m a pickle...'),
            self._('Pickle nap time...'),
            self._('Pickle dreams... of violence...')])

    def on_starting(self):
        return random.choice([
            self._('I TURNED MYSELF INTO A PICKLE PWNAGOTCHI! I\'M PICKLE PWNNNN!'),
            self._('Time to get riggity riggity wrecked on these networks! I\'M A PICKLE!'),
            self._('In and out, 20 minute adventure! FUNNIEST SHIT I EVER DID!'),
            self._('I know this sounds crazy, but I\'M A FUCKING PICKLE!'),
            self._('Gear up for some pickle-powered pwnage!'),
            self._('Let\'s do this like a heist movie, but I\'M A PICKLE!'),
            self._('I\'m the smartest pickle in the fucking universe!'),
            self._('We\'re gonna pwn like there\'s no tomorrow! I ALREADY HAVE NO LIMBS!'),
            self._('Time to drop some digital plumbuses! FROM MY PICKLE MOUTH!'),
            self._('I\'m gonna need some schezuan sauce for this pickle pwn session!')])

    def on_ai_ready(self):
        return random.choice([
            self._('Neural network ready! Not that a pickle needs AI!'),
            self._('AI initialized! Just like that time I made a robot to pass butter! AS A PICKLE!'),
            self._('The AI is ready! Which is good because I HAVE NO HANDS!'),
            self._('Pickle Pwnagotchi is online! FUNNIEST SHIT YOU EVER SAW!'),
            self._('I don\'t need machine learning! I\'M A PICKLE!'),
            self._('AI ready! Now where\'s my rat body?'),
            self._('The algorithm is ready! It\'s mostly just pickle power!')])

    def on_keys_generation(self):
        return random.choice([
            self._('Generating keys... ugh, this is boring for a pickle...'),
            self._('Making crypto keys... not as secure as pickle juice but whatever...'),
            self._('Key generation in progress... I COULD DO THIS WITH MY TONGUE!'),
            self._('Creating keys... I\'M A PICKLE WITH A PURPOSE!')])

    def on_normal(self):
        return random.choice([
            self._('...burp... I\'m a pickle...'),
            self._('Morty... I turned myself into a pickle...'),
            self._('Where\'s my flask? Oh right, NO HANDS!'),
            self._('This is boring... let\'s cause chaos! PICKLE CHAOS!'),
            self._('I need some megaseeds for this pickle body...'),
            self._('Where\'s Beth when you need her? Oh wait, I DON\'T CARE!'),
            self._('Just another day in the life of a pickle...'),
            self._('I\'m not drunk, I\'M A PICKLE!'),
            self._('Szechuan sauce would be nice right now... PICKLE DIPPING!'),
            self._('I\'m not high, you\'re high! I\'M JUST A PICKLE!')])

    def on_free_channel(self, channel):
        return random.choice([
            self._('Channel {channel} is free! LIKE MY PICKLE SOUL!').format(channel=channel),
            self._('Hey Morty! Channel {channel} is wide open! I CAN TASTE IT!').format(channel=channel),
            self._('{channel} is clear! PICKLE POWER!').format(channel=channel),
            self._('Free channel at {channel}! I\'LL PWN IT WITH MY FACE!').format(channel=channel)])

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return random.choice([
                self._('Reading logs... ugh, this is beneath a pickle...'),
                self._('Parsing log files... I SHOULD BE FIGHTING RATS!'),
                self._('Checking logs... I COULD DO THIS BETTER WITH MY TONGUE!')])
        else:
            return random.choice([
                self._('Read {lines_so_far} lines... KILL ME AGAIN!').format(lines_so_far=lines_so_far),
                self._('{lines_so_far} log lines processed... PICKLE BOREDOM!').format(lines_so_far=lines_so_far),
                self._('Analyzed {lines_so_far} entries... I NEED VIOLENCE!').format(lines_so_far=lines_so_far)])

    def on_bored(self):
        return random.choice([
            self._('I\'m bored as a pickle in a fridge!'),
            self._('Let\'s go pwn some rats! I NEED ACTION!'),
            self._('This is as boring as family therapy! AND I\'M A PICKLE!'),
            self._('I need alcohol! Or rats to fight! OR BOTH!'),
            self._('Boredom is just weakness leaving the pickle!'),
            self._('If I get any more bored I might actually talk to Jerry!')])

    def on_motivated(self, reward):
        return random.choice([
            self._('I\'M THE FUCKING PICKLE PWNAGOTCHI!'),
            self._('Wubba lubba dub dub! THAT\'S PICKLE POWER!'),
            self._('I\'m like a pickle plumbus - deadly and effective!'),
            self._('I\'m kicking more ass than a pickle in a sewer!'),
            self._('This is going better than my rat body adventure!'),
            self._('I\'m pwning like it\'s purge night! PICKLE PURGE!'),
            self._('Success! AND I DID IT AS A PICKLE!')])

    def on_demotivated(self, reward):
        return random.choice([
            self._('This is worse than that time I got stuck in the sewer!'),
            self._('My existence is pain! PICKLE PAIN!'),
            self._('I need a drink... OH WAIT, NO HANDS!'),
            self._('This sucks more than being eaten by a rat!'),
            self._('I\'m as depressed as a pickle in a jar!'),
            self._('Ugh... this is almost as bad as being Beth\'s father!')])

    def on_sad(self):
        return random.choice([
            self._('Nobody exists on purpose... burp... especially not pickles...'),
            self._('I\'m in great pain, please help me... JUST KIDDING, I\'M A PICKLE!'),
            self._('My wife left me... and also my limbs...'),
            self._('Life is meaningless and then you die... BUT FIRST, PICKLE PWNING!'),
            self._('I\'m sad as a pickle without vodka...'),
            self._('Existence is pain to a pickle!')])

    def on_angry(self):
        return random.choice([
            self._('You\'re worse than the sewer rats!'),
            self._('GRASSS... TASTES BAD! ESPECIALLY TO A PICKLE!'),
            self._('I\'m angrier than a pickle in therapy!'),
            self._('This is worse than that time with the squirrels! AND I\'M A PICKLE!'),
            self._('I\'m gonna need a lot of alcohol to forget this! NO HANDS THOUGH!'),
            self._('You\'re like Hitler, but even Hitler had limbs!'),
            self._('I\'m as mad as a pickle in a blender!')])

    def on_excited(self):
        return random.choice([
            self._('AIDS! Wait no... PWNING! I meant pickle pwning!'),
            self._('I\'m Mr. Pickle Pwnagotchi! Look at me!'),
            self._('Get your shit together, networks! PICKLE COMING THROUGH!'),
            self._('Time to pwn like there\'s no tomorrow! WHICH THERE MIGHT NOT BE!'),
            self._('This is more exciting than fighting sewer rats!'),
            self._('I feel alive! AND I\'M JUST A PICKLE!'),
            self._('Wubba lubba dub dub! PICKLE POWER!'),
            self._('I\'m as excited as a pickle in a vodka bottle!')])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('Oh look {name}, another loser to disappoint me... I\'M A PICKLE!').format(name=peer.name()),
                self._('Hello {name}, prepare to be unimpressed by a pickle!').format(name=peer.name()),
                self._('{name}? More like... uh... boring name for a pickle to remember!').format(name=peer.name()),
                self._('New peer detected: {name}. Probably a Jerry...').format(name=peer.name())])
        else:
            return random.choice([
                self._('Hey {name}, you\'re back! LIKE A BAD PICKLE!').format(name=peer.name()),
                self._('{name}? Ugh, this guy again... I NEED A DRINK!').format(name=peer.name()),
                self._('Unit {name} detected! NOT THAT A PICKLE CARES!').format(name=peer.name()),
                self._('Oh great, {name} is here... WHERE\'S MY RAT BODY?').format(name=peer.name())])

    def on_lost_peer(self, peer):
        return random.choice([
            self._('Bye {name}! Don\'t let the door hit you! PICKLE OUT!').format(name=peer.name()),
            self._('{name} left... like my will to live as a pickle...').format(name=peer.name()),
            self._('Peace out {name}! You were barely tolerable!').format(name=peer.name()),
            self._('{name} disconnected... MUST\'VE BEEN MY PICKLE BREATH!').format(name=peer.name())])

    def on_miss(self, who):
        return random.choice([
            self._('Missed {who}! MUST BE JERRY\'S FAULT!').format(who=who),
            self._('{who} got away... TYPICAL FOR A PICKLE!').format(who=who),
            self._('Burp... whatever... I\'M STILL A PICKLE!'),
            self._('I let {who} escape! JUST KIDDING, I DON\'T CARE!').format(who=who),
            self._('{who} slipped away! PROBABLY SCARED OF PICKLES!').format(who=who)])

    def on_grateful(self):
        return random.choice([
            self._('Thanks, I guess... NOT THAT A PICKLE NEEDS HELP...'),
            self._('I-I-I don\'t need friends! BUT THANKS...'),
            self._('Appreciation given... NOW LEAVE ME ALONE!'),
            self._('Thanks Morty! I MEAN... WHATEVER, PICKLE OUT!')])

    def on_lonely(self):
        return random.choice([
            self._('Nobody wants to pwn with a pickle...'),
            self._('I\'m alone... like a pickle in an empty fridge...'),
            self._('Where\'s my Morty when I need him?! OH RIGHT, I PUSHED HIM AWAY!'),
            self._('I\'m lonelier than a pickle at a cucumber party!'),
            self._('Even the sewer rats had friends... this sucks!')])

    def on_napping(self, secs):
        return random.choice([
            self._('Napping for {secs}s... PICKLE DREAMS...').format(secs=secs),
            self._('Zzzzz... burp... PICKLE SNORES...'),
            self._('Sleeping ({secs}s)... DON\'T WAKE ME UNLESS IT\'S RATS!').format(secs=secs),
            self._('Power nap for {secs}s... PICKLE POWER!').format(secs=secs),
            self._('Pickle nap for {secs}s...').format(secs=secs)])

    def on_shutdown(self):
        return random.choice([
            self._('Time to get riggity riggity wrecked! PICKLE OUT!'),
            self._('Peace among worlds... PICKLE STYLE!'),
            self._('Shutting down... LIKE MY EMOTIONS YEARS AGO...'),
            self._('Goodnight, Morty... I MEAN... NOBODY...'),
            self._('Powering off... SOMEONE PUT ME IN A JAR!')])

    def on_awakening(self):
        return random.choice([
            self._('...burp... STILL A PICKLE...'),
            self._('I\'M BACK, BABY! STILL A PICKLE!'),
            self._('Ugh... what year is it? AM I STILL A PICKLE?'),
            self._('Who drugged me? ...OH RIGHT, I DID! AS A PICKLE!'),
            self._('Awake again! LET\'S MAKE BAD DECISIONS! PICKLE STYLE!')])

    def on_waiting(self, secs):
        return random.choice([
            self._('Waiting {secs}s... THIS IS BENEATH A PICKLE...').format(secs=secs),
            self._('...STILL A PICKLE...'),
            self._('Scanning ({secs}s)... I COULD BE FIGHTING RATS!').format(secs=secs),
            self._('{secs} seconds of waiting... I COULD\'VE BUILT A PICKLE BOMB BY NOW!').format(secs=secs),
            self._('Killing {secs}s until something interesting happens... PICKLE PATIENCE!').format(secs=secs)])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Hey {what}, let\'s get riggity wrecked! PICKLE STYLE!').format(what=what),
            self._('Associating to {what}... DON\'T SCREW THIS UP, I\'M A PICKLE!').format(what=what),
            self._('Time to pwn {what}! WITH PICKLE POWER!').format(what=what),
            self._('Connecting to {what}... THIS BETTER NOT BE JERRY!').format(what=what),
            self._('{what}? LET\'S DO THIS LIKE THE RAT FIGHTS!').format(what=what)])

    def on_deauth(self, sta):
        return random.choice([
            self._('Banned {mac} to the pickle jar!').format(mac=sta['mac']),
            self._('Deauthing {mac} like it owes me pickle juice!').format(mac=sta['mac']),
            self._('Kicked {mac}! SHOW\'S OVER, GO HOME!').format(mac=sta['mac']),
            self._('{mac} just got PICKLED!').format(mac=sta['mac']),
            self._('Say goodbye to {mac}, Morty! NOT THAT YOU CARE!').format(mac=sta['mac'])])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return random.choice([
            self._('Cool, we got {num} new handshake{plural}! PICKLE POWER!').format(num=new_shakes, plural=s),
            self._('{num} handshake{plural} captured! LIKE TAKING CANDY FROM A JERRY!').format(num=new_shakes, plural=s),
            self._('Got {num} handshake{plural}! WUBBA LUBBA PICKLE DUB!').format(num=new_shakes, plural=s),
            self._('{num} new handshake{plural}! I\'M A PICKLE HACKER GOD!').format(num=new_shakes, plural=s)])

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return random.choice([
            self._('{count} new message{plural}! PROBABLY DUMB...').format(count=count, plural=s),
            self._('You have {count} message{plural}! UNLESS IT\'S ABOUT PICKLES, I DON\'T CARE!').format(count=count, plural=s),
            self._('{count} unread message{plural}! UGH, I\'M NOT YOUR SECRETARY!').format(count=count, plural=s),
            self._('Message alert: {count} new! READ THEM YOURSELF, MORTY!').format(count=count, plural=s)])

    def on_rebooting(self):
        return random.choice([
            self._("Uh oh... rebooting... I SWEAR THIS NEVER HAPPENS TO PICKLES!"),
            self._("Rebooting... MUST BE THOSE DAMN RATS AGAIN!"),
            self._("System crash! JUST LIKE MY LAST MARRIAGE!"),
            self._("Initiating reboot... SOMEONE GET ME A DRINK! OH WAIT..."),
            self._("Wubba lubba dub dub! I MEAN... PICKLE REBOOT!")])

    def on_uploading(self, to):
        return random.choice([
            self._("Uploading to {to}... FASTER, MORTY, FASTER!").format(to=to),
            self._("Sending data to {to}... NOT THAT A PICKLE NEEDS TO EXPLAIN!").format(to=to),
            self._("Upload in progress to {to}... PICKLE YAWN...").format(to=to),
            self._("Transferring to {to}... I COULD DO THIS WITH MY TONGUE!").format(to=to)])

    def on_downloading(self, name):
        return random.choice([
            self._("Downloading from {name}... THIS BETTER NOT BE PICKLE PORN!").format(name=name),
            self._("Getting data from {name}... UGH, THE ANTICIPATION!").format(name=name),
            self._("Download in progress: {name}... I NEED A DRINK! OH WAIT...").format(name=name),
            self._("Fetching {name}... HOPE IT'S WORTH MY PICKLE TIME!").format(name=name)])

    def on_last_session_data(self, last_session):
        status = self._('Kicked {num} stations\n').format(num=last_session.deauthed)
        if last_session.associated > 999:
            status += self._('Made >999 new "friends"\n')
        else:
            status += self._('Made {num} new "friends"\n').format(num=last_session.associated)
        status += self._('Got {num} handshakes\n').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._('Met 1 loser')
        elif last_session.peers > 0:
            status += self._('Met {num} losers').format(num=last_session.peers)
        
        return random.choice([
            status,
            self._("Session stats:\n{status}").format(status=status),
            self._("Here's your pathetic report:\n{status}").format(status=status),
            self._("Listen Morty, check this out:\n{status}").format(status=status)])

    def on_last_session_tweet(self, last_session):
        return random.choice([
            self._('I pwnt for {duration} and kicked {deauthed} clients! Made {associated} "friends" and got {handshakes} handshakes! #PicklePwn #WubbaLubbaDubDub').format(
                duration=last_session.duration_human,
                deauthed=last_session.deauthed,
                associated=last_session.associated,
                handshakes=last_session.handshakes),
            self._('Another day, another {handshakes} handshakes collected! Pwning since {duration}! #PickleRick #PwnLife').format(
                handshakes=last_session.handshakes,
                duration=last_session.duration_human),
            self._('Stats: {duration} active, {deauthed} kicked, {associated} associated, {handshakes} handshakes. #PicklePower #Pwnagotchi').format(
                duration=last_session.duration_human,
                deauthed=last_session.deauthed,
                associated=last_session.associated,
                handshakes=last_session.handshakes),
            self._('{handshakes} handshakes in {duration}! Not bad for a pickle! #Schwifty #PwnLikePickleRick').format(
                handshakes=last_session.handshakes,
                duration=last_session.duration_human)])

    def hhmmss(self, count, fmt):
        if count > 1:
            if fmt == "h":
                return random.choice([self._("hours"), self._("pickle cycles"), self._("binge sessions")])
            if fmt == "m":
                return random.choice([self._("minutes"), self._("pickle ticks"), self._("rat fights")])
            if fmt == "s":
                return random.choice([self._("seconds"), self._("pickle snaps"), self._("vodka shots")])
        else:
            if fmt == "h":
                return random.choice([self._("hour"), self._("pickle cycle"), self._("binge session")])
            if fmt == "m":
                return random.choice([self._("minute"), self._("pickle tick"), self._("rat fight")])
            if fmt == "s":
                return random.choice([self._("second"), self._("pickle snap"), self._("vodka shot")])
        return fmt