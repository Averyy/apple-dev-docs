# USDLayer.Permission

**Framework**: USDKit  
**Kind**: enum

Access permission for a spec.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum Permission
```

## Topics

### Enumeration Cases
- [USDLayer.Permission.private](usdlayer/permission/private.md)
  Accessible only within the defining layer.
- [USDLayer.Permission.public](usdlayer/permission/public.md)
  Accessible from any layer.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [USDValueProtocol](usdvalueprotocol.md)

## See Also

- [static func find(identifier: String) -> USDLayer?](usdlayer/find(identifier:).md)
  Returns an already-loaded layer with this identifier, or `nil` if none is loaded. Does no I/O.
- [static func open(String, options: USDLayer.OpenOptions) throws -> USDLayer](usdlayer/open(_:options:).md)
  Returns an already-loaded layer at the identifier, or opens it from the resolved asset path.
- [USDLayer.OpenOptions](usdlayer/openoptions.md)
  Options for opening a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/permission)*