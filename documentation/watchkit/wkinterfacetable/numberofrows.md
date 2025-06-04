# numberOfRows

**Framework**: Watchkit  
**Kind**: property

The number of row controllers available for you to retrieve.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var numberOfRows: Int { get }
```

## Overview

The value of this property is `0` until you call the [`setRowTypes(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacetable/setrowtypes(_:)) or [`setNumberOfRows(_:withRowType:)`](https://developer.apple.com/documentation/watchkit/wkinterfacetable/setnumberofrows(_:withrowtype:)) method. After calling one of those methods, this property contains the number of row controllers that were created.

## See Also

- [func rowController(at: Int) -> Any?](rowcontroller(at:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetable/rowcontroller(at:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetable/numberofrows)*