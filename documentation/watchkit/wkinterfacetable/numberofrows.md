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

#### Discussion

The value of this property is `0` until you call the [`setRowTypes(_:)`](wkinterfacetable/setrowtypes(_:).md) or [`setNumberOfRows(_:withRowType:)`](wkinterfacetable/setnumberofrows(_:withrowtype:).md) method. After calling one of those methods, this property contains the number of row controllers that were created.

## See Also

- [func rowController(at: Int) -> Any?](wkinterfacetable/rowcontroller(at:).md)
  Returns the row controller for the row at the specified index in the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetable/numberofrows)*