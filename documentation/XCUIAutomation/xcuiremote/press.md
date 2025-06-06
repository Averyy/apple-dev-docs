# press(_:)

**Framework**: Xcuiautomation  
**Kind**: method

Sends a momentary press of a button on a physical remote control.

**Availability**:
- tvOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
func press(_ remoteButton: XCUIRemote.Button)
```

## Parameters

- `remoteButton`: The button on the physical remote control that you want to press.

## See Also

- [func press(XCUIRemote.Button, forDuration: TimeInterval)](xcuiremote/press(_:forduration:).md)
  Sends a press and hold of a button on a physical remote control, holding for the specified duration.
- [enum XCUIRemoteButton](xcuiremote/button.md)
  A button on a physical remote control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiremote/press(_:))*