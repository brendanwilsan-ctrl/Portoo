const API="http://127.0.0.1:5000";

let editId=null;

async function loadSkill(){

const res=await fetch(API+"/skill");

const data=await res.json();

const table=document.getElementById("skillTable");

table.innerHTML="";

data.forEach(skill=>{

table.innerHTML+=`

<tr>

<td>${skill.nama_skill}</td>

<td>${skill.persentase}%</td>

<td>

<button onclick='editSkill(${JSON.stringify(skill)})'>

Edit

</button>

<button onclick="deleteSkill(${skill.id})">

Delete

</button>

</td>

</tr>

`;
});
}
function editSkill(skill){
editId=skill.id;
nama_skill.value=skill.nama_skill;
persentase.value=skill.persentase;
submitBtn.innerHTML="Update";
}
skillForm.addEventListener("submit",async e=>{
e.preventDefault();
const fd=new FormData();
fd.append("nama_skill",nama_skill.value);
fd.append("persentase",persentase.value);
let url=API+"/skill";
let method="POST";
if(editId){
url=API+"/skill/"+editId;
method="PUT";
}
const res=await fetch(url,{
method,
body:fd
});
const hasil=await res.json();
alert(hasil.message);
skillForm.reset();
editId=null;
submitBtn.innerHTML="Simpan";
loadSkill();
});
async function deleteSkill(id){
if(!confirm("Hapus skill?")) return;
const res=await fetch(API+"/skill/"+id,{
method:"DELETE"
});
const hasil=await res.json();
alert(hasil.message);
loadSkill();
}
loadSkill();