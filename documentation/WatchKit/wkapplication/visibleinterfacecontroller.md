# visibleInterfaceController

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

Returns the last visible interface controller.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
var visibleInterfaceController: WKInterfaceController? { get }
```

```objc
@property (nonatomic, readonly, nullable) WKInterfaceController * visibleInterfaceController;
```

## Discussion

Use this property to determine which interface controller the app is currently displaying. For example, in the app delegate’s [`handle(_:)`](../wkapplicationdelegate/handle%28_%29-4vdjo.md) method for a snapshot request, use this property to determine the user interface’s current contents, and make any changes before the system takes the snapshot.

Or, when a Handoff activity launches the app, use the [`handleActiveWorkoutRecovery()`](../wkapplicationdelegate/handleactiveworkoutrecovery%28%29.md) method’s `userInfo` dictionary to determine what to display. Then use the [`visibleInterfaceController`](./visibleinterfacecontroller.md) property to determine whether to push or pop to a different interface controller.

This property contains the following values based on the app’s current state:

- **Just launched**: The app’s [`rootInterfaceController`](./rootinterfacecontroller.md).
- **Running in the foreground**: The currently presented interface controller.
- **Running in the background**: The last interface controller presented by the app.

## See Also

### Getting the interface controller
- [var rootInterfaceController: WKInterfaceController?](./rootinterfacecontroller.md)
  The app’s root interface controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/visibleinterfacecontroller)*