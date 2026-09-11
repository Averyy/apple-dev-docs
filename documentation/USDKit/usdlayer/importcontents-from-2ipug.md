# importContents(from:)

**Framework**: USDKit  
**Kind**: method

Replaces the layer’s contents with the layer file at the given path.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func importContents(from path: FilePath) throws
```

#### Discussion

> **Note**: An error if the file cannot be read or parsed.

## Parameters

- `path`: The path of the layer file to read.

## See Also

- [func export(to: URL) throws](usdlayer/export(to:)-7vouy.md)
  Writes the layer’s contents to a file at the given URL.
- [func export(to: FilePath) throws](usdlayer/export(to:)-5hboj.md)
  Writes the layer’s contents to a file at the given path.
- [func importContents(from: String) throws](usdlayer/importcontents(from:)-99hnf.md)
  Replaces the layer’s contents with the USDA string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/importcontents(from:)-2ipug)*