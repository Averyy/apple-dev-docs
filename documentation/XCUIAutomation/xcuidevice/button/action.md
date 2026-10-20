# XCUIDevice.Button.action

**Framework**: XCUIAutomation  
**Kind**: case  
**Role**: Case

The device’s action button.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- watchOS
- Xcode 16.3+

## Declaration

```swift
case action
```

```c
XCUIDeviceButtonAction
```

#### Discussion

The button you use for specific actions in workout apps, available in watchOS 9 and later on Apple Watch Ultra. You can use [`hasHardwareButton(_:)`](../hashardwarebutton%28_%29.md) to check for its availability from your test.

## See Also

### Device buttons
- [XCUIDevice.Button.home](./home.md)
  The device’s home button.
- [XCUIDevice.Button.volumeUp](./volumeup.md)
  The device’s volume up button.
- [XCUIDevice.Button.volumeDown](./volumedown.md)
  The device’s volume down button.
- [XCUIDevice.Button.camera](./camera.md)
  The device’s camera button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuidevice/button/action)*