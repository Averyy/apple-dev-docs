# USDKit

**Framework**: USDKit  
**Kind**: module

Author, compose, and manipulate Universal Scene Description content from Swift.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

#### Overview

USDKit is the Swift API for authoring, composing, and manipulating Universal Scene Description (USD) content. USD is an open scene-interchange format originated by Pixar and now stewarded by the Alliance for OpenUSD; it represents 3D scenes, assets, and animations across digital-content-creation tools and runtime engines. USDKit exposes a curated subset of OpenUSD through a hand-written, ABI-stable Swift surface.

The framework centers on three core types. A [`USDLayer`](usdlayer.md) represents a single USD document — either a file on disk or an anonymous in-memory document — and serves as the unit of scene description. A [`USDStage`](usdstage-4sfi1.md) assembles a hierarchy from one or more layers by applying USD’s composition rules to a root layer, producing the runtime view of a scene. Each node in that hierarchy is a [`USDPrim`](usdprim.md), which carries a path, attributes, relationships, references, and child primitives. Because multiple layers can define or override the same primitive, the stage composes the contributions from each layer to produce the final scene.

Typical work in USDKit includes generating USD documents procedurally, extracting information from existing assets, applying bulk transformations across composed scenes, and building editors or pipeline tools. The framework also provides the supporting types that authoring depends on — type-erased value containers, interned string tokens, and transform operations — along with a RealityKit integration layer for rendering and playing composed scenes inside an entity hierarchy.

## Topics

### Essentials
- [struct USDStage](usdstage-4sfi1.md)
  A composed, runtime view of a USD scene assembled from one or more layers.
- [struct USDPrim](usdprim.md)
  A single node in a stage’s scene hierarchy that holds attributes, relationships, metadata, and child prims.
- [struct USDLayer](usdlayer.md)
  A single USD document that stores scene description in a file or in memory.
### Values and tokens
- [struct USDValue](usdvalue.md)
  A type-erased container for a value stored in a Universal Scene Description file.
- [protocol USDValueProtocol](usdvalueprotocol.md)
  A type that can be wrapped in a [`USDValue`](usdvalue.md).
- [struct USDToken](usdtoken.md)
  An interned, efficiently compared string that names prims, properties, and other scene-description identifiers.
### Transforms
- [struct USDTransformOperation](usdtransformoperation.md)
  A single transform applied to a prim, such as a translation, rotation, scale, or matrix.
### RealityKit rendering and playback
- [struct USDStageComponent](usdstagecomponent.md)
  A component that renders a USD stage as RealityKit entities.
- [class USDPlayer](usdplayer.md)
  An object that drives timeline playback of a USD stage in RealityKit.
### Render data
- [struct MeshData](meshdata.md)
  The geometry of a mesh extracted from a USD stage for rendering in RealityKit.
- [struct MaterialData](materialdata.md)
  A material, including its shader graph and assigned textures, extracted from a USD stage for rendering.
- [struct TextureData](texturedata.md)
  A texture, including its pixel data and layout, extracted from a USD stage for rendering.
- [struct TextureLevelInfo](texturelevelinfo.md)
  The byte layout of a single mip level within a texture’s pixel data.
- [struct DeformationData](deformationdata.md)
  The blend-shape, skinning, and renormalization data that animates a mesh extracted from a USD stage.
### Render data identifiers
- [struct MeshID](meshid.md)
  Mesh resource identifier
- [struct MaterialID](materialid.md)
  Material resource identifier
- [struct TextureID](textureid.md)
  Texture resource identifier
- [struct DeformationID](deformationid.md)
  Deformation resource identifier
### Render diagnostics
- [struct USDRenderError](usdrendererror.md)
  An error that occurs while rendering or converting a USD stage for RealityKit.
### Legacy types
- [struct UsdStage](usdstage-mo6c.md)
  An empty stand-in for the stage type that defines no members of its own.
- [struct UsdRenderMessage](usdrendermessage.md)
  A diagnostic message emitted while rendering or converting a USD stage.
- [protocol StageKitPlugin](stagekitplugin.md)
  An internal registration point used by USDKit’s bundled plugins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/USDKit)*