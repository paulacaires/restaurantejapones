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

function abrirModalCardapio() {
  document.getElementById("modalCardapio").classList.add("ativo");
}

function abrirModalConsumo() {
  document.getElementById("modalConsumo").classList.add("ativo");
}

function fecharModalEstoque(event) {
    // Fechar apenas clicando fora do conteúdo
    if (event.target.classList.contains("modal-overlay")) {
        event.target.classList.remove("ativo");
    }
}

// Autocomplete dos alunos
function buscarAluno() {
    const termo = document.getElementById("busca_aluno").value;

    if (termo.length < 2) {
        document.getElementById("lista-alunos").innerHTML = "";
        return;
    }

    fetch(`/clientes/buscar?nome=${encodeURIComponent(termo)}`)
        .then(res => res.json())
        .then(data => {
            const lista = document.getElementById("lista-alunos");
            lista.innerHTML = "";

            data.forEach(aluno => {
                const item = document.createElement("div");
                item.classList.add("autocomplete-item");
                item.textContent = `${aluno.nome} (${aluno.cpf})`;

                item.onclick = () => {
                    document.getElementById("busca_aluno").value = aluno.nome;
                    document.getElementById("cliente_cpf").value = aluno.cpf;
                    lista.innerHTML = "";
                };

                lista.appendChild(item);
            });
        });
}

function setAvaliacao(valor) {
    const estrelas = document.querySelectorAll("#estrelas span");
    document.getElementById("avaliacao").value = valor;

    estrelas.forEach((s, index) => {
        if (index < valor) {
            s.textContent = "⭐";
            s.classList.add("ativa");
        } else {
            s.textContent = "☆";
            s.classList.remove("ativa");
        }
    });
}

// Avaliação com estrelas
document.addEventListener("DOMContentLoaded", () => {
    const estrelas = document.querySelectorAll(".estrela");
    const inputAvaliacao = document.getElementById("avaliacao");

    estrelas.forEach(estrela => {
        estrela.addEventListener("click", () => {
            const valor = estrela.dataset.valor;
            inputAvaliacao.value = valor;

            estrelas.forEach(e => {
                e.textContent = e.dataset.valor <= valor ? "⭐" : "☆";
            });
        });
    });
});