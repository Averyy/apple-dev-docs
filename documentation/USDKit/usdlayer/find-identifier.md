# find(identifier:)

**Framework**: USDKit  
**Kind**: method

Returns an already-loaded layer with this identifier, or `nil` if none is loaded. Does no I/O.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func find(identifier: String) -> USDLayer?
```

#### Return Value

The matching layer, or `nil` if none is loaded.

## Parameters

- `identifier`: The layer identifier to look up.

## See Also

- [static func open(String, options: USDLayer.OpenOptions) throws -> USDLayer](usdlayer/open(_:options:).md)
  Returns an already-loaded layer at the identifier, or opens it from the resolved asset path.
- [USDLayer.OpenOptions](usdlayer/openoptions.md)
  Options for opening a layer.
- [USDLayer.Permission](usdlayer/permission.md)
  Access permission for a spec.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/find(identifier:))*