dnd_races = {
    # Core Races
    "Human": "Versatile and adaptable, with extra skills or ability score boosts.",
    "Elf": "Graceful and long-lived, often skilled in magic or archery.",
    "Dwarf": "Hardy and strong, known for resilience, craftsmanship, and battle prowess.",
    "Halfling": "Small and lucky, often stealthy and nimble.",
    "Gnome": "Clever and inventive, often associated with illusions and tinkering.",
    "Half-Elf": "A mix of human and elf traits, charismatic and adaptable.",
    "Half-Orc": "Strong and intimidating, often excelling in combat.",

    # Expanded & Popular Races
    "Dragonborn": "Draconic humanoids with breath weapons and resistance to certain damage types.",
    "Tiefling": "Descendants of fiends, often charismatic and resistant to fire, with innate magic.",
    "Aasimar": "Celestial-touched beings with divine magic and radiant abilities.",
    "Firbolg": "Large, gentle forest dwellers with nature-based magic.",
    "Goliath": "Mountain-dwelling giants with great physical power.",
    "Tabaxi": "Agile cat-people with keen senses and curiosity.",
    "Kenku": "Raven-like humanoids that mimic sounds and are natural rogues.",
    "Tortle": "Turtle-like beings with natural armor and a love for exploration.",
    "Lizardfolk": "Cold-blooded reptilian beings with a survivalist mindset.",
    "Hobgoblin": "Martial and disciplined, excelling in teamwork.",
    "Orc": "Strong, aggressive warriors, often with endurance-focused traits.",
    "Kobold": "Small draconic creatures with teamwork abilities and trap-making skills.",
    "Yuan-ti Pureblood": "Serpent-like beings with innate magic and poison resistance.",

    # Exotic & Setting-Specific Races
    "Warforged": "Sentient constructs built for war but seeking purpose.",
    "Changeling": "Shapechangers that can alter their appearance at will.",
    "Shifter": "Were-creature hybrids with temporary boosts to physical abilities.",
    "Githyanki": "Astral travelers with martial and psionic abilities.",
    "Githzerai": "Psionic monks with strong mental discipline.",
    "Kalashtar": "Psychic beings bound to dream-spirits.",
    "Simic Hybrid": "Genetically modified creatures with animalistic traits.",
    "Vedalken": "Logical, emotion-controlled humanoids focused on intellect.",
    "Triton": "Aquatic beings with resistance to cold and water-based abilities.",
    "Owlin": "Owl-like humanoids with flight and keen senses.",

    # Anthropomorphic & Unique Races
    "Harengon": "Rabbit-like humanoids with great agility.",
    "Minotaur": "Large, labyrinth-dwelling warriors.",
    "Satyr": "Fey creatures with natural charisma and charm.",
    "Leonin": "Lion-like warriors with prideful traditions.",
    "Loxodon": "Elephantine beings with wisdom and great endurance."
}
dnd_race_stats = {
    # Core Races
    "Human": {'Strength': 10, 'Dexterity': 10, 'Constitution': 10, 'Wisdom': 10, 'Intelligence': 10, 'Charisma': 10},
    "Elf": {'Strength': 8, 'Dexterity': 14, 'Constitution': 10, 'Wisdom': 12, 'Intelligence': 12, 'Charisma': 10},
    "Dwarf": {'Strength': 12, 'Dexterity': 8, 'Constitution': 14, 'Wisdom': 12, 'Intelligence': 10, 'Charisma': 10},
    "Halfling": {'Strength': 8, 'Dexterity': 14, 'Constitution': 12, 'Wisdom': 10, 'Intelligence': 10, 'Charisma': 12},
    "Gnome": {'Strength': 8, 'Dexterity': 12, 'Constitution': 10, 'Wisdom': 10, 'Intelligence': 14, 'Charisma': 12},
    "Half-Elf": {'Strength': 10, 'Dexterity': 12, 'Constitution': 10, 'Wisdom': 10, 'Intelligence': 10, 'Charisma': 14},
    "Half-Orc": {'Strength': 14, 'Dexterity': 10, 'Constitution': 12, 'Wisdom': 10, 'Intelligence': 8, 'Charisma': 10},

    # Expanded & Popular Races
    "Dragonborn": {'Strength': 14, 'Dexterity': 10, 'Constitution': 12, 'Wisdom': 10, 'Intelligence': 8, 'Charisma': 12},
    "Tiefling": {'Strength': 8, 'Dexterity': 10, 'Constitution': 10, 'Wisdom': 10, 'Intelligence': 12, 'Charisma': 14},
    "Aasimar": {'Strength': 10, 'Dexterity': 10, 'Constitution': 10, 'Wisdom': 12, 'Intelligence': 10, 'Charisma': 14},
    "Firbolg": {'Strength': 12, 'Dexterity': 8, 'Constitution': 12, 'Wisdom': 14, 'Intelligence': 10, 'Charisma': 10},
    "Goliath": {'Strength': 14, 'Dexterity': 10, 'Constitution': 14, 'Wisdom': 10, 'Intelligence': 8, 'Charisma': 8},
    "Tabaxi": {'Strength': 10, 'Dexterity': 14, 'Constitution': 10, 'Wisdom': 10, 'Intelligence': 12, 'Charisma': 12},
    "Kenku": {'Strength': 8, 'Dexterity': 14, 'Constitution': 10, 'Wisdom': 12, 'Intelligence': 12, 'Charisma': 8},
    "Tortle": {'Strength': 14, 'Dexterity': 8, 'Constitution': 14, 'Wisdom': 12, 'Intelligence': 10, 'Charisma': 8},
    "Lizardfolk": {'Strength': 12, 'Dexterity': 10, 'Constitution': 12, 'Wisdom': 12, 'Intelligence': 8, 'Charisma': 8},
    "Hobgoblin": {'Strength': 12, 'Dexterity': 12, 'Constitution': 12, 'Wisdom': 10, 'Intelligence': 10, 'Charisma': 8},
    "Orc": {'Strength': 14, 'Dexterity': 10, 'Constitution': 14, 'Wisdom': 8, 'Intelligence': 8, 'Charisma': 10},
    "Kobold": {'Strength': 8, 'Dexterity': 14, 'Constitution': 10, 'Wisdom': 8, 'Intelligence': 10, 'Charisma': 12},
    "Yuan-ti Pureblood": {'Strength': 8, 'Dexterity': 10, 'Constitution': 10, 'Wisdom': 12, 'Intelligence': 14, 'Charisma': 12},

    # Exotic & Setting-Specific Races
    "Warforged": {'Strength': 14, 'Dexterity': 10, 'Constitution': 14, 'Wisdom': 10, 'Intelligence': 10, 'Charisma': 8},
    "Changeling": {'Strength': 8, 'Dexterity': 12, 'Constitution': 10, 'Wisdom': 10, 'Intelligence': 12, 'Charisma': 14},
    "Shifter": {'Strength': 12, 'Dexterity': 14, 'Constitution': 12, 'Wisdom': 10, 'Intelligence': 8, 'Charisma': 8},
    "Githyanki": {'Strength': 12, 'Dexterity': 12, 'Constitution': 10, 'Wisdom': 10, 'Intelligence': 12, 'Charisma': 8},
    "Githzerai": {'Strength': 8, 'Dexterity': 14, 'Constitution': 10, 'Wisdom': 12, 'Intelligence': 12, 'Charisma': 8},
    "Kalashtar": {'Strength': 8, 'Dexterity': 10, 'Constitution': 10, 'Wisdom': 12, 'Intelligence': 12, 'Charisma': 14},
    "Simic Hybrid": {'Strength': 12, 'Dexterity': 12, 'Constitution': 12, 'Wisdom': 10, 'Intelligence': 10, 'Charisma': 8},
    "Vedalken": {'Strength': 8, 'Dexterity': 10, 'Constitution': 10, 'Wisdom': 12, 'Intelligence': 14, 'Charisma': 8},
    "Triton": {'Strength': 12, 'Dexterity': 10, 'Constitution': 12, 'Wisdom': 10, 'Intelligence': 10, 'Charisma': 10},
    "Owlin": {'Strength': 8, 'Dexterity': 14, 'Constitution': 10, 'Wisdom': 12, 'Intelligence': 12, 'Charisma': 10},

    # Anthropomorphic & Unique Races
    "Harengon": {'Strength': 10, 'Dexterity': 14, 'Constitution': 10, 'Wisdom': 12, 'Intelligence': 10, 'Charisma': 12},
    "Minotaur": {'Strength': 14, 'Dexterity': 10, 'Constitution': 14, 'Wisdom': 8, 'Intelligence': 8, 'Charisma': 8},
    "Satyr": {'Strength': 8, 'Dexterity': 12, 'Constitution': 10, 'Wisdom': 10, 'Intelligence': 10, 'Charisma': 14},
    "Leonin": {'Strength': 14, 'Dexterity': 12, 'Constitution': 12, 'Wisdom': 10, 'Intelligence': 10, 'Charisma': 8},
    "Loxodon": {'Strength': 14, 'Dexterity': 8, 'Constitution': 14, 'Wisdom': 12, 'Intelligence': 10, 'Charisma': 8}
}
