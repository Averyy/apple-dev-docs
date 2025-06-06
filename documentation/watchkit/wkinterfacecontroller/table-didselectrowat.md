# table(_:didSelectRowAt:)

**Framework**: Watchkit  
**Kind**: method

Called to let you know that the user selected a row in the table.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func table(_ table: WKInterfaceTable, didSelectRowAt rowIndex: Int)
```

#### Discussion

Use this method to respond to row selections in a table. You might use the selection of a row to display a new interface controller or update the state of your app. If you connected an action method to the table in your storyboard file, WatchKit does not call this method.

This method is called on your WatchKit extension’s main thread. Implementation of the method is optional.

## Parameters

- `table`: The table object whose row was selected.
- `rowIndex`: The zero-based index of the row that was selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/table(_:didselectrowat:))*