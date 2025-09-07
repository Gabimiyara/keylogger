document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".buttons button");
    const output = document.getElementById("output");

    buttons.forEach(button => {
        button.addEventListener("click", () => {
            const fileName = button.getAttribute("data-file");

            fetch(fileName)
                .then(response => {
                    if (!response.ok) {
                        throw new Error("Network response was not ok");
                    }
                    return response.json();
                })
                .then(data => {
                    output.textContent = JSON.stringify(data, null, 2);
                })
                .catch(error => {
                    output.textContent = "Error loading file: " + error;
                });
        });
    });
});
