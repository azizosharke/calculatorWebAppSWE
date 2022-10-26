<template>
  <div class="p-3" style="max-width: 400px; margin: 50px auto; background: #234">
    
    <!-- Calculator Result -->
    <div class="w-full rounded m-1 p-3 text-right lead font-weight-bold text-white bg-vue-dark">
      {{ calculatorValue || 0 }}
    </div>

    <!-- Calculator buttons -->
    <div class="row no-gutters">
      <div class="col-3" v-for="n in calculatorElements" :key="n">
        <div class="lead text-white text-center m-1 py-3 bg-vue-dark rounded hover-class"
          :class="{'bg-vue-green': ['C','*','/','-','+','%','=', 'log' , 'exp'].includes(n)}"
          @click="action(n)"
        >
          {{n}}
        </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'Calculator',
  props: {
    msg: String
  },
  data() {
    return {
      calculatorValue: '',
      calculatorElements: ['C','*','/','-',7,8,9,'+',4,5,6,'%',1,2,3,'=',0,'.','log','exp','^','(',')','hi']
    }
  },
  methods: {
    action(n) {

      if (!(['C', '=', 'log', 'exp'].includes(n))) {
        this.calculatorValue += n + '';
      }

      // Clear button
      if (n === 'C') {
        this.calculatorValue = '';
      }
      if (n === 'log') {
        this.calculatorValue += n + '('
      }
      if (n === 'exp') {
        this.calculatorValue += n + '('
      }
      // Equals button
      if (n === '=') {
        this.calculatorValue = '';
      }
      if(n === '%'){
        this.calculatorValue = this.calculatorValue / 100 + '';
      }
    }
  }
}

</script>


<style scoped>
  .bg-vue-dark {
    background: #141414;
  }
  .hover-class:hover {
    cursor: pointer;
    background: #bdbeb7;
  }
  .bg-vue-green {
    background: #380202;
  }
</style>