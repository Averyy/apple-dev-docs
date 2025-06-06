# contextsForSegue(withIdentifier:in:rowIndex:)

**Framework**: Watchkit  
**Kind**: method

Returns the context objects to pass to a page-based set of interface controllers when a row in a table is tapped.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func contextsForSegue(withIdentifier segueIdentifier: String, in table: WKInterfaceTable, rowIndex: Int) -> [Any]?
```

#### Return Value

An array of objects to pass to the new interface controllers. The number of objects in the array must match the number of interface controllers that are present in the page-based interface that is the target of the segue. Use this object to communicate important information to the new interface controller, such as the data to display or any relevant state information. You may return `nil` if you want, but doing so is not recommended.

#### Discussion

When you create a modal segue from a table row to a set of interface controllers in a page-based arrangement, the system calls this method when that segue is triggered. Use this method to provide the new interface controllers with any contextual data they need to display their content. The objects in the array are passed directly to the [`awake(withContext:)`](wkinterfacecontroller/awake(withcontext:).md) method of the corresponding interface controllers.

This method is called on your WatchKit extension’s main thread. Implementation of this method is optional but is recommended if you use segues in your storyboard file. You do not need to call `super` in your implementation. For segues originating from a button, use the [`contextsForSegue(withIdentifier:)`](wkinterfacecontroller/contextsforsegue(withidentifier:).md) method instead.

## Parameters

- `segueIdentifier`: The identifier of the segue that was triggered. When configuring your interface, specify the identifier for a segue in the Attributes inspector.
- `table`: The table object containing the row that was tapped.
- `rowIndex`: The zero-based index of the row that was tapped by the user.

## See Also

- [func contextForSegue(withIdentifier: String) -> Any?](wkinterfacecontroller/contextforsegue(withidentifier:).md)
  Returns the context object to pass to the specified interface controller when a button is tapped.
- [func contextsForSegue(withIdentifier: String) -> [Any]?](wkinterfacecontroller/contextsforsegue(withidentifier:).md)
  Returns the context objects to pass to a page-based set of interface controllers when a button is tapped.
- [func contextForSegue(withIdentifier: String, in: WKInterfaceTable, rowIndex: Int) -> Any?](wkinterfacecontroller/contextforsegue(withidentifier:in:rowindex:).md)
  Returns the context object to pass to the specified interface controller when a row in a table is tapped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextsforsegue(withidentifier:in:rowindex:))*