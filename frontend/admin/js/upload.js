const API = "http://127.0.0.1:5000";
document
.getElementById("uploadBtn")
.addEventListener("click", async () => {
    const fileInput = document.getElementById("file");
    if (fileInput.files.length === 0) {
        alert("Pilih gambar terlebih dahulu.");
        return;
    }
    const formData = new FormData();
    formData.append(
        "file",
        fileInput.files[0]
    );

    try {
        const response = await fetch(API + "/upload", {
            method: "POST",
            body: formData
        });
        const result = await response.json();

        if (result.status === "success") {
            document.getElementById("preview").src = result.url;
            document.getElementById("hasil").value = result.url;
            alert("Upload berhasil.");

        } else {
            alert(result.message);
        }

    } catch (err) {
        console.error(err);
        alert("Upload gagal.");
    }
});

