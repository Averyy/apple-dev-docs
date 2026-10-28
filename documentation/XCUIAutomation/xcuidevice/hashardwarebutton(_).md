# hasHardwareButton(_:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

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
func hasHardwareButton(_ button: XCUIDevice.Button) -> Bool
```

```objc
- (BOOL) hasHardwareButton:(XCUIDeviceButton) button;
```

## Return Value

`True` if the device has this type of button, otherwise `False`.

## Discussion

Use this method to check if the device supports the particular button type you provide.

## Parameters

- `button`: The type of physical button on an iOS device to check for.

## See Also

### Interacting with buttons and the Digital Crown
- [func press(XCUIDevice.Button)](./press%28_%29.md)
  Simulates the user pressing a physical button.
- [XCUIDevice.Button](./button.md)
  A physical button on an iOS device.
- [func rotateDigitalCrown(delta: CGFloat)](./rotatedigitalcrown%28delta%29.md)
  Simulates the user rotating the Digital Crown on an Apple Watch by the delta amount.
- [func rotateDigitalCrown(delta: CGFloat, velocity: XCUIGestureVelocity)](./rotatedigitalcrown%28delta,velocity%29.md)
  Simulates the user rotating the Digital Crown on an Apple Watch by the delta amount and speed you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuidevice/hashardwarebutton(_:))*