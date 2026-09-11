# exportPackage(options:)

**Framework**: USDKit  
**Kind**: method

Packages the stage into a USDZ archive and returns it as in-memory data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func exportPackage(options: USDStage.ExportOptions = []) throws -> Data
```

#### Discussion

The stage and its referenced assets are bundled into a USDZ archive in memory. Layer structure is preserved - this operation does not flatten.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/exportpackage(options:))*