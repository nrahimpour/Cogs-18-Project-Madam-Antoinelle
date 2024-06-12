"""A collection of function for doing my project."""

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
