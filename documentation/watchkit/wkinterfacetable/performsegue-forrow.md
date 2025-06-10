# performSegue(forRow:)

**Framework**: WatchKit  
**Kind**: method

Performs the segue for the specified row.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func performSegue(forRow row: Int)
```

#### Discussion

This method lets you programmatically transition to a new interface controller. It triggers the segue defined in your storyboard file for the specified row controller.

While similar to the [`WKInterfaceController`](wkinterfacecontroller.md) class’s [`pushController(withName:context:)`](wkinterfacecontroller/pushcontroller(withname:context:).md) method, this method supports Item Pagination . If Item Pagination is enabled, you must use this method when programmatically navigating through a table’s hierarchy. For more information on Item Pagination, see [`Support Item Pagination`](wkinterfacetable#Support-Item-Pagination.md).

## Parameters

- `row`: The index of the row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetable/performsegue(forrow:))*