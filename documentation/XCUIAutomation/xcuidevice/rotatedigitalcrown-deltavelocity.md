# rotateDigitalCrown(delta:velocity:)

**Framework**: Xcuiautomation  
**Kind**: method

Simulates the user rotating the Digital Crown on an Apple Watch by the delta amount and speed you provide.

**Availability**:
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
func rotateDigitalCrown(delta rotationalDelta: CGFloat, velocity: XCUIGestureVelocity)
```

#### Discussion

Provide a positive value for `rotationalDelta` to indicate scrolling upward or a negative value to indicate scrolling downward, regardless of the orientation of the watch. A `rotationalDelta` value of `1.0` indicates a full rotation of the Digital Crown. Specify a `velocity` in rotations per second; the system ignores the sign of the `velocity` you provide.

## Parameters

- `rotationalDelta`: A float value that indicates the fraction of a full rotation of the Digital Crown.
- `velocity`: A value that represents how fast to rotate the Digital Crown, in rotations per second.

## See Also

- [func press(XCUIDevice.Button)](xcuidevice/press(_:).md)
  Simulates the user pressing a physical button.
- [func hasHardwareButton(XCUIDevice.Button) -> Bool](xcuidevice/hashardwarebutton(_:).md)
  Determines whether the device supports the button type you provide.
- [XCUIDevice.Button](xcuidevice/button.md)
  A physical button on an iOS device.
- [func rotateDigitalCrown(delta: CGFloat)](xcuidevice/rotatedigitalcrown(delta:).md)
  Simulates the user rotating the Digital Crown on an Apple Watch by the delta amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuidevice/rotatedigitalcrown(delta:velocity:))*