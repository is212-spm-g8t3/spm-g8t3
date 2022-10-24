<template>
  <div>
    <a-alert
      v-if="visible"
      :message="message"
      :type="type"
      :closable="closable"
      :after-close="handleClose"
      style="margin-bottom: 10px;"
      show-icon
      banner
    />
  </div>
</template>

<script>

export default {
   
  data() {
    return {
    //   visible: true,
    };
  },
  props: ["message", "visible", "type", "closable"],
  methods: {
    handleClose() {
      this.visible = false;
    },
  },
};
</script>