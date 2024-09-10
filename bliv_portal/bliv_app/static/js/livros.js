function confirmAddToCart(bookId, bookTitle) {
    // Preenche o modal com o título do livro
    document.getElementById('bookTitle').textContent = bookTitle;

    // Exibe o modal
    $('#confirmModal').modal('show');

    // Ao clicar em confirmar, adiciona ao carrinho
    document.getElementById('confirmButton').onclick = function() {
        addToCart(bookId);
    };
}

function addToCart(bookId) {
    // Faz uma requisição AJAX para adicionar o livro ao carrinho
    fetch(`/adicionar-ao-carrinho/${bookId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Função para pegar o CSRF token no Django
        }
    })
    .then(response => {
        if (response.ok) {
            // Fecha o modal
            $('#confirmModal').modal('hide');

            // Exibe o toast de sucesso
            $('#successToast').toast('show');
        }
    });
}

// Função para pegar o CSRF token (necessário para requisições POST no Django)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Verifica se este cookie começa com o nome que queremos
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
