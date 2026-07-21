# exportPackage(options:)

**Framework**: USDKit  
**Kind**: method

Packages the stage into a USDZ archive and returns it as in-memory data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func exportPackage(options: USDStage.ExportOptions = []) throws -> Data
```

#### Discussion

The stage and its referenced assets are bundled into a USDZ archive in memory. Layer structure is preserved - this operation does not flatten.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/exportpackage(options:))*