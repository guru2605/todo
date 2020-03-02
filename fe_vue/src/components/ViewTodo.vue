<template>
  <div>
    <b-modal v-model="viewModal" title="View Todo">
        <b>Title:</b> {{todo.title}}
        <br/>
        <b>Description:</b> {{todo.description}}
    </b-modal>
  </div>
</template>

<script>
export default {
    data(){
        return{
            viewModal:false
        }
    },
    props:['todo'],
    mounted() {
        this.viewModal = true
    }
}
</script>

<style>

</style>