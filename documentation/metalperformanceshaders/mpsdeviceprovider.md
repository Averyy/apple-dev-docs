# MPSDeviceProvider

**Framework**: Metal Performance Shaders  
**Kind**: intf

An interface that enables the setting of a Metal device for unarchived objects.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol MPSDeviceProvider
```

## Topics

### Instance Methods
- [func mpsMTLDevice() -> (any MTLDevice)!](mpsdeviceprovider/2875211-mpsmtldevice.md)

## Relationships

### Conforming Types
- [MPSKeyedUnarchiver](mpskeyedunarchiver.md)

## See Also

- [class NSKeyedArchiver](../foundation/nskeyedarchiver.md)
  An encoder that stores an object’s data to an archive referenced by keys.
- [class MPSKeyedUnarchiver](mpskeyedunarchiver.md)
  A keyed archiver that supports Metal Performance Shaders kernel decoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsdeviceprovider)*