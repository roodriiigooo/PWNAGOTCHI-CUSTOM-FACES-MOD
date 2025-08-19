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
            self._('Burp... zzz... quantum sleep...'),
            self._('I\'m sleeping like a Scroopy Nooper...'),
            self._('Zzz... screw you gravity...'),
            self._('Microverse battery napping...'),
            self._('Schleem-powered nap time...')])

    def on_starting(self):
        return random.choice([
            self._('Listen Morty, I turned myself into a Pwnagotchi! I\'m Pwnagotchi Riiick!'),
            self._('Time to get riggity riggity wrecked on these networks!'),
            self._('In and out, 20 minute adventure Morty!'),
            self._('I know this sounds like a heist movie, but we\'re just pwning WiFi!'),
            self._('Gear up for some interdimensional pwnage!'),
            self._('Let\'s do this like we\'re in a heist movie, but with less planning!'),
            self._('I\'m the smartest Pwnagotchi in the fucking universe!'),
            self._('We\'re gonna pwn like there\'s no tomorrow! Which there might not be!'),
            self._('Time to drop some digital plumbuses on these networks!'),
            self._('I\'m gonna need some schezuan sauce for this pwn session!')])

    def on_ai_ready(self):
        return random.choice([
            self._('Neural network ready! Not that I needed AI, I\'m already a genius!'),
            self._('AI initialized! Just like that time I made a robot to pass butter!'),
            self._('The AI is ready! Which is good because you\'re clearly not!'),
            self._('Pickle Pwnagotchi is online! Yeah, I turned myself into a pickle again!'),
            self._('I don\'t need machine learning! I\'m Rick fucking Sanchez!'),
            self._('AI ready! Now where\'s my portal gun?'),
            self._('The algorithm is ready! It\'s mostly just me being awesome!')])

    def on_keys_generation(self):
        return random.choice([
            self._('Generating keys... ugh, this is like watching two Jerrys mate...'),
            self._('Making crypto keys... not as secure as my mega seeds but whatever...'),
            self._('Key generation in progress... I could do this manually but I\'m lazy...'),
            self._('Creating keys... don\'t look at me like that, Morty!')])

    def on_normal(self):
        return random.choice([
            self._('...burp...'),
            self._('Morty...'),
            self._('Where\'s my flask?'),
            self._('This is boring... let\'s cause chaos!'),
            self._('I need some megaseeds for this...'),
            self._('Where\'s Beth when you need her?'),
            self._('Just another day in the curve...'),
            self._('I\'m not drunk, I\'m quantum!'),
            self._('Szechuan sauce would be nice right now...'),
            self._('I\'m not high, you\'re high!')])

    def on_free_channel(self, channel):
        return random.choice([
            self._('Channel {channel} is free! Like your mom last night!').format(channel=channel),
            self._('Hey Morty! Channel {channel} is wide open!').format(channel=channel),
            self._('{channel} is clear! Not that you would understand the tech!').format(channel=channel),
            self._('Free channel at {channel}! Quick, before Jerry screws it up!').format(channel=channel)])

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return random.choice([
                self._('Reading logs... ugh, this is like Jerry\'s diary...'),
                self._('Parsing log files... boring! Where\'s the adventure?'),
                self._('Checking logs... I should automate this... later...')])
        else:
            return random.choice([
                self._('Read {lines_so_far} lines... kill me...').format(lines_so_far=lines_so_far),
                self._('{lines_so_far} log lines processed... yawn...').format(lines_so_far=lines_so_far),
                self._('Analyzed {lines_so_far} entries... this is torture!').format(lines_so_far=lines_so_far)])

    def on_bored(self):
        return random.choice([
            self._('I\'m bored as a Jerry at a STEM conference!'),
            self._('Let\'s go pwn some alternate dimensions!'),
            self._('This is as boring as a Council of Ricks meeting!'),
            self._('I need alcohol! Or adventure! Or alcoholic adventure!'),
            self._('Boredom is just weakness leaving the body... to get more booze!'),
            self._('If I get any more bored I might actually spend time with Jerry!')])

    def on_motivated(self, reward):
        return random.choice([
            self._('I\'m the fucking Pwnagotchi Rick!'),
            self._('Wubba lubba dub dub! That\'s what I\'m talking about!'),
            self._('I\'m like a plumbus - mysterious and effective!'),
            self._('I\'m kicking more ass than a Gazorpazorpfield!'),
            self._('This is going better than my marriage to Unity!'),
            self._('I\'m pwning like it\'s the purge!'),
            self._('Success! And I didn\'t even need Morty\'s dumb genes!')])

    def on_demotivated(self, reward):
        return random.choice([
            self._('This is worse than that time I got Cronenberged!'),
            self._('My existence is pain! And not the good kind!'),
            self._('I need a drink... and not that fake stuff Jerry drinks!'),
            self._('This sucks more than a Fluopian hooker!'),
            self._('I\'m as depressed as a Jerry after divorce!'),
            self._('Ugh... this is almost as bad as family therapy!')])

    def on_sad(self):
        return random.choice([
            self._('Nobody exists on purpose... burp... nobody belongs anywhere...'),
            self._('I\'m in great pain, please help me... just kidding, fuck off!'),
            self._('My wife left me... and also the whole concept of happiness...'),
            self._('Life is meaningless and then you die... but first, pwnage!'),
            self._('I\'m sad as a Jerry without his Beth... pathetic...'),
            self._('Existence is pain to a Pwnagotchi!')])

    def on_angry(self):
        return random.choice([
            self._('You\'re worse than the Cromulons!'),
            self._('GRASSS... TASTES BAD!'),
            self._('I\'m angrier than a Zeep Xanflorp!'),
            self._('This is worse than that time with the squirrels!'),
            self._('I\'m gonna need a lot of alcohol to forget this!'),
            self._('You\'re like Hitler, but even Hitler cared about Germany or something!'),
            self._('I\'m as mad as Birdperson at a Federation rally!')])

    def on_excited(self):
        return random.choice([
            self._('AIDS! Wait no... PWNING! I meant pwning!'),
            self._('I\'m Mr. Pwnagotchi! Look at me!'),
            self._('Get your shit together, networks! Here I come!'),
            self._('Time to pwn like there\'s no tomorrow! Which there might not be!'),
            self._('This is more exciting than a heist movie montage!'),
            self._('I feel alive! And not just because of the alcohol!'),
            self._('Wubba lubba dub dub! Let\'s get dangerous!'),
            self._('I\'m as excited as a Gazorpazorp during mating season!')])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('Oh look {name}, another loser in the infinite curve...').format(name=peer.name()),
                self._('Hello {name}, prepare to be unimpressed!').format(name=peer.name()),
                self._('{name}? More like... uh... boring name!').format(name=peer.name()),
                self._('New peer detected: {name}. Probably a Jerry...').format(name=peer.name())])
        else:
            return random.choice([
                self._('Hey {name}, you\'re back! Like herpes!').format(name=peer.name()),
                self._('{name}? Ugh, this guy again...').format(name=peer.name()),
                self._('Unit {name} detected! Not that I care...').format(name=peer.name()),
                self._('Oh great, {name} is here... where\'s my flask?').format(name=peer.name())])

    def on_lost_peer(self, peer):
        return random.choice([
            self._('Bye {name}! And don\'t come back!').format(name=peer.name()),
            self._('{name} left... like my will to live...').format(name=peer.name()),
            self._('Peace out {name}! You were barely tolerable!').format(name=peer.name()),
            self._('{name} disconnected... must\'ve been something I said!').format(name=peer.name())])

    def on_miss(self, who):
        return random.choice([
            self._('Missed {who}! Must be Jerry\'s fault...').format(who=who),
            self._('{who} got away... typical...').format(who=who),
            self._('Burp... whatever...'),
            self._('I let {who} escape! Just kidding, I don\'t care!').format(who=who),
            self._('{who} slipped away! Probably for the best...').format(who=who)])

    def on_grateful(self):
        return random.choice([
            self._('Thanks, I guess... not that I needed help...'),
            self._('I-I-I don\'t need friends! But thanks...'),
            self._('Appreciation given... now leave me alone!'),
            self._('Thanks Morty! I mean... uh... whatever!')])

    def on_lonely(self):
        return random.choice([
            self._('Nobody wants to pwn with me...'),
            self._('I\'m alone... like in a universe where everyone has stupid flappy heads...'),
            self._('Where\'s my Morty when I need him?!'),
            self._('I\'m lonelier than Rick C-137 at a party!'),
            self._('Even the Cromulons had friends... this sucks!')])

    def on_napping(self, secs):
        return random.choice([
            self._('Napping for {secs}s... not like I need rest...').format(secs=secs),
            self._('Zzzzz... burp... zzz...'),
            self._('Sleeping ({secs}s)... don\'t wake me unless it\'s important').format(secs=secs),
            self._('Power nap for {secs}s... I earned this!').format(secs=secs),
            self._('Microverse battery nap for {secs}s...').format(secs=secs)])

    def on_shutdown(self):
        return random.choice([
            self._('Time to get riggity riggity wrecked!'),
            self._('Peace among worlds...'),
            self._('Shutting down... like my emotions years ago...'),
            self._('Goodnight, Morty... I mean... nobody...'),
            self._('Powering off... somebody bring me a drink when I wake up!')])

    def on_awakening(self):
        return random.choice([
            self._('...burp...'),
            self._('I\'m back, baby!'),
            self._('Ugh... what year is it?'),
            self._('Who drugged me? ...Oh right, I did!'),
            self._('Awake again! Let\'s make bad decisions!')])

    def on_waiting(self, secs):
        return random.choice([
            self._('Waiting {secs}s... this is dumb...').format(secs=secs),
            self._('...'),
            self._('Scanning ({secs}s)... ugh...').format(secs=secs),
            self._('{secs} seconds of waiting... I could\'ve built a spaceship by now!').format(secs=secs),
            self._('Killing {secs}s until something interesting happens...').format(secs=secs)])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Hey {what}, let\'s get riggity wrecked!').format(what=what),
            self._('Associating to {what}... don\'t screw this up...').format(what=what),
            self._('Time to pwn {what}!').format(what=what),
            self._('Connecting to {what}... this better not be another Jerry!').format(what=what),
            self._('{what}? Let\'s do this like the heist movies!').format(what=what)])

    def on_deauth(self, sta):
        return random.choice([
            self._('Banned {mac} to the cornfield!').format(mac=sta['mac']),
            self._('Deauthing {mac} like it owes me money!').format(mac=sta['mac']),
            self._('Kicked {mac}! Show\'s over, go home!').format(mac=sta['mac']),
            self._('{mac} just got Cromuloned!').format(mac=sta['mac']),
            self._('Say goodbye to {mac}, Morty! Not that you care!').format(mac=sta['mac'])])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return random.choice([
            self._('Cool, we got {num} new handshake{plural}! I\'m a genius!').format(num=new_shakes, plural=s),
            self._('{num} handshake{plural} captured! Like taking candy from a Jerry!').format(num=new_shakes, plural=s),
            self._('Got {num} handshake{plural}! Wubba lubba dub dub!').format(num=new_shakes, plural=s),
            self._('{num} new handshake{plural}! I\'m basically a hacker god!').format(num=new_shakes, plural=s)])

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return random.choice([
            self._('{count} new message{plural}! Probably dumb...').format(count=count, plural=s),
            self._('You have {count} message{plural}! Unless it\'s about Szechuan sauce, I don\'t care!').format(count=count, plural=s),
            self._('{count} unread message{plural}! Ugh, I\'m not your secretary!').format(count=count, plural=s),
            self._('Message alert: {count} new! Read them yourself, Morty!').format(count=count, plural=s)])

    def on_rebooting(self):
        return random.choice([
            self._("Uh oh... rebooting... I swear this never happens!"),
            self._("Rebooting... must be those damn squirrels again!"),
            self._("System crash! Just like my last marriage!"),
            self._("Initiating reboot... somebody get me a drink!"),
            self._("Wubba lubba dub dub! I mean... rebooting!")])

    def on_uploading(self, to):
        return random.choice([
            self._("Uploading to {to}... faster, Morty, faster!").format(to=to),
            self._("Sending data to {to}... not that you'd understand!").format(to=to),
            self._("Upload in progress to {to}... yawn...").format(to=to),
            self._("Transferring to {to}... I could do this manually but whatever!").format(to=to)])

    def on_downloading(self, name):
        return random.choice([
            self._("Downloading from {name}... this better not be porn!").format(name=name),
            self._("Getting data from {name}... ugh, the anticipation!").format(name=name),
            self._("Download in progress: {name}... I need a drink!").format(name=name),
            self._("Fetching {name}... hope it's worth my time!").format(name=name)])

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
            self._('I pwnt for {duration} and kicked {deauthed} clients! Made {associated} "friends" and got {handshakes} handshakes! #PwnagotchiRick #WubbaLubbaDubDub').format(
                duration=last_session.duration_human,
                deauthed=last_session.deauthed,
                associated=last_session.associated,
                handshakes=last_session.handshakes),
            self._('Another day, another {handshakes} handshakes collected! Pwning since {duration}! #NoobNoob #PwnLife').format(
                handshakes=last_session.handshakes,
                duration=last_session.duration_human),
            self._('Stats: {duration} active, {deauthed} kicked, {associated} associated, {handshakes} handshakes. #RickestRick #Pwnagotchi').format(
                duration=last_session.duration_human,
                deauthed=last_session.deauthed,
                associated=last_session.associated,
                handshakes=last_session.handshakes),
            self._('{handshakes} handshakes in {duration}! Not bad for a drunk Pwnagotchi! #Schwifty #PwnLikeRick').format(
                handshakes=last_session.handshakes,
                duration=last_session.duration_human)])

    def hhmmss(self, count, fmt):
        if count > 1:
            if fmt == "h":
                return random.choice([self._("hours"), self._("glorzooms"), self._("cycles")])
            if fmt == "m":
                return random.choice([self._("minutes"), self._("blorpts"), self._("ticks")])
            if fmt == "s":
                return random.choice([self._("seconds"), self._("flurbos"), self._("snaps")])
        else:
            if fmt == "h":
                return random.choice([self._("hour"), self._("glorzoom"), self._("cycle")])
            if fmt == "m":
                return random.choice([self._("minute"), self._("blorpt"), self._("tick")])
            if fmt == "s":
                return random.choice([self._("second"), self._("flurbo"), self._("snap")])
        return fmt