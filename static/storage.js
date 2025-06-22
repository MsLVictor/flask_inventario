import { renderProducts } from './render.js';

export async function carregarProdutos() {
  const res = await fetch("/produtos");
  if (!res.ok) throw new Error("Erro ao carregar produtos");
  return res.json();
}

export async function adicionarProduto(produto) {
  const res = await fetch("/produtos", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(produto)
  });
  if (!res.ok) throw new Error("Erro ao adicionar produto");
  return res.json();
}

export async function editarProduto(id, produto) {
  const res = await fetch(`/produtos/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(produto)
  });
  if (!res.ok) throw new Error("Erro ao editar produto");
  return res.json();
}

export async function deletarProduto(id) {
  const res = await fetch(`/produtos/${id}`, { method: "DELETE" });
  if (!res.ok) throw new Error("Erro ao deletar produto");
  return res.json();
}
