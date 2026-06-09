# open(_:options:)

**Framework**: USDKit  
**Kind**: method

Returns an already-loaded layer at the identifier, or opens it from the resolved asset path.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func open(_ identifier: String, options: USDLayer.OpenOptions = []) throws -> USDLayer
```

#### Return Value

The opened layer.

#### Discussion

> **Note**: An error if the layer cannot be opened or created.

## Parameters

- `identifier`: The layer identifier — typically a file path, URL, or anonymous identifier.
- `options`: Pass `.createNew` to create a fresh layer, overwriting any existing file at the identifier.

## See Also

- [static func find(identifier: String) -> USDLayer?](usdlayer/find(identifier:).md)
  Returns an already-loaded layer with this identifier, or `nil` if none is loaded. Does no I/O.
- [USDLayer.OpenOptions](usdlayer/openoptions.md)
  Options for opening a layer.
- [USDLayer.Permission](usdlayer/permission.md)
  Access permission for a spec.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/open(_:options:))*