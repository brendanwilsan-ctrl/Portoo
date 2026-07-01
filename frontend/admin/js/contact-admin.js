const API = "http://127.0.0.1:5000";

const table = document.getElementById("contactTable");

async function loadContact() {

    try {

        const response = await fetch(API + "/contact");
        const data = await response.json();

        table.innerHTML = "";

        data.forEach(contact => {

            table.innerHTML += `
                <tr>
                    <td>${contact.nama}</td>
                    <td>${contact.email}</td>
                    <td>${contact.subjek}</td>
                    <td>${contact.pesan}</td>
                    <td>
                        <button onclick="deleteContact(${contact.id})">
                            Delete
                        </button>
                    </td>
                </tr>
            `;

        });

    } catch (err) {

        console.error(err);
        alert("Gagal memuat data contact.");

    }

}

async function deleteContact(id) {

    if (!confirm("Yakin ingin menghapus pesan ini?")) {
        return;
    }

    try {

        const response = await fetch(API + "/contact/" + id, {
            method: "DELETE"
        });

        const result = await response.json();

        alert(result.message);

        loadContact();

    } catch (err) {

        console.error(err);
        alert("Gagal menghapus data.");
    }
}
loadContact();

