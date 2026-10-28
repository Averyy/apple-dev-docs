# item(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the web history item that corresponds to the specified web location.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func item(for URL: URL!) -> WebHistoryItem!
```

```objc
- (WebHistoryItem *) itemForURL:(NSURL *) URL;
```

## Return Value

The web history item that represents visits to the specified URL, or `nil` if none was found.

## Parameters

- `URL`: The location, as a URL, of the webpage that was visited.

## See Also

### Getting Web History Items
- [func orderedItemsLastVisited(onDay: NSCalendarDate!) -> [Any]!](./ordereditemslastvisited%28onday%29.md)
  Returns web history items that were last visited on the specified date.
- [var orderedLastVisitedDays: [Any]!](./orderedlastvisiteddays.md)
  An array of all calendar days represented in the web history.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistory/item(for:))*