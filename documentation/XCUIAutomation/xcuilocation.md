# XCUILocation

**Framework**: XCUIAutomation  
**Kind**: class

A proxy that simulates a device’s location in terms of its longitude, latitude, and course information.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
class XCUILocation
```

## Topics

### Creating a location
- [init(location: CLLocation)](xcuilocation/init(location:).md)
  Initializes a proxy that simulates latitude, longitude, and course information based on the location object you provide.
### Determining the location
- [var location: CLLocation](xcuilocation/location.md)
  Returns the object that contains the latitude, longitude, and course information this proxy simulates for the device.
- [var debugDescription: String](xcuilocation/debugdescription.md)
  A textual description of the location suitable for debugging.

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
- [Sendable](../swift/sendable.md)

## See Also

- [var orientation: UIDeviceOrientation](xcuidevice/orientation.md)
  The orientation of the device.
- [var location: XCUILocation?](xcuidevice/location.md)
  The proxy location a test uses to simulate longitude, latitude, and course information for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuilocation)*