document.getElementById('craftingForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let formData = new FormData(this);

    fetch('/calculate', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.tree) {
            document.getElementById('output').innerText = data.tree;
        } else if (data.error) {
            document.getElementById('output').innerText = data.error;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
