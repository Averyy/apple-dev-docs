# export(to:)

**Framework**: USDKit  
**Kind**: method

Writes the layer’s contents to a file at the given URL.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func export(to url: URL) throws
```

#### Discussion

> **Note**: An error if the layer cannot be written.

## Parameters

- `url`: The destination file URL.

## See Also

- [func export(to: FilePath) throws](usdlayer/export(to:)-5hboj.md)
  Writes the layer’s contents to a file at the given path.
- [func importContents(from: FilePath) throws](usdlayer/importcontents(from:)-2ipug.md)
  Replaces the layer’s contents with the layer file at the given path.
- [func importContents(from: String) throws](usdlayer/importcontents(from:)-99hnf.md)
  Replaces the layer’s contents with the USDA string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/export(to:)-7vouy)*