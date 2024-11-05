document.getElementById('demoForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the default form submission
    submitForm();  // Call the function to handle redirection
});

function submitForm() {
    window.location.href = "{{ url_for('choose') }}";
}
