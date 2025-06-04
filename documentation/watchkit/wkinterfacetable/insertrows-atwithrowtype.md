# insertRows(at:withRowType:)

**Framework**: WatchKit  
**Kind**: method

Inserts rows into the table at the specified indexes.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func insertRows(at rows: IndexSet, withRowType rowType: String)
```

#### Discussion

This method inserts the new row controllers into the existing array of row controllers using the semantics defined by the [`insert(_:at:)`](https://developer.apple.com/documentation/foundation/nsmutablearray/1416482-insert) method of [`NSMutableArray`](https://developer.apple.com/documentation/Foundation/NSMutableArray).

## Parameters

- `rows`: An index set containing the locations for the new rows. Each new row controller object is inserted into the array of row controllers in turn and at the specified index after earlier insertions have been made.
- `rowType`: The type of the row controllers to insert. This string corresponds to the value in the Identifier attribute of a row controller definition in your storyboard file.

## See Also

- [func removeRows(at: IndexSet)](removerows(at:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetable/removerows(at:)))
  Removes the specified rows from the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetable/insertrows(at:withrowtype:))*