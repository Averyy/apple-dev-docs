# XCUIApplication.State

**Framework**: XCUIAutomation  
**Kind**: enum  
**Role**: Enumeration

The possible states of an application during UI testing.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
enum State
```

```c
enum XCUIApplicationState : NSUInteger;
```

## Topics

### Enumeration cases
- [XCUIApplication.State.unknown](./state-swift.enum/unknown.md)
  The application’s current state is unknown.
- [XCUIApplication.State.notRunning](./state-swift.enum/notrunning.md)
  The application isn’t running.
- [XCUIApplication.State.runningBackgroundSuspended](./state-swift.enum/runningbackgroundsuspended.md)
  The application is running in the background, but is suspended.
- [XCUIApplication.State.runningBackground](./state-swift.enum/runningbackground.md)
  The application is running in the background.
- [XCUIApplication.State.runningForeground](./state-swift.enum/runningforeground.md)
  The application is running in the foreground.
### Initializers
- [init?(rawValue: UInt)](./state-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Determining application state
- [var state: XCUIApplication.State](./state-swift.property.md)
  The most recent state of the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/state-swift.enum)*