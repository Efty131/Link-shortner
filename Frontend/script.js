const form = document.getElementById('shortener-form');
      const resultDiv = document.getElementById('result');

      form.addEventListener('submit', (event) => {
        event.preventDefault();

        const formData = new FormData(form);
        fetch('http://localhost:5000/shortner', {
          method: 'POST',
          body: formData,
        })
          .then(response => response.text())
          .then(shortLink => {
            resultDiv.innerHTML = `<h3>Short link: <a href="${shortLink}">${shortLink}</a></h3>`;
          })
          .catch(error => {
            resultDiv.innerHTML = `<h3>Error: ${error.message}</h3>`;
          });
      });