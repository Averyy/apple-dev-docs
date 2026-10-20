# orderedLastVisitedDays

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

An array of all calendar days represented in the web history.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var orderedLastVisitedDays: [Any]! { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray * orderedLastVisitedDays;
```

## See Also

### Getting Web History Items
- [func orderedItemsLastVisited(onDay: NSCalendarDate!) -> [Any]!](./ordereditemslastvisited%28onday%29.md)
  Returns web history items that were last visited on the specified date.
- [func item(for: URL!) -> WebHistoryItem!](./item%28for%29.md)
  Returns the web history item that corresponds to the specified web location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistory/orderedlastvisiteddays)*