# rowController(at:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Returns the row controller for the row at the specified index in the table.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func rowController(at index: Int) -> Any?
```

```objc
- (id) rowControllerAtIndex:(NSInteger) index;
```

## Return Value

The row controller object, or `nil` if there are no row controllers yet or `index` is out of bounds.

## Discussion

Call the [`setRowTypes(_:)`](./setrowtypes%28_%29.md) or [`setNumberOfRows(_:withRowType:)`](./setnumberofrows%28_,withrowtype%29.md) method before using this method to retrieve any row controllers. After you call one of those methods, the table creates row controllers for each row type and stores them internally in an array. Use this method to retrieve those row controllers.

## Parameters

- `index`: The zero-based index of the row. This parameter must be between zero and the total number of rows specified in the [`numberOfRows`](./numberofrows.md) property.

## See Also

### Getting the Row Controllers
- [var numberOfRows: Int](./numberofrows.md)
  The number of row controllers available for you to retrieve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetable/rowcontroller(at:))*