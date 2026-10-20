# exportPackage(to:options:)

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

Packages the stage into a USDZ archive.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func exportPackage(to url: URL, options: USDStage.ExportOptions = []) throws
```

#### Discussion

The stage and its referenced assets are bundled into a USDZ file. Layer structure is preserved — this operation does not flatten.

Throws an error if the extension is not `.usdz`.

## See Also

### Exporting the stage
- [func exportPackage(to: FilePath, options: USDStage.ExportOptions) throws](./exportpackage%28to,options%29-2x7yr.md)
  Packages the stage into a USDZ archive.
- [func exportFlattened(to: URL) throws](./exportflattened%28to%29-98kpc.md)
  Exports the stage as a flattened USD file.
- [func exportFlattened(to: FilePath) throws](./exportflattened%28to%29-6717d.md)
  Exports the stage as a flattened USD file.
- [USDStage.ExportOptions](./exportoptions.md)
  Options for packaging a stage into a USDZ file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/exportpackage(to:options:)-6s2wk)*