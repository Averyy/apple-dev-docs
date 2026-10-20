# rotateDigitalCrown(delta:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Simulates the user rotating the Digital Crown on an Apple Watch by the delta amount.

**Availability**:
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
func rotateDigitalCrown(delta rotationalDelta: CGFloat)
```

```objc
- (void) rotateDigitalCrownByDelta:(CGFloat) rotationalDelta;
```

#### Discussion

Provide a positive value for `rotationalDelta` to indicate scrolling upward or a negative value to indicate scrolling downward, regardless of the orientation of the watch. A `rotationalDelta` value of `1.0` indicates a full rotation of the Digital Crown.

## Parameters

- `rotationalDelta`: A float value that indicates the fraction of a full rotation of the Digital Crown.

## See Also

### Interacting with buttons and the Digital Crown
- [func press(XCUIDevice.Button)](./press%28_%29.md)
  Simulates the user pressing a physical button.
- [func hasHardwareButton(XCUIDevice.Button) -> Bool](./hashardwarebutton%28_%29.md)
  Determines whether the device supports the button type you provide.
- [XCUIDevice.Button](./button.md)
  A physical button on an iOS device.
- [func rotateDigitalCrown(delta: CGFloat, velocity: XCUIGestureVelocity)](./rotatedigitalcrown%28delta,velocity%29.md)
  Simulates the user rotating the Digital Crown on an Apple Watch by the delta amount and speed you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuidevice/rotatedigitalcrown(delta:))*