# press(_:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Sends a momentary press of a button on a physical remote control.

**Availability**:
- tvOS
- Xcode 16.3+

## Declaration

```swift
func press(_ remoteButton: XCUIRemote.Button)
```

```objc
- (void) pressButton:(XCUIRemoteButton) remoteButton;
```

## Parameters

- `remoteButton`: The button on the physical remote control that you want to press.

## See Also

### Pressing remote buttons
- [func press(XCUIRemote.Button, forDuration: TimeInterval)](./press%28_,forduration%29.md)
  Sends a press and hold of a button on a physical remote control, holding for the specified duration.
- [enum XCUIRemoteButton](./button.md)
  A button on a physical remote control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiremote/press(_:))*