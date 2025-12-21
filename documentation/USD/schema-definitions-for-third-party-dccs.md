# Schema definitions for third-party DCCs

**Framework**: USD

Update your local USD library to add interactive and augmented reality features.

#### Overview

These schema definition files contain a codified version of the specification addendum defined by [`OpenUSD schemas for AR`](usd-schemas-for-ar.md). As a developer of third-party DCC software, you enable your users to configure interactive and AR features in their 3D assets by implementing the specification and providing additional UI.

#### Integrate Interactive and Ar Schemas

To recognize and validate syntax, and to participate in USD features such as transform hierarchies, incorporate the new interactive and AR schemas into your DCC by copying the `schema.usda` files into your USD library and rebuilding. For more information, see [`Generating New Schema Classes`](https://developer.apple.comhttps://openusd.org/docs/Generating-New-Schema-Classes.html).

## See Also

- [OpenUSD schemas for AR](usd-schemas-for-ar.md)
  Add augmented reality functionality to your 3D content using USD schemas.
- [Creating USD files for Apple devices](creating-usd-files-for-apple-devices.md)
  Generate 3D assets that render as expected.
- [Validating feature support for USD files](validating-usd-files.md)
  Ensure that the renderer that displays your USD assets supports its features.
- [Placing a prim in the real world](placing-a-prim-in-the-real-world.md)
  Anchor a prim to a real-world object that the runtime recognizes in the physical environment.
- [Previewing a Model with AR Quick Look](../ARKit/previewing-a-model-with-ar-quick-look.md)
  Display a model or scene that the user can move, scale, and share with others.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/schema-definitions-for-third-party-dccs)*