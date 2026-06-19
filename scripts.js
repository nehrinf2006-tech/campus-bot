async function sendMessage() {

    const input = document.getElementById("prompt");
    const chatBox = document.getElementById("chat-box");

    const message = input.value.trim();

    if(message === "") return;

    chatBox.innerHTML += `
        <div class="user-message">
            ${message}
        </div>
    `;

    input.value = "";

    try{

        const response = await fetch("http://127.0.0.1:8000/chat",{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                message:message
            })
        });

        const data = await response.json();

        chatBox.innerHTML += `
            <div class="bot-message">
                ${data.reply}
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

    }catch(error){

        chatBox.innerHTML += `
            <div class="bot-message">
                Server connection failed.
            </div>
        `;
    }
}