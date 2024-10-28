document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("profile-form");
    const progressBarFill = document.getElementById("progress-bar-fill");


    const requiredFields = Array.from(form.elements).filter((field) => field.hasAttribute("required"));
    const totalFields = requiredFields.length;


    function updateProgressBar() {
        let completedFields = requiredFields.filter((field) => field.value.trim() !== "").length;
        let progress = Math.round((completedFields / totalFields) * 100);
        
        progressBarFill.style.width = `${progress}%`;
        progressBarFill.textContent = `${progress}%`;
    }


    requiredFields.forEach((field) => {
        field.addEventListener("input", updateProgressBar);
    });


    updateProgressBar();
});
