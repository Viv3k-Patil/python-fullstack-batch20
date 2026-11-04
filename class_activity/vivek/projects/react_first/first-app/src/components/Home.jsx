
import React from "react";
import {
  BrowserRouter,
  Routes,
  Route,
  Link
} from "react-router-dom";

import "./App.css";

// Home Component
function Home() {
  return (
    <div className="page">
      <h1>Welcome to Home Page</h1>
      <p>This is our home page. Welcome to our website!</p>
    </div>
  );
}

// About Component
function About() {
  return (
    <div className="page">
      <h1>About Us</h1>
      <p>
        We are a company focused on providing
        the best services to our customers.
      </p>
    </div>
  );
}

// Contact Component
function Contact() {
  return (
    <div className="page">
      <h1>Contact Us</h1>
      <p>Email: example@gmail.com</p>
      <p>Phone: +91 9876543210</p>
    </div>
  );
}

// Main App Component
function App() {
  return (
    <BrowserRouter>

      <nav className="navbar">
        <h2>NewGen Institute</h2>

        <div className="nav-links">

          <Link to="/">Home</Link>

          <Link to="/about">About</Link>

          <Link to="/contact">Contact</Link>

        </div>
      </nav>

      <main>
        <Routes>

          <Route path="/" element={<Home />} />
          <Route path='/home' element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />

        </Routes>
      </main>

    </BrowserRouter>
  );
}

export default App;
