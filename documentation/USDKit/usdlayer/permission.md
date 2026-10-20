# USDLayer.Permission

**Framework**: USDKit  
**Kind**: enum  
**Role**: Enumeration

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
- [USDLayer.Permission.private](./permission/private.md)
  Accessible only within the defining layer.
- [USDLayer.Permission.public](./permission/public.md)
  Accessible from any layer.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [USDValueProtocol](../usdvalueprotocol.md)

## See Also

### Opening and finding layers
- [static func find(identifier: String) -> USDLayer?](./find%28identifier%29.md)
  Returns an already-loaded layer with this identifier, or `nil` if none is loaded. Does no I/O.
- [static func open(String, options: USDLayer.OpenOptions) throws -> USDLayer](./open%28_,options%29.md)
  Returns an already-loaded layer at the identifier, or opens it from the resolved asset path.
- [USDLayer.OpenOptions](./openoptions.md)
  Options for opening a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/permission)*