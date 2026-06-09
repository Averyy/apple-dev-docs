# exportPackage(to:options:)

**Framework**: USDKit  
**Kind**: method

Packages the stage into a USDZ archive.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func exportPackage(to url: URL, options: USDStage.ExportOptions = []) throws
```

#### Discussion

The stage and its referenced assets are bundled into a USDZ file. Layer structure is preserved — this operation does not flatten.

Throws an error if the extension is not `.usdz`.

## See Also

- [func exportPackage(to: FilePath, options: USDStage.ExportOptions) throws](usdstage-4sfi1/exportpackage(to:options:)-2x7yr.md)
  Packages the stage into a USDZ archive.
- [func exportFlattened(to: URL) throws](usdstage-4sfi1/exportflattened(to:)-98kpc.md)
  Exports the stage as a flattened USD file.
- [func exportFlattened(to: FilePath) throws](usdstage-4sfi1/exportflattened(to:)-6717d.md)
  Exports the stage as a flattened USD file.
- [USDStage.ExportOptions](usdstage-4sfi1/exportoptions.md)
  Options for packaging a stage into a USDZ file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage-4sfi1/exportpackage(to:options:)-6s2wk)*