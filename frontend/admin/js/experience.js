const API="http://127.0.0.1:5000";

let editId=null;
async function loadExperience(){
const res=await fetch(API+"/experience");
const data=await res.json();
experienceTable.innerHTML="";
data.forEach(item=>{
experienceTable.innerHTML+=`
<tr>
<td>${item.perusahaan}</td>
<td>${item.posisi}</td>
<td>${item.mulai} - ${item.selesai}</td>
<td>
<button
onclick='editExperience(${JSON.stringify(item)})'>
Edit
</button>
<button
onclick='deleteExperience(${item.id})'>
Delete
</button>
</td>
</tr>
`;  

});

}

function editExperience(item){

editId=item.id;
perusahaan.value=item.perusahaan;
posisi.value=item.posisi;
mulai.value=item.mulai;
selesai.value=item.selesai;
deskripsi.value=item.deskripsi;
submitBtn.innerHTML="Update";

}

experienceForm.addEventListener("submit",async(e)=>{
e.preventDefault();

const fd=new FormData();

fd.append("perusahaan",perusahaan.value);
fd.append("posisi",posisi.value);
fd.append("mulai",mulai.value);
fd.append("selesai",selesai.value);
fd.append("deskripsi",deskripsi.value);
let url=API+"/experience";
let method="POST";
if(editId){
url=API+"/experience/"+editId;
method="PUT";
}
const res=await fetch(url,{
method,
body:fd
});
const hasil=await res.json();
alert(hasil.message);
experienceForm.reset();
editId=null;
submitBtn.innerHTML="Simpan";
loadExperience();
});
async function deleteExperience(id){
if(!confirm("Hapus data?")) return;
const res=await fetch(API+"/experience/"+id,{
method:"DELETE"
});
const hasil=await res.json();
alert(hasil.message);
loadExperience();
}
loadExperience();