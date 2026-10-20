# RealityKit updates

**Framework**: Updates  
**Role**: Article

Learn about important changes in RealityKit.

#### Overview

Browse notable changes in [RealityKit](../RealityKit/RealityKit.md).

#### June 2025

##### General

- Create hover effect groups to indicate entities that need to highlight together using [`HoverEffectComponent.GroupID`](../RealityKit/hovereffectcomponent/groupid.md).
- Present popovers from volumes using [`PresentationComponent`](../RealityKit/presentationcomponent.md).
- Manually create instances of entities using [`MeshInstancesComponent`](../RealityKit/meshinstancescomponent.md).
- Animate entities implicitly using [`animate(_:body:completion:)`](../RealityKit/entity/animate%28_,body,completion%29.md).
- Create and modify attachments in a more streamlined fashion using [`ViewAttachmentComponent`](../RealityKit/viewattachmentcomponent.md).
- Make entities render behind real-world objects based on depth using [`EnvironmentBlendingComponent`](../RealityKit/environmentblendingcomponent.md).
- Implement post-processing effects using [`RealityViewPostProcessEffect`](../RealityKit/realityviewpostprocesseffect.md) and [`PostProcessEffectContext`](../RealityKit/postprocesseffectcontext.md).
- Attach models together using [`attach(_:to:)`](../RealityKit/entity/attach%28_,to%29.md).
- [`TextureResource`](../RealityKit/textureresource.md) now supports AVIF textures and entities you load from USDZ files that contain AVIF textures using [`init(named:in:)`](../RealityKit/entity/init%28named,in%29.md)  so they render correctly.
- Load entities from Data objects using [`init(from:configurations:)`](../RealityKit/entity/init%28from,configurations%29.md).

##### Image presentation

- Generate spatial scenes using [`ImagePresentationComponent.Spatial3DImage`](../RealityKit/imagepresentationcomponent/spatial3dimage.md) and present them (along with 2D images and spatial photos) using [`ImagePresentationComponent`](../RealityKit/imagepresentationcomponent.md).
- Receive notifications related to presenting images using [`ImagePresentationEvents`](../RealityKit/imagepresentationevents.md).
- Use [`Model3DAsset`](../RealityKit/model3dasset.md) with [`Model3D`](../RealityKit/model3d.md) to play animations in Model3D Views.

##### ARKit integration

- Receive updates about ARKit anchors directly in RealityKit using [`AnchorStateEvents`](../RealityKit/anchorstateevents.md) and [`SceneEvents.TrackingStateUpdate`](../RealityKit/sceneevents/trackingstateupdate.md).

##### SwiftUI integration

- Use SwiftUI implicit animations using the [`Animation`](../SwiftUI/animation.md) modifier with RealityKit entities and components.
- Keep SwiftUI state in sync with RealityKit state using [`Entity.Observable`](../RealityKit/entity/observable-swift.struct.md).
- Present USD variants in [`Model3D`](../RealityKit/model3d.md) using [`Entity.ConfigurationCatalog`](../RealityKit/entity/configurationcatalog.md).
- Specify the frame sizing and alignment option for RealityView using [`RealityViewLayoutOption`](../RealityKit/realityviewlayoutoption.md).

##### Video presentation

- Play spatial video, 180°, 360°, wide-FOV APMP video, and Apple Immersive Video in  [`VideoPlayerComponent`](../RealityKit/videoplayercomponent.md).
- Retrieve the loading status when playing video using [`VideoPlayerComponent`](../RealityKit/videoplayercomponent.md) with [`currentRenderingStatus`](../RealityKit/videoplayercomponent/currentrenderingstatus.md).
- Receive notifications when a video stops playing due to a comfort violation using [`VideoPlayerEvents.VideoComfortMitigationDidOccur`](../RealityKit/videoplayerevents/videocomfortmitigationdidoccur.md).

##### Gestures and entity interaction

- Implement six degree of freedom (6DOF) gestures for manipulating entities using [`ManipulationComponent`](../RealityKit/manipulationcomponent.md).
- Leverage [`GestureComponent`](../RealityKit/gesturecomponent.md) to support gestures on individual entities.

#### June 2024

##### General

- Add artistic lights and shadows to your visionOS app with [`PointLightComponent`](../RealityKit/pointlightcomponent.md), [`DirectionalLightComponent`](../RealityKit/directionallightcomponent.md), [`SpotLightComponent`](../RealityKit/spotlightcomponent.md), and [`DynamicLightShadowComponent`](../RealityKit/dynamiclightshadowcomponent.md).
- Manage spatial tracking in your app with the [`SpatialTrackingSession`](../RealityKit/spatialtrackingsession.md).
- Use [`LowLevelMesh`](../RealityKit/lowlevelmesh.md) to efficiently bring your mesh data to RealityKit, including custom vertex attributes, formats, and layouts.
- Use an [`AnimationLibraryComponent`](../RealityKit/animationlibrarycomponent.md) to store associated animations with an entity that plays the animations.
- Create an  [`IKComponent`](../RealityKit/ikcomponent.md) to animate a skeletal model with an inverse kinematics [`IKComponent.Solver`](../RealityKit/ikcomponent/solver.md).
- Use an [`AudioLibraryComponent`](../RealityKit/audiolibrarycomponent.md) to store associated audio with an entity that plays the audio.
- Stream generated audio in real time with [`AudioGeneratorController`](../RealityKit/audiogeneratorcontroller.md).
- Manage the meshes on your blend shapes with [`BlendShapeWeightsComponent`](../RealityKit/blendshapeweightscomponent.md).
- Create more engaging sound effects by configuring rolloff and reverb with the [`SpatialAudioComponent`](../RealityKit/spatialaudiocomponent.md).
- Customize hover effects when using [`HoverEffectComponent`](../RealityKit/hovereffectcomponent.md), such as spotlight styles, highlight styles, or shader-backed hover effects for additional control over hover behaviors.

##### Models and materials

- Optimize material initialization with a [`CustomMaterial.Program`](../RealityKit/custommaterial/program-swift.class.md) to compile backing shaders.
- Use [`init(from:)`](../RealityKit/textureresource/init%28from%29.md) to efficiently update custom texture data in RealityKit, including custom pixel formats, texture types, swizzle, and texture usage.
- Create cube texture resources with [`init(cubeFromEquirectangular:named:quality:faceSize:options:)`](../RealityKit/textureresource/init%28cubefromequirectangular,named,quality,facesize,options%29.md) or [`init(cubeFromImage:named:options:)`](../RealityKit/textureresource/init%28cubefromimage,named,options%29.md).
- Access additional texture resource properties: [`arrayLength`](../RealityKit/textureresource/arraylength.md), [`depth`](../RealityKit/textureresource/depth.md), [`pixelFormat`](../RealityKit/textureresource/pixelformat.md), and [`textureType`](../RealityKit/textureresource/texturetype.md).
- Add a clearcoat to your custom materials with [`clearcoatNormal`](../RealityKit/custommaterial/clearcoatnormal-swift.property.md).

##### Physics and simulations

- Apply force effects on rigid bodies with the [`ForceEffect`](../RealityKit/forceeffect.md).
- Create simulations such as hinge and slider joints with [`PhysicsJoint`](../RealityKit/physicsjoint.md).

##### Immersive environments

- Anchor dockable videos by attaching a [`DockingRegionComponent`](../RealityKit/dockingregioncomponent.md) to your entity.
- Peer into other immersive worlds with a [`PortalComponent`](../RealityKit/portalcomponent.md), and allow objects from that world to enter yours with [`PortalCrossingComponent`](../RealityKit/portalcrossingcomponent.md).
- Further control the lighting in your environment with [`EnvironmentLightingConfigurationComponent`](../RealityKit/environmentlightingconfigurationcomponent.md).

## See Also

### Technology and frameworks
- [Accelerate updates](./accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](./accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](./activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](./adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](./appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](./appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](./appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](./apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](./applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](./applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](./arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](./audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](./authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](./avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](./avfoundation.md)
  Learn about important changes to AVFoundation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/realitykit)*