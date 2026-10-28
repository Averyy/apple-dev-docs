# curvesAtTop

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the rows shrink to match the curved corners at the top of the screen.

**Availability**:
- watchOS 5.1+

## Declaration

```swift
var curvesAtTop: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL curvesAtTop;
```

## Discussion

Defaults to [`false`](../../Swift/false.md). If [`true`](../../Swift/true.md), table rows near the top of the screen shrink so that the curved corners don’t clip them. Typically, this property has no effect when the status bar is visible. It also has no effect on Apple Watch Series 3 or earlier.

## See Also

### Scrolling
- [func scrollToRow(at: Int)](./scrolltorow%28at%29.md)
  Scrolls the row at the specified index into view.
- [var curvesAtBottom: Bool](./curvesatbottom.md)
  A Boolean value that determines whether the rows shrink to match the curved corners at the bottom of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetable/curvesattop)*