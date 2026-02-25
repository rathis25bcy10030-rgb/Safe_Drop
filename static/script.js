document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");
    const fileInput = document.querySelector("input[type='file']");
    const messageDisplay = document.getElementById("message");

    if (!form || !fileInput) {
        console.error("Form or file input not found.");
        return;
    }

    const allowedExtensions = ["pdf", "png", "jpg", "jpeg"];
    const maxSize = 5 * 1024 * 1024; // 5MB

    form.addEventListener("submit", function (event) {
        const file = fileInput.files[0];

        // Reset message on new attempt
        messageDisplay.innerText = ""; 

        if (!file) {
            messageDisplay.style.color = "#ff4c4c"; 
            messageDisplay.innerText = "Please select a file.";
            event.preventDefault();
            return;
        }

        if (file.size > maxSize) {
            messageDisplay.style.color = "#ff4c4c";
            messageDisplay.innerText = "File size exceeds 5MB limit.";
            event.preventDefault();
            return;
        }

        const fileExtension = file.name.split(".").pop().toLowerCase();

        if (!allowedExtensions.includes(fileExtension)) {
            messageDisplay.style.color = "#ff4c4c";
            messageDisplay.innerText = "Invalid file type. Only PDF, JPG, PNG allowed.";
            event.preventDefault();
            return;
        }

        // Display success message while the file is uploading to Python
        messageDisplay.style.color = "#00f5ff"; 
        messageDisplay.innerText = "File looks safe. Uploading to server...";
    });
});