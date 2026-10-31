function ThemeDemo() {
    const isDark = false;

    return (
        <div style={{
            backgroundColor: isDark ? "#222" : "white",
            color: isDark ? "white" : "black",
            padding: "20px",
            borderRadius: "10px"
        }}>
            <h2>{isDark ? "🌙 Dark Mode" : "☀️ Light Mode"}</h2>

            <p>
                {isDark
                    ? "Welcome to Dark Mode! 😎"
                    : "Welcome to Light Mode! 😊"}
            </p>
        </div>
    );
}

export default ThemeDemo;