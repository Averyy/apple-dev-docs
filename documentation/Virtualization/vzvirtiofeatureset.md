# VZVirtioFeatureSet

**Framework**: Virtualization  
**Kind**: class

Values that represent a set of Virtio feature bits.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class VZVirtioFeatureSet
```

#### Overview

A `VZVirtioFeatureSet` encapsulates the 64-bit Virtio feature set as two 32-bit subsets. The Virtio specification currently supports up to 64 feature bits, where subset0 represents bits 0 through 31 and subset1 represents bits 32 through 63.

Don’t instantiate `VZVirtioFeatureSet` directly. It’s provided through the `VZCustomVirtioDeviceConfiguration.mandatoryFeatures` and `VZCustomVirtioDeviceConfiguration.optionalFeatures` properties.

## Topics

### Instance Properties
- [var subset0: UInt32](vzvirtiofeatureset/subset0.md)
  An unsigned 32-bit integer that represents Virtio feature bits 0 through 31.
- [var subset1: UInt32](vzvirtiofeatureset/subset1.md)
  An unsigned 32-bit integer that represents Virtio feature bits 32 through 63.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZNegotiatedVirtioFeatureSet](vznegotiatedvirtiofeatureset.md)
  Values that represent a set of negotiated Virtio feature bits.
- [class VZNegotiatedVirtioFeatureSet](vznegotiatedvirtiofeatureset.md)
  Values that represent a set of negotiated Virtio feature bits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiofeatureset)*