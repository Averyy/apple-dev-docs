# orderedItemsLastVisited(onDay:)

**Framework**: WebKit  
**Kind**: method

Returns web history items that were last visited on the specified date.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func orderedItemsLastVisited(onDay calendarDate: NSCalendarDate!) -> [Any]!
```

#### Return Value

An array of web history items that were last visited on the specified date.

## Parameters

- `calendarDate`: The date on which the web history items were last visited.

## See Also

- [var orderedLastVisitedDays: [Any]!](webhistory/orderedlastvisiteddays.md)
  An array of all calendar days represented in the web history.
- [func item(for: URL!) -> WebHistoryItem!](webhistory/item(for:).md)
  Returns the web history item that corresponds to the specified web location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistory/ordereditemslastvisited(onday:))*