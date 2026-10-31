function HeroList() {
    const heroes = [
        { id: 1, emoji: "🕷️", name: "Spider-Man", power: "Web-Slinging", age: 25 },
        { id: 2, emoji: "🤖", name: "Iron Man", power: "Genius Inventor", age: 48 },
        { id: 3, emoji: "⚡", name: "Thor", power: "Lightning", age: 1500 },
        { id: 4, emoji: "💪", name: "Hulk", power: "Super Strength", age: 40 },
        { id: 5, emoji: "🔮", name: "Doctor Strange", power: "Magic", age: 42 },
    ];

    return (
        <div>
            { /* this is comment */ }
            <h2>🦸 Superhero List 🦸‍♀️</h2>
            <ul>
                {heroes.map((hero) => (
                    <li key={hero.id}>
                        {hero.emoji} Hero: {hero.name} |
                        ⚡ Power: {hero.power} |
                        🎂 Age: {hero.age}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default HeroList;