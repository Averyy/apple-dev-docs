# removeRows(at:)

**Framework**: Watchkit  
**Kind**: method

Removes the specified rows from the table.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func removeRows(at rows: IndexSet)
```

## Overview

This method removes row controllers from the table using the same semantics defined by the [`removeObjects(at:)`](https://developer.apple.com/documentation/foundation/nsmutablearray/1410154-removeobjects) method of [`NSMutableArray`](https://developer.apple.com/documentation/Foundation/NSMutableArray).

## Parameters

- `rows`: An index set corresponding to the rows you want to remove. If any of the indexes are invalid, this method raises an exception.

## See Also

- [func insertRows(at: IndexSet, withRowType: String)](insertrows(at:withrowtype:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetable/insertrows(at:withrowtype:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetable/removerows(at:))*