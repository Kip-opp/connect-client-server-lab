fetch("http://localhost:5000/events")
  .then(response => response.json())
  .then(events => {
    events.forEach(renderEvent);
  })
  .catch(error => console.error('Error fetching events:', error));

document.querySelector("form").addEventListener("submit", (e) => {
  e.preventDefault();
  const title = document.querySelector("#title").value;

  fetch("http://localhost:5000/events", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title })
  })
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(renderEvent)
  .then(() => {
    document.querySelector("#title").value = '';
  })
  .catch(error => console.error('Error posting event:', error));
});

function renderEvent(event) {
  const li = document.createElement("li");
  li.textContent = event.title;
  document.querySelector("#event-list").appendChild(li);
}