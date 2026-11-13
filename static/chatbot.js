
(() => {
  "use strict";

  const root = document.getElementById("learning-hub-chat");
  if (!root) return;

  const endpoint = root.dataset.endpoint;
  const subjectKey = root.dataset.subjectKey || "";
  const lessonId = root.dataset.lessonId || "";

  const toggleButton = document.getElementById("chat-toggle");
  const closeButton = document.getElementById("chat-close");
  const panel = document.getElementById("chat-panel");
  const messagesContainer = document.getElementById("chat-messages");
  const typingIndicator = document.getElementById("chat-typing");
  const form = document.getElementById("chat-form");
  const input = document.getElementById("chat-input");
  const sendButton = document.getElementById("chat-send");

  if (
    !endpoint ||
    !toggleButton ||
    !closeButton ||
    !panel ||
    !messagesContainer ||
    !typingIndicator ||
    !form ||
    !input ||
    !sendButton
  ) {
    return;
  }

  let history = [];
  let isSending = false;

  panel.hidden = true;
  panel.style.display = "none";

  function openChat() {
    panel.hidden = false;
    panel.style.display = "flex";
    toggleButton.setAttribute("aria-expanded", "true");
    input.focus();
  }

  function closeChat() {
    panel.hidden = true;
    panel.style.display = "none";
    toggleButton.setAttribute("aria-expanded", "false");
    toggleButton.focus();
  }

  function scrollToBottom() {
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }

  function renderMath(element) {
    if (typeof window.renderMathInElement !== "function") return;

    window.renderMathInElement(element, {
      delimiters: [
        { left: "\\[", right: "\\]", display: true },
        { left: "\\(", right: "\\)", display: false }
      ],
      throwOnError: false,
      strict: "ignore",
      trust: false
    });
  }

  function addMessage(text, sender) {
    const message = document.createElement("div");
    message.className =
      sender === "user"
        ? "chat-message user-message"
        : "chat-message assistant-message";

    const bubble = document.createElement("div");
    bubble.className = "chat-bubble";

    // Use textContent so model responses cannot inject HTML or scripts.
    bubble.textContent = String(text);
    bubble.style.whiteSpace = "pre-wrap";

    message.appendChild(bubble);
    messagesContainer.appendChild(message);

    renderMath(bubble);
    scrollToBottom();

    return message;
  }

  function setSending(sending) {
    isSending = sending;
    sendButton.disabled = sending;
    input.disabled = sending;
    typingIndicator.hidden = !sending;
    scrollToBottom();
  }

  function keepRecentHistory() {
    history = history.slice(-10);
  }

  async function sendMessage() {
    const messageText = input.value.trim();

    if (!messageText || isSending) return;

    addMessage(messageText, "user");
    input.value = "";
    input.style.height = "auto";

    setSending(true);

    try {
      const payload = {
        message: messageText,
        history: history.slice(-10)
      };

      if (subjectKey) {
        payload.subject_key = subjectKey;
      }

      if (lessonId && Number.isInteger(Number(lessonId))) {
        payload.lesson_id = Number(lessonId);
      }

      const response = await fetch(endpoint, {
        method: "POST",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
      });

      let data;

      try {
        data = await response.json();
      } catch {
        throw new Error("The server returned an unexpected response. Please refresh the page and try again.");
      }

      if (!response.ok || typeof data.reply !== "string") {
        throw new Error(
          typeof data.error === "string"
            ? data.error
            : "I couldn't get a response. Please try again."
        );
      }

      const reply = data.reply.trim();

      addMessage(reply, "assistant");

      history.push(
        { role: "user", text: messageText },
        { role: "model", text: reply }
      );

      keepRecentHistory();
    } catch (error) {
      addMessage(
        error.message || "Something went wrong. Please try again.",
        "assistant"
      );
    } finally {
      setSending(false);
      input.focus();
    }
  }

  toggleButton.addEventListener("click", openChat);
  closeButton.addEventListener("click", closeChat);

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    sendMessage();
  });

  input.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      form.requestSubmit();
    }
  });

  input.addEventListener("input", () => {
    input.style.height = "auto";
    input.style.height = `${Math.min(input.scrollHeight, 120)}px`;
  });
})();
