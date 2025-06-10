# activate()

**Framework**: XCUIAutomation  
**Kind**: method

Activates the application.

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
func activate()
```

#### Discussion

This call is synchronous. The application is in a state ready to handle events when this method returns.

If the application isn’t running prior to calling [`activate()`](xcuiapplication/activate().md), it launches automatically.

If the application previously launched via [`launch()`](xcuiapplication/launch().md), the system supplies the launch arguments and environment variables from the original call to [`launch()`](xcuiapplication/launch().md) again.

Unlike [`launch()`](xcuiapplication/launch().md), a call to [`activate()`](xcuiapplication/activate().md) doesn’t terminate the existing instance if the application is already running.

The system reports any failure in the activation or launch sequence as a test failure and the test is halted at that point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/activate())*