<template>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand href="#">Controle de Estoque</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/">Início</b-nav-item>
          <b-nav-item to="/estoque">Estoque</b-nav-item>
          <b-nav-item to="/clientes">Clientes</b-nav-item>
          <b-nav-item to="/pagamentos">Pagamentos</b-nav-item>
          <b-nav-item to="/vendas">Vendas</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </template>
  
  <script>
  export default {
    name: "NavBar",
  };
  </script>
  
  <style scoped>
  /* Custom styles for navbar if necessary */
  </style>
  