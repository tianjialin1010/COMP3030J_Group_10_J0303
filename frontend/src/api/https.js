import axios from 'axios'
 import qs from 'qs'
 import Config from '../config';

 axios.defaults.timeout = 5000;
 axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';
 axios.defaults.baseURL = '';

 function buildApiUrl(url) {
  return `${Config.apiUrl}/${Config.apiPrefix}/${url}`;
}

axios.interceptors.request.use((config) => {
    if(config.method == 'post'){
        config.data = qs.stringify(config.data);
    }
    return config;
}, (error) => {
    console.log('error params')
    return Promise.reject(error);
}
);

axios.interceptors.response.use((res) => {
    if(!res.data.success) {
        return Promise.resolve(res);
    }
    return res;
}, (error) => {
    console.log('Network error')
    return Promise.reject(error);
}
);

//返回一个Promise(发送post请求)
export function fetchPost(url, params) {
    let apiUrl = buildApiUrl(url);
    return new Promise((resolve, reject) => {
        axios.post(apiUrl, params)
            .then(response => {
                resolve(response);
            }, err => {
                reject(err);
            })
            .catch((error) => {
                reject(error)
            })
    })
}
////返回一个Promise(发送get请求)
export function fetchGet(url, param) {
    let apiUrl = buildApiUrl(url);
    return new Promise((resolve, reject) => {
        axios.get(apiUrl, {params: param})
            .then(response => {
                resolve(response)
            }, err => {
                reject(err)
            })
            .catch((error) => {
                reject(error)
            })
    })
}

export default {
    fetchGet,
    fetchPost
}