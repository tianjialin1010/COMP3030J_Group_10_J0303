<!-- src/components/TranslatorProvider.vue-->
<template>
  <slot></slot>
</template>

<script>
import { useTranslator } from '../plugins/translator';

export default {
  name: 'TranslatorProvider',
  setup() {
    useTranslator();
  }
};
</script>
