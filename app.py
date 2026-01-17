#!/usr/bin/env python3
"""
Vibe Oracle - A mystical mood divination experience
Answer abstract questions, receive cosmic wisdom
"""

import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# The Oracle's wisdom
TEXTURES = ["velvet", "static", "honey", "gravel", "fog", "lightning", "moss", "mercury"]
COLORS = ["burnt orange", "electric blue", "void black", "golden hour", "bruise purple", "seafoam", "rust", "neon pink"]
SOUNDS = ["distant thunder", "dial-up internet", "wind chimes", "muffled bass", "rain on tin", "vinyl crackle", "cathedral echo", "microwave hum"]
TIMES = ["3:47 AM", "golden hour", "the moment before lightning", "sunday morning", "eternal tuesday", "the hour between dog and wolf", "never o'clock", "deja vu"]
ELEMENTS = ["fire that doesn't burn", "water that remembers", "earth that dreams", "air that whispers secrets", "void that comforts", "light that weighs nothing", "shadow that protects"]

SPIRIT_ANIMALS = [
    {"name": "The Sleepy Capybara", "meaning": "You have mastered the art of unbothered existence. Your power is radical acceptance."},
    {"name": "The Philosophical Crow", "meaning": "You collect shiny thoughts. You see patterns others miss. You're probably right about that thing."},
    {"name": "The Anxious Hummingbird", "meaning": "Your energy is electric but scattered. You contain multitudes, possibly too many."},
    {"name": "The Melancholy Whale", "meaning": "You feel everything deeply. Your sadness is oceanic but so is your capacity for joy."},
    {"name": "The Chaotic Raccoon", "meaning": "You thrive in beautiful messes. Your 3 AM decisions are sometimes genius."},
    {"name": "The Ancient Tortoise", "meaning": "You're playing the long game. Time moves differently for you, and that's your advantage."},
    {"name": "The Dramatic Peacock", "meaning": "You were meant to be witnessed. Your presence is the point."},
    {"name": "The Skeptical Cat", "meaning": "You trust your instincts. You're right to be suspicious of that person."},
    {"name": "The Hopeful Moth", "meaning": "You're drawn to light even when it burns. Your optimism is both your weakness and superpower."},
    {"name": "The Overthinking Octopus", "meaning": "Eight arms, eight simultaneous anxieties. But also: eight solutions brewing."},
]

VIBE_READINGS = [
    "You're in your {texture} era. This is neither good nor bad—it simply is. Lean into the {texture}.",
    "The universe sees you vibrating at the frequency of {color}. This attracts: interesting strangers, minor inconveniences, unexpected compliments.",
    "Your soul currently sounds like {sound}. This will shift when you finally say the thing you've been avoiding.",
    "You exist at {time}—perpetually. This explains a lot, doesn't it?",
    "Your element today is {element}. Harness this by doing absolutely nothing about it.",
    "The void consulted its notes. You're exactly where you're supposed to be, which is annoying but true.",
    "Something you lost will return. Something you're holding too tightly wants to leave. Let it.",
    "Your ancestors are watching. They're confused by your phone but proud of your resilience.",
    "A door is closing. Another is opening. A third, secret door exists that you haven't noticed yet.",
    "The energy you put out this week will return threefold. Hopefully you were being normal.",
]

COSMIC_ADVICE = [
    "Drink water. Not because of health—because you're 60% ocean and the ocean is restless today.",
    "That thing you're procrastinating? It will take 15 minutes. You've spent 3 hours dreading it.",
    "Reply to the text. Or don't. The universe is indifferent but your friend is not.",
    "Your next breakthrough is disguised as a breakdown. Stay hydrated.",
    "The sign you've been looking for is: maybe just do the thing?",
    "Trust the timing. But also, time isn't real. But also, your deadline is.",
    "You already know the answer. You just don't like it.",
    "The call is coming from inside the house. The house is your own brain.",
    "Be delusional in your self-belief. The odds are made up anyway.",
    "Rest is not a reward. It's a requirement. The grind can wait.",
    "Some bridges are meant to be burned. Bring marshmallows.",
    "Your intuition is trying to tell you something. Possibly that you're tired.",
    "This, too, shall pass. Specifically, around 3 PM next Thursday.",
    "You contain galaxies. Unfortunately, so does everyone else. Adjust expectations accordingly.",
]


def generate_reading(answers):
    """Generate a personalized vibe reading based on answers."""
    # Use answers to seed randomness for consistency
    seed = hash(str(answers)) % 10000
    random.seed(seed)

    # Select spirit animal
    spirit_animal = random.choice(SPIRIT_ANIMALS)

    # Generate vibe description
    texture = random.choice(TEXTURES)
    color = random.choice(COLORS)
    sound = random.choice(SOUNDS)
    time = random.choice(TIMES)
    element = random.choice(ELEMENTS)

    reading_template = random.choice(VIBE_READINGS)
    reading = reading_template.format(
        texture=texture, color=color, sound=sound, time=time, element=element
    )

    # Cosmic advice
    advice = random.sample(COSMIC_ADVICE, 3)

    # Vibe percentage (always oddly specific)
    vibe_percent = random.randint(67, 94)

    # Reset random seed
    random.seed()

    return {
        "spirit_animal": spirit_animal,
        "reading": reading,
        "advice": advice,
        "vibe_percent": vibe_percent,
        "texture": texture,
        "color": color,
        "time": time,
        "element": element,
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/divine", methods=["POST"])
def divine():
    data = request.get_json()
    answers = data.get("answers", {})
    reading = generate_reading(answers)
    return jsonify(reading)


if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("  🔮 Vibe Oracle")
    print("=" * 50)
    print("\n  The Oracle awaits at: http://localhost:5010")
    print("  Press Ctrl+C to close the portal\n")
    app.run(debug=True, port=5010)
