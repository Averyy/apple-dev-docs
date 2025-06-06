# XCUIDevice.Button

**Framework**: Xcuiautomation  
**Kind**: enum

A physical button on an iOS device.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
enum Button
```

#### Overview

The [`XCUIDevice.Button.volumeUp`](xcuidevice/button/volumeup.md) and [`XCUIDevice.Button.volumeDown`](xcuidevice/button/volumedown.md) buttons aren’t available in Simulator. Use `targetEnvironment(simulator)` in Swift, or `TARGET_OS_SIMULATOR` in Objective-C, to check that your test isn’t running in Simulator before calling these APIs.

## Topics

### Device buttons
- [XCUIDevice.Button.home](xcuidevice/button/home.md)
  The device’s home button.
- [XCUIDevice.Button.volumeUp](xcuidevice/button/volumeup.md)
  The device’s volume up button.
- [XCUIDevice.Button.volumeDown](xcuidevice/button/volumedown.md)
  The device’s volume down button.
- [XCUIDevice.Button.action](xcuidevice/button/action.md)
  The device’s action button.
- [XCUIDevice.Button.camera](xcuidevice/button/camera.md)
  The device’s camera button.
### Initializers
- [init?(rawValue: Int)](xcuidevice/button/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](xcuidevice/button/equatable-implementations.md)
- [RawRepresentable Implementations](xcuidevice/button/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func press(XCUIDevice.Button)](xcuidevice/press(_:).md)
  Simulates the user pressing a physical button.
- [func hasHardwareButton(XCUIDevice.Button) -> Bool](xcuidevice/hashardwarebutton(_:).md)
  Determines whether the device supports the button type you provide.
- [func rotateDigitalCrown(delta: CGFloat)](xcuidevice/rotatedigitalcrown(delta:).md)
  Simulates the user rotating the Digital Crown on an Apple Watch by the delta amount.
- [func rotateDigitalCrown(delta: CGFloat, velocity: XCUIGestureVelocity)](xcuidevice/rotatedigitalcrown(delta:velocity:).md)
  Simulates the user rotating the Digital Crown on an Apple Watch by the delta amount and speed you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuidevice/button)*