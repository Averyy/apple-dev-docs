# press(_:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Simulates the user pressing a physical button.

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
func press(_ button: XCUIDevice.Button)
```

```objc
- (void) pressButton:(XCUIDeviceButton) button;
```

## Parameters

- `button`: The button to press on the device.

## See Also

### Interacting with buttons and the Digital Crown
- [func hasHardwareButton(XCUIDevice.Button) -> Bool](./hashardwarebutton%28_%29.md)
  Determines whether the device supports the button type you provide.
- [XCUIDevice.Button](./button.md)
  A physical button on an iOS device.
- [func rotateDigitalCrown(delta: CGFloat)](./rotatedigitalcrown%28delta%29.md)
  Simulates the user rotating the Digital Crown on an Apple Watch by the delta amount.
- [func rotateDigitalCrown(delta: CGFloat, velocity: XCUIGestureVelocity)](./rotatedigitalcrown%28delta,velocity%29.md)
  Simulates the user rotating the Digital Crown on an Apple Watch by the delta amount and speed you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuidevice/press(_:))*