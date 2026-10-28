# removeRows(at:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified rows from the table.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func removeRows(at rows: IndexSet)
```

```objc
- (void) removeRowsAtIndexes:(NSIndexSet *) rows;
```

## Discussion

This method removes row controllers from the table using the same semantics defined by the [`removeObjects(at:)`](../../Foundation/nsmutablearray/removeobjects%28at%29.md) method of [`NSMutableArray`](../../Foundation/nsmutablearray.md).

## Parameters

- `rows`: An index set corresponding to the rows you want to remove. If any of the indexes are invalid, this method raises an exception.

## See Also

### Inserting and Removing Rows
- [func insertRows(at: IndexSet, withRowType: String)](./insertrows%28at,withrowtype%29.md)
  Inserts rows into the table at the specified indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetable/removerows(at:))*