const landing = document.getElementById("landing");
const chatView = document.getElementById("chat-view");
const messageInput = document.getElementById("message-input");

// "Start talking" button: hide the welcome page, show the chat
document.getElementById("start-btn").addEventListener("click", () => {
  landing.classList.remove("active");
  chatView.classList.add("active");
  setTimeout(() => messageInput.focus(), 500);
});

// "Back" button: return to the welcome page
document.getElementById("back-btn").addEventListener("click", () => {
  chatView.classList.remove("active");
  landing.classList.add("active");
});
