# state

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Instance Property

The most recent state of the application.

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
var state: XCUIApplication.State { get }
```

```objc
@property (readonly) XCUIApplicationState state;
```

#### Discussion

The system monitors the app to update this property as the app’s state changes. Consequently, the system updates the value of this property asynchronously.

The system makes the following guarantees:

- When [`launch()`](./launch%28%29.md) and [`activate()`](./activate%28%29.md) return successfully, the state of the application is [`XCUIApplication.State.runningForeground`](./state-swift.enum/runningforeground.md). An exception to this is launching or activating a macOS agent application with [`LSUIElement`](../../BundleResources/information-property-list/lsuielement.md) set in its `Info.plist `file. This kind of application never gains foreground status and its state is [`XCUIApplication.State.runningBackground`](./state-swift.enum/runningbackground.md) instead.
- When [`terminate()`](./terminate%28%29.md) returns successfully, the state of the application is [`XCUIApplication.State.notRunning`](./state-swift.enum/notrunning.md).

## See Also

### Determining application state
- [XCUIApplication.State](./state-swift.enum.md)
  The possible states of an application during UI testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/state-swift.property)*