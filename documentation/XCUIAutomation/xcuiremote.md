# XCUIRemote

**Framework**: XCUIAutomation  
**Kind**: class  
**Role**: Class

A class that simulates interaction with a physical remote control.

**Availability**:
- tvOS
- Xcode 16.3+

## Declaration

```swift
@MainActor
class XCUIRemote
```

```objc
@interface XCUIRemote : NSObject
```

## Topics

### Accessing the simulated remote
- [class var shared: XCUIRemote](./xcuiremote/shared.md)
  The simulated physical remote control.
### Pressing remote buttons
- [func press(XCUIRemote.Button)](./xcuiremote/press%28_%29.md)
  Sends a momentary press of a button on a physical remote control.
- [func press(XCUIRemote.Button, forDuration: TimeInterval)](./xcuiremote/press%28_,forduration%29.md)
  Sends a press and hold of a button on a physical remote control, holding for the specified duration.
- [enum XCUIRemoteButton](./xcuiremote/button.md)
  A button on a physical remote control.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiremote)*