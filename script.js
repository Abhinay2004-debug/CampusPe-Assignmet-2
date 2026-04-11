$(document).ready(function () {

  const responses = [
    "That's interesting!",
    "Tell me more.",
    "I can help with that.",
    "Here's what I think..."
  ];

  const messages = $(".messages");
  const input = $("#messageInput");
  const sendBtn = $("#sendBtn");
  const typing = $(".typing-indicator");

  // Enable send button
  input.on("input", function () {
    sendBtn.prop("disabled", input.val().trim() === "");
    this.style.height = "auto";
    this.style.height = this.scrollHeight + "px";
  });

  // Send message
  function addMessage(text, sender) {
    const msg = `<div class="message ${sender}">${text}</div>`;
    messages.append(msg);
    scrollBottom();
  }

  function scrollBottom() {
    messages.scrollTop(messages[0].scrollHeight);
  }

  function sendMessage() {
    const text = input.val().trim();
    if (!text) return;

    addMessage(text, "user");
    input.val("");
    sendBtn.prop("disabled", true);

    $(".welcome-screen").hide();

    typing.removeClass("d-none");

    setTimeout(() => {
      typing.addClass("d-none");
      const reply = responses[Math.floor(Math.random() * responses.length)];
      addMessage(reply, "ai");
    }, 1500);
  }

  // Button click
  sendBtn.click(sendMessage);

  // Enter key
  input.keypress(function (e) {
    if (e.which === 13 && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });

  // Sidebar toggle
  $("#menuBtn").click(function () {
    $(".sidebar").toggleClass("active");
  });

});