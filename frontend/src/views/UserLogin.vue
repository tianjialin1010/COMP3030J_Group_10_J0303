<template>
    <div>
      <el-form ref="loginForm" :model="form" :rules="rules" label-width="80px" class="login-box">
        <h3 class="login-title">欢迎登录</h3>
        <el-form-item label="账号" prop="username">
          <el-input type="text" placeholder="请输入账号" v-model="form.username"/>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" placeholder="请输入密码" v-model="form.password"/>
       </el-form-item>
       <el-form-item>
         <el-button class="login-button" type="primary" v-on:click="onSubmit('loginForm')">登录</el-button>
       </el-form-item>
     </el-form>

     <el-dialog
       title="温馨提示"
       :visible.v-model:propName="dialogVisible"
      width="30%"
       :before-close="handleClose">
       <span>请输入账号和密码</span>
       <span v-slot="footer" class="dialog-footer">
         <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
       </span>
     </el-dialog>

     <el-dialog
       title="温馨提示"
       :visible.v-model:propName="dialogVisible1"
       width="30%"
       :before-close="handleClose">
       <span>错误的账号或密码</span>
      <span v-slot="footer" class="dialog-footer">
         <el-button type="primary" @click="dialogVisible1 = false">确 定</el-button>
       </span>
     </el-dialog>
   </div>
 </template>

 <script>
 import https from '../api/https.js'
   export default {
     name: "UserLogin",
     data() {
       return {
         form: {
           username: '',
           password: ''
         },

         // 表单验证，需要在 el-form-item 元素中增加 prop 属性
         rules: {
           username: [
             {required: true, message: '账号不可为空', trigger: 'blur'}
           ],
           password: [
             {required: true, message: '密码不可为空', trigger: 'blur'}
           ]
         },

         // 对话框显示和隐藏
         dialogVisible: false,
         dialogVisible1: false,
       }
     },
     methods: {
       onSubmit(formName) {
         // 为表单绑定验证功能
         this.$refs[formName].validate((valid) => {
              var username = this.form['username'];
              var pwd = this.form['password'];
              var login_info = {username: username, password: pwd};

           if (valid) {
               https.fetchPost('login', login_info).then((data) => {
                              console.log(data.data['code'])
                              if (data.data['code'] == 200) {
                                  this.$router.push("/home");
                              } else {
                 this.dialogVisible1 = true;
                 return false;
               }
                          })
             // 使用 vue-router 路由到指定页面，该方式称之为编程式导航
             //this.$router.push("/main");
           } else {
             this.dialogVisible = true;
             return false;
           }
         });
       },
       handleClose() {

       }
     }
   }
 </script>

 <style lang="scss" scoped>
    .login-button {
        text-align: center;
    }
  .login-box {
    border: 1px solid #DCDFE6;
    width: 350px;
    margin: 180px auto;
    padding: 35px 35px 15px 35px;
    border-radius: 5px;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    box-shadow: 0 0 25px #909399;
  }

  .login-title {
    text-align: center;
    margin: 0 auto 40px auto;
    color: #303133;
  }
</style>
