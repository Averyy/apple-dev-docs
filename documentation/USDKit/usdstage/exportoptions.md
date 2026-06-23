# USDStage.ExportOptions

**Framework**: USDKit  
**Kind**: struct

Options for packaging a stage into a USDZ file.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ExportOptions
```

## Topics

### Structures
- [USDStage.ExportOptions.TextureQuality](usdstage/exportoptions/texturequality.md)
  A texture quality level.
### Type Properties
- [static var preferSmallMeshFiles: USDStage.ExportOptions](usdstage/exportoptions/prefersmallmeshfiles.md)
  Reduce meshes’ file size via quantization and compression.
- [static var preferSmallTextureFiles: USDStage.ExportOptions](usdstage/exportoptions/prefersmalltexturefiles.md)
  Reduce textures’ file size at the standard quality level.
### Type Methods
- [static func preferSmallTextureFiles(quality: USDStage.ExportOptions.TextureQuality) -> USDStage.ExportOptions](usdstage/exportoptions/prefersmalltexturefiles(quality:).md)
  Reduce textures’ file size at the specified quality level.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func exportPackage(to: URL, options: USDStage.ExportOptions) throws](usdstage/exportpackage(to:options:)-6s2wk.md)
  Packages the stage into a USDZ archive.
- [func exportPackage(to: FilePath, options: USDStage.ExportOptions) throws](usdstage/exportpackage(to:options:)-2x7yr.md)
  Packages the stage into a USDZ archive.
- [func exportFlattened(to: URL) throws](usdstage/exportflattened(to:)-98kpc.md)
  Exports the stage as a flattened USD file.
- [func exportFlattened(to: FilePath) throws](usdstage/exportflattened(to:)-6717d.md)
  Exports the stage as a flattened USD file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/exportoptions)*