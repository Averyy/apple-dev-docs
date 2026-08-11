# USDKit

**Framework**: USDKit  
**Kind**: module

Author, compose, and manipulate Universal Scene Description content from Swift.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

#### Overview

USDKit is the Swift API for authoring, composing, and manipulating Universal Scene Description (USD) content. USD is an open scene-interchange format originated by Pixar and now stewarded by the Alliance for OpenUSD; it represents 3D scenes, assets, and animations across digital-content-creation tools and runtime engines. USDKit exposes a curated subset of OpenUSD through a hand-written, ABI-stable Swift surface.

The framework centers on three core types. A [`USDLayer`](usdlayer.md) represents a single USD document — either a file on disk or an anonymous in-memory document — and serves as the unit of scene description. A [`USDStage`](usdstage.md) assembles a hierarchy from one or more layers by applying USD’s composition rules to a root layer, producing the runtime view of a scene. Each node in that hierarchy is a [`USDPrim`](usdprim.md), which carries a path, attributes, relationships, references, and child primitives. Because multiple layers can define or override the same primitive, the stage composes the contributions from each layer to produce the final scene.

Typical work in USDKit includes generating USD documents procedurally, extracting information from existing assets, applying bulk transformations across composed scenes, and building editors or pipeline tools. The framework also provides the supporting types that authoring depends on — type-erased value containers, interned string tokens, and transform operations — along with a RealityKit integration layer for rendering and playing composed scenes inside an entity hierarchy.

## Topics

### Essentials
- [struct USDStage](usdstage.md)
  A 3D scene composed from one or more Universal Scene Description (USD) documents.
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
  Drives timeline playback of a USD stage and produces per-frame render data.
### Render diagnostics
- [struct USDRenderError](usdrendererror.md)
  An error produced when rendering a USD stage fails.
### Structures
- [struct USDArray](usdarray.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/USDKit)*