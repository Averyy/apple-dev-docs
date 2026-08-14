# Creating USD files for Apple devices

**Framework**: USD

Generate 3D assets that render as expected.

#### Overview

Universal Scene Description (USD) is a comprehensive 3D content-creation technology that supports a variety of real-time and offline workflows. Depending on the device and its operating system, there are four renderers that might display a 3D asset you create for your real-time apps and AR experiences: RealityKit, Raytracer, Storm, or SceneKit. Each renderer supports a specific subset of the USD features. Use only USD features supported by the renderer that displays your asset to ensure that it renders and functions as desired. For detailed information about which USD features each renderer supports, see [`Validating feature support for USD files`](validating-usd-files.md).

#### Use Metallic Workflows for Shading

All renderers use a physically based rendering (PBR) technique that the USD specification calls the *metallic workflow*. A metallic workflow shader takes metallic, roughness, and base color values as its core inputs. Most digital content-creation tools (DCCs) support PBR metallic workflow shaders and many of them default to using it.

USD and many DCCs also support a second PBR technique called the *specular workflow* (sometimes also called the *glossy workflow*). The specular workflow renders assets using another algorithm that takes different input values. Only Storm and Raytracer support the specular workflow, so for maximum compatibility use metallic workflow shaders in your DCC so your preview renders accurately represent how your final rendered asset looks.

> **Note**: Find more information and an example shader implementation for both of USD’s PBR workflows by reading the [`USDPreviewSurface shader page`](https://developer.apple.comhttps://openusd.org/release/spec_usdpreviewsurface.html) in the USD specification.

#### Target a Renderer

Your app or operating system will use one of four renderers based on these factors:

- **RealityKit**: The RealityKit renderer is part of the RealityKit framework. It handles drawing for Reality Composer, Reality Composer Pro and RealityKit scenes. Keynote on visionOS, Freeform, and Xcode also use RealityKit to render USDZ files. In macOS 26, QuickLook uses RealityKit to render USDZ files. Starting with macOS 27, Preview defaults to RealityKit for all USD file types and allows selecting Storm or Raytracer, and QuickLook also defaults to RealityKit for all USD file types and allows selecting Storm. Starting with macOS 27, Preview uses the USDKit backend for RealityKit rendering, and QuickLook uses USDKit when rendering non-USDZ files. USDKit has differences from the legacy RealityKit backend, such as not supporting interactive behaviors.
- **Raytracer**: The Raytracer renderer is available in Preview on macOS 27 and later. It provides high-quality path-traced rendering and supports the same USD features as Storm.
- **Storm**: The Storm renderer is a Metal-native implementation of Pixar’s high-performance preview renderer. In macOS 26, QuickLook on macOS uses Storm to render USD, USDA, and USDC files, and Preview uses Storm to display all USD file types, as well as files that may be converted to USD. Starting with macOS 27, Storm is available as an alternative renderer to RealityKit in both Preview and QuickLook.
- **SceneKit**: The SceneKit renderer is part of the deprecated SceneKit framework. It renders 3D content in iWork for macOS and iOS, Motion, and all other apps that use the SceneKit framework, as well as renders SceneKit scenes in Xcode and Preview.

Use the process outlined below to ensure that your USD assets render correctly and function as expected in your app.

#### Understand Coordinate Systems and Units

Different DCCs use different conventions for which axis points up and how large one scene unit is. RealityKit uses Y-up orientation and meters as its unit scale. If you import an asset and it appears rotated or incorrectly scaled, a mismatched coordinate system or unit scale is likely the cause.

Test asset importing early in your workflow so that you can establish a consistent approach for any adjustments. Some DCCs let you configure the export coordinate system and unit scale directly. Preview on macOS 27 and later also allows you to adjust coordinate system and scale when opening USD files.

#### Choose the Right Usd File Format

USD assets can be stored in three file formats, each suited to different stages of your workflow:

- **USDA** is a plain-text format. It is easy to read, diff, and resolve merge conflicts, making it well-suited for collaborative scene files where multiple people may be editing at once. Reality Composer Pro uses USDA as its native scene format.
- **USDC** is a binary format. It is more compact and faster to load than USDA, making it the preferred format for geometry-heavy assets and large scenes.
- **USDZ** is a self-contained zip archive that bundles a USD file with all its dependencies — textures, audio, and other assets — into a single file. USDZ is the recommended format for distributing and sharing assets. Files packaged as USDZ cannot be edited without first unzipping them.

Export directly to USDC from your DCC when working with geometry. Use USDZ when your asset is ready to distribute or deploy.

#### Validate Your Usd Assets

USD files that aren’t well-formed may not work correctly. Validate that your assets conform to the USD specification before including them in your app by using OpenUSD’s `usdchecker` command-line tool.

#### Validate Your Content in Your Target Renderer

Structural validation with `usdchecker` does not catch visual or behavioral issues. Open your assets in the renderer you’re targeting — for example, Reality Composer Pro or Preview — as early as possible in your workflow. Problems like missing materials, incorrect lighting, or unsupported features are much easier to address when caught on individual assets rather than after a full scene has been built.

For RealityKit specifically, test in Reality Composer Pro or on device, since rendering behavior can differ from other preview tools.

#### Use the Latest Usd Schemas

Preliminary schemas are proposals for extending USD with new capabilities that have not yet been standardized by the OpenUSD project or the [`Alliance for OpenUSD (AOUSD)`](https://developer.apple.comhttps://aousd.org). Apple uses preliminary schemas to introduce features — such as anchoring, text rendering, and interactive behaviors — ahead of formal standardization.

Because preliminary schemas are proposals, their structure and behavior can change at any time. Avoid relying on preliminary schemas for production content that needs to remain stable across operating system releases. Renderer support for preliminary schemas also varies — a schema supported by one renderer may not be supported by another.

When a preliminary schema you use becomes standardized, re-export your assets using the standard USD schema to ensure long-term compatibility and the broadest renderer support.

#### Keep Your Polygon Count Low

The number of triangles your renderer must draw each frame is one of the most significant factors affecting performance. Focus on how many triangles are *visible at any one time*, not just the total count in your scene.

A few guidelines:

- **Scale detail to viewer distance.** Nearby objects justify more triangles than objects far from the viewer. Model and optimize each asset based on how large it will appear on screen. To help judge this, place a camera in your DCC at eye height (approximately 1.5m) at the center of your scene and use it to preview how your content will appear from the viewer’s perspective.
- **Split large geometry into chunks.** Large objects like terrain or environments should be divided into smaller meshes. This allows the renderer to cull sections that are off camera rather than drawing the entire object every frame.
- **Account for your presentation context.** Immersive apps occupy significantly more screen area than apps in the shared space and typically require more optimization work. Test performance in the context your app will actually run in.

Test early and often. Performance is easier to manage when you track it throughout development rather than at the end.

#### Target Your Use of Subdivision

USD supports a feature called *subdivision surfaces*, which tells the renderer to generate additional geometry on-the-fly to make the entity render more smoothly. Target your use of this feature to instances when you most need smooth rendering. Each level of subdivision increases the number of rendered polygons in the model by a factor of four, which can have substantial performance implications.

> **Note**: The default `subdivisionScheme` value in USD is `catmullClark`, a subdivision surfaces algorithm. This means subdivision surfaces is automatically enabled for assets that don’t explicitly include a subdivision scheme. To ensure that subdivision surfaces is not enabled for your asset, explicitly set `subdivisionScheme` to `none` when exporting from a DCC. For more information, see the [`documentation for GetSubdivisionSchemeAttr() in the USD specification.`](https://developer.apple.comhttps://openusd.org/release/api/class_usd_geom_mesh.html) You can also use the support scripts below to set `subdivisionScheme` to `none` automatically in your USD files.

#### Target Your Use of Double Sided Geometry

USD geometry can be set to render both sides of a surface by setting the `doubleSided` attribute. Target your use of this feature as its support varies by renderer, which may affect how your content is represented, and its performance.

> **Note**: The default `doubleSided` value is off, however some DCCs enable it automatically during export. It is recommended to review your applications export settings to make sure it is only enabled when desired. You can also use the support scripts below to turn off `doubleSided` on your geometry.

#### Limit Rigged Models to a Single Skeleton

USD supports skeletal animation, which you can use to animate a character or other complex model by manipulating a hierarchy of bones or joints to deform the model. Many DCCs allow you to use multiple *skeletons* (sometimes called *armatures* or *rigs*), to deform a single mesh. For example, for a character model, you might create one skeleton to handle facial animation and a second one to control general body movement. Before exporting models with multiple skeletons to a USD file, merge all the skeletons into a single joint or bone hierarchy. Models with multiple hierarchies can cause performance and compatibility issues with all renderers.

> **Note**: All DCCs implement skeletal animation using either a hierarchy of bones or joints. Both approaches deform the model for animation, but use different underlying data representations. DCCs that use bone-based skeletons automatically convert the skeleton to joints when exporting to USD, because USD only supports joint-based skeletons.

#### Include Material and Skeleton Bindings

USD requires that any geometry with an applied material use the `MaterialBindingAPI`. It also requires that any geometry that has a skeleton use the `SkelBindingAPI`. Without these APIs, the material or skeleton information may not be read by an application.

> **Note**: Some DCC versions may not correctly apply these bindings in a USD file. You can use the support script below to automatically apply them to geometry that has the attributes.

#### Expose Configurations As Variants

USD supports the ability to have multiple representations of an object using a feature called `variants`. USD files define the primary hierarchy path in the file using the `defaultPrim` metadata. Variants that are defined in this `defaultPrim` hierarchy path are shown to the user as configuration options when using QuickLook with USDZ files. When a configuration option is selected, the appearance of the USD being viewed in QuickLook will change to respect the selected variant.

> **Note**: Variants can be authored in some DCCs or using the USD API. You can also use the support script below to combine USDZ files into a single file as variants, as long as they only vary in their material or skeleton animations.

#### Use Efficient Textures

Textures are among the largest contributors to file size and runtime memory usage.

Size your textures to match their visual importance. Objects that appear small on screen or far from the viewer don’t need the same resolution as objects directly in front of the user. Large geometry that occupies most of the view — such as a sky dome — may require significantly higher resolution to avoid visible blurring.

USD files may use a wide range of texture formats, however USDZ files may only include JPEG, PNG, EXR, and AVIF. Use AVIF textures where possible for the best balance between quality and file size. You can use Preview or the `usdcrush` command line tool to compress the textures within your USDZ file to use AVIF.

When building your app in Xcode, textures are compressed automatically. A texture set that is several gigabytes uncompressed will typically reduce to a fraction of that size after compilation. Factor this in when evaluating your texture budget — you don’t need to manually compress everything to its final size during development.

#### Pack Your Textures

Grayscale data textures — such as roughness, metallic, and ambient occlusion — can be combined into the individual channels of a single RGB texture. This *texture packing* reduces the number of texture files in your asset and enables GPU compression, which doesn’t apply to standalone grayscale textures. Packing your textures can meaningfully reduce the total size of your assets.

##### Color Spaces

Select the correct color space for each texture when authoring and importing materials:

- Use **sRGB** for perceptual textures that are displayed directly — such as base color and unlit color.
- Use **linear** (or data) for grayscale textures and HDR images — such as roughness, metallic, ambient occlusion, and normal maps. These textures should not have any color space transformation applied.

Ensure the color space settings in your DCC match the intended encoding of each texture when exporting. Mismatched color spaces cause incorrect rendering that can be subtle and hard to diagnose.

##### Normal Map Formats

There are two common normal map formats: **OpenGL** and **DirectX**. They are visually similar but the DirectX format has its green channel inverted relative to OpenGL. RealityKit expects normal maps in OpenGL format. If your normal maps look incorrect after importing, try inverting the green channel in your DCC before exporting.

#### Minimize Alpha Transparency

Transparent materials are significantly more expensive to render than opaque ones. The GPU must compute the same pixels multiple times for each overlapping layer of transparency — an effect called *overdraw*. Stacked layers of transparency compound this cost.

Where possible:

- Use geometry instead of alpha-clipped cards for detailed edges, such as grass blades or foliage. This trades a small increase in triangle count for a large reduction in overdraw.
- Limit the use of semi-transparent materials and avoid having many transparent surfaces overlap in view.

In most cases, more triangles with fewer transparent pixels is the better trade-off.

#### Bake Lighting Where Possible

> **Note**: This section applies to RealityKit.

Dynamic real-time lights have a runtime performance cost. Where your scene’s lighting does not need to respond to real-world conditions, bake the lighting information into your textures in a DCC, then use unlit materials in RealityKit. Unlit materials are significantly cheaper to render than PBR materials with dynamic lighting.

Use dynamic lights sparingly — for example, only for objects that must respond to real-world illumination or interactive events. For PBR assets that need some environmental shading without fully dynamic lighting, consider using Image-Based Lighting (IBL), which adds view-dependent reflections and diffuse shading from a pre-rendered environment image at a much lower runtime cost than real-time lights.

#### Converting Dense Meshes

Reduce the number of polygons in your geometry and the number of individual meshes to maximize performance.

When working with computer aided design (CAD) files or other dense meshes, use a DCC to retopologize and simplify the geometry. Combine separate mesh objects that share the same material into a single mesh where possible — fewer draw calls improve rendering performance. Avoid exporting every component of a CAD assembly as a separate mesh unless the pieces need to move or be treated independently.

> **Note**: Watch [`Optimize your 3D assets for spatial computing`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2024/10186) to learn more about best practices for textures and meshes.

#### Convert Your Models From Other Formats

Use Preview or the `usdcat` command line tool to convert models from common 3D formats such as Alembic, OBJ, STL, and PLY into USD. To package a converted asset and its dependencies into a USDZ file, use Preview or the `usdzip` command line tool.

If you have been using Reality Converter to create USDZ files, Preview is the recommended replacement. Export directly to USD from your content creation tool when possible, or to one of the supported conversion formats first. Unsupported formats will require an intermediate conversion step using a DCC.

> **Note**: Conversions may not perfectly represent all source data so review your converted files to confirm the output meets your needs.  Conversion tools keep pace with USD standardization, improving their output as schemas mature, and the conversion process itself may also improve between operating system versions. Conversion results are not guaranteed to be identical across operating system versions. For example, PLY files containing Gaussian splat data were converted using a preliminary schema in macOS 26 to preserve the data; in macOS 27 and later, the same files convert to the standardized USD form.

#### Support Scripts

We provide a set of scripts to assist you in creating great USD files, using the OpenUSD Python API. These scripts will help address many of the points above within your USD files, or enable you to create USDZ files using variants.

To download these scripts, see [`USD Support Scripts`](https://developer.apple.comhttps://developer.apple.com/download/files/USD-Support-Scripts.zip).

## Topics

### Understanding USD concepts
- [USD concepts](usd-concepts.md)
  Learn the core terms and ideas behind Universal Scene Description (USD).
### Validating USD feature support
- [Validating feature support for USD files](validating-usd-files.md)
  Ensure that the renderer that displays your USD assets supports its features.

## See Also

- [OpenUSD schemas for AR](usd-schemas-for-ar.md)
  Add augmented reality functionality to your 3D content using USD schemas.
- [Schema definitions for third-party DCCs](schema-definitions-for-third-party-dccs.md)
  Update your local USD library to add interactive and augmented reality features.
- [Validating feature support for USD files](validating-usd-files.md)
  Ensure that the renderer that displays your USD assets supports its features.
- [Placing a prim in the real world](placing-a-prim-in-the-real-world.md)
  Anchor a prim to a real-world object that the runtime recognizes in the physical environment.
- [Previewing a Model with AR Quick Look](../arkit/previewing-a-model-with-ar-quick-look.md)
  Display a model or scene that the user can move, scale, and share with others.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/creating-usd-files-for-apple-devices)*