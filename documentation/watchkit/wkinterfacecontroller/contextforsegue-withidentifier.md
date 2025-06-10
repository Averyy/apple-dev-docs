# contextForSegue(withIdentifier:)

**Framework**: WatchKit  
**Kind**: method

Returns the context object to pass to the specified interface controller when a button is tapped.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func contextForSegue(withIdentifier segueIdentifier: String) -> Any?
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md)

#### Return Value

The object to pass to the new interface controller. Use this object to communicate important information to the new interface controller, such as the data to be displayed or any relevant state information. You may return `nil` if you want, but doing so is not recommended.

#### Discussion

When you create a segue from a button to a single interface controller, the system calls this method when that segue is triggered. Use this method to provide the new interface controller with any contextual data it needs to display its content. The object you return is passed directly to the new interface controller’s [`awake(withContext:)`](wkinterfacecontroller/awake(withcontext:).md) method.

WatchKit calls this method on your WatchKit extension’s main thread. Implementation of this method is optional but is recommended if you use segues in your storyboard file. You do not need to call `super` in your implementation. For segues originating from a table row, use the [`contextForSegue(withIdentifier:in:rowIndex:)`](wkinterfacecontroller/contextforsegue(withidentifier:in:rowindex:).md) method instead.

## Parameters

- `segueIdentifier`: The identifier of the segue that was triggered. When configuring your interface, specify the identifier for a segue in the Attributes inspector.

## See Also

- [func contextsForSegue(withIdentifier: String) -> [Any]?](wkinterfacecontroller/contextsforsegue(withidentifier:).md)
  Returns the context objects to pass to a page-based set of interface controllers when a button is tapped.
- [func contextForSegue(withIdentifier: String, in: WKInterfaceTable, rowIndex: Int) -> Any?](wkinterfacecontroller/contextforsegue(withidentifier:in:rowindex:).md)
  Returns the context object to pass to the specified interface controller when a row in a table is tapped.
- [func contextsForSegue(withIdentifier: String, in: WKInterfaceTable, rowIndex: Int) -> [Any]?](wkinterfacecontroller/contextsforsegue(withidentifier:in:rowindex:).md)
  Returns the context objects to pass to a page-based set of interface controllers when a row in a table is tapped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextforsegue(withidentifier:))*