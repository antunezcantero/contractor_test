<template>
  <v-container fluid>
    <!-- <v-responsive class="d-flex align-center text-center fill-height"> -->
    <tool-buttons
      @loadData="loadData"
      @deleteRecord="deleteRecord"
      @clearSelected="clearSelected"
      @showMessage="showMessage"
      :selected="selected"
      :items="table.items"
      :priority="priority"
    />

    <v-data-table
      show-select
      v-model="selected"
      :headers="table.headers"
      :items="table.items"
      item-value="id"
      class="elevation-1"
    >
      <template v-slot:item.priority="{ item }">
        {{
          priority.length
            ? priority.find((x) => x.id == item.raw.priority).name
            : item.raw.priority
        }}
      </template>
    </v-data-table>
    <!-- </v-responsive> -->

    <v-snackbar v-model="snackbar" variant="tonal">
      {{ snackMessage }}
      <template v-slot:actions>
        <v-btn variant="icon" @click="snackbar = false" icon="mdi-close">
        </v-btn>
      </template>
    </v-snackbar>
  </v-container>
</template>

<script setup>
import { onMounted } from "vue";
import refs from "./refs";
import axios from "axios";
import { VDataTable } from "vuetify/labs/VDataTable";
import ToolButtons from "../toolButtons/ToolButtons.vue";

const { snackbar, snackMessage, drawer, selected, priority, table } = refs();

onMounted(() => {
  loadData();
  loadPriority();
});

const loadData = async () => {
  await axios
    .get("/contractor")
    .then((response) => {
      table.value.items = response.data;
    })
    .catch((error) => {
      console.log(error);
    });
};

const loadPriority = async () => {
  // Load priorities
  await axios
    .get("/priority")
    .then((response) => {
      priority.value = response.data;
    })
    .catch((error) => {
      console.log(error);
    });
};

const deleteRecord = () => {
  if (selected.value.length) {
    if (confirm("Do you want to remove the selected records?") == true) {
      selected.value.forEach((x) => {
        axios
          .delete(`/contractor/${x}`)
          .then((response) => {
            showMessage("Deleted records");
          })
          .catch((error) => {
            console.log(error);
          });
      });
    }
  } else {
    alert("You have not record selected!");
  }
};

const clearSelected = () => {
  selected.value = [];
};

const showMessage = (msg) => {
  snackMessage.value = `${msg}!`;
  snackbar.value = true;

  loadData();
};
</script>
