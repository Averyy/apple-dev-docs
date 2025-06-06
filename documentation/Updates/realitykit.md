# RealityKit updates

**Framework**: Updates

Learn about important changes in RealityKit.

#### Overview

Browse notable changes in [`RealityKit`](https://developer.apple.com/documentation/RealityKit).

#### June 2024

##### General

- Add artistic lights and shadows to your visionOS app with [`PointLightComponent`](https://developer.apple.com/documentation/RealityKit/PointLightComponent), [`DirectionalLightComponent`](https://developer.apple.com/documentation/RealityKit/DirectionalLightComponent), [`SpotLightComponent`](https://developer.apple.com/documentation/RealityKit/SpotLightComponent), and [`DynamicLightShadowComponent`](https://developer.apple.com/documentation/RealityKit/DynamicLightShadowComponent).
- Manage spatial tracking in your app with the [`SpatialTrackingSession`](https://developer.apple.com/documentation/RealityKit/SpatialTrackingSession).
- Use [`LowLevelMesh`](https://developer.apple.com/documentation/RealityKit/LowLevelMesh) to efficiently bring your mesh data to RealityKit, including custom vertex attributes, formats, and layouts.
- Use an [`AnimationLibraryComponent`](https://developer.apple.com/documentation/RealityKit/AnimationLibraryComponent) to store associated animations with an entity that plays the animations.
- Create an  [`IKComponent`](https://developer.apple.com/documentation/RealityKit/IKComponent) to animate a skeletal model with an inverse kinematics [`IKComponent.Solver`](https://developer.apple.com/documentation/RealityKit/IKComponent/Solver).
- Use an [`AudioLibraryComponent`](https://developer.apple.com/documentation/RealityKit/AudioLibraryComponent) to store associated audio with an entity that plays the audio.
- Stream generated audio in real time with [`AudioGeneratorController`](https://developer.apple.com/documentation/RealityKit/AudioGeneratorController).
- Manage the meshes on your blend shapes with [`BlendShapeWeightsComponent`](https://developer.apple.com/documentation/RealityKit/BlendShapeWeightsComponent).
- Create more engaging sound effects by configuring rolloff and reverb with the [`SpatialAudioComponent`](https://developer.apple.com/documentation/RealityKit/SpatialAudioComponent).
- Customize hover effects when using [`HoverEffectComponent`](https://developer.apple.com/documentation/RealityKit/HoverEffectComponent), such as spotlight styles, highlight styles, or shader-backed hover effects for additional control over hover behaviors.
- Create an environment resource from a cube texture that has quality and compression options with doc://com.apple.documentation/documentation/realitykit/environmentresource/init(cube:options:)-5v70i, and access environment resources with [`skybox`](https://developer.apple.com/documentation/RealityKit/EnvironmentResource/skybox).

##### Models and Materials

- Optimize material initialization with a [`CustomMaterial.Program`](https://developer.apple.com/documentation/RealityKit/CustomMaterial/Program-swift.class) to compile backing shaders.
- Bring your two-dimensional vector content into 3D with doc://com.apple.documentation/documentation/realitykit/meshresource/init(extruding:extrusionoptions:)-3h21u.
- Control the compression of loaded textures with [`compression`](https://developer.apple.com/documentation/RealityKit/TextureResource/CreateOptions/compression).
- Create texture resources from doc://com.apple.documentation/documentation/realitykit/textureresource/cubemap(slices:named:options:)-7k9y6, [`texture2DArray(slices:named:options:)`](https://developer.apple.com/documentation/RealityKit/TextureResource/texture2DArray(slices:named:options:)-50g10) or [`texture3D(slices:named:options:)`](https://developer.apple.com/documentation/RealityKit/TextureResource/texture3D(slices:named:options:)-6pude).
- Use [`init(from:)`](https://developer.apple.com/documentation/RealityKit/TextureResource/init(from:)-42r55) to efficiently update custom texture data in RealityKit, including custom pixel formats, texture types, swizzle, and texture usage.
- Create cube texture resources with [`init(cubeFromEquirectangular:named:quality:faceSize:options:)`](https://developer.apple.com/documentation/RealityKit/TextureResource/init(cubeFromEquirectangular:named:quality:faceSize:options:)-bqd7) or [`init(cubeFromImage:named:options:)`](https://developer.apple.com/documentation/RealityKit/TextureResource/init(cubeFromImage:named:options:)-9dcus).
- Create cube, 2D array, and 3D texture resources from data with doc://com.apple.documentation/documentation/realitykit/textureresource/init(dimensions:format:contents:)-28vgd, [`init(dimensions:format:contents:)`](https://developer.apple.com/documentation/RealityKit/TextureResource/init(dimensions:format:contents:)-324ls), or [`init(dimensions:format:contents:)`](https://developer.apple.com/documentation/RealityKit/TextureResource/init(dimensions:format:contents:)-64sua).
- Access additional texture resource properties: [`arrayLength`](https://developer.apple.com/documentation/RealityKit/TextureResource/arrayLength), [`depth`](https://developer.apple.com/documentation/RealityKit/TextureResource/depth), [`pixelFormat`](https://developer.apple.com/documentation/RealityKit/TextureResource/pixelFormat), and [`textureType`](https://developer.apple.com/documentation/RealityKit/TextureResource/textureType).
- Add a clearcoat to your custom materials with [`clearcoatNormal`](https://developer.apple.com/documentation/RealityKit/CustomMaterial/clearcoatNormal-swift.property).

##### Physics and Simulations

- Apply force effects on rigid bodies with the [`ForceEffect`](https://developer.apple.com/documentation/RealityKit/ForceEffect).
- Create simulations such as hinge and slider joints with [`PhysicsJoint`](https://developer.apple.com/documentation/RealityKit/PhysicsJoint).

##### Immersive Environments

- Anchor dockable videos by attaching a [`DockingRegionComponent`](https://developer.apple.com/documentation/RealityKit/DockingRegionComponent) to your entity.
- Peer into other immersive worlds with a [`PortalComponent`](https://developer.apple.com/documentation/RealityKit/PortalComponent), and allow objects from that world to enter yours with [`PortalCrossingComponent`](https://developer.apple.com/documentation/RealityKit/PortalCrossingComponent).
- Further control the lighting in your environment with [`EnvironmentLightingConfigurationComponent`](https://developer.apple.com/documentation/RealityKit/EnvironmentLightingConfigurationComponent).

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Intents updates](appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [Apple Pencil updates](applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md)
  Learn about important changes to AVFoundation.
- [Bundle Resources updates](bundleresources.md)
  Learn about important changes to Bundle Resources.
- [ContactsUI updates](contactsui.md)
  Learn about important changes to ContactsUI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/realitykit)*