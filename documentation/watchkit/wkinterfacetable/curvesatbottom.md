# curvesAtBottom

**Framework**: Watchkit  
**Kind**: property

A Boolean value that determines whether the rows shrink to match the curved corners at the bottom of the screen.

**Availability**:
- watchOS 5.1+

## Declaration

```swift
var curvesAtBottom: Bool { get set }
```

#### Discussion

Defaults to [`false`](https://developer.apple.com/documentation/swift/false). If [`true`](https://developer.apple.com/documentation/swift/true), table rows near the bottom of the screen shrink so that the curved corners don’t clip them. This property has no effect on Apple Watch Series 3 or earlier.

## See Also

- [func scrollToRow(at: Int)](wkinterfacetable/scrolltorow(at:).md)
  Scrolls the row at the specified index into view.
- [var curvesAtTop: Bool](wkinterfacetable/curvesattop.md)
  A Boolean value that determines whether the rows shrink to match the curved corners at the top of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetable/curvesatbottom)*