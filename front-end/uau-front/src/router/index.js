import { createRouter, createWebHistory } from 'vue-router';
// import Home from '../components/Home.vue';
import ProdutoEstoque from '../components/ProdutoEstoque.vue';
// import Clientes from '../components/Clientes.vue';
// import Pagamentos from '../components/Pagamentos.vue';
// import Vendas from '../components/Vendas.vue';

const routes = [
//   { path: '/', component: Home },
  { path: '/estoque', component: ProdutoEstoque },
//   { path: '/clientes', component: Clientes },
//   { path: '/pagamentos', component: Pagamentos },
//   { path: '/vendas', component: Vendas },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;


