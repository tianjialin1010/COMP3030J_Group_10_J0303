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

      // 创建渲染器
      const renderer = new THREE.WebGLRenderer({ antialias: true });
      renderer.setSize(width, height);
      container.appendChild(renderer.domElement);

      // 加载模型
      const loader = new GLTFLoader();
      loader.load('/api/model.glb', (gltf) => {
        const model = gltf.scene;
        scene.add(model);

        // 遍历场景，读取并添加光影和摄像头
        let camera;
        gltf.scene.traverse((node) => {
          if (node.isLight) {
            scene.add(node);
          }
          if (node.isCamera) {
            camera = node;
          }
        });

        // 确保找到摄像头，如果没有找到则创建默认摄像头
        if (!camera) {
          camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
          camera.position.set(0, 0, 5);
        }

        // 获取动画并播放
        const mixer = new THREE.AnimationMixer(model);
        gltf.animations.forEach((clip) => {
          const action = mixer.clipAction(clip);
          action.setLoop(THREE.LoopOnce); // 只播放一次
          action.clampWhenFinished = true; // 保持动画结束时的姿势
          action.play();
        });

        // 动画循环
        const clock = new THREE.Clock();
        const animate = () => {
          requestAnimationFrame(animate);
          const delta = clock.getDelta() * 0.5; // 调整播放速度为0.5倍
          mixer.update(delta);
          renderer.render(scene, camera);
        };

        animate();

        // 添加OrbitControls
        const controls = new OrbitControls(camera, renderer.domElement);
        controls.update();
      });
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
