const API = "http://127.0.0.1:5000";
async function loadProfile() {
    const response = await fetch(API + "/profile");
    const profile = await response.json();
    if (!profile) return;
    document.getElementById("nama").textContent =
        profile.nama || "";
    document.getElementById("profesi").textContent =
        profile.profesi || "";
    document.getElementById("deskripsi").textContent =
        profile.deskripsi || "";
    document.getElementById("email").textContent =
        "Email : " + (profile.email || "");
    document.getElementById("telepon").textContent =
        "Telepon : " + (profile.telepon || "");
    if(profile.foto){
        document.getElementById("foto").src = profile.foto;
    }
}
async function loadSkill(){
    const response = await fetch(API + "/skill");
    const skills = await response.json();
    const skillList =
        document.getElementById("skillList");
    skillList.innerHTML = "";
    skills.forEach(skill=>{
        skillList.innerHTML += `
        <div class="skill">
            <div class="skill-name">
                ${skill.nama_skill}
                (${skill.persentase}%)
            </div>
            <div class="bar">
                <div
                    class="progress"
                    style="width:${skill.persentase}%">
                </div>
            </div>
        </div>
        `;
    });

}
async function loadExperience(){
    const response =
        await fetch(API + "/experience");
    const data =
        await response.json();
    const list =
        document.getElementById("experienceList");
    list.innerHTML = "";
    data.forEach(item=>{
        list.innerHTML += `
        <div class="card">
            <h3>${item.posisi}</h3>
            <h4>${item.perusahaan}</h4>
            <p>
                ${item.mulai}
            -
                ${item.selesai}
            </p>
            <p>
                ${item.deskripsi}
            </p>
        </div>
        `;
    });
}
async function loadProject(){
    const response =
        await fetch(API + "/project");
    const data =
        await response.json();
    const list =
        document.getElementById("projectList");
    list.innerHTML = "";
    data.forEach(project=>{
        list.innerHTML += `
        <div class="card">
            <img
                src="${project.gambar}"
                class="project-img">
            <h3>
                ${project.nama_project}
            </h3>
            <p>
                ${project.deskripsi}
            </p>
            <p>
                <b>Teknologi :</b>
                ${project.teknologi}
            </p>
            <a
                href="${project.github}"
                target="_blank"
                class="project-link">
                Github
            </a>
            <a
                href="${project.demo}"
                target="_blank"
                class="project-link">
                Demo
            </a>
        </div>
        `;
    });
}
loadProfile();
loadSkill();
loadExperience();
loadProject();
window.addEventListener("scroll",()=>{
    const nav=document.querySelector("nav");
    if(window.scrollY>60){
        nav.style.background="rgba(2,6,23,.92)";
        nav.style.boxShadow="0 10px 30px rgba(0,0,0,.35)";
    }else{
        nav.style.background="rgba(15,23,42,.6)";
        nav.style.boxShadow="none";
    }
});
const observer=new IntersectionObserver(entries=>{
    entries.forEach(entry=>{
        if(entry.isIntersecting){
            entry.target.style.opacity=1;
            entry.target.style.transform="translateY(0)";
        }
    });
});
document.querySelectorAll(".skill,.card,.contact-card").forEach(el=>{
    el.style.opacity=0;
    el.style.transform="translateY(40px)";
    el.style.transition=".7s";
    observer.observe(el);
});