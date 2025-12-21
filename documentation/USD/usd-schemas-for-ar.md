# OpenUSD schemas for AR

**Framework**: USD

Add augmented reality functionality to your 3D content using USD schemas.

#### Overview

Universal Scene Description (USD) is a widely-supported specification for the interchange and storage of 3D graphic data. USD files are the preferred interchange format for apps displaying 3D and AR content using the [`ARKit`](https://developer.apple.com/documentation/ARKit) and [`RealityKit`](https://developer.apple.com/documentation/RealityKit) frameworks. Apple, in collaboration with Pixar, developed a set of schemas to extend USD for AR use cases. These schemas, among other things, add the ability to:

- Anchor 3D content at a specific location in the real world.
- React to real-world situations.
- Participate in a physics simulation.
- Connect audio effects to a location.
- Annotate the environment by displaying text.

These schemas allow you to include the data needed to support augmented reality features in AR Quick Look, and also let you use USD files in place of `.reality` files when writing [`RealityKit`](https://developer.apple.com/documentation/RealityKit) apps. Reality Composer Pro uses these schemas to store data for AR features, like anchoring, in its USDA scene files.

To enable AR features in assets from a third-party digital content-creation (DCC) tool that doesn’t support these schemas, export the file as a `.usda` file using the [`USD Toolset`](https://developer.apple.comhttps://openusd.org/release/toolset.html) and edit them by hand.

> **Note**:  These new schemas (see [`Schema definitions for third-party DCCs`](schema-definitions-for-third-party-dccs.md)) are included in the Universal Scene Description specification as an addendum and are marked as preliminary. The addendum also adds metadata (name-value pairs; see [`Metadata`](https://developer.apple.comhttps://openusd.org/release/glossary.html#usdglossary-metadata)), and new data properties ([`Property`](https://developer.apple.comhttps://openusd.org/release/glossary.html#usdglossary-property)). To provide feedback on the addendum, use the [`Feedback Assistant`](https://developer.apple.comhttps://feedbackassistant.apple.com/welcome).

##### Implement Ar Functionality

The following illustration depicts a virtual castle rendered by a , the app or system framework that implements the AR functionality described in the schemas. The prim for the virtual castle (USD refers to individual units of 3D content as  see [`UsdPrim`](https://developer.apple.comhttps://openusd.org/docs/api/class_usd_prim.html)) instructs the runtime to place the castle on a known image in the physical environment, called the image anchor. When the user comes into proximity with the anchor, the runtime displays the 3D visualization of the castle. Falling snowflakes represent additional prims that behave as if in accordance with gravity, and disappear as they approach a real-world surface.

![An illustration of two tables. On the surface of the table on the left, a two-dimensional image of a castle labeled “image anchor” is outlined by a dotted line to indicate that it is replaceable. The table on the right is the same table, viewed through an AR experience created by the app’s camera pass-through on an iOS device. A virtual castle rests on top of the table in place of the 2D image. Virtual snowflakes descend from virtual clouds to fall around the 3D visualization of the castle. Shadows on the table beneath the snowflakes indicate that the runtime projects the location at which each snowflake will land on the table.](https://docs-assets.developer.apple.com/published/50d3890af48ae074a7c3c96da56ba618/usdz-schemas-for-ar-1%402x.png)

## Topics

### Animation
- [autoPlay](autoplay.md)
  Metadata that specifies whether an animation plays automatically on load.
- [playbackMode](playbackmode.md)
  Metadata that controls animation idling until a behavior takes over.
### Anchoring
- [Placing a prim in the real world](placing-a-prim-in-the-real-world.md)
  Anchor a prim to a real-world object that the runtime recognizes in the physical environment.
- [Preliminary_AnchoringAPI](preliminary-anchoringapi.md)
  A schema that defines the placement of a prim and its children at a real-world location.
- [Preliminary_ReferenceImage](preliminary-referenceimage.md)
  A schema that defines the properties of an image in the physical environment.
### Behaviors
- [Actions and triggers](actions-and-triggers.md)
  Enable visual and audible responses to programmatic or environmental events.
### Text
- [Preliminary_Text](preliminary-text.md)
  A prim that renders 3D text in a scene.
### Scenes and lighting
- [Specifying a lighting environment in AR Quick Look](../ARKit/specifying-a-lighting-environment-in-ar-quick-look.md)
  Add metadata to your USDZ file to specify its lighting characteristics.
- [preferredIblVersion](preferrediblversion.md)
  Metadata that determines the lighting environment of virtual content.
- [sceneLibrary](scenelibrary.md)
  Metadata that partitions an asset into scene-based units.
### Digital content creation
- [Schema definitions for third-party DCCs](schema-definitions-for-third-party-dccs.md)
  Update your local USD library to add interactive and augmented reality features.

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/usd/usd-schemas-for-ar)*