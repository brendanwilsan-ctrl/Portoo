const API="http://127.0.0.1:5000";

let editId=null;

async function loadProfile(){

const res=await fetch(API+"/profile");

const data=await res.json();

const table=document.getElementById("profileTable");

table.innerHTML="";

if(!data)return;

const profile=Array.isArray(data)?data[0]:data;

table.innerHTML=`
<tr>

<td>${profile.nama}</td>

<td>${profile.profesi}</td>

<td>${profile.email}</td>

<td>

<button
class="edit"
onclick='editProfile(${JSON.stringify(profile)})'>

Edit

</button>

<button
class="delete"
onclick="deleteProfile(${profile.id})">

Delete

</button>

</td>

</tr>
`;
}
function editProfile(profile){
editId=profile.id;
nama.value=profile.nama;
profesi.value=profile.profesi;
deskripsi.value=profile.deskripsi;
email.value=profile.email;
telepon.value=profile.telepon;
alamat.value=profile.alamat;
foto.value=profile.foto;
submitBtn.innerHTML="Update";
}
profileForm.addEventListener("submit",async e=>{
e.preventDefault();
const fd=new FormData();
fd.append("nama",nama.value);
fd.append("profesi",profesi.value);
fd.append("deskripsi",deskripsi.value);
fd.append("email",email.value);
fd.append("telepon",telepon.value);
fd.append("alamat",alamat.value);
fd.append("foto",foto.value);
let url=API+"/profile";
let method="POST";
if(editId){
url=API+"/profile/"+editId;
method="PUT";
}
const res=await fetch(url,{
method,
body:fd
});
const hasil=await res.json();
alert(hasil.message);
profileForm.reset();
submitBtn.innerHTML="Simpan";
editId=null;
loadProfile();
});
async function deleteProfile(id){
if(!confirm("Hapus profile?")) return;
const res=await fetch(API+"/profile/"+id,{
method:"DELETE"
});
const hasil=await res.json();
alert(hasil.message);
loadProfile();
}
loadProfile();