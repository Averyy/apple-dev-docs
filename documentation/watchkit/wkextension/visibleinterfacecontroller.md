# visibleInterfaceController

**Framework**: WatchKit  
**Kind**: property

Returns the last visible interface controller.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
@MainActor
var visibleInterfaceController: WKInterfaceController? { get }
```

#### Discussion

Use this property to determine which interface controller is currently displayed by the app. For example, in the extension delegate’s [`handle(_:)`](wkextensiondelegate/handle(_:)-92ulv.md)  method for a snapshot request,  use this property to determine the user interface’s current contents, and make any changes before the snapshot is taken.

Or, when the app is launched due to a Handoff activity, use the [`handleUserActivity(_:)`](wkextensiondelegate/handleuseractivity(_:).md) method’s `userInfo` dictionary to determine what to display. Then use the [`visibleInterfaceController`](wkextension/visibleinterfacecontroller.md) property to determine whether to push or pop to a different interface controller.

This property contains the following values based on the app’s current state:

## See Also

- [var rootInterfaceController: WKInterfaceController?](wkextension/rootinterfacecontroller.md)
  The app’s root interface controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/visibleinterfacecontroller)*