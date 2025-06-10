# VTEncodeInfoFlags

**Framework**: Video Toolbox  
**Kind**: struct

Flags that indicate encoder state.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
struct VTEncodeInfoFlags
```

## Topics

### Info Flags
- [static var asynchronous: VTEncodeInfoFlags](vtencodeinfoflags/asynchronous.md)
  A flag that indicates that an encode operation ran asynchronously.
- [static var frameDropped: VTEncodeInfoFlags](vtencodeinfoflags/framedropped.md)
  A flag that indicates that a frame dropped during encoding.
### Initializers
- [init(rawValue: UInt32)](vtencodeinfoflags/init(rawvalue:).md)
  Creates a flags structure with a raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class VTCompressionSession](vtcompressionsession.md)
  A reference to a VideoToolbox compression session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtencodeinfoflags)*