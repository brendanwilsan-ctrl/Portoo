const API = "http://127.0.0.1:5000";
async function loadDashboard(){
    const profile = await fetch(API+"/profile").then(r=>r.json());
    const skill = await fetch(API+"/skill").then(r=>r.json());
    const experience = await fetch(API+"/experience").then(r=>r.json());
    const project = await fetch(API+"/project").then(r=>r.json());
    document.getElementById("totalProfile").textContent =
        profile ? 1 : 0;
    document.getElementById("totalSkill").textContent =
        skill.length;
    document.getElementById("totalExperience").textContent =
        experience.length;
    document.getElementById("totalProject").textContent =
        project.length;
        if(localStorage.getItem("login") !== "true"){

    window.location.href="login.html";

}
        if(!localStorage.getItem("login")){

    window.location.href="login.html";

}
}
loadDashboard();
function logout(){

    if(confirm("Yakin ingin logout?")){

        localStorage.removeItem("login");

        window.location.href="login.html";

    }

}