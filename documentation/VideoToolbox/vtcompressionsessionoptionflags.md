# VTCompressionSessionOptionFlags

**Framework**: Video Toolbox  
**Kind**: struct  
**Role**: Structure

Flags to pass to a compression session.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
struct VTCompressionSessionOptionFlags
```

```c
enum VTCompressionSessionOptionFlags : uint32_t;
```

## Topics

### Option Flags
- [static var beginFinalPass: VTCompressionSessionOptionFlags](./vtcompressionsessionoptionflags/beginfinalpass.md)
  A flag that indicates the last pass in a multi-pass compression session.
### Initializers
- [init(rawValue: UInt32)](./vtcompressionsessionoptionflags/init%28rawvalue%29.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessionoptionflags)*