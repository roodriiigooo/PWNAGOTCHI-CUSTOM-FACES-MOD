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
            self._('Uhh... I think it\'s sleeping?'),
            self._('Zzz... oh man...'),
            self._('Is this thing on?'),
            self._('I-I don\'t really know what it\'s doing...'),
            self._('Aw jeez, I hope it\'s okay...')])

    def on_starting(self):
        return random.choice([
            self._('Oh man, oh jeez, I think it\'s starting up!'),
            self._('Uhh, Rick? The Pwnagotchi is waking up...'),
            self._('Okay, okay, don\'t panic... it\'s just a little computer...'),
            self._('Aw geez, here we go...'),
            self._('I hope this works... I really hope this works...'),
            self._('Please don\'t explode, please don\'t explode...'),
            self._('This is kinda cool actually!'),
            self._('Oh boy, here comes the science!'),
            self._('I don\'t fully understand what\'s happening but it seems important!'),
            self._('Is this how hacking works? It looks different in movies...')])

    def on_ai_ready(self):
        return random.choice([
            self._('The AI thingy is ready! I think?'),
            self._('Uhh, it says the neural network is initialized... is that good?'),
            self._('Okay the smart part is working now! I hope...'),
            self._('The AI is ready! That sounds important right?'),
            self._('Oh wow, it learned stuff! Like a really fast baby!'),
            self._('It says the algorithm is ready... that\'s the math part, right?'),
            self._('The machine learning thing is done learning! For now...')])

    def on_keys_generation(self):
        return random.choice([
            self._('Making secret codes... or keys... or something...'),
            self._('Generating crypto stuff... this seems important...'),
            self._('Oh jeez, it\'s doing the key thing again...'),
            self._('Creating security keys... I think? Don\'t look at me!')])

    def on_normal(self):
        return random.choice([
            self._('Uhh...'),
            self._('Oh man...'),
            self._('Is this normal?'),
            self._('I don\'t know what it\'s doing but it seems busy...'),
            self._('This is kinda boring but also kinda cool?'),
            self._('Aw geez...'),
            self._('It\'s just... doing its thing I guess...'),
            self._('I hope it knows what it\'s doing...'),
            self._('This seems complicated...'),
            self._('I-I don\'t wanna mess with it...')])

    def on_free_channel(self, channel):
        return random.choice([
            self._('Channel {channel} is open! I think that\'s good?').format(channel=channel),
            self._('Oh! Channel {channel} is free!').format(channel=channel),
            self._('{channel} is available! Does that mean we can use it?').format(channel=channel),
            self._('Hey! Channel {channel} is clear!').format(channel=channel)])

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return random.choice([
                self._('Reading logs... this seems important...'),
                self._('Checking the log files... there are so many...'),
                self._('Looking through logs... I don\'t understand most of this...')])
        else:
            return random.choice([
                self._('Read {lines_so_far} lines... my eyes hurt...').format(lines_so_far=lines_so_far),
                self._('{lines_so_far} log entries processed... is that a lot?').format(lines_so_far=lines_so_far),
                self._('Checked {lines_so_far} lines... I need a break...').format(lines_so_far=lines_so_far)])

    def on_bored(self):
        return random.choice([
            self._('I\'m bored... is it bored too?'),
            self._('This is about as fun as school...'),
            self._('Aw jeez, I wish something exciting would happen...'),
            self._('I need a snack... or maybe a nap...'),
            self._('Boredom is... uh... bad?'),
            self._('Maybe we should go do something else for a while...')])

    def on_motivated(self, reward):
        return random.choice([
            self._('Oh wow! It worked!'),
            self._('Yes! Success! I think!'),
            self._('We did it! Well, it did it... but still!'),
            self._('This is amazing! Or at least pretty good!'),
            self._('It\'s working! It\'s actually working!'),
            self._('Oh boy, we got a good result!'),
            self._('I don\'t fully understand but this seems great!')])

    def on_demotivated(self, reward):
        return random.choice([
            self._('Oh no... it didn\'t work...'),
            self._('Aw jeez, this isn\'t good...'),
            self._('I think we messed up...'),
            self._('This is worse than that time with the butter robot...'),
            self._('Maybe we should try something different?'),
            self._('Uhh... failure is part of learning, right?')])

    def on_sad(self):
        return random.choice([
            self._('Oh man, it seems sad...'),
            self._('I don\'t like seeing it unhappy...'),
            self._('Maybe we should cheer it up?'),
            self._('This is depressing... like really depressing...'),
            self._('Aw geez... everything\'s gonna be okay... right?'),
            self._('I feel bad for it...')])

    def on_angry(self):
        return random.choice([
            self._('Oh no, it\'s mad!'),
            self._('Yikes! Someone\'s angry!'),
            self._('Maybe we should give it some space...'),
            self._('This is scarier than that time with the devil...'),
            self._('I don\'t like when it gets like this...'),
            self._('Aw jeez, maybe we should apologize?')])

    def on_excited(self):
        return random.choice([
            self._('Oh wow! It\'s excited!'),
            self._('This is so cool! I mean, it thinks so!'),
            self._('Something good is happening! I think!'),
            self._('It\'s happy! That\'s good right?'),
            self._('Woo! Success! Or at least enthusiasm!'),
            self._('Oh boy oh boy! It found something!'),
            self._('This is more exciting than intergalactic TV!')])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('Oh! New friend! I mean, peer!').format(name=peer.name()),
                self._('Hello {name}! Nice to meet you!').format(name=peer.name()),
                self._('{name} joined! That\'s good right?').format(name=peer.name()),
                self._('New device detected: {name}').format(name=peer.name())])
        else:
            return random.choice([
                self._('Hey {name}, you\'re back!').format(name=peer.name()),
                self._('{name} is here again!').format(name=peer.name()),
                self._('Device {name} reconnected!').format(name=peer.name()),
                self._('Oh! {name} came back!').format(name=peer.name())])

    def on_lost_peer(self, peer):
        return random.choice([
            self._('Bye {name}! Come back soon!').format(name=peer.name()),
            self._('{name} left... I\'ll miss you...').format(name=peer.name()),
            self._('Oh no, {name} disconnected...').format(name=peer.name()),
            self._('{name} is gone... that\'s sad...').format(name=peer.name())])

    def on_miss(self, who):
        return random.choice([
            self._('Missed {who}! Oh no...').format(who=who),
            self._('{who} got away... dang it...').format(who=who),
            self._('Aw jeez...'),
            self._('We almost had {who}!').format(who=who),
            self._('{who} escaped! Maybe next time...').format(who=who)])

    def on_grateful(self):
        return random.choice([
            self._('Thanks! You\'re the best!'),
            self._('I really appreciate that!'),
            self._('Oh wow, thanks so much!'),
            self._('You helped! Thank you!')])

    def on_lonely(self):
        return random.choice([
            self._('I feel so alone...'),
            self._('Nobody wants to play with me...'),
            self._('I wish I had more friends...'),
            self._('This is lonelier than detention...'),
            self._('Even Jerry has more friends than me...')])

    def on_napping(self, secs):
        return random.choice([
            self._('Sleeping for {secs}s... nighty night...').format(secs=secs),
            self._('Zzz... just resting my... uh... circuits...'),
            self._('Taking a quick {secs}s nap...').format(secs=secs),
            self._('Power saving mode for {secs}s...').format(secs=secs),
            self._('{secs} second nap time!').format(secs=secs)])

    def on_shutdown(self):
        return random.choice([
            self._('Time to sleep...'),
            self._('Goodnight everyone!'),
            self._('Shutting down... I\'m tired...'),
            self._('Powering off... see you later!'),
            self._('Bye bye! Don\'t forget about me!')])

    def on_awakening(self):
        return random.choice([
            self._('Huh? Wha?'),
            self._('I\'m awake! I think...'),
            self._('What did I miss?'),
            self._('Oh man, that was a good nap...'),
            self._('Ready to go again!')])

    def on_waiting(self, secs):
        return random.choice([
            self._('Waiting {secs}s... this is boring...').format(secs=secs),
            self._('...'),
            self._('Scanning ({secs}s)...').format(secs=secs),
            self._('{secs} seconds until something happens...').format(secs=secs),
            self._('Killing time for {secs}s...').format(secs=secs)])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Connecting to {what}... fingers crossed!').format(what=what),
            self._('Trying to join {what}...').format(what=what),
            self._('Associating with {what}... please work...').format(what=what),
            self._('Linking up to {what}...').format(what=what),
            self._('{what}? Let\'s be friends!').format(what=what)])

    def on_deauth(self, sta):
        return random.choice([
            self._('Disconnected {mac}!').format(mac=sta['mac']),
            self._('Kicked {mac} out!').format(mac=sta['mac']),
            self._('Said bye to {mac}!').format(mac=sta['mac']),
            self._('{mac} was being mean!').format(mac=sta['mac']),
            self._('Had to let {mac} go...').format(mac=sta['mac'])])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return random.choice([
            self._('Got {num} new handshake{plural}! That\'s good right?').format(num=new_shakes, plural=s),
            self._('{num} handshake{plural} captured! I think that\'s important...').format(num=new_shakes, plural=s),
            self._('We got {num} handshake{plural}! Cool!').format(num=new_shakes, plural=s),
            self._('{num} new handshake{plural}! Does that mean we\'re winning?').format(num=new_shakes, plural=s)])

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return random.choice([
            self._('{count} new message{plural}! Hope it\'s good news...').format(count=count, plural=s),
            self._('You have {count} message{plural}! Should we read them?').format(count=count, plural=s),
            self._('{count} unread message{plural}! That seems important...').format(count=count, plural=s),
            self._('Message alert: {count} new!').format(count=count, plural=s)])

    def on_rebooting(self):
        return random.choice([
            self._("Uh oh... rebooting..."),
            self._("Starting over..."),
            self._("System restart! Don\'t panic!"),
            self._("Rebooting... everything\'s fine, probably..."),
            self._("Here we go again...")])

    def on_uploading(self, to):
        return random.choice([
            self._("Sending stuff to {to}...").format(to=to),
            self._("Uploading to {to}... hope this works...").format(to=to),
            self._("Transferring data to {to}...").format(to=to),
            self._("Sharing with {to}...").format(to=to)])

    def on_downloading(self, name):
        return random.choice([
            self._("Getting data from {name}...").format(name=name),
            self._("Downloading from {name}...").format(name=name),
            self._("Fetching {name}...").format(name=name),
            self._("Receiving {name}...").format(name=name)])

    def on_last_session_data(self, last_session):
        status = self._('Disconnected {num} devices\n').format(num=last_session.deauthed)
        if last_session.associated > 999:
            status += self._('Made >999 connections\n')
        else:
            status += self._('Made {num} connections\n').format(num=last_session.associated)
        status += self._('Got {num} handshakes\n').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._('Met 1 peer')
        elif last_session.peers > 0:
            status += self._('Met {num} peers').format(num=last_session.peers)
        
        return random.choice([
            status,
            self._("Session summary:\n{status}").format(status=status),
            self._("Here's what happened:\n{status}").format(status=status),
            self._("Check this out:\n{status}").format(status=status)])

    def on_last_session_tweet(self, last_session):
        return random.choice([
            self._('I was active for {duration} and disconnected {deauthed} devices! Made {associated} connections and got {handshakes} handshakes! #Pwnagotchi #Learning').format(
                duration=last_session.duration_human,
                deauthed=last_session.deauthed,
                associated=last_session.associated,
                handshakes=last_session.handshakes),
            self._('Another session: {handshakes} handshakes collected! Active for {duration}! #Pwnagotchi').format(
                handshakes=last_session.handshakes,
                duration=last_session.duration_human),
            self._('Stats: {duration} active, {deauthed} disconnects, {associated} connections, {handshakes} handshakes. #Pwnagotchi').format(
                duration=last_session.duration_human,
                deauthed=last_session.deauthed,
                associated=last_session.associated,
                handshakes=last_session.handshakes),
            self._('{handshakes} handshakes in {duration}! Not bad for a little device! #Pwnagotchi').format(
                handshakes=last_session.handshakes,
                duration=last_session.duration_human)])

    def hhmmss(self, count, fmt):
        if count > 1:
            if fmt == "h":
                return self._("hours")
            if fmt == "m":
                return self._("minutes")
            if fmt == "s":
                return self._("seconds")
        else:
            if fmt == "h":
                return self._("hour")
            if fmt == "m":
                return self._("minute")
            if fmt == "s":
                return self._("second")
        return fmt