<template>
  <el-row class="openai">
    <el-container>
      <el-header class="title">
        <p>OPENAI</p>
      </el-header>
      <el-main>
        <el-card class="box-card">
          <div v-for="(entry, index) in chatHistory" :key="index" :class="[entry.type]">
            <pre>{{ entry.message }}</pre>
          </div>
          <el-input autosize class="message" placeholder="输入你的问题然后回车" v-model="message" clearable
            size="large" :disabled="isdisabled" @keyup.enter="Message" />
        </el-card>
      </el-main>
    </el-container>
  </el-row>
</template>

<script lang="ts">
import { ref } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const chatHistory = ref<Array<ChatEntry>>([]);
    const message = ref('');
    const isdisabled = ref(false);
    const Message = () => {
      isdisabled.value = true
      if (!message.value) return;
      axios
        .post('http://127.0.0.1:5000/', {
          message: message.value,
        })
        .then((res) => {
          chatHistory.value.push({
            type: 'self',
            message: message.value,
          });

          chatHistory.value.push({
            type: 'ai',
            message: res.data["answer"],
          });
          message.value = '';
          isdisabled.value = false
        });
    };

    return {
      chatHistory,
      message,
      Message,
      isdisabled
    }
  }
}

interface ChatEntry {
  type: string;
  message: string;
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.openai {
  height: inherit;
  overflow: auto;
  background-color: #4b82e9;
  background-size: 100% 100%;
}

.title {
  color: #fff;
  text-align: center;

  p {
    font-size: 48px;
    font-weight: bold;
  }
}

.box-card {
  width: 80%;
  position: absolute;
  left: 10%;

  .self {
    margin: 5px;
    border-radius: 10px;
    padding: 10px;
    background-color: rgb(237, 237, 237);
  }

  .ai {
    margin: 5px;
    border-radius: 10px;
    padding: 10px;
    background-color: rgb(237, 237, 237);
  }

  pre {
    white-space: pre-wrap;
    white-space: -moz-pre-wrap;
    white-space: -o-pre-wrap;
    word-wrap: break-word;
  }

  .message {
    position: relative;
    bottom: 0px;
  }

  .answer {
    background-color: #f1f1f1;
    border-radius: 3px;
    font-size: 16px;
    margin-top: 10px;
  }
}
</style>