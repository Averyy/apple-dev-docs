# Validating feature support for USD files

**Framework**: USD

Ensure that the renderer that displays your USD assets supports its features.

#### Overview

Depending on the device, its operating system, and the app, there are four renderers that might display your 3D assets: RealityKit, Raytracer, Storm, or SceneKit. Each renderer supports a subset of the USD features. Use the tables below to determine which features are available. See [`Creating USD files for Apple devices`](creating-usd-files-for-apple-devices.md) for more information on how to determine which engine renders your USD asset. This article identifies feature support for assets imported from USD files.

In some cases, the renderers might support features listed below, but do not support importing those features from USD files, and will be marked as unsupported. In the case of Storm, feature support may differ from the open source version.

#### Review General and Media Features

Each rendering engine supports a set of general and media attributes that cover fundamental features, such as which file types the renderer supports, and whether it supports *instancing*, which is a performance optimization where a renderer can inexpensively display a single asset multiple times in a scene.

| USD | RealityKit | Raytracer | Storm | SceneKit |
| --- | --- | --- | --- | --- |
| Instancing | ✔ | ✔ | ✔ | ✔ |
| Point instancing |  | ✔ | ✔ |  |
| Transform animation | ✔ | ✔ | ✔ | ✔ |
| .usdz files | ✔ | ✔ | ✔ | ✔ |
| .usd / .usdc / .usda | ✔ | ✔ | ✔ | ✔ |
| Visibility attribute | ✔ | ✔ | ✔ | ✔ |
| Defer payload loading |  | ✔ | ✔ |  |
| Variants | ✔ | ✔ | ✔ | partial |
| Spatial audio | ✔ |  |  |  |
| Accessibility | ✔ |  |  |  |

- RealityKit supports instancing of mesh and texture data from imported USD files.
- Accessibility data is supported when using USDKit to visualize content with RealityKit.

Variant support is handled differently between the renderers:

- All renderers support loading the active variant.
- RalityKit, Storm and Raytracer support changing the variant after loading the asset but this depends on the context. they are presented in
- In Reality Composer Pro, RealityKit also supports changing the variant after loading the asset.
- QuickLook allows you to change variants on the default prim after loading a USDZ asset.

#### Review Geometry Feature Support

USD supports multiple ways to represent the shape of a 3D object, and has several features that affect the way these objects render.

If a renderer doesn’t support a feature that:

- defines the shape of a 3D object, such as a NURBS patch (a mathematical description of a 3D surface), then the object doesn’t render at all. For example, assets defined using a NURBS patch render on Storm, but not on SceneKit or RealityKit.
- modifies how an asset renders, the feature is just not used, but the object still displays. For example, an asset that uses subdivision surfaces (a feature that generates additional geometry on the fly) displays on all renderers, but only generates the additional geometry when supported.

| USD | RealityKit | Raytracer | Storm | SceneKit |
| --- | --- | --- | --- | --- |
| Polygon meshes | ✔ | ✔ | ✔ | ✔ |
| Vertex animation |  | ✔ | ✔ |  |
| Primitive shapes | ✔ | ✔ | ✔ | ✔ |
| Double-sided meshes |  | ✔ | ✔ | ✔ |
| Subdivision | ✔ | ✔ | ✔ | ✔ |
| NURBS patches |  |  |  |  |
| Basis curves |  | partial |  |  |
| Tetrahedral meshes |  |  |  |  |
| Points |  |  | ✔ | ✔ |
| Camera |  | ✔ | ✔ | ✔ |
| Spatial cameras | ✔ | ✔ | ✔ |  |
| Immersive cameras |  | ✔ |  |  |
| Geometry subsets | ✔ | ✔ | ✔ | ✔ |
| Alembic | ✔ | ✔ | ✔ | ✔ |
| Draco compression |  |  |  |  |
| Vertex colors | ✔ | ✔ | ✔ | ✔ |
| Purpose | ✔ | ✔ | ✔ | ✔ |

All renderers support using attributes specified in the USD file.

- Primitive Shapes are basic geometry types such as cubes, cones, and spheres. The plane type is not supported.
- Alembic supports requires files written using the Ogawa format. The Legacy HDF5 format is not supported.
- The Preview purpose is used by all renderers.
- RealityKit supports subdivision on objects using a USD preview surface shader. Objects with custom MaterialX materials use standard polygonal meshes.
- Tetrahedral meshes (`TetMesh`) are volumetric meshes used in simulation and engineering data.
- Spatial and Immersive cameras are Apple camera types only supported in the Preview app on macOS 27 and later.
- Raytracer supports catmull-rom basis curves only.

#### Review Lighting Support

The USD specification supports many kinds of lights, some that are well-suited to real-time use and others that are primarily intended for use in offline production tasks, such as rendering animations or special effects for movies, because they are computationally expensive. SceneKit and Storm don’t support USD light types that are too computationally expensive for real-time use. Because RealityKit is an AR-first renderer, it doesn’t use any lights included in a USD file, and instead bases its lighting on the scene’s real-world lighting.

| USD | RealityKit | Raytracer | Storm | SceneKit |
| --- | --- | --- | --- | --- |
| Rectangle light |  | ✔ |  |  |
| Distant light |  | ✔ | ✔ | ✔ |
| Sphere light |  | ✔ | ✔ | ✔ |
| Cylinder light |  | ✔ | ✔ |  |
| Dome light |  | ✔ | ✔ | ✔ |
| Disk light |  | ✔ |  |  |
| Mesh light |  | partial |  |  |
| Volume light |  | partial |  |  |
| Light shaping |  | partial |  | ✔ |
| Shadow API |  | ✔ |  |  |
| Light lists |  | ✔ |  |  |
| Portal light |  | ✔ |  |  |

- Raytracer supports mesh lights and volume lights, but without proper light sampling.
- Raytracer has partial support for light shaping.

#### Review Physics Support

USD supports many physics simulation features. Only the RealityKit renderer supports simulation features.

| USD | RealityKit | Raytracer | Storm | SceneKit |
| --- | --- | --- | --- | --- |
| Physics scene | ✔ |  |  |  |
| Rigid body | ✔ |  |  |  |
| Mass | ✔ |  |  |  |
| Collisions | ✔ |  |  |  |
| Mesh collisions |  |  |  |  |
| Physics materials | ✔ |  |  |  |
| Collision groups |  |  |  |  |
| Filtered pairs |  |  |  |  |
| Physics joints |  |  |  |  |
| Physics limits |  |  |  |  |
| Physics drive |  |  |  |  |
| Articulation root |  |  |  |  |

- USDKit does not support loading Physics data into RealityKit.

#### Review Shader Features

The USD specification includes a number of features for use by shaders and even includes a number of pre-defined shaders to ensure consistent rendering across platforms.

| USD | RealityKit | Raytracer | Storm | SceneKit |
| --- | --- | --- | --- | --- |
| Material graph | ✔ | ✔ | ✔ | ✔ |
| USD preview surface shader | ✔ | ✔ | ✔ | ✔ |
| MaterialX | ✔ | ✔ | ✔ |  |
| Textures | ✔ | ✔ | ✔ | ✔ |
| AVIF Textures | ✔ | ✔ | ✔ | ✔ |
| Texture wrap modes | ✔ | ✔ | ✔ | ✔ |
| Texture channel references | partial | ✔ | ✔ | ✔ |
| Texture transforms | partial | ✔ | ✔ | ✔ |
| Specular workflow |  | ✔ | ✔ |  |
| Multiple UV sets | partial | ✔ | ✔ | ✔ |
| Scale | partial | ✔ | ✔ | ✔ |
| Bias |  | ✔ | ✔ | ✔ |
| ColorSpace | ✔ | ✔ | ✔ |  |
| Displacement |  | ✔ |  |  |

Each renderer may support MaterialX nodes to different degrees. Verify your asset rendering against your renderer of choice. The [`ShaderGraph`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph) documentation covers the support for RealityKit.

RealityKit has partial support for some shader features:

- **Texture channel references**: RealityKit supports only a single packed texture per material. You can, however, reference multiple scalar channels within a single texture.
- **Texture transforms**: RealityKit supports a single `UsdTransform2d` per material. If a material contains multiple `UsdTransform2D` instances, the renderer will use the first one it finds.
- **Multiple UV sets**: RealityKit supports two UV Sets.
- **Scale**: RealityKit supports USD texture scaling except for normal map textures.
- **ColorSpace**: RealityKit supports some known colorSpaces like DisplayP3 and sRGB. Color constants and textures will get conversions applied if colorSpace specifies a known name like “srgb_texture”, “lin_srgb”, “srgb_displayp3”, or “lin_displayp3”.
- **sourceColorSpace**: If colorSpace is not specified then the sourceColorSpace attribute is used for conversion of color textures, such as “sRGB” or “raw”.

If no colorSpace or sourceColorSpace value is provided then the embedded image color profile is used when loading color textures.

#### Review Skeletons

Skeletal animation deforms a model based on a hierarchy of joints, which allows you to animate character assets and complex mechanical objects.

| USD | RealityKit | Raytracer | Storm | SceneKit |
| --- | --- | --- | --- | --- |
| Skeletons | ✔ | ✔ | ✔ | ✔ |
| Skeleton animation | ✔ | ✔ | ✔ | ✔ |
| Blend Shapes | ✔ | ✔ | ✔ | ✔ |

#### Review Volumes and Particles

USD supports volumetric data and particle-based representations. These are used for effects such as smoke, fire, and clouds, as well as for 3D Gaussian Splats captured from real-world scenes.

| USD | RealityKit | Raytracer | Storm | SceneKit |
| --- | --- | --- | --- | --- |
| Volumes (OpenVDB) |  | ✔ | ✔ |  |
| Gaussian Splats |  |  | partial |  |

- Storm renders Gaussian Splats as points rather than full volumetric splats.

## See Also

- [OpenUSD schemas for AR](usd-schemas-for-ar.md)
  Add augmented reality functionality to your 3D content using USD schemas.
- [Schema definitions for third-party DCCs](schema-definitions-for-third-party-dccs.md)
  Update your local USD library to add interactive and augmented reality features.
- [Creating USD files for Apple devices](creating-usd-files-for-apple-devices.md)
  Generate 3D assets that render as expected.
- [Placing a prim in the real world](placing-a-prim-in-the-real-world.md)
  Anchor a prim to a real-world object that the runtime recognizes in the physical environment.
- [Previewing a Model with AR Quick Look](../arkit/previewing-a-model-with-ar-quick-look.md)
  Display a model or scene that the user can move, scale, and share with others.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/validating-usd-files)*