    import { deletarProduto } from "./storage.js";
    import { preencherFormulario } from "./form.js";
    // Nota: A função carregarProdutos que você passa para renderProducts
    // geralmente é a mesma função que busca todos os produtos e os renderiza.
    // Vamos precisar dela aqui também.

    document.addEventListener('DOMContentLoaded', function() {
        const searchInput = document.getElementById('searchInput');
        const productListBody = document.getElementById('product-list');

        // Função para carregar e exibir os produtos, incluindo os botões de ação
        async function loadProducts(searchTerm = '') { // Tornar assíncrona para usar await no deletar
            // Adiciona uma classe para "fade-out" a lista existente antes de carregar novos dados
            productListBody.classList.add('fade-out');

            // Um pequeno atraso antes de fazer a requisição para permitir a animação de fade-out
            setTimeout(async () => { // Usar async aqui também
                try {
                    const response = await fetch('/search_essencia?q=' + encodeURIComponent(searchTerm));
                    if (!response.ok) {
                        throw new Error('Network response was not ok ' + response.statusText);
                    }
                    const data = await response.json();

                    // Limpa o conteúdo atual da lista/tabela
                    productListBody.innerHTML = '';

                    // Preenche a lista/tabela com os novos dados e adiciona os botões
                    data.produtos.forEach(produto => {
                        const tr = document.createElement('tr');
                        // Adiciona a classe 'product-item' à linha para a animação
                        tr.classList.add('product-item');

                        tr.innerHTML = `
                            <td>${produto.nome}</td>
                            <td>${produto.quantidade}</td>
                            <td>R$ ${produto.preco.toFixed(2)}</td>
                            <td></td> `;

                        const tdAcoes = tr.querySelector("td:last-child");

                        // Botão deletar
                        const btnDel = document.createElement("button");
                        btnDel.textContent = "🗑️";
                        btnDel.addEventListener("click", async () => {
                            await deletarProduto(produto.id);
                            // Após deletar, recarrega a lista (manter termo de pesquisa atual)
                            loadProducts(searchInput.value);
                        });

                        // Botão editar
                        const btnEdit = document.createElement("button");
                        btnEdit.textContent = "✏️";
                        btnEdit.addEventListener("click", () => {
                            preencherFormulario(produto.id, produto.nome, produto.quantidade, produto.preco);
                        });

                        tdAcoes.appendChild(btnDel);
                        tdAcoes.appendChild(btnEdit);

                        productListBody.appendChild(tr);

                        // Força o navegador a recalcular o estilo para a transição acontecer
                        void tr.offsetWidth; // truque para forçar reflow

                        // Adiciona a classe 'show' para iniciar a animação de fade-in
                        tr.classList.add('show');
                    });
                } catch (error) {
                    console.error('Erro ao buscar produtos:', error);
                } finally {
                    // Remover a classe de fade-out no final, mesmo em caso de erro
                    productListBody.classList.remove('fade-out');
                }
            }, 100); // Atraso de 100ms para o fade-out da lista antiga
        }

        // Adiciona um listener para o evento 'input', que dispara a cada digitação
        searchInput.addEventListener('input', function() {
            const searchTerm = searchInput.value;
            loadProducts(searchTerm);
        });

        // Carrega os produtos quando a página é carregada pela primeira vez
        // Isso substituirá a renderização inicial do Jinja2
        loadProducts();

        // Se você tiver um botão de "Adicionar" ou outras interações que precisem recarregar a lista,
        // você precisará chamar `loadProducts()` neles também.
        // Exemplo:
        // document.getElementById('submitButton').addEventListener('click', async (event) => {
        //     event.preventDefault(); // Impede o envio padrão do formulário
        //     // ... sua lógica para adicionar produto ...
        //     await adicionarProduto(...); // Assumindo que você tem essa função
        //     loadProducts(searchInput.value); // Recarrega a lista após adicionar
        // });
    });