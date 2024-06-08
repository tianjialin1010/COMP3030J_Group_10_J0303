<template>
  <div id="model-container"></div>
</template>

<script>
import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

export default {
  name: 'Model',
  props: {
    src: {
      type: String,
      required: true
    }
  },
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

      // 创建渲染器
      const renderer = new THREE.WebGLRenderer({ antialias: true });
      renderer.setSize(width, height);
      container.appendChild(renderer.domElement);

      // 创建光源
      const ambientLight = new THREE.AmbientLight(0xffffff); // 环境光
      scene.add(ambientLight);
      const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
      directionalLight.position.set(7.3589, -6.9283, 4.9583); // 设置光源位置
      scene.add(directionalLight);

      // 创建相机
      const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
      camera.position.set(7.3589, -6.9283, 4.9583); // 设置相机位置
      camera.rotation.set(63.559 * Math.PI / 180, 0, 46 * Math.PI / 180); // 设置相机旋转

      // 加载模型
      const loader = new GLTFLoader();
      loader.load(this.src, (gltf) => {
        const model = gltf.scene;
        scene.add(model);

        // 动画播放设置
        const mixer = new THREE.AnimationMixer(model);
        gltf.animations.forEach((clip) => {
          const action = mixer.clipAction(clip);
          action.setLoop(THREE.LoopRepeat, Infinity); // 无限循环播放
          action.clampWhenFinished = true; // 保持动画结束时的姿势
          action.play();
        });

        // 动画循环
        const clock = new THREE.Clock();
        const animate = () => {
          requestAnimationFrame(animate);
          const delta = clock.getDelta();
          mixer.update(delta);
          renderer.render(scene, camera);
        };

        animate();

        // 添加OrbitControls
        const controls = new OrbitControls(camera, renderer.domElement);
        controls.update();
      }, undefined, function (error) {
        console.error('An error happened', error);
      });
    }
  }
};
</script>

<style scoped>
#model-container {
  width: 100%;
  height: 500px; /* 根据需要调整尺寸 */
}
</style>
