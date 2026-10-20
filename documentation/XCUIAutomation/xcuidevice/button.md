# XCUIDevice.Button

**Framework**: XCUIAutomation  
**Kind**: enum  
**Role**: Enumeration

A physical button on an iOS device.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
enum Button
```

```c
enum XCUIDeviceButton : NSInteger;
```

## Topics

### Device buttons
- [XCUIDevice.Button.home](./button/home.md)
  The device’s home button.
- [XCUIDevice.Button.volumeUp](./button/volumeup.md)
  The device’s volume up button.
- [XCUIDevice.Button.volumeDown](./button/volumedown.md)
  The device’s volume down button.
- [XCUIDevice.Button.action](./button/action.md)
  The device’s action button.
- [XCUIDevice.Button.camera](./button/camera.md)
  The device’s camera button.
### Initializers
- [init?(rawValue: Int)](./button/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Interacting with buttons and the Digital Crown
- [func press(XCUIDevice.Button)](./press%28_%29.md)
  Simulates the user pressing a physical button.
- [func hasHardwareButton(XCUIDevice.Button) -> Bool](./hashardwarebutton%28_%29.md)
  Determines whether the device supports the button type you provide.
- [func rotateDigitalCrown(delta: CGFloat)](./rotatedigitalcrown%28delta%29.md)
  Simulates the user rotating the Digital Crown on an Apple Watch by the delta amount.
- [func rotateDigitalCrown(delta: CGFloat, velocity: XCUIGestureVelocity)](./rotatedigitalcrown%28delta,velocity%29.md)
  Simulates the user rotating the Digital Crown on an Apple Watch by the delta amount and speed you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuidevice/button)*