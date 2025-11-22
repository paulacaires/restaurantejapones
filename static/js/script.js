// Abre/fecha o menu mobile
document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".nav-links");

  toggle.addEventListener("click", () => {
    nav.classList.toggle("open");
  });
});

function abrirModalEstoque() {
    document.getElementById("modalEstoque").classList.add("ativo");
}

function fecharModalEstoque(event) {
    // Fechar apenas clicando fora do conteúdo
    if (event.target.classList.contains("modal-overlay")) {
        event.target.classList.remove("ativo");
    }
}