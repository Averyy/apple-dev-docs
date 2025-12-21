# USD

**Framework**: USD

An efficient and scalable way to represent 3D scenes.

#### Overview

[`Universal Scene Description`](https://developer.apple.comhttps://openusd.org/release/index.html) (, though commonly referred to as ) is an efficient, scalable system for authoring, reading, and streaming graphics data. Originally developed by Pixar for their feature films, it is now a proposed open standard being promoted by the [`Alliance for OpenUSD (AOUSD)`](https://developer.apple.comhttps://aousd.org). Apple and Pixar are both founding members of the AOUSD.

USD is also Apple’s format of choice for 3D Content, including 3D content used for Augmented Reality. You can load USD files in your RealityKit and ARKit apps or import them into your Reality Composer Pro projects. You can even embed USD content in your apps or on web sites using AR Quick Look. USD is also an extensible format, allowing apps that use it to create custom schemas to store and load data needed to support custom features. For an example, see the proposed [`OpenUSD schemas for AR`](usd-schemas-for-ar.md) that Apple created, in conjunction with Pixar, to extend USD to support AR functionality like anchoring.

Unlike other interchange specifications, USD supports assembling any number of assets into virtual sets, scenes, shots, and worlds, and allows non-destructive editing with a single, consistent API and stored in a single scenegraph. Although it is common practice to create separate USD files for individual 3D model, USD files can reference other USD files, and even override the contents of referenced USD files, allowing a completely non-destructive workflow.

> **Note**: Apple platforms ship with support for USD built-in, but you can also compile USD from [`source code`](https://developer.apple.comhttps://github.com/PixarAnimationStudios/OpenUSD) to try out features and tooling that are new or are still under-development.

## Topics

### Essentials
- [OpenUSD schemas for AR](usd-schemas-for-ar.md)
  Add augmented reality functionality to your 3D content using USD schemas.
- [Schema definitions for third-party DCCs](schema-definitions-for-third-party-dccs.md)
  Update your local USD library to add interactive and augmented reality features.
- [Creating USD files for Apple devices](creating-usd-files-for-apple-devices.md)
  Generate 3D assets that render as expected.
- [Validating feature support for USD files](validating-usd-files.md)
  Ensure that the renderer that displays your USD assets supports its features.
- [Placing a prim in the real world](placing-a-prim-in-the-real-world.md)
  Anchor a prim to a real-world object that the runtime recognizes in the physical environment.
- [Previewing a Model with AR Quick Look](../ARKit/previewing-a-model-with-ar-quick-look.md)
  Display a model or scene that the user can move, scale, and share with others.


---

*[View on Apple Developer](https://developer.apple.com/documentation/USD)*