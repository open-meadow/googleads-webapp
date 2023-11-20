SERVER_URL = "http://127.0.0.1:5000"

// When user clicks on Google Sign-In, it returns OAuth info
function handleLogin (response) {
    console.log(response);
    localStorage.setItem("token", response.credential);
}

// redirect to GoogleAds Authentication
function onLinkAdsAccount() {
    window.location.href = `${SERVER_URL}/authorize`;
}