# pushController(withName:context:)

**Framework**: WatchKit  
**Kind**: method

Pushes a new interface controller onto the screen.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func pushController(withName name: String, context: Any?)
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md)

#### Discussion

Use this method to perform a navigation-style transition to the specified interface controller. The system initializes the new interface controller with the specified context object and animates the transition asynchronously. During the transition, the currently visible interface controller’s content disappears from the screen and is replaced by the content of the new controller.

Always call this method from your WatchKit extension’s main thread.

> **Note**:  If Item Pagination  is enabled, do not use this method to respond to the selection of a table row. Use [`performSegue(forRow:)`](wkinterfacetable/performsegue(forrow:).md)  instead.

## Parameters

- `name`: The name of the interface controller you want to display. In your storyboard, the name of an interface controller is stored in the object’s Identifier property, which is located in the attributes inspector.
- `context`: An object to pass to the new interface controller. Use the object in this parameter to communicate important information to the new interface controller, such as the data to display or any relevant state information. You may specify   for this parameter if you want, but doing so is not recommended.

## See Also

- [func pop()](wkinterfacecontroller/pop.md)
  Pops the current interface controller from the screen.
- [func popToRootController()](wkinterfacecontroller/poptorootcontroller.md)
  Pops all interface controllers except the app’s initial interface controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pushcontroller(withname:context:))*