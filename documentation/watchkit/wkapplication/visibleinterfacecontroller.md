# visibleInterfaceController

**Framework**: Watchkit  
**Kind**: property

Returns the last visible interface controller.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
var visibleInterfaceController: WKInterfaceController? { get }
```

#### Discussion

Use this property to determine which interface controller the app is currently displaying. For example, in the app delegate’s [`handle(_:)`](wkapplicationdelegate/handle(_:)-4vdjo.md) method for a snapshot request, use this property to determine the user interface’s current contents, and make any changes before the system takes the snapshot.

Or, when a Handoff activity launches the app, use the [`handleActiveWorkoutRecovery()`](wkapplicationdelegate/handleactiveworkoutrecovery().md) method’s `userInfo` dictionary to determine what to display. Then use the [`visibleInterfaceController`](wkapplication/visibleinterfacecontroller.md) property to determine whether to push or pop to a different interface controller.

This property contains the following values based on the app’s current state:

## See Also

- [var rootInterfaceController: WKInterfaceController?](wkapplication/rootinterfacecontroller.md)
  The app’s root interface controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/visibleinterfacecontroller)*