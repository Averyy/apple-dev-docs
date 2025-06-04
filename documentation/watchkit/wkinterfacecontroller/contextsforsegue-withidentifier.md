# contextsForSegue(withIdentifier:)

**Framework**: WatchKit  
**Kind**: method

Returns the context objects to pass to a page-based set of interface controllers when a button is tapped.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func contextsForSegue(withIdentifier segueIdentifier: String) -> [Any]?
```

#### Return Value

An array of objects to pass to the new interface controllers. The number of objects in the array must match the number of interface controllers that are present in the page-based interface that is the target of the segue. Use this object to communicate important information to the new interface controller, such as the data to display or any relevant state information. You may return `nil` if you want, but doing so is not recommended.

#### Discussion

When you create a modal segue from a button to a set of interface controllers in a page-based arrangement, the system calls this method when that segue is triggered. Use this method to provide the new interface controllers with any contextual data they need to display their content. The objects in the array are passed directly to the [`awake(withContext:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/awake(withcontext:)) method of the corresponding interface controllers.

WatchKit calls this method on your WatchKit extension’s main thread. Implementation of this method is optional but is recommended if you use segues in your storyboard file. You do not need to call `super` in your implementation. For segues originating from a table row, use the [`contextsForSegue(withIdentifier:in:rowIndex:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextsforsegue(withidentifier:in:rowindex:)) method instead.

## Parameters

- `segueIdentifier`: The identifier of the segue that was triggered. Specify the identifier for a segue in the Attributes inspector when configuring your interface.

## See Also

- [func contextForSegue(withIdentifier: String) -> Any?](contextforsegue(withidentifier:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextforsegue(withidentifier:)))
  Returns the context object to pass to the specified interface controller when a button is tapped.
- [func contextForSegue(withIdentifier: String, in: WKInterfaceTable, rowIndex: Int) -> Any?](contextforsegue(withidentifier:in:rowindex:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextforsegue(withidentifier:in:rowindex:)))
  Returns the context object to pass to the specified interface controller when a row in a table is tapped.
- [func contextsForSegue(withIdentifier: String, in: WKInterfaceTable, rowIndex: Int) -> [Any]?](contextsforsegue(withidentifier:in:rowindex:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextsforsegue(withidentifier:in:rowindex:)))
  Returns the context objects to pass to a page-based set of interface controllers when a row in a table is tapped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextsforsegue(withidentifier:))*