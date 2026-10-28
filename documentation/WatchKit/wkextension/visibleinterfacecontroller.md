# visibleInterfaceController

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

Returns the last visible interface controller.

**Availability**:
- watchOS 4.0+ - Deprecated in 9.2

## Declaration

```swift
var visibleInterfaceController: WKInterfaceController? { get }
```

```objc
@property (nonatomic, readonly, nullable) WKInterfaceController * visibleInterfaceController;
```

## Discussion

Use this property to determine which interface controller is currently displayed by the app. For example, in the extension delegate’s [`handle(_:)`](../wkextensiondelegate/handle%28_%29-92ulv.md)  method for a snapshot request,  use this property to determine the user interface’s current contents, and make any changes before the snapshot is taken.

Or, when the app is launched due to a Handoff activity, use the [`handleUserActivity(_:)`](../wkextensiondelegate/handleuseractivity%28_%29.md) method’s `userInfo` dictionary to determine what to display. Then use the [`visibleInterfaceController`](./visibleinterfacecontroller.md) property to determine whether to push or pop to a different interface controller.

This property contains the following values based on the app’s current state:

- **Just launched**: The app’s [`rootInterfaceController`](./rootinterfacecontroller.md).
- **Running in the foreground**: The currently presented interface controller.
- **Running in the background**: The last interface controller presented by the app.

## See Also

### Getting the interface controllers
- [var rootInterfaceController: WKInterfaceController?](./rootinterfacecontroller.md)
  The app’s root interface controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/visibleinterfacecontroller)*