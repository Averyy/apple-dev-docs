# XCUIApplication.State

**Framework**: Xcuiautomation  
**Kind**: enum

The possible states of an application during UI testing.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
enum State
```

## Topics

### Enumeration cases
- [XCUIApplication.State.unknown](xcuiapplication/state-swift.enum/unknown.md)
  The application’s current state is unknown.
- [XCUIApplication.State.notRunning](xcuiapplication/state-swift.enum/notrunning.md)
  The application isn’t running.
- [XCUIApplication.State.runningBackgroundSuspended](xcuiapplication/state-swift.enum/runningbackgroundsuspended.md)
  The application is running in the background, but is suspended.
- [XCUIApplication.State.runningBackground](xcuiapplication/state-swift.enum/runningbackground.md)
  The application is running in the background.
- [XCUIApplication.State.runningForeground](xcuiapplication/state-swift.enum/runningforeground.md)
  The application is running in the foreground.
### Initializers
- [init?(rawValue: UInt)](xcuiapplication/state-swift.enum/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](xcuiapplication/state-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](xcuiapplication/state-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var state: XCUIApplication.State](xcuiapplication/state-swift.property.md)
  The most recent state of the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/state-swift.enum)*