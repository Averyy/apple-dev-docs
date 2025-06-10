# state

**Framework**: XCUIAutomation  
**Kind**: property

The most recent state of the application.

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
@MainActor
var state: XCUIApplication.State { get }
```

#### Discussion

The system monitors the app to update this property as the app’s state changes. Consequently, the system updates the value of this property asynchronously.

The system makes the following guarantees:

- When [`launch()`](xcuiapplication/launch().md) and [`activate()`](xcuiapplication/activate().md) return successfully, the state of the application is [`XCUIApplication.State.runningForeground`](xcuiapplication/state-swift.enum/runningforeground.md). An exception to this is launching or activating a macOS agent application with [`LSUIElement`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/LSUIElement) set in its `Info.plist `file. This kind of application never gains foreground status and its state is [`XCUIApplication.State.runningBackground`](xcuiapplication/state-swift.enum/runningbackground.md) instead.
- When [`terminate()`](xcuiapplication/terminate().md) returns successfully, the state of the application is [`XCUIApplication.State.notRunning`](xcuiapplication/state-swift.enum/notrunning.md).

## See Also

- [XCUIApplication.State](xcuiapplication/state-swift.enum.md)
  The possible states of an application during UI testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/state-swift.property)*