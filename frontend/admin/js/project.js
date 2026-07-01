const API="http://127.0.0.1:5000";

let editId=null;

async function loadProject(){

const res=await fetch(API+"/project");

const data=await res.json();

projectTable.innerHTML="";

data.forEach(project=>{

projectTable.innerHTML+=`

<tr>

<td>${project.nama_project}</td>

<td>${project.teknologi}</td>

<td>

<button onclick='editProject(${JSON.stringify(project)})'>

Edit

</button>

<button onclick='deleteProject(${project.id})'>

Delete

</button>

</td>

</tr>

`;

});

}

function editProject(project){

editId=project.id;

nama_project.value=project.nama_project;

deskripsi.value=project.deskripsi;

teknologi.value=project.teknologi;

github.value=project.github;

demo.value=project.demo;

gambar.value=project.gambar;

submitBtn.innerHTML="Update";

}

projectForm.addEventListener("submit",async(e)=>{

e.preventDefault();

const fd=new FormData();

fd.append("nama_project",nama_project.value);
fd.append("deskripsi",deskripsi.value);
fd.append("teknologi",teknologi.value);
fd.append("github",github.value);
fd.append("demo",demo.value);
fd.append("gambar",gambar.value);

let url=API+"/project";
let method="POST";

if(editId){

url=API+"/project/"+editId;
method="PUT";

}

const res=await fetch(url,{
method,
body:fd
});

const hasil=await res.json();

alert(hasil.message);

projectForm.reset();

editId=null;

submitBtn.innerHTML="Simpan";

loadProject();

});

async function deleteProject(id){

if(!confirm("Hapus project?")) return;

const res=await fetch(API+"/project/"+id,{
method:"DELETE"
});

const hasil=await res.json();

alert(hasil.message);

loadProject();

}

loadProject();