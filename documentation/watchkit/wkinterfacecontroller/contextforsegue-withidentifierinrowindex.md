# contextForSegue(withIdentifier:in:rowIndex:)

**Framework**: Watchkit  
**Kind**: method

Returns the context object to pass to the specified interface controller when a row in a table is tapped.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor func contextForSegue(withIdentifier segueIdentifier: String, in table: WKInterfaceTable, rowIndex: Int) -> Any?
```

## Overview

The object to pass to the new interface controller. Use this object to communicate important information to the new interface controller, such as the data to display or any relevant state information. You may specify `nil` if you want, but doing so is not recommended.

## Parameters

- `segueIdentifier`: The identifier of the segue that was triggered. Specify the identifier for a segue in the Attributes inspector when configuring your interface.
- `table`: The table object containing the row that was tapped.
- `rowIndex`: The zero-based index of the row that was tapped by the user.

## Discussion

WatchKit calls this method when a segue attached to a table row is triggered. Use this method to provide the new interface controller with any contextual data it needs to display its content. The object you return is passed directly to the new interface controller’s [`awake(withContext:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/awake(withcontext:)) method.

This method is called on your WatchKit extension’s main thread. Implementation of this method is optional but is recommended if you use segues in your storyboard file. You do not need to call `super` in your implementation. For segues originating from a button, use the [`contextsForSegue(withIdentifier:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextsforsegue(withidentifier:)) method instead.

## See Also

- [func contextForSegue(withIdentifier: String) -> Any?](contextforsegue(withidentifier:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextforsegue(withidentifier:)))
- [func contextsForSegue(withIdentifier: String) -> [Any]?](contextsforsegue(withidentifier:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextsforsegue(withidentifier:)))
- [func contextsForSegue(withIdentifier: String, in: WKInterfaceTable, rowIndex: Int) -> [Any]?](contextsforsegue(withidentifier:in:rowindex:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextsforsegue(withidentifier:in:rowindex:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextforsegue(withidentifier:in:rowindex:))*