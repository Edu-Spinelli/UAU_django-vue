<template>
  <div>
    <h1>Adicionar Produto ao Estoque</h1>
    <form @submit.prevent="adicionarProduto">
      <label for="nome">Nome do Produto:</label>
      <input v-model="produto.nome" type="text" id="nome" />

      <label for="tipo">Tipo do Produto:</label>
      <input v-model="produto.tipo" type="text" id="tipo" />

      <label for="preco_pago">Preço Pago:</label>
      <input v-model="produto.preco_pago" type="number" id="preco_pago" />

      <label for="quantidade">Quantidade:</label>
      <input v-model="produto.quantidade" type="number" id="quantidade" />

      <button type="submit">Adicionar Produto</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "ProdutoEstoque",  // Alterado para ser multi-palavra
  data() {
    return {
      produto: {
        nome: '',
        tipo: '',
        preco_pago: 0,
        quantidade: 0,
      },
    };
  },
  methods: {
    adicionarProduto() {
      // Aqui você pode conectar com sua API para enviar os dados
      console.log("Produto adicionado:", this.produto);
      // Limpar os campos do formulário
      this.produto = {
        nome: '',
        tipo: '',
        preco_pago: 0,
        quantidade: 0,
      };
    },
  },
};
</script>
