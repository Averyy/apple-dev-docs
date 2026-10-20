# USDStage.ExportOptions

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

Options for packaging a stage into a USDZ file.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ExportOptions
```

## Topics

### Structures
- [USDStage.ExportOptions.TextureQuality](./exportoptions/texturequality.md)
  A texture quality level.
### Type Properties
- [static var preferSmallMeshFiles: USDStage.ExportOptions](./exportoptions/prefersmallmeshfiles.md)
  Reduce meshes’ file size via quantization and compression.
- [static var preferSmallTextureFiles: USDStage.ExportOptions](./exportoptions/prefersmalltexturefiles.md)
  Reduce textures’ file size at the standard quality level.
### Type Methods
- [static func preferSmallTextureFiles(quality: USDStage.ExportOptions.TextureQuality) -> USDStage.ExportOptions](./exportoptions/prefersmalltexturefiles%28quality%29.md)
  Reduce textures’ file size at the specified quality level.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Exporting the stage
- [func exportPackage(to: URL, options: USDStage.ExportOptions) throws](./exportpackage%28to,options%29-6s2wk.md)
  Packages the stage into a USDZ archive.
- [func exportPackage(to: FilePath, options: USDStage.ExportOptions) throws](./exportpackage%28to,options%29-2x7yr.md)
  Packages the stage into a USDZ archive.
- [func exportFlattened(to: URL) throws](./exportflattened%28to%29-98kpc.md)
  Exports the stage as a flattened USD file.
- [func exportFlattened(to: FilePath) throws](./exportflattened%28to%29-6717d.md)
  Exports the stage as a flattened USD file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/exportoptions)*