# numberOfRows

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The number of row controllers available for you to retrieve.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var numberOfRows: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger numberOfRows;
```

#### Discussion

The value of this property is `0` until you call the [`setRowTypes(_:)`](./setrowtypes%28_%29.md) or [`setNumberOfRows(_:withRowType:)`](./setnumberofrows%28_,withrowtype%29.md) method. After calling one of those methods, this property contains the number of row controllers that were created.

## See Also

### Getting the Row Controllers
- [func rowController(at: Int) -> Any?](./rowcontroller%28at%29.md)
  Returns the row controller for the row at the specified index in the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetable/numberofrows)*