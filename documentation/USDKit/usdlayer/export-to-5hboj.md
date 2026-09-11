# export(to:)

**Framework**: USDKit  
**Kind**: method

Writes the layer’s contents to a file at the given path.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func export(to path: FilePath) throws
```

#### Discussion

> **Note**: An error if the layer cannot be written.

## Parameters

- `path`: The destination file path.

## See Also

- [func export(to: URL) throws](usdlayer/export(to:)-7vouy.md)
  Writes the layer’s contents to a file at the given URL.
- [func importContents(from: FilePath) throws](usdlayer/importcontents(from:)-2ipug.md)
  Replaces the layer’s contents with the layer file at the given path.
- [func importContents(from: String) throws](usdlayer/importcontents(from:)-99hnf.md)
  Replaces the layer’s contents with the USDA string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/export(to:)-5hboj)*