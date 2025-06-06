# item(for:)

**Framework**: Webkit  
**Kind**: method

Returns the web history item that corresponds to the specified web location.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func item(for URL: URL!) -> WebHistoryItem!
```

#### Return Value

The web history item that represents visits to the specified URL, or `nil` if none was found.

## Parameters

- `URL`: The location, as a URL, of the webpage that was visited.

## See Also

- [func orderedItemsLastVisited(onDay: NSCalendarDate!) -> [Any]!](webhistory/ordereditemslastvisited(onday:).md)
  Returns web history items that were last visited on the specified date.
- [var orderedLastVisitedDays: [Any]!](webhistory/orderedlastvisiteddays.md)
  An array of all calendar days represented in the web history.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistory/item(for:))*