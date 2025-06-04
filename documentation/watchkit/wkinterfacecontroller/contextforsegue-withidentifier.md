# contextForSegue(withIdentifier:)

**Framework**: Watchkit  
**Kind**: method

Returns the context object to pass to the specified interface controller when a button is tapped.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor func contextForSegue(withIdentifier segueIdentifier: String) -> Any?
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/navigating-between-scenes))

## Overview

The object to pass to the new interface controller. Use this object to communicate important information to the new interface controller, such as the data to be displayed or any relevant state information. You may return `nil` if you want, but doing so is not recommended.

## Parameters

- `segueIdentifier`: The identifier of the segue that was triggered. When configuring your interface, specify the identifier for a segue in the Attributes inspector.

## Discussion

When you create a segue from a button to a single interface controller, the system calls this method when that segue is triggered. Use this method to provide the new interface controller with any contextual data it needs to display its content. The object you return is passed directly to the new interface controller’s [`awake(withContext:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/awake(withcontext:)) method.

WatchKit calls this method on your WatchKit extension’s main thread. Implementation of this method is optional but is recommended if you use segues in your storyboard file. You do not need to call `super` in your implementation. For segues originating from a table row, use the [`contextForSegue(withIdentifier:in:rowIndex:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextforsegue(withidentifier:in:rowindex:)) method instead.

## See Also

- [func contextsForSegue(withIdentifier: String) -> [Any]?](contextsforsegue(withidentifier:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextsforsegue(withidentifier:)))
- [func contextForSegue(withIdentifier: String, in: WKInterfaceTable, rowIndex: Int) -> Any?](contextforsegue(withidentifier:in:rowindex:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextforsegue(withidentifier:in:rowindex:)))
- [func contextsForSegue(withIdentifier: String, in: WKInterfaceTable, rowIndex: Int) -> [Any]?](contextsforsegue(withidentifier:in:rowindex:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextsforsegue(withidentifier:in:rowindex:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextforsegue(withidentifier:))*