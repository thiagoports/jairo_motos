// static/js/catalogo.js

document.addEventListener('DOMContentLoaded', function () {
  // Referências ao modal e aos elementos internos
  const modal = document.getElementById('modal-moto');
  const spanFechar = document.getElementById('modal-fechar');

  const imagemModal = document.getElementById('modal-imagem');
  const modeloModal = document.getElementById('modal-modelo');
  const descricaoModal = document.getElementById('modal-descricao');
  const anoModal = document.getElementById('modal-ano');
  const precoModal = document.getElementById('modal-preco');

  document.querySelectorAll('.botao-ver-mais').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const modelo = this.getAttribute('data-modelo') || '';
      const descricao = this.getAttribute('data-descricao') || '';
      const ano = this.getAttribute('data-ano') || '';
      const preco = this.getAttribute('data-preco') || '';
      const imagemUrl = this.getAttribute('data-imagem') || '';

      modeloModal.textContent = modelo;
      descricaoModal.textContent = descricao;

      const valorNumber = parseFloat(preco);
      if (!isNaN(valorNumber)) {
        precoModal.textContent = valorNumber.toLocaleString('pt-BR', {
          style: 'currency',
          currency: 'BRL'
        });
      } else {
        precoModal.textContent = preco;
      }

      anoModal.textContent = ano;
      imagemModal.src = imagemUrl;
      imagemModal.alt = modelo;

      modal.style.display = 'block';
    });
  });

  spanFechar.addEventListener('click', function () {
    modal.style.display = 'none';
  });

  window.addEventListener('click', function (event) {
    if (event.target === modal) {
      modal.style.display = 'none';
    }
  });
});
