# press(_:forDuration:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Sends a press and hold of a button on a physical remote control, holding for the specified duration.

**Availability**:
- tvOS
- Xcode 16.3+

## Declaration

```swift
func press(_ remoteButton: XCUIRemote.Button, forDuration duration: TimeInterval)
```

```objc
- (void) pressButton:(XCUIRemoteButton) remoteButton forDuration:(NSTimeInterval) duration;
```

## Parameters

- `remoteButton`: The button on the physical remote control that you want to press and hold.
- `duration`: The duration of the button press and hold in seconds.

## See Also

### Pressing remote buttons
- [func press(XCUIRemote.Button)](./press%28_%29.md)
  Sends a momentary press of a button on a physical remote control.
- [enum XCUIRemoteButton](./button.md)
  A button on a physical remote control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiremote/press(_:forduration:))*