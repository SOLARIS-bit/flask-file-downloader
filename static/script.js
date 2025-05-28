document.addEventListener("DOMContentLoaded", () => {
  fetch("/api/files")
    .then((response) => response.json())
    .then((data) => {
      const list = document.getElementById("file-list");
      data.forEach((file) => {
        const item = document.createElement("li");
        item.innerHTML = `
          ${file.name} – ${file.size} bytes – ${file.modif_date}
          <a href="/download/${file.name}">Télécharger</a>
        `;
        list.appendChild(item);
      });
    });
});
