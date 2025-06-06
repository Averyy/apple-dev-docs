# hasHardwareButton(_:)

**Framework**: Xcuiautomation  
**Kind**: method

Determines whether the device supports the button type you provide.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+
- Xcode 16.3+

## Declaration

```swift
@MainActor
func hasHardwareButton(_ button: XCUIDevice.Button) -> Bool
```

#### Return Value

`True` if the device has this type of button, otherwise `False`.

#### Discussion

Use this method to check if the device supports the particular button type you provide.

## Parameters

- `button`: The type of physical button on an iOS device to check for.

## See Also

- [func press(XCUIDevice.Button)](xcuidevice/press(_:).md)
  Simulates the user pressing a physical button.
- [XCUIDevice.Button](xcuidevice/button.md)
  A physical button on an iOS device.
- [func rotateDigitalCrown(delta: CGFloat)](xcuidevice/rotatedigitalcrown(delta:).md)
  Simulates the user rotating the Digital Crown on an Apple Watch by the delta amount.
- [func rotateDigitalCrown(delta: CGFloat, velocity: XCUIGestureVelocity)](xcuidevice/rotatedigitalcrown(delta:velocity:).md)
  Simulates the user rotating the Digital Crown on an Apple Watch by the delta amount and speed you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuidevice/hashardwarebutton(_:))*