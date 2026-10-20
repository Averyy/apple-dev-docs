# curvesAtBottom

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the rows shrink to match the curved corners at the bottom of the screen.

**Availability**:
- watchOS 5.1+

## Declaration

```swift
var curvesAtBottom: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL curvesAtBottom;
```

#### Discussion

Defaults to [`false`](../../Swift/false.md). If [`true`](../../Swift/true.md), table rows near the bottom of the screen shrink so that the curved corners don’t clip them. This property has no effect on Apple Watch Series 3 or earlier.

## See Also

### Scrolling
- [func scrollToRow(at: Int)](./scrolltorow%28at%29.md)
  Scrolls the row at the specified index into view.
- [var curvesAtTop: Bool](./curvesattop.md)
  A Boolean value that determines whether the rows shrink to match the curved corners at the top of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetable/curvesatbottom)*