# scrollToRow(at:)

**Framework**: Watchkit  
**Kind**: method

Scrolls the row at the specified index into view.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func scrollToRow(at index: Int)
```

## Parameters

- `index`: The index of the row to be displayed. Specifying an index less than   scrolls to the top of the list. Specifying an index greater than the total number of row controllers scrolls to the bottom of the list.

## See Also

- [var curvesAtBottom: Bool](wkinterfacetable/curvesatbottom.md)
  A Boolean value that determines whether the rows shrink to match the curved corners at the bottom of the screen.
- [var curvesAtTop: Bool](wkinterfacetable/curvesattop.md)
  A Boolean value that determines whether the rows shrink to match the curved corners at the top of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetable/scrolltorow(at:))*