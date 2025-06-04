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

- [var curvesAtBottom: Bool](curvesatbottom.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetable/curvesatbottom))
- [var curvesAtTop: Bool](curvesattop.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetable/curvesattop))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetable/scrolltorow(at:))*