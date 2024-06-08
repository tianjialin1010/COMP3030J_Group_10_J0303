<template>
  <div class="chat-container">
    <div class="chat-area" id="chatArea">
      <div v-for="(message, index) in messages" :key="index" :class="messageClass(message.sender)">
        {{ message.text }}
      </div>
    </div>
    <div class="input-container">
      <input type="text" v-model="userInput" placeholder="Type your message here..." @keyup.enter="sendChat">
      <button @click="sendChat">Send</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userInput: '',
      messages: []
    };
  },
  methods: {
    sendChat() {
      let userInput = this.userInput.trim();
      if (!userInput) return; // Don't send empty messages

      this.appendMessage(userInput, 'user');

      // Clear input after sending
      this.userInput = '';

      // Simulate sending to an API
      axios.post('/chat', { message: userInput })
        .then(response => {
          this.appendMessage(response.data.answer, 'bot');
        })
        .catch(error => {
          console.error('Error:', error);
          this.appendMessage('Failed to get response.', 'bot');
        });
    },
    appendMessage(text, sender) {
      this.messages.push({ text: text, sender: sender });
    },
    messageClass(sender) {
      return sender === 'user' ? 'user-message' : 'bot-message';
    }
  }
}
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  justify-content: flex-end;
  padding: 20px;
}
.chat-area {
  flex-grow: 1;
  overflow-y: auto;
  padding: 10px;
  border: 1px solid #ccc;
  margin-bottom: 10px;
}
.input-container {
  display: flex;
  padding: 10px;
}
.input-container input {
  flex-grow: 1;
  padding: 10px;
  margin-right: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.input-container button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}
.input-container button:hover {
  background-color: #0056b3;
}
.message {
  margin: 5px 0;
  padding: 10px;
  border-radius: 10px;
  max-width: 100%;
}
.user-message {
  background-color: #dcf8c6;
  align-self: flex-end;
}
.bot-message {
  background-color: #e5e5ea;
  align-self: flex-start;
}
</style>
