# MPSKeyedUnarchiver

**Framework**: Metal Performance Shaders  
**Kind**: cl

A keyed archiver that supports Metal Performance Shaders kernel decoding.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSKeyedUnarchiver : NSKeyedUnarchiver
```

## Topics

### Initializers
- [init?(device: any MTLDevice)](mpskeyedunarchiver/2951874-init.md)
- [init(forReadingFrom: Data, device: any MTLDevice, error: NSErrorPointer)](mpskeyedunarchiver/2966644-init.md)
- [init(forReadingWith: Data, device: any MTLDevice)](mpskeyedunarchiver/2951877-init.md)
### Instance Methods
- [func mpsMTLDevice() -> any MTLDevice](mpskeyedunarchiver/2951880-mpsmtldevice.md)
### Type Methods
- [class func unarchiveObject(with: Data, device: any MTLDevice) -> Any?](mpskeyedunarchiver/2951881-unarchiveobject.md)
- [class func unarchiveObject(withFile: String, device: any MTLDevice) -> Any?](mpskeyedunarchiver/2951875-unarchiveobject.md)
- [class func unarchiveTopLevelObject(with: Data, device: any MTLDevice) -> Any](mpskeyedunarchiver/2951876-unarchivetoplevelobject.md)
- [class func unarchivedObject(of: AnyClass, from: Data, device: any MTLDevice) -> Any](mpskeyedunarchiver/2976453-unarchivedobject.md)
- [class func unarchivedObject(ofClasses: Set<AnyHashable>, from: Data, device: any MTLDevice) -> Any](mpskeyedunarchiver/2976454-unarchivedobject.md)

## Relationships

### Inherits From
- [NSKeyedUnarchiver](../foundation/nskeyedunarchiver.md)
### Conforms To
- [MPSDeviceProvider](mpsdeviceprovider.md)

## See Also

- [class NSKeyedArchiver](../foundation/nskeyedarchiver.md)
  An encoder that stores an object’s data to an archive referenced by keys.
- [protocol MPSDeviceProvider](mpsdeviceprovider.md)
  An interface that enables the setting of a Metal device for unarchived objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpskeyedunarchiver)*