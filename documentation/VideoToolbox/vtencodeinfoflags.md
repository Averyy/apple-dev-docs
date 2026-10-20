# VTEncodeInfoFlags

**Framework**: Video Toolbox  
**Kind**: struct  
**Role**: Structure

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

```c
enum VTEncodeInfoFlags : UInt32;
```

## Topics

### Info Flags
- [static var asynchronous: VTEncodeInfoFlags](./vtencodeinfoflags/asynchronous.md)
  A flag that indicates that an encode operation ran asynchronously.
- [static var frameDropped: VTEncodeInfoFlags](./vtencodeinfoflags/framedropped.md)
  A flag that indicates that a frame dropped during encoding.
### Initializers
- [init(rawValue: UInt32)](./vtencodeinfoflags/init%28rawvalue%29.md)
  Creates a flags structure with a raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Data Types
- [class VTCompressionSession](./vtcompressionsession.md)
  A reference to a VideoToolbox compression session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtencodeinfoflags)*