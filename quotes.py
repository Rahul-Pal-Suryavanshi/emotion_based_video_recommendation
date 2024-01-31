import random

quotes = [
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "The way to get started is to quit talking and begin doing.",
    "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle. As with all matters of the heart, you'll know when you find it.",
    "If life were predictable it would cease to be life, and be without flavor.",
    "It does not matter how slowly you go as long as you do not stop.",]

anger_quotes = ["Holding onto anger is like drinking poison and expecting the other person to die. - Buddha",
"An angry man opens his mouth and shuts his eyes. - Cato the Elder",
"Anger is a wind which blows out the lamp of the mind. - Robert G. Ingersoll",
"The greatest remedy for anger is delay. - Titus Livius",
"For every minute you remain angry, you give up sixty seconds of peace of mind. - Ralph Waldo Emerson",
"Anger is never without a reason, but seldom with a good one. - Benjamin Franklin",
"The best way to control your anger is to think before you act. - Anonymous",
"Anger is one letter short of danger. - Unknown",
"The things that cause anger are more apt to cure it. - Lucius Annaeus Seneca",
"The greatest man is he who does not lose his temper. - Confucius."]

happy_quotes = ["Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
"The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
"Happiness is a warm puppy. - Charles M. Schulz",
"Happiness is a journey, not a destination. - Ben Sweetland",
"Happiness is not a destination, it's a method of life. - Burton Hills",
"Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
"The greatest happiness you can have is knowing that you do not necessarily require happiness. - William Saroyan",
"Happiness is not the absence of problems, it's the ability to deal with them. - Steve Maraboli",
"The only way to find true happiness is to risk being completely cut open. - Chuck Palahniuk",
"Happiness is not a possession to be prized, it is a quality of thought, a state of mind. - Daphne Du Maurier."]

fear_quotes = ["Fear is not real. The only place that fear can exist is in our thoughts of the future. It is a product of our imagination, causing us to fear things that do not at present and may not ever exist. - Will Smith",
"Fear is inevitable, I have to accept that, but I cannot allow it to paralyze me. - Isabel Allende",
"Fear is the mind-killer. - Frank Herbert",
"Don't let yesterday take up too much of today. - Will Rogers",
"Fear is a darkroom where negatives develop. - Usman B. Asif",
"We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light. - Plato",
"Fear is temporary. Regret is forever. - Unknown",
"I learned that courage was not the absence of fear, but the triumph over it. The brave man is not he who does not feel afraid, but he who conquers that fear. - Nelson Mandela",
"Fear is the thief of dreams. - Unknown",
"Fear is not an option. It is a choice. - Coco Chanel."]

sad_quotes = ["Sadness is but a wall between two gardens. - Khalil Gibran",
"The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
"Tears are words the heart can't express. - Unknown",
"Sometimes the strongest among us are the ones who smile through silent pain, cry behind closed doors, and fight battles nobody knows about. - Unknown",
"Sadness is but a sunbeam in the heart. - Thomas Moore",
"We must embrace pain and burn it as fuel for our journey. - Kenji Miyazawa",
"Sadness flies away on the wings of time. - Jean de La Fontaine",
"Tears are often the telescope by which men see far into heaven. - Henry Ward Beecher",
"Sadness is an emotion that is often underestimated. - Unknown",
"Sadness is only for those who have not learned the art of mindfulness. - Thich Nhat Hanh.",]

surprise_quotes = ["Life is full of surprises, and they’re not always good. - Agatha Christie",
"The greatest discovery of my generation is that a human being can alter his life by altering his attitudes. - William James",
"Everyday holds the possibility of a miracle. - Elizabeth David",
"The only way to predict the future is to have power to shape the future. - Eric Hoffer",
"Life is a constant process of adjustment and surprise. - Marcel Proust",
"The best things in life are the people we love, the places we’ve been, and the memories we’ve made along the way. - Unknown",
"Every moment is a fresh beginning. - T.S. Eliot",
"Every day holds the possibility of a miracle. - Elizabeth David",
"Expect the unexpected. - Unknown",
"Life is full of surprises and serendipity. Being open to unexpected turns in the road is an important part of success. - Hilary Swank.",]

def quote(data):
    if data == "Anger":
        return random.choice(anger_quotes)
    
    elif data == "Neutral":
        return random.choice(quotes)
    
    elif data == "Fear":
        return random.choice(fear_quotes)
    
    elif data == "Sad":
        return random.choice(sad_quotes)
    
    elif data == "Happy":
        return random.choice(happy_quotes)
    
    elif data == "Surprise":
        return random.choice(surprise_quotes)
    