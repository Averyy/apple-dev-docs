# XCUIRemote

**Framework**: XCUIAutomation  
**Kind**: class

A class that simulates interaction with a physical remote control.

**Availability**:
- tvOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
class XCUIRemote
```

## Topics

### Accessing the simulated remote
- [class var shared: XCUIRemote](xcuiremote/shared.md)
  The simulated physical remote control.
### Pressing remote buttons
- [func press(XCUIRemote.Button)](xcuiremote/press(_:).md)
  Sends a momentary press of a button on a physical remote control.
- [func press(XCUIRemote.Button, forDuration: TimeInterval)](xcuiremote/press(_:forduration:).md)
  Sends a press and hold of a button on a physical remote control, holding for the specified duration.
- [enum XCUIRemoteButton](xcuiremotebutton.md)
  A button on a physical remote control.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiremote)*