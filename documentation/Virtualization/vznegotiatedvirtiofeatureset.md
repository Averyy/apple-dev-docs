# VZNegotiatedVirtioFeatureSet

**Framework**: Virtualization  
**Kind**: class

Values that represent a set of negotiated Virtio feature bits.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class VZNegotiatedVirtioFeatureSet
```

#### Overview

A [`VZNegotiatedVirtioFeatureSet`](vznegotiatedvirtiofeatureset.md) represents the set of Virtio features the device and the driver have negotiated.

[`VZNegotiatedVirtioFeatureSet`](vznegotiatedvirtiofeatureset.md) encapsulates the 64-bit Virtio feature set as two 32-bit subsets. The Virtio specification currently supports up to 64 feature bits, where subset0 represents bits 0 through 31 and subset1 represents bits 32 through 63.

Don’t instantiate [`VZNegotiatedVirtioFeatureSet`](vznegotiatedvirtiofeatureset.md) directly. Instead, first configure the device feature set through the [`mandatoryFeatures`](vzcustomvirtiodeviceconfiguration/mandatoryfeatures.md) and [`optionalFeatures`](vzcustomvirtiodeviceconfiguration/optionalfeatures.md) properties. Virtio negotiation then takes place when the guest boots and, after Virtio negotiation completes, the set of negotiated features is available in the [`negotiatedFeatures`](vzcustomvirtiodevice/negotiatedfeatures.md) property.

## Topics

### Instance Properties
- [var subset0: UInt32](vznegotiatedvirtiofeatureset/subset0.md)
  The values that represent feature bits 0 through 31.
- [var subset1: UInt32](vznegotiatedvirtiofeatureset/subset1.md)
  The value that represent feature bits 32 through 63.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZVirtioFeatureSet](vzvirtiofeatureset.md)
  Values that represent a set of Virtio feature bits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznegotiatedvirtiofeatureset)*