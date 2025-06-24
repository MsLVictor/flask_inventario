import { adicionarProduto, editarProduto, carregarProdutos as fetchProdutos } from "./storage.js";
import { renderProducts } from "./render.js";

let modoEdicaoId = null;

export function configurarFormulario() {
  const form = document.getElementById("product-form");
  const btnSubmit = document.getElementById("submitButton");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const nome = form.nome.value.trim();
    const quantidade = parseInt(form.quantidade.value);
    const preco = parseFloat(form.preco.value);

    try {
      if (modoEdicaoId) {
        await editarProduto(modoEdicaoId, { nome, quantidade, preco });
        modoEdicaoId = null;
        btnSubmit.textContent = "Adicionar";
      } else {
        await adicionarProduto({ nome, quantidade, preco });
      }

      form.reset();
      carregarProdutos();
    } catch (err) {
      alert("Erro ao salvar produto");
      console.error(err);
    }
  });
}

export async function carregarProdutos() {
  try {
    const produtos = await fetchProdutos();
    renderProducts(produtos, carregarProdutos);
  } catch (err) {
    console.error("Erro ao carregar produtos:", err);
  }
}

export function preencherFormulario(id, nome, quantidade, preco) {
  modoEdicaoId = id;

  const form = document.getElementById("product-form");
  const btnSubmit = document.getElementById("submitButton");

  form.nome.value = nome;
  form.quantidade.value = quantidade;
  form.preco.value = preco;

  btnSubmit.textContent = "Atualizar";
}