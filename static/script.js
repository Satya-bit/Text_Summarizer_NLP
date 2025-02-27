function startTypingEffect(text) {
    let outputDiv = document.getElementById("output-container");
    let index = 0;

    function typeEffect() {
        if (index < text.length) {
            outputDiv.innerHTML += text.charAt(index);
            index++;
            setTimeout(typeEffect, 50); // Adjust typing speed here
        }
    }
    
    typeEffect(); // Start the effect
}
