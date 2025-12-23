function submitIssue() {
    const issueText = document.getElementById("issue").value;

    if (issueText.trim() === "") {
        alert("Please enter an issue");
        return;
    }

    document.getElementById("response").textContent = "Processing your issue...";

    fetch("/issue", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            issue: issueText
        })
    })
    .then(response => response.json())
    .then(data => {
    document.getElementById("response").textContent =
        "Ticket ID: " + data.ticket_id + "\n" +
        "Category: " + data.category + "\n" +
        "Status: " + data.status + "\n\n" +
        "Suggested Solution:\n" + data.suggested_solution;
});

    })
    .catch(error => {
        document.getElementById("response").textContent =
            "Error connecting to server";
    });
}

