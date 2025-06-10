# appearance

**Framework**: XCUIAutomation  
**Kind**: property

The interface style of the device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- Xcode 16.3+

## Declaration

```swift
@MainActor
var appearance: XCUIDevice.Appearance { get set }
```

#### Discussion

Use this property to get or set the interface appearance the system uses for applications running on the device. The example below captures the initial appearance value and sets the device to Dark Mode:

```swift
let previousAppearance = XCUIDevice.shared.appearance 
XCUIDevice.shared.appearance = .dark
```

Set the property once in your test fixture’s setup or intialization code to set an appearance for all the test methods in that fixture.

## See Also

- [var system: XCUISystem](xcuidevice/system.md)
  An object that provides an interface to OS-specific properties and actions.
- [XCUIDevice.Appearance](xcuidevice/appearance-swift.enum.md)
  Constants that indicate an interface style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuidevice/appearance-swift.property)*