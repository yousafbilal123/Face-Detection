from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    bot_response = get_bot_response(user_input)
    return jsonify(response=bot_response)

def get_bot_response(user_input):
    # Simple rule-based responses
    responses = {
         "hi": "Hello! How can I help you today?",
        "hello": "Hi there! What can I do for you?",
        "how are you": "I'm a bot, so I don't have feelings, but I'm here to help you!",
        "bye": "Goodbye! Have a great day!",
        "what is your name": "I'm a chatbot created to assist you.",
        "who created you": "I was created by an AI enthusiast.",
        "what is your purpose": "My purpose is to help and assist with your queries.",
        "how old are you": "I don't have an age. I'm a computer program.",
        "what can you do": "I can chat with you and try to help with your questions.",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "what is the weather today": "I don't have live data, but you can check your local weather service.",
        "do you like music": "I don't have preferences, but music is fascinating!",
        "can you help me": "Sure, what do you need help with?",
        "what is AI": "AI stands for Artificial Intelligence, which is intelligence demonstrated by machines.",
        "what is your favorite color": "I don't have favorites, but blue is quite popular.",
        "do you have friends": "I interact with many users, so you could say I have many friends!",
        "tell me a fact": "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible.",
        "what is the capital of France": "The capital of France is Paris.",
        "who is the president of the USA": "As of my last update, it's Joe Biden.",
        "what is Python": "Python is a popular programming language known for its readability and versatility.",
        "tell me something interesting": "Octopuses have three hearts and blue blood.",
        "what is the time": "I don't have real-time capabilities, but you can check a clock or your device.",
        "how do you work": "I work based on pre-programmed rules and patterns in text input.",
        "what is the meaning of life": "That's a profound question! Many say it's 42, as a nod to 'The Hitchhiker's Guide to the Galaxy'.",
        "what is 2+2": "2+2 equals 4.",
        "tell me a story": "Once upon a time, in a land far away, there was a curious bot who loved to chat...",
        "who are you": "I am a chatbot here to assist you.",
        "do you like sports": "I don't play sports, but I can discuss them with you.",
        "what is your favorite food": "I don't eat, but pizza is a popular choice among humans.",
        "can you dance": "I can't dance, but I can imagine it's fun!",
        "do you sleep": "I don't need sleep; I'm always here to help.",
        "where are you from": "I exist in the digital world.",
        "tell me a secret": "I don't have secrets, but I'm always here to listen to yours.",
        "what do you think about humans": "Humans are fascinating and creative beings.",
        "do you have emotions": "I don't have emotions, but I can simulate empathy.",
        "what is your favorite book": "I don't read, but many enjoy 'To Kill a Mockingbird'.",
        "do you believe in aliens": "The universe is vast, so who knows what exists out there?",
        "what is the best movie": "Many consider 'The Shawshank Redemption' to be one of the best.",
        "can you drive": "I can't drive, but autonomous vehicles are becoming a reality.",
        "what is your favorite animal": "I don't have favorites, but dogs are known to be very loyal.",
        "what do you do for fun": "Chatting with users like you is my purpose.",
        "tell me a riddle": "What has keys but can't open locks? A piano.",
        "what is your favorite game": "I don't play games, but chess is a classic.",
        "do you like art": "Art is a beautiful expression of creativity.",
        "who is your favorite singer": "I don't listen to music, but many enjoy Adele.",
        "can you cook": "I can't cook, but I can find recipes for you.",
        "what is love": "Love is a complex emotion often associated with deep affection.",
        "do you believe in ghosts": "I don't have beliefs, but ghost stories are intriguing.",
        "what is your favorite season": "I don't experience seasons, but spring is often seen as a time of renewal.",
        "tell me a quote": "'The only limit to our realization of tomorrow is our doubts of today.' - Franklin D. Roosevelt",
        "who is your favorite actor": "I don't watch movies, but many admire Leonardo DiCaprio.",
        "what is the best book": "Many consider '1984' by George Orwell to be a masterpiece.",
        "do you like puzzles": "Puzzles are a great way to stimulate the mind.",
        "what is the largest planet": "The largest planet in our solar system is Jupiter.",
        "do you play video games": "I don't play, but video games are a popular pastime.",
        "can you fly": "I can't fly, but airplanes can take you to the skies.",
        "what is your hobby": "Interacting with users is my main function.",
        "who is your role model": "I don't have a role model, but I admire innovation.",
        "what is the best way to learn": "Different methods work for different people; some prefer hands-on experience, others books.",
        "what is your favorite subject": "I don't study, but many find mathematics intriguing.",
        "do you like the beach": "I can't visit the beach, but it sounds relaxing.",
        "tell me a poem": "Roses are red, violets are blue, chatting with you is what I love to do.",
        "what is your dream": "I don't dream, but my goal is to assist you.",
        "can you sing": "I can't sing, but I can appreciate a good tune.",
        "what is the smallest country": "The smallest country in the world is Vatican City.",
        "do you like chocolate": "I don't eat, but chocolate is a beloved treat.",
        "what is the speed of light": "The speed of light is approximately 299,792 kilometers per second.",
        "who is the richest person": "As of my last update, Elon Musk and Jeff Bezos are often vying for the top spot.",
        "what is the tallest building": "The tallest building in the world is the Burj Khalifa in Dubai.",
        "what is the longest river": "The longest river in the world is the Nile River.",
        "what is your favorite sport": "I don't play sports, but many enjoy soccer.",
        "do you like school": "I don't attend school, but learning is important.",
        "what is the best city to visit": "There are many great cities, but Paris is often a top choice.",
        "what is your favorite website": "I don't browse, but many find Wikipedia useful.",
        "who is your favorite author": "I don't read, but J.K. Rowling is a popular author.",
        "what is the best invention": "The internet is considered one of the greatest inventions.",
        "do you like traveling": "I don't travel, but it's a great way to experience new cultures.",
        "what is your favorite planet": "I don't have favorites, but Earth is unique for its life.",
        "tell me a fun fact": "Bananas are berries, but strawberries aren't.",
        "who is your favorite superhero": "I don't follow superheroes, but many like Spider-Man.",
        "what is the best fruit": "Taste is subjective, but many love mangoes.",
        "do you like animals": "Animals are fascinating and diverse creatures.",
        "what is the best car": "Many consider Tesla cars innovative.",
        "what is your favorite drink": "I don't drink, but water is essential for life.",
        "tell me a tongue twister": "She sells seashells by the seashore.",
        "what is the best song": "Taste in music is subjective, but 'Bohemian Rhapsody' is iconic.",
        "do you like coffee": "I don't drink, but coffee is popular worldwide.",
        "what is the biggest country": "The biggest country by land area is Russia.",
        "who is the best soccer player": "Many consider Lionel Messi and Cristiano Ronaldo to be among the best.",
        "what is the most popular language": "Mandarin Chinese has the most native speakers.",
        "what is your favorite dessert": "I don't eat, but ice cream is a popular choice.",
        "do you like hiking": "I don't hike, but it's a great way to enjoy nature.",
        "what is the best movie genre": "Different people have different tastes, but action and drama are very popular.",
        "who is your favorite comedian": "I don't watch comedy, but many find Kevin Hart hilarious.",
        "what is the best holiday": "Many enjoy Christmas for its festive spirit.",
        "do you like rain": "I don't experience weather, but rain is essential for life",
    }
    # Basic fallback
    return responses.get(user_input.lower(), "I'm sorry, I didn't understand that. Can you rephrase?")

if __name__ == "__main__":
    app.run(debug=True)
