<template>
  <div ref="container" class="w-full h-full"></div>
</template>

<script>
import * as THREE from 'three'
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'

export default {
  name: 'ModelViewer',
  props: {
    fullscreen: {
      type: Boolean,
      default: false
    },
    modelUrl: {
      type: String,
      required: true
    }
  },
  mounted() {
    const container = this.$refs.container

    const scene = new THREE.Scene()
    scene.background = new THREE.Color(0xdddddd)

    this.camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000)
    this.camera.position.set(4, 2, 5)
    this.camera.rotation.y = THREE.MathUtils.degToRad(-80)

    this.renderer = new THREE.WebGLRenderer({ antialias: true })
    this.renderer.setSize(container.clientWidth, container.clientHeight)
    this.renderer.setPixelRatio(window.devicePixelRatio)
    this.renderer.shadowMap.enabled = true
    container.appendChild(this.renderer.domElement)

    const controls = new OrbitControls(this.camera, this.renderer.domElement)
    controls.enableDamping = true
    controls.dampingFactor = 0.05
    controls.screenSpacePanning = false
    controls.maxPolarAngle = Math.PI / 2

    const ambientLight = new THREE.AmbientLight(0xffffff, 100)
    scene.add(ambientLight)

    const directionalLight1 = new THREE.DirectionalLight(0xffffff, 10)
    directionalLight1.position.set(5, 10, 7.5)
    directionalLight1.castShadow = true
    directionalLight1.shadow.mapSize.width = 1024
    directionalLight1.shadow.mapSize.height = 1024
    directionalLight1.shadow.camera.near = 0.5
    directionalLight1.shadow.camera.far = 50
    scene.add(directionalLight1)

    const directionalLight2 = new THREE.DirectionalLight(0xffffff, 10)
    directionalLight2.position.set(5, 10, 7.5)
    scene.add(directionalLight2)

    const directionalLight3 = new THREE.DirectionalLight(0xffffff, 100)
    directionalLight2.position.set(-5, 10, -7.5)
    scene.add(directionalLight3)

    const loader = new GLTFLoader()
    loader.load(this.modelUrl, (gltf) => {
      const model = gltf.scene
      model.traverse((node) => {
        if (node.isMesh) {
          node.castShadow = true
          node.receiveShadow = true
        }
      })

      scene.add(model)

      const box = new THREE.Box3().setFromObject(model)
      const center = box.getCenter(new THREE.Vector3())
      this.camera.lookAt(center)

      const animations = gltf.animations
      if (animations && animations.length) {
        const mixer = new THREE.AnimationMixer(model)
        const clock = new THREE.Clock()

        let lastClipIndex = animations.length - 1

        const playAllAnimations = () => {
          let clipIndex = 0

          const playNextClip = () => {
            if (clipIndex < animations.length) {
              const clip = animations[clipIndex]
              const action = mixer.clipAction(clip)
              action.reset().play()
              action.clampWhenFinished = true
              action.loop = THREE.LoopOnce

              mixer.addEventListener('finished', () => {
                clipIndex++
                playNextClip()
              })
            } else {
              const lastClip = animations[lastClipIndex]
              const lastAction = mixer.clipAction(lastClip)
              lastAction.reset().play()
              lastAction.loop = THREE.LoopRepeat
            }
          }

          playNextClip()
        }

        playAllAnimations()

        const animate = () => {
          requestAnimationFrame(animate)
          const delta = clock.getDelta()
          mixer.update(delta)
          controls.update()
          this.renderer.render(scene, this.camera)
        }
        animate()
      }
    }, undefined, (error) => {
      console.error('An error occurred while loading the model:', error)
    })

    const animate = () => {
      requestAnimationFrame(animate)
      controls.update()
      this.renderer.render(scene, this.camera)
    }
    animate()

    window.addEventListener('resize', this.onWindowResize)
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onWindowResize)
  },
  methods: {
    onWindowResize() {
      const container = this.$refs.container
      this.camera.aspect = container.clientWidth / container.clientHeight
      this.camera.updateProjectionMatrix()
      this.renderer.setSize(container.clientWidth, container.clientHeight)
    }
  },
  data() {
    return {
      camera: null,
      renderer: null
    }
  }
}
</script>

<style scoped>
.w-full {
  width: 100%;
}
.h-full {
  height: 100%;
}
</style>
