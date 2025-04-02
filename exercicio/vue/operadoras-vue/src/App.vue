<template>
  <div class="container">
    <h1>Buscar Operadoras</h1>
    <input v-model="termo" placeholder="Digite o Nome Fantasia" @keyup.enter="buscar" />
    <button @click="buscar">Buscar</button>

    <div v-if="loading">Carregando...</div>
    <div v-else-if="operadoras.length === 0 && termo">Nenhuma operadora encontrada.</div>

    <ul v-else>
      <li v-for="op in operadoras" :key="op.registro_ans">
        <strong>{{ op.nome_fantasia }}</strong> - {{ op.cidade }} / {{ op.uf }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      termo: "",
      operadoras: [],
      loading: false
    };
  },
  methods: {
    async buscar() {
      if (!this.termo) return;

      this.loading = true;
      this.erro = "";

      try {
        console.log("Chamando API em:", `/buscar/?termo=${this.termo}`); // <-- Veja se a URL está correta
        const response = await axios.get(`/buscar/?termo=${this.termo}`);
        console.log("Resposta da API:", response.data); // <-- Veja a resposta no console
        this.operadoras = response.data;
      } catch (error) {
        console.error("Erro ao buscar:", error);
        this.erro = "Erro ao buscar operadoras. Tente novamente.";
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style>
.container {
  max-width: 600px;
  margin: auto;
  text-align: center;
  font-family: Arial, sans-serif;
}

input {
  padding: 10px;
  width: 80%;
  margin: 10px 0;
  border: 1px solid #ccc;
}

button {
  padding: 10px;
  cursor: pointer;
  background-color: #007bff;
  color: white;
  border: none;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  padding: 10px;
  border-bottom: 1px solid #ddd;
}
</style>
