document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("profile-form");
    const progressBarFill = document.getElementById("progress-bar-fill");

    // Required fields for profile completion
    const requiredFields = Array.from(form.elements).filter((field) => field.hasAttribute("required"));
    const totalFields = requiredFields.length;

    // Update progress bar based on form completion
    function updateProgressBar() {
        let completedFields = requiredFields.filter((field) => field.value.trim() !== "").length;
        let progress = Math.round((completedFields / totalFields) * 100);
        
        progressBarFill.style.width = `${progress}%`;
        progressBarFill.textContent = `${progress}%`;
    }

    // Event listener for each required field
    requiredFields.forEach((field) => {
        field.addEventListener("input", updateProgressBar);
    });

    // Initial progress bar update
    updateProgressBar();
});
