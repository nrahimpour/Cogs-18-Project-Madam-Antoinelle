"""Classes used throughout project"""
# dictionary of all the groups of cards and their meanings
tarot_deck = {
    'Major Arcana':{ 
        'The Fool': 'innonence, new beginnings',
        'The Magician': 'willpower, desire',
        'The High Priestess': 'intuitive, unconscious',
        'The Empress': 'motherhood, fertility',
        'The Emperor': 'authority, structure',
        'The Hierophant': 'tradition, conformity',
        'The Lovers': 'partnerships, duality',
        'The Chariot': 'direction, control',
        'Strength': 'inner strength, bravery',
        'The Hermit': 'contemplation, search for truth',
        'The Wheel of Fortune': 'change, cycles',
        'Justice': 'cause and effect, clarity',
        'The Hanged Man': 'sacrifice, release',
        'Death': 'end of cycle, beginnings',
        'Temperence': 'middle path, patience',
        'The Devil': 'addiction, materialism',
        'The Tower': 'sudden upheaval, broken pride',
        'The Star': 'hope, faith',
        'The Moon': 'unconscuious, illusions',
        'The Sun': 'joy, success',
        'Judgement': 'reflection, reckoning',
        'The World': 'fulfillment, harmony',
    },
    
    'Wands':{
        'King of Wands': 'influence, respect',
        'Queen of Wands': 'creativity, growth',
        'Knight of Wands': 'determination, energetic',
        'Page of Wands': 'enthusiasm, travel',
        'Ace of Wands': 'inspriation, potential',
        'Two of Wands': 'focus, planning',
        'Three of Wands': 'strategy, strength',
        'Four of Wands': 'union, celebration',
        'Five of Wands': 'conflict, disagreement',
        'Six of Wands': 'victory, confidence',
        'Seven of Wands': 'challenge, struggle',
        'Eight of Wands': 'action, balance',
        'Nine of Wands': 'courage, persistence',
        'Ten of Wands': 'burden, stress', 
    }, 
    
    'Cups':{
        'King of Cups': 'balance, generosity',
        'Queen of Cups': 'protection, intuition',
        'Knight of Cups': 'advancement, inspiration',
        'Page of Cups': 'confidence, happiness',
        'Ace of Cups': 'compassion, purity',
        'Two of Cups': 'health, partnership',
        'Three of Cups': 'community, friendship',
        'Four of Cups': 'meditation, resentment',
        'Five of Cups': 'loss, neglect',
        'Six of Cups': 'innocence, nostalgia',
        'Seven of Cups': 'illusion, imagination',
        'Eight of Cups': 'abandonment, loss of interest',
        'Nine of Cups': 'happiness, satisfaction',
        'Ten of Cups': 'abundance, satisfaction',   
    },
    
    'Swords':{
        'King of Swords': 'intellect, authority',
        'Queen of Swords': 'confidence, assurance',
        'Knight of Swords': 'stubborn, brash overbearing',
        'Page of Swords': 'thoughtfullness, charity',
        'Ace of Swords': 'focus, clarity',
        'Two of Swords': 'intuition, compromise',
        'Three of Swords': 'pain, grief',
        'Four of Swords': 'contemplation, meditation',
        'Five of Swords': 'selfishness, tension',
        'Six of Swords': 'solutions, change',
        'Seven of Swords': 'betryal, escape',
        'Eight of Swords': 'isolation, imprisonment',
        'Nine of Swords': 'depression, crisis',
        'Ten of Swords': 'betrayal, surrender',
    },
    
    'Pentacles':{
        'King of Penatacles': 'power, influence',
        'Queen of Penatacles': 'prosperity, pleasure',
        'Knight of Penatacles': 'prepared, efficient',
        'Page of Penatacles': 'opportunity, discovery',
        'Ace of Penatacles': 'stability, new beginnings',
        'Two of Penatacles': 'renewal, adaptability',
        'Three of Penatacles': 'success, collaboration',
        'Four of Penatacles': 'stability, control',
        'Five of Penatacles': 'isolation, poverty',
        'Six of Penatacles': 'generosity, charity',
        'Seven of Penatacles': 'profit, reward',
        'Eight of Penatacles': 'creativity, concentration',
        'Nine of Penatacles': 'luxury, success',
        'Ten of Penatacles': 'wealth, family',
    }
}

import random

class TarotReading:
    """Simulates the drawing of a tarot card at random and the interpretation of said card."""
    
    def __init__(self, tarot_deck):
        self.tarot_deck = tarot_deck
        
    def draw_a_card(self):
        """Simulates the drawing of a random tarot card.
        
        Returns:
            A random suit and a random card from that suit.
        """
    
        all_cards = []
    
        #select a random card and its suit from the tarot deck
        for suit in self.tarot_deck:
            for card in self.tarot_deck[suit]:
                all_cards.append((card, suit))
                
        random_draw, random_suit = random.choice(all_cards)
        return random_suit, random_draw

    def interpret(self, suit, card):
        """Interpret the card that was drawn.
        
        Returns:
            The interpreatation of the drawn tarot card.
        """
        
        #check if the card is in the current suite's cards, and return the interpretation if not
        for suit, cards in self.tarot_deck.items():
            if card in cards:
                return cards[card]
        
        return self.tarot_deck[suit][card]
    
    def do_a_reading(self):
        """Draws the card, interprets it, and then prints the reading.
        
        Prints:
            A greeting message followed by the randomly drawn card's suit, specific name, and interpretation.
        """
        #draw a random card and print the reading
        random_suit, random_draw = self.draw_a_card()
        interpretation = self.interpret(random_suit, random_draw)
        
        print('Suit: {}\nCard: {}'.format(random_suit, random_draw))
        print('Interpretation:', interpretation)
        
reading = TarotReading(tarot_deck)

class FortuneTeller:
    """url: https://sonsuzdesign.blog/2020/12/17/building-a-chatbot-in-python-beginners-guide/
    
    I used this to guide me for the structure of the chatbot.
    Some code is modifed, some is direct, and some is my own.
    """
    
    def __init__(self, options, responses):
        self.options = options
        self.responses = responses
        self.bot_template = 'Madam Antoinelle: {0}'
    
    #send a message to the user by printing the bot's response
    def send_message(self, message):
        response = self.respond(message)
        print(self.bot_template.format(response))
    
    #determine bot response based on user input message
    def respond(self, message):
        if message in self.responses:
            return random.choice(self.responses[message])
        else:
            return random.choice(self.responses["default"])
        
    def start(self):
        """Displays a welcome message and prompts the user to input their name.
           Recieves user's name then prompts the user to ask about their fortune.
           Continuously listens for user input and responds accordingly until the user exits.
        """
        
        print('Greetings and Salutations! Welcome to your reading!\n'
              '\nMadam Antoinelle: What would you like me to call you?')
        user_name = input()
        print(self.bot_template.format('What a lovely name, {}!\n'
                                       'Please ask me about your fortune by asking' 
                                       ' \"What is my fortune?\"!'
                                       .format(user_name)))

        while True:
            #check if user input = exit to print goodbye message, else continue
            user_input = input().strip()
            if user_input.lower() == 'exit':
                print(self.bot_template.format('May the stars align our paths again!'))
                break
            self.send_message(user_input)
            
            #check if user input asks for a fortune then provide options to choose from
            if user_input.lower() == 'what is my fortune?':
                print(self.bot_template.format('In what area do you seek enlightenment? Pick one:'))
                print(', '.join(self.options))
                response = input().strip().capitalize()
                self.send_message(response)
            
            #check if user input = options and provide a tarot reading
            if response.lower() in [option.lower() for option in self.options]:
                reading = TarotReading(tarot_deck)
                reading.do_a_reading()
            else:
                print("Sorry, there was an issue with the tarot reading. Please try again.")
                
            print(self.bot_template.format('Anything else?'))
                  
options = ['Love', 'School', 'Work', 'Money', 'Family']

#dictionary of different responses to different categories to do a reading on
responses = {
 
    'What is my fortune?': [
       'Let me reveal your fortune!',
       'Let\'s see what the cards have in store for you!',
    ],
    
    'Love': [
        'Let\'s see what your love life has in store for you...',
        'The cards will tell us about your romantic endeavors...',
        'Ah, matters of the heart! Let\'s delve into your love life...',
    ],
 
    'School': [
        'What will the cards say about your education?',
        'Education is key! Let\'s see what the cards say...',
        'Let us explore your academic journey...'
    ],
    
    'Work': [
        'Hmmmm about your career, the stars say...',
        'Career insights coming right up!',
        'What do the cards say about your professional life...'
    ],
        
    'Money': [
        'What will the heavens say about your financial situation...',
        'Will you gain a large sum of money or lose it all...',
    ],
    
    'Family': [
        'How sweet of you, let\'s take a look...',
        'Family is important! Let me read your cards.',
        'How will your family life be affected?'
    ],
        
    'default': [
        'I am not sure I understand. Can you be more specific?',
        'Sorry, I\'m not quite getting it. Could you rephrase?'
    ]
}

fortune_teller = FortuneTeller(options, responses)
fortune_teller.start()