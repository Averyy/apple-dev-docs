# export(to:)

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

Writes the layer’s contents to a file at the given URL.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func export(to url: URL) throws
```

## Discussion

> **Throws**: An error if the layer cannot be written.

## Parameters

- `url`: The destination file URL.

## See Also

### Exporting and importing
- [func export(to: FilePath) throws](./export%28to%29-5hboj.md)
  Writes the layer’s contents to a file at the given path.
- [func importContents(from: FilePath) throws](./importcontents%28from%29-2ipug.md)
  Replaces the layer’s contents with the layer file at the given path.
- [func importContents(from: String) throws](./importcontents%28from%29-99hnf.md)
  Replaces the layer’s contents with the USDA string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/export(to:)-7vouy)*