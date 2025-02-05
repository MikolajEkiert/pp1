import json as j
content={
  "title": "The Enigma of Epsilon",
  "author": "Aria S. Hawthorne",
  "genre": "Science Fiction",
  "publication_year": 2021,
  "summary": "In a futuristic world where reality blurs with virtual realms, protagonist Alex Mercer discovers a hidden truth that challenges the very fabric of existence.",
  "main_characters": [
    {
      "name": "Alex Mercer",
      "role": "Protagonist",
      "description": "A brilliant hacker and tech enthusiast who stumbles upon a mysterious enigma that changes the course of their life."
    },
    {
      "name": "Epsilon",
      "role": "Enigmatic Entity",
      "description": "A sentient being that transcends the boundaries of reality and virtual space, holding the key to the secrets of the universe."
    }
  ],
  "themes": ["Virtual Reality", "Existentialism", "Technological Mysteries"],
  "rating": 4.8
}
with open('book.json', 'w') as f:
    j.dump(content, f, indent=4)