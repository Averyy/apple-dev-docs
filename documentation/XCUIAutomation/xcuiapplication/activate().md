# activate()

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Activates the application.

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
func activate()
```

```objc
- (void) activate;
```

## Discussion

This call is synchronous. The application is in a state ready to handle events when this method returns.

If the application isn’t running prior to calling [`activate()`](./activate%28%29.md), it launches automatically.

If the application previously launched via [`launch()`](./launch%28%29.md), the system supplies the launch arguments and environment variables from the original call to [`launch()`](./launch%28%29.md) again.

Unlike [`launch()`](./launch%28%29.md), a call to [`activate()`](./activate%28%29.md) doesn’t terminate the existing instance if the application is already running.

The system reports any failure in the activation or launch sequence as a test failure and the test is halted at that point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/activate())*