document.getElementById("loginForm")
.addEventListener("submit", async function(e){
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);
    try {
        const response = await fetch(
            "http://127.0.0.1:5000/login",
            {
                method: "POST",
                body: formData
            }
        );
        const result = await response.json();
        if(result.status === "success"){
    window.location.href = "dashboard.html";
}else{
    alert(result.message);
}
    } catch(error){
        console.error(error);
        alert("Gagal terhubung ke server");
    }
});