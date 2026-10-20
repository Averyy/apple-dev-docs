# insertRows(at:withRowType:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Inserts rows into the table at the specified indexes.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func insertRows(at rows: IndexSet, withRowType rowType: String)
```

```objc
- (void) insertRowsAtIndexes:(NSIndexSet *) rows withRowType:(NSString *) rowType;
```

#### Discussion

This method inserts the new row controllers into the existing array of row controllers using the semantics defined by the [`insert(_:at:)`](../../Foundation/nsmutablearray/insert%28_,at%29-73pln.md) method of [`NSMutableArray`](../../Foundation/nsmutablearray.md).

## Parameters

- `rows`: An index set containing the locations for the new rows. Each new row controller object is inserted into the array of row controllers in turn and at the specified index after earlier insertions have been made.
- `rowType`: The type of the row controllers to insert. This string corresponds to the value in the Identifier attribute of a row controller definition in your storyboard file.

## See Also

### Inserting and Removing Rows
- [func removeRows(at: IndexSet)](./removerows%28at%29.md)
  Removes the specified rows from the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetable/insertrows(at:withrowtype:))*