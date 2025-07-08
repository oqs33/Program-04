<!-- 登录 -->
<!-- src/views/Login.vue -->
<template>
    <div class="auth-container">
      <div class="auth-box">
        <!-- 登录表单 -->
        <div v-if="showLogin" class="auth-form login-form">
          <h2 class="form-title">用户登录</h2>
          <form @submit.prevent="handleLogin">
            <div class="form-group">
              <label>用户名：</label>
              <input v-model="loginForm.name" type="text" required placeholder="请输入用户名">
            </div>
            <div class="form-group">
              <label>密码：</label>
              <input v-model="loginForm.password" type="password" required placeholder="请输入密码">
            </div>
            <button type="submit" class="submit-btn">
              <span>登录</span>
            </button>
            <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
          </form>
          <router-link to="/register" class="switch-link">
            没有账号？立即注册
          </router-link>
        </div>
      </div>
    </div>
 </template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router' // 需要导入路由
import axios from 'axios'

const router = useRouter() // 获取路由实例
const showLogin = ref(true)
const loginForm = ref({
  name: '',
  password: ''
})

const handleLogin = async () => {
  try {
    // 直接通过 loginForm.value 获取值
    const response = await axios.post('http://localhost:8000/login', {
      name: loginForm.value.name,
      password: loginForm.value.password
    })
    if (response.status === 200) {
      alert('success')
      localStorage.setItem('name', loginForm.value.name);
      router.push('/') // 使用路由实例跳转
    }
  } catch (error) {
    console.error('登录失败:', error)
    // 错误处理逻辑
    //alert('falied')
  }
}
</script>
  
  <style scoped>
  .auth-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: calc(100vh - 124px);
    background: #f4f4f4;
  }
  
  .auth-box {
    width: 100%;
    max-width: 400px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,.1);
    padding: 40px;
  }
  
  .form-title {
    text-align: center;
    margin-bottom: 30px;
    color: #222;
    font-size: 1.5rem;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 5px;
    color: #666;
  }
  
  .form-group input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 1rem;
  }
  
  .form-group input:focus {
    border-color: #00a1d6;
    outline: none;
  }
  
  .submit-btn {
    width: 100%;
    background: #00a1d6;
    color: white;
    padding: 12px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
    transition: background 0.2s;
  }
  
  .submit-btn:hover {
    background: #00b5e5;
  }
  
  .form-footer {
    text-align: center;
    margin-top: 20px;
  }
  
  .switch-link {
    color: #00a1d6;
    cursor: pointer;
    font-size: 0.9rem;
  }
  
  .switch-link:hover {
    text-decoration: underline;
  }
  
  /* 注册表单样式调整 */
  .register-form {
    display: none;
  }
  
  </style>