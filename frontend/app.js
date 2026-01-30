const API_URL = "http://localhost:8000/events";

async function fetchEvents() {
  try {
    const res = await fetch(API_URL);
    const events = await res.json();

    const container = document.getElementById("events");
    container.innerHTML = "";

    if (events.length === 0) {
      container.innerHTML = "<p>No events yet</p>";
      return;
    }

    events.forEach(e => {
      const p = document.createElement("p");
      p.textContent = e.message;
      container.appendChild(p);
    });
  } catch (err) {
    console.error("Fetch failed:", err);
  }
}

fetchEvents();

setInterval(fetchEvents, 15000);
