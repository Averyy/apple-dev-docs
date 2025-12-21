# Validating feature support for USD files

**Framework**: USD

Ensure that the renderer that displays your USD assets supports its features.

#### Overview

Depending on the device, its operating system, and the app, there are three renderers that might display your 3D assets: RealityKit, SceneKit, or Storm. Each renderer supports a subset of the USD features. Use the tables below to determine which features are available. See [`Creating USD files for Apple devices`](creating-usd-files-for-apple-devices.md) for more information on how to determine which engine renders your USD asset. This article identifies feature support for assets imported from USD files. In some cases, the renderers might support features listed below, but do not support importing those features from USD files. In the case of Storm, feature support may differ from the open source version.

#### Review General and Media Features

Each rendering engine supports a set of general and media attributes that cover fundamental features, such as which file types the renderer supports, and whether it supports , which is a performance optimization where a renderer can inexpensively display a single asset multiple times in a scene.

| USD | RealityKit | SceneKit | Storm |
| --- | --- | --- | --- |
| Instancing | ✔ | ✔ | ✔ |
| Point instancing |  |  | ✔ |
| Transform animation | ✔ | ✔ | ✔ |
| .usdz files | ✔ | ✔ | ✔ |
| .usd / .usdc / .usda | ✔ | ✔ | ✔ |
| Visibility attribute | ✔ | ✔ | ✔ |
| Defer payload loading |  |  | ✔ |
| Variants | ✔ | partial | ✔ |
| Spatial audio | ✔ |  |  |

Variant support is handled differently between the three renderers:

- All three renderers support loading the active variant.
- Storm supports changing the variant after loading the asset.
- In Reality Composer Pro, RealityKit also supports changing the variant after loading the asset.
- QuickLook allows you to change variants on the default prim after loading a USDZ asset.
- RealityKit supports instancing of mesh and texture data from imported USD files.
- RealityKit supports instancing, .usd, .usdc, .usda, visibility attribute, and variants starting with visionOS 2.0, Reality Composer Pro, macOS 15, iOS 18, and iPadOS 18.

#### Review Geometry Feature Support

USD supports multiple ways to represent the shape of a 3D object, and has several features that affect the way these objects render.

If a renderer doesn’t support a feature that:

- defines the shape of a 3D object, such as a NURBS patch (a mathematical description of a 3D surface), then the object doesn’t render at all. For example, assets defined using a NURBS patch render on Storm, but not on SceneKit or RealityKit.
- modifies how an asset renders, the feature is just not used, but the object still displays. For example, an asset that uses subdivision surfaces (a feature that generates additional geometry on the fly) displays on all three renderers, but only generates the additional geometry when supported.

| USD | RealityKit | SceneKit | Storm |
| --- | --- | --- | --- |
| Polygon meshes | ✔ | ✔ | ✔ |
| Vertex animation |  |  | ✔ |
| Primitive shapes | ✔ | ✔ | ✔ |
| Double-sided meshes |  | ✔ | ✔ |
| Subdivision | ✔ | ✔ | ✔ |
| NURBS patches |  |  |  |
| Basis curves |  |  |  |
| Points |  | ✔ | ✔ |
| Camera |  | ✔ | ✔ |
| Geometry subsets | ✔ | ✔ | ✔ |
| Alembic | ✔ | ✔ | ✔ |
| Draco compression |  |  |  |
| Vertex colors | ✔ | ✔ | ✔ |
| Purpose | ✔ | ✔ | ✔ |

All three renderers support using attributes specified in the USD file, but RealityKit only supports Alembic and vertex colors on Reality Composer Pro, visionOS, visionOS Simulator, macOS 15, iOS 18, iPadOS 18 and later.

- Primitive Shapes are basic geometry types such as cubes, cones, and spheres. The plane type is not supported.
- Alembic supports requires files written using the Ogawa format. The Legacy HDF5 format is not supported.
- The Preview purpose is used by all three renderers.
- RealityKit supports subdivision on objects using a USD preview surface shader, starting with visionOS 2, macOS 15, iOS 18, and iPadOS 18. Objects with custom MaterialX materials use standard polygonal meshes.

#### Review Lighting Support

The USD specification supports many kinds of lights, some that are well-suited to real-time use and others that are primarily intended for use in offline production tasks, such as rendering animations or special effects for movies, because they are computationally expensive. SceneKit and Storm don’t support USD light types that are too computationally expensive for real-time use. Because RealityKit is an AR-first renderer, it doesn’t use any lights included in a USD file, and instead bases its lighting on the scene’s real-world lighting.

| USD | RealityKit | SceneKit | Storm |
| --- | --- | --- | --- |
| Rectangle light |  |  |  |
| Distant light |  | ✔ | ✔ |
| Sphere light |  | ✔ | ✔ |
| Cylinder light |  |  | ✔ |
| Dome light |  | ✔ | ✔ |
| Disk light |  |  |  |
| Mesh light |  |  |  |
| Volume light |  |  |  |
| Light shaping |  | ✔ |  |
| Shadow API |  |  |  |
| Light lists |  |  |  |
| Light filters |  |  |  |
| Portal light |  |  |  |

#### Review Physics Support

USD supports many physics simulation features. Only the RealityKit renderer supports simulation features.

| USD | RealityKit | SceneKit | Storm |
| --- | --- | --- | --- |
| Physics scene | ✔ |  |  |
| Rigid body | ✔ |  |  |
| Mass | ✔ |  |  |
| Collisions | ✔ |  |  |
| Mesh collisions |  |  |  |
| Physics materials | ✔ |  |  |
| Collision groups |  |  |  |
| Filtered pairs |  |  |  |
| Physics joints |  |  |  |
| Physics limits |  |  |  |
| Physics drive |  |  |  |
| Articulation root |  |  |  |

#### Review Shader Features

The USD specification includes a number of features for use by shaders and even includes a number of pre-defined shaders to ensure consistent rendering across platforms.

| USD | RealityKit | SceneKit | Storm |
| --- | --- | --- | --- |
| Material graph | ✔ | ✔ | ✔ |
| USD preview surface shader | ✔ | ✔ | ✔ |
| MaterialX | ✔ |  | ✔ |
| Textures | ✔ | ✔ | ✔ |
| AVIF Textures | ✔ | ✔ | ✔ |
| Texture wrap modes | ✔ | ✔ | ✔ |
| Texture channel references | partial | ✔ | ✔ |
| Texture transforms | partial | ✔ | ✔ |
| Specular workflow |  |  | ✔ |
| Multiple UV sets | partial | ✔ | ✔ |
| Scale | partial | ✔ | ✔ |
| Bias |  | ✔ | ✔ |
| ColorSpace | ✔ |  | ✔ |
| Displacement |  |  |  |

MaterialX support is available on Reality Composer Pro, visionOS, visionOS Simulator, macOS 15, iOS 18, iPadOS 18 and later.

Textures in the AVIF format are supported in visionOS 2.4, visionOS Simulator 2.4, macOS 15.4, iOS 18.4, iPadOS 18.4 and later.

RealityKit has partial support for some shader features:

If no colorSpace or sourceColorSpace value is provided then the embedded image color profile is used when loading color textures.

#### Review Skeletons

Skeletal animation deforms a model based on a hierarchy of joints, which allows you to animate character assets and complex mechanical objects.

| USD | RealityKit | SceneKit | Storm |
| --- | --- | --- | --- |
| Skeletons | ✔ | ✔ | ✔ |
| Skeleton animation | ✔ | ✔ | ✔ |
| Blend Shapes | ✔ | ✔ | ✔ |

- RealityKit supports Blend Shapes starting with visionOS 2, macOS 15, iOS 18, and iPadOS 18.

## See Also

- [OpenUSD schemas for AR](usd-schemas-for-ar.md)
  Add augmented reality functionality to your 3D content using USD schemas.
- [Schema definitions for third-party DCCs](schema-definitions-for-third-party-dccs.md)
  Update your local USD library to add interactive and augmented reality features.
- [Creating USD files for Apple devices](creating-usd-files-for-apple-devices.md)
  Generate 3D assets that render as expected.
- [Placing a prim in the real world](placing-a-prim-in-the-real-world.md)
  Anchor a prim to a real-world object that the runtime recognizes in the physical environment.
- [Previewing a Model with AR Quick Look](../ARKit/previewing-a-model-with-ar-quick-look.md)
  Display a model or scene that the user can move, scale, and share with others.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/validating-usd-files)*