// When user clicks on Google Sign-In, it returns OAuth info
function handleLogin (response) {
    console.log(response);
    localStorage.setItem("token", response.credential);
}