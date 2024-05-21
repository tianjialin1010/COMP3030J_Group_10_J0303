<template>
  <div id="model-container"></div>
</template>

<script>
import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

export default {
  name: 'Model',
  mounted() {
    this.initThreeJS();
  },
  methods: {
    initThreeJS() {
      const container = document.getElementById('model-container');
      const width = container.clientWidth;
      const height = container.clientHeight;

      // 创建场景
      const scene = new THREE.Scene();

      // 创建相机
      const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
      camera.position.set(0, 0, 5);

      // 创建渲染器
      const renderer = new THREE.WebGLRenderer({ antialias: true });
      renderer.setSize(width, height);
      container.appendChild(renderer.domElement);

      // 加载模型
      const loader = new GLTFLoader();
      loader.load('/api/model.glb', (gltf) => {
        scene.add(gltf.scene);
      });

      // 添加灯光
      const ambientLight = new THREE.AmbientLight(0x404040); // 环境光
      scene.add(ambientLight);
      const directionalLight = new THREE.DirectionalLight(0xffffff, 1); // 平行光
      directionalLight.position.set(5, 5, 5).normalize();
      scene.add(directionalLight);

      // 添加OrbitControls
      const controls = new OrbitControls(camera, renderer.domElement);
      controls.update();

      // 动画循环
      const animate = () => {
        requestAnimationFrame(animate);
        controls.update();
        renderer.render(scene, camera);
      };

      animate();
    }
  }
};
</script>

<style scoped>
#model-container {
  width: 100%;
  height: 100vh; /* 根据需要调整尺寸 */
}
</style>
