// Function to open the modal and generate referral ID
document.querySelector('.enroll-button').addEventListener('click', function () {
    fetch('/generate_referral_link')
    .then(response => response.json())
    .then(data => {
        if (data.referralLink) {
            const referralLink = data.referralLink;
    
    document.getElementById('generatedLink').textContent = referralLink;
    document.getElementById('referModal').style.display = 'block';
    
    // Set the share links with the referral link
    document.getElementById('whatsappShare').href = `https://api.whatsapp.com/send?text=${encodeURIComponent(referralLink)}`;
    document.getElementById('instagramShare').href = `https://instagram.com/share?url=${encodeURIComponent(referralLink)}`;
    document.getElementById('emailShare').href = `mailto:?subject=Check out this course&body=${encodeURIComponent(referralLink)}`;
    document.getElementById('facebookShare').href = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(referralLink)}`;
    document.getElementById('twitterShare').href = `https://twitter.com/intent/tweet?text=Check out this course&url=${encodeURIComponent(referralLink)}`;
    document.getElementById('linkedinShare').href = `https://www.linkedin.com/shareArticle?mini=true&url=${encodeURIComponent(referralLink)}&title=Check out this course`;
    document.getElementById('telegramShare').href = `https://telegram.me/share/url?url=${encodeURIComponent(referralLink)}&text=Check out this course`;
} else {
    alert('Error generating referral link. Please log in.');
}
})
.catch(err => {
console.error('Error:', err);
alert('Error generating referral link. Please try again.');
});
});

// Close the modal when clicking on the close button
document.querySelector('.close-button').addEventListener('click', function () {
    document.getElementById('referModal').style.display = 'none';
});

// Close modal when clicking outside of the content area
window.onclick = function(event) {
    if (event.target == document.getElementById('referModal')) {
        document.getElementById('referModal').style.display = 'none';
    }
}

// Copy referral link to clipboard
function copyReferral() {
    const linkText = document.getElementById('generatedLink').textContent;
    navigator.clipboard.writeText(linkText).then(() => {
        alert('Referral link copied to clipboard!');
    }).catch(() => {
        alert('Failed to copy link.');
    });
}
