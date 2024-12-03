document.querySelector('.enroll-button').addEventListener('click', function () {
    const courseName = 'ios'; // Replace this with the course name 
    fetch(`/generate_referral_link?course=${courseName}`)
        .then(response => response.json())
        .then(data => {
            if (data.referralLink) {
                const referralLink = data.referralLink;

                // Display the referral link
                document.getElementById('generatedLink').textContent = referralLink;
                document.getElementById('referModal').style.display = 'block';

                // Update sharing options
                document.getElementById('whatsappShare').href = `https://api.whatsapp.com/send?text=${encodeURIComponent(referralLink)}`;
                document.getElementById('instagramShare').href = `https://instagram.com/share?url=${encodeURIComponent(referralLink)}`;
                document.getElementById('emailShare').href = `mailto:?subject=Check out this course&body=${encodeURIComponent(referralLink)}`;
                document.getElementById('facebookShare').href = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(referralLink)}`;
                document.getElementById('twitterShare').href = `https://twitter.com/intent/tweet?text=Check out this course&url=${encodeURIComponent(referralLink)}`;
                document.getElementById('linkedinShare').href = `https://www.linkedin.com/shareArticle?mini=true&url=${encodeURIComponent(referralLink)}&title=Check out this course`;
                document.getElementById('telegramShare').href = `https://telegram.me/share/url?url=${encodeURIComponent(referralLink)}&text=Check out this course`;
            } else {
                alert('Error generating referral link.');
            }
        })
        .catch(error => console.error('Error:', error));
});


// Close the modal when clicking the close button
document.querySelector('.close-button').addEventListener('click', function () {
    document.getElementById('referModal').style.display = 'none';
});

// Close the modal when clicking outside the modal content
window.onclick = function(event) {
    if (event.target == document.getElementById('referModal')) {
        document.getElementById('referModal').style.display = 'none';
    }
};

// Copy the referral link to the clipboard
function copyReferral() {
    const linkText = document.getElementById('generatedLink').textContent;
    navigator.clipboard.writeText(linkText).then(() => {
        alert('Referral link copied to clipboard!');
    }).catch(() => {
        alert('Failed to copy link.');
    });
}
