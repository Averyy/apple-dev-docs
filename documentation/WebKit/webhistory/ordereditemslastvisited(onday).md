# orderedItemsLastVisited(onDay:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns web history items that were last visited on the specified date.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func orderedItemsLastVisited(onDay calendarDate: NSCalendarDate!) -> [Any]!
```

```objc
- (NSArray *) orderedItemsLastVisitedOnDay:(NSCalendarDate *) calendarDate;
```

#### Return Value

An array of web history items that were last visited on the specified date.

## Parameters

- `calendarDate`: The date on which the web history items were last visited.

## See Also

### Getting Web History Items
- [var orderedLastVisitedDays: [Any]!](./orderedlastvisiteddays.md)
  An array of all calendar days represented in the web history.
- [func item(for: URL!) -> WebHistoryItem!](./item%28for%29.md)
  Returns the web history item that corresponds to the specified web location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistory/ordereditemslastvisited(onday:))*