# press(_:forDuration:)

**Framework**: XCUIAutomation  
**Kind**: method

Sends a press and hold of a button on a physical remote control, holding for the specified duration.

**Availability**:
- tvOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
func press(_ remoteButton: XCUIRemote.Button, forDuration duration: TimeInterval)
```

## Parameters

- `remoteButton`: The button on the physical remote control that you want to press and hold.
- `duration`: The duration of the button press and hold in seconds.

## See Also

- [func press(XCUIRemote.Button)](xcuiremote/press(_:).md)
  Sends a momentary press of a button on a physical remote control.
- [enum XCUIRemoteButton](xcuiremotebutton.md)
  A button on a physical remote control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiremote/press(_:forduration:))*