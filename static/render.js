import { deletarProduto } from "./storage.js";
import { preencherFormulario } from "./form.js";

export function renderProducts(produtos, carregarProdutos) {
  const lista = document.getElementById("product-list");
  lista.innerHTML = "";


  produtos.forEach(p => {
    const tr = document.createElement("tr");

    tr.innerHTML = `
      <td>${p.nome}</td>
      <td>${p.quantidade}</td>
      <td>R$ ${p.preco.toFixed(2)}</td>
      <td></td>
    `;

    const tdAcoes = tr.querySelector("td:last-child");

    // Botão deletar
    const btnDel = document.createElement("button");
    btnDel.textContent = "🗑️";
    btnDel.addEventListener("click", async () => {
      await deletarProduto(p.id);
      carregarProdutos();
    });

    // Botão editar
    const btnEdit = document.createElement("button");
    btnEdit.textContent = "✏️";
    btnEdit.addEventListener("click", () => {
      preencherFormulario(p.id, p.nome, p.quantidade, p.preco);
    });

    tdAcoes.appendChild(btnDel);
    tdAcoes.appendChild(btnEdit);

    lista.appendChild(tr);
  });
}
