# RealityKit updates

**Framework**: Updates

Learn about important changes in RealityKit.

#### Overview

Browse notable changes in [`RealityKit`](https://developer.apple.com/documentation/realitykit).

#### June 2025

##### General

- Create hover effect groups to indicate entities that need to highlight together using [`HoverEffectComponent.GroupID`](https://developer.apple.com/documentation/realitykit/hovereffectcomponent/groupid).
- Present popovers from volumes using [`PresentationComponent`](https://developer.apple.com/documentation/realitykit/presentationcomponent).
- Manually create instances of entities using [`MeshInstancesComponent`](https://developer.apple.com/documentation/realitykit/meshinstancescomponent).
- Animate entities implicitly using [`animate(_:body:completion:)`](https://developer.apple.com/documentation/realitykit/entity/animate(_:body:completion:)).
- Create and modify attachments in a more streamlined fashion using [`ViewAttachmentComponent`](https://developer.apple.com/documentation/realitykit/viewattachmentcomponent).
- Make entities render behind real-world objects based on depth using [`EnvironmentBlendingComponent`](https://developer.apple.com/documentation/realitykit/environmentblendingcomponent).
- Implement post-processing effects using [`RealityViewPostProcessEffect`](https://developer.apple.com/documentation/realitykit/realityviewpostprocesseffect) and [`PostProcessEffectContext`](https://developer.apple.com/documentation/realitykit/postprocesseffectcontext).
- Attach models together using [`attach(_:to:)`](https://developer.apple.com/documentation/realitykit/entity/attach(_:to:)).
- [`TextureResource`](https://developer.apple.com/documentation/realitykit/textureresource) now supports AVIF textures and entities you load from USDZ files that contain AVIF textures using [`init(named:in:)`](https://developer.apple.com/documentation/realitykit/entity/init(named:in:))  so they render correctly.
- Load entities from Data objects using [`init(from:configurations:)`](https://developer.apple.com/documentation/realitykit/entity/init(from:configurations:)).

##### Image Presentation

- Generate spatial scenes using [`ImagePresentationComponent.Spatial3DImage`](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent/spatial3dimage) and present them (along with 2D images and spatial photos) using [`ImagePresentationComponent`](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent).
- Receive notifications related to presenting images using [`ImagePresentationEvents`](https://developer.apple.com/documentation/realitykit/imagepresentationevents).
- Use [`Model3DAsset`](https://developer.apple.com/documentation/realitykit/model3dasset) with [`Model3D`](https://developer.apple.com/documentation/realitykit/model3d) to play animations in Model3D Views.

##### Arkit Integration

- Receive updates about ARKit anchors directly in RealityKit using [`AnchorStateEvents`](https://developer.apple.com/documentation/realitykit/anchorstateevents) and [`SceneEvents.TrackingStateUpdate`](https://developer.apple.com/documentation/realitykit/sceneevents/trackingstateupdate).

##### Swiftui Integration

- Use SwiftUI implicit animations using the [`Animation`](https://developer.apple.com/documentation/swiftui/animation) modifier with RealityKit entities and components.
- Keep SwiftUI state in sync with RealityKit state using [`Entity.Observable`](https://developer.apple.com/documentation/realitykit/entity/observable-swift.struct).
- Present USD variants in [`Model3D`](https://developer.apple.com/documentation/realitykit/model3d) using [`Entity.ConfigurationCatalog`](https://developer.apple.com/documentation/realitykit/entity/configurationcatalog).
- Specify the frame sizing and alignment option for RealityView using [`RealityViewLayoutOption`](https://developer.apple.com/documentation/realitykit/realityviewlayoutoption).

##### Video Presentation

- Play spatial video, 180°, 360°, wide-FOV APMP video, and Apple Immersive Video in  [`VideoPlayerComponent`](https://developer.apple.com/documentation/realitykit/videoplayercomponent).
- Retrieve the loading status when playing video using [`VideoPlayerComponent`](https://developer.apple.com/documentation/realitykit/videoplayercomponent) with [`currentRenderingStatus`](https://developer.apple.com/documentation/realitykit/videoplayercomponent/currentrenderingstatus).
- Receive notifications when a video stops playing due to a comfort violation using [`VideoPlayerEvents.VideoComfortMitigationDidOccur`](https://developer.apple.com/documentation/realitykit/videoplayerevents/videocomfortmitigationdidoccur).

##### Gestures and Entity Interaction

- Implement six degree of freedom (6DOF) gestures for manipulating entities using [`ManipulationComponent`](https://developer.apple.com/documentation/realitykit/manipulationcomponent).
- Leverage [`GestureComponent`](https://developer.apple.com/documentation/realitykit/gesturecomponent) to support gestures on individual entities.

#### June 2024

##### General

- Add artistic lights and shadows to your visionOS app with [`PointLightComponent`](https://developer.apple.com/documentation/realitykit/pointlightcomponent), [`DirectionalLightComponent`](https://developer.apple.com/documentation/realitykit/directionallightcomponent), [`SpotLightComponent`](https://developer.apple.com/documentation/realitykit/spotlightcomponent), and [`DynamicLightShadowComponent`](https://developer.apple.com/documentation/realitykit/dynamiclightshadowcomponent).
- Manage spatial tracking in your app with the [`SpatialTrackingSession`](https://developer.apple.com/documentation/realitykit/spatialtrackingsession).
- Use [`LowLevelMesh`](https://developer.apple.com/documentation/realitykit/lowlevelmesh) to efficiently bring your mesh data to RealityKit, including custom vertex attributes, formats, and layouts.
- Use an [`AnimationLibraryComponent`](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent) to store associated animations with an entity that plays the animations.
- Create an  [`IKComponent`](https://developer.apple.com/documentation/realitykit/ikcomponent) to animate a skeletal model with an inverse kinematics [`IKComponent.Solver`](https://developer.apple.com/documentation/realitykit/ikcomponent/solver).
- Use an [`AudioLibraryComponent`](https://developer.apple.com/documentation/realitykit/audiolibrarycomponent) to store associated audio with an entity that plays the audio.
- Stream generated audio in real time with [`AudioGeneratorController`](https://developer.apple.com/documentation/realitykit/audiogeneratorcontroller).
- Manage the meshes on your blend shapes with [`BlendShapeWeightsComponent`](https://developer.apple.com/documentation/realitykit/blendshapeweightscomponent).
- Create more engaging sound effects by configuring rolloff and reverb with the [`SpatialAudioComponent`](https://developer.apple.com/documentation/realitykit/spatialaudiocomponent).
- Customize hover effects when using [`HoverEffectComponent`](https://developer.apple.com/documentation/realitykit/hovereffectcomponent), such as spotlight styles, highlight styles, or shader-backed hover effects for additional control over hover behaviors.

##### Models and Materials

- Optimize material initialization with a [`CustomMaterial.Program`](https://developer.apple.com/documentation/realitykit/custommaterial/program-swift.class) to compile backing shaders.
- Use [`init(from:)`](https://developer.apple.com/documentation/realitykit/textureresource/init(from:)) to efficiently update custom texture data in RealityKit, including custom pixel formats, texture types, swizzle, and texture usage.
- Create cube texture resources with [`init(cubeFromEquirectangular:named:quality:faceSize:options:)`](https://developer.apple.com/documentation/realitykit/textureresource/init(cubefromequirectangular:named:quality:facesize:options:)) or [`init(cubeFromImage:named:options:)`](https://developer.apple.com/documentation/realitykit/textureresource/init(cubefromimage:named:options:)).
- Access additional texture resource properties: [`arrayLength`](https://developer.apple.com/documentation/realitykit/textureresource/arraylength), [`depth`](https://developer.apple.com/documentation/realitykit/textureresource/depth), [`pixelFormat`](https://developer.apple.com/documentation/realitykit/textureresource/pixelformat), and [`textureType`](https://developer.apple.com/documentation/realitykit/textureresource/texturetype).
- Add a clearcoat to your custom materials with [`clearcoatNormal`](https://developer.apple.com/documentation/realitykit/custommaterial/clearcoatnormal-swift.property).

##### Physics and Simulations

- Apply force effects on rigid bodies with the [`ForceEffect`](https://developer.apple.com/documentation/realitykit/forceeffect).
- Create simulations such as hinge and slider joints with [`PhysicsJoint`](https://developer.apple.com/documentation/realitykit/physicsjoint).

##### Immersive Environments

- Anchor dockable videos by attaching a [`DockingRegionComponent`](https://developer.apple.com/documentation/realitykit/dockingregioncomponent) to your entity.
- Peer into other immersive worlds with a [`PortalComponent`](https://developer.apple.com/documentation/realitykit/portalcomponent), and allow objects from that world to enter yours with [`PortalCrossingComponent`](https://developer.apple.com/documentation/realitykit/portalcrossingcomponent).
- Further control the lighting in your environment with [`EnvironmentLightingConfigurationComponent`](https://developer.apple.com/documentation/realitykit/environmentlightingconfigurationcomponent).

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/realitykit)*