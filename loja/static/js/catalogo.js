// static/js/catalogo.js

document.addEventListener('DOMContentLoaded', function () {
  const modal = document.getElementById('modal-moto');
  const btnFechar = document.getElementById('modal-fechar');

  const imgModal = document.getElementById('modal-imagem');
  const modeloModal = document.getElementById('modal-modelo');
  const descModal = document.getElementById('modal-descricao');
  const precoModal = document.getElementById('modal-preco');

  // Três <li> que podem aparecer/ sumir:
  const liAno = document.getElementById('li-ano');
  const liMarca = document.getElementById('li-marca');
  const liTipo = document.getElementById('li-tipo');

  const spanAno = document.getElementById('modal-ano');
  const spanMarca = document.getElementById('modal-marca');
  const spanTipo = document.getElementById('modal-tipo');

  document.querySelectorAll('.botao-ver-mais').forEach(function (btn) {
    btn.addEventListener('click', function () {
      // 1) Lê TODOS os data-attributes do botão:
      const nomeOuModelo = btn.getAttribute('data-modelo') || '';
      const descricao = btn.getAttribute('data-descricao') || '';
      const anoRaw = btn.getAttribute('data-ano') || '';       // string vazia ou número
      const precoRaw = btn.getAttribute('data-preco') || '';
      const imgUrl = btn.getAttribute('data-imagem') || '';
      const marca = btn.getAttribute('data-marca') || '';
      const tipo = btn.getAttribute('data-tipo') || '';

      // 2) Sempre preenche modelo/nome e descrição
      modeloModal.textContent = nomeOuModelo;
      descModal.textContent = descricao;

      // 3) Formata preço, se for número
      const valorNumber = parseFloat(precoRaw);
      if (!isNaN(valorNumber)) {
        precoModal.textContent = valorNumber.toLocaleString('pt-BR', {
          style: 'currency',
          currency: 'BRL'
        });
      } else {
        precoModal.textContent = precoRaw;
      }

      // 4) Decide se é Moto (anoRaw é número) ou Acessório (anoRaw vazio/NaN)
      const anoNumber = parseInt(anoRaw, 10);
      if (!isNaN(anoNumber)) {
        // === É UMA MOTO ===
        //  - exibe “li-ano” e “li-marca”
        liAno.style.display = 'list-item';
        spanAno.textContent = anoNumber;

        liMarca.style.display = 'list-item';
        spanMarca.textContent = marca;

        //  - esconde “li-tipo”
        liTipo.style.display = 'none';

      } else {
        // === É UM ACESSÓRIO ===
        //  - oculta “li-ano” e “li-marca”
        liAno.style.display = 'none';
        liMarca.style.display = 'none';

        //  - exibe “li-tipo”
        liTipo.style.display = 'list-item';
        spanTipo.textContent = tipo;
      }

      // 5) Atualiza a imagem
      imgModal.src = imgUrl;
      imgModal.alt = nomeOuModelo;

      // 6) Exibe o modal
      modal.style.display = 'block';
    });
  });

  // Fecha ao clicar no “×”
  btnFechar.addEventListener('click', function () {
    modal.style.display = 'none';
  });

  // Fecha ao clicar fora da caixa de conteúdo
  window.addEventListener('click', function (event) {
    if (event.target === modal) {
      modal.style.display = 'none';
    }
  });
});
