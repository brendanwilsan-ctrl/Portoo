document.getElementById("contactForm")
.addEventListener("submit", async function(e){

    e.preventDefault();

    const formData = new FormData();

    formData.append(
        "nama",
        document.getElementById("contact_nama").value
    );

    formData.append(
        "email",
        document.getElementById("contact_email").value
    );

    formData.append(
        "subjek",
        document.getElementById("contact_subjek").value
    );

    formData.append(
        "pesan",
        document.getElementById("contact_pesan").value
    );

    try{

        const response = await fetch(
            "http://127.0.0.1:5000/contact",
            {
                method:"POST",
                body:formData
            }
        );

        const result = await response.json();

        alert(result.message);

        document.getElementById("contactForm").reset();

    }catch(error){

        console.error(error);

        alert("Gagal mengirim pesan.");

    }

});