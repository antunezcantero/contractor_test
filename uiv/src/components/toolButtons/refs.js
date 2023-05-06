import { ref } from "vue"

export default {
    snackbar: ref(false),
    snackMessage: ref(""),
    dialogImport: ref(false),
    options: ref({
        items: ["Export-PDF", "Print"],
        model: "Export-PDF",
    })
}