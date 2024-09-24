 //countdown timer
 let countdownTime = 600; // Countdown time in seconds (10 minutes)
 let timerInterval;
 
 const countdownDisplay = document.getElementById("countdown");
 const startButton = document.getElementById("startBtn");
 const resetButton = document.getElementById("resetBtn");
 
 function startCountdown() {
     clearInterval(timerInterval); // Clear any existing intervals
     timerInterval = setInterval(() => {
         if (countdownTime <= 0) {
             clearInterval(timerInterval);
             alert("Time's up!");
             return;
         }
 
         countdownTime--;
         updateDisplay();
     }, 1000);
 }
 
 function resetCountdown() {
     clearInterval(timerInterval);
     countdownTime = 600; // Reset to 10 minutes
     updateDisplay();
 }
 
 function updateDisplay() {
     const minutes = Math.floor(countdownTime / 60);
     const seconds = countdownTime % 60;
 
     countdownDisplay.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
 }
 
 // Event Listeners
 startButton.addEventListener("click", startCountdown);
 resetButton.addEventListener("click", resetCountdown);
 
 // Initial display
 updateDisplay();

 //chat bot 
 const chatbotToggler = document.querySelector(".chatbot-toggler");
  const closeBtn = document.querySelector(".close-btn");
  const chatbox = document.querySelector(".chatbox");
  const chatInput = document.querySelector(".chat-input textarea");
  const sendChatBtn = document.querySelector(".chat-input i");
  
  let userMessage = null; // Variable to store user's message
  const inputInitHeight = chatInput.scrollHeight;
  
  // API configuration
  const API_KEY = "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"; // Your API key here
  const API_URL = `https://api.groq.com/openai/v1/chat/completions`;
  
  const createChatLi = (message, className) => {
      // Create a chat <li> element with passed message and className
      const chatLi = document.createElement("li");
      chatLi.classList.add("chat", `${className}`);
      let chatContent = className === "outgoing" ? `<p></p>` : `<i class="fa-solid fa-circle-user"></i><p></p>`;
      chatLi.innerHTML = chatContent;
      chatLi.querySelector("p").textContent = message;
      return chatLi; // return chat <li> element
  }
  
  const generateResponse = async (chatElement) => {
      const messageElement = chatElement.querySelector("p");    
          const data = {
              messages: [
                  {
                      role: 'user',
                      content: userMessage,
                  },
              ],
              model: 'llama3-8b-8192', // Specify the model you want to use
          };
  
          try {
              const response = await fetch(API_URL, {
                  method: 'POST',
                  headers: {
                      'Authorization': `Bearer ${API_KEY}`,
                      'Content-Type': 'application/json',
                  },
                  body: JSON.stringify(data), // Convert data to JSON string
              });
  
              if (!response.ok) {
                  throw new Error(`HTTP error! Status: ${response.status}`);
              }
  
              const responseData = await response.json(); // Parse JSON response
              // console.log('Response from API:', responseData.choices[0].message.content);
              messageElement.textContent = responseData.choices[0].message.content
          } catch (error) {
              // Handle error
              messageElement.classList.add("error");
              messageElement.textContent = error.message;
          } finally {
              chatbox.scrollTo(0, chatbox.scrollHeight);
          }
      
  }
      const handleChat = () => {
          userMessage = chatInput.value.trim(); // Get user entered message and remove extra whitespace
          if (!userMessage) return;
  
          // Clear the input textarea and set its height to default
          chatInput.value = "";
          chatInput.style.height = `${inputInitHeight}px`;
  
          // Append the user's message to the chatbox
          chatbox.appendChild(createChatLi(userMessage, "outgoing"));
          chatbox.scrollTo(0, chatbox.scrollHeight);
  
          setTimeout(() => {
              // Display "Thinking..." message while waiting for the response
              const incomingChatLi = createChatLi("Thinking...", "incoming");
              chatbox.appendChild(incomingChatLi);
              chatbox.scrollTo(0, chatbox.scrollHeight);
              generateResponse(incomingChatLi);
          }, 600);
      }
  
      chatInput.addEventListener("input", () => {
          // Adjust the height of the input textarea based on its content
          chatInput.style.height = `${inputInitHeight}px`;
          chatInput.style.height = `${chatInput.scrollHeight}px`;
      });
  
      chatInput.addEventListener("keydown", (e) => {
          // If Enter key is pressed without Shift key and the window 
          // width is greater than 800px, handle the chat
          if (e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
              e.preventDefault();
              handleChat();
          }
      });
  
      sendChatBtn.addEventListener("click", handleChat);
      closeBtn.addEventListener("click", () => document.body.classList.remove("show-chatbot"));
      chatbotToggler.addEventListener("click", () => document.body.classList.toggle("show-chatbot"));

    