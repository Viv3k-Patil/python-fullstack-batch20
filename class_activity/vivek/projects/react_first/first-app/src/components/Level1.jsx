import React, { useState, useEffect } from "react";

function App() {
  const [weather, setWeather] = useState(null);

  useEffect(() => {
    fetch(
    "https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
  )
    .then((res) => res.json())
    .then((data) => setWeather(data.current));

    console.log("re-render")
  }, [])
  

  return (
    <div>
      <h1>Weather App - Level 1</h1>

      {weather && (
        <div>
          <h2>Current Weather</h2>
          <p>Temperature: {weather.temperature_2m} °C</p>
          <p>Humidity: {weather.relative_humidity_2m}%</p>
          <p>Wind Speed: {weather.wind_speed_10m} km/h</p>
        </div>
      )}
    </div>
  );
}

export default App;