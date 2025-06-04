# curvesAtTop

**Framework**: Watchkit  
**Kind**: property

A Boolean value that determines whether the rows shrink to match the curved corners at the top of the screen.

**Availability**:
- watchOS 5.1+

## Declaration

```swift
var curvesAtTop: Bool { get set }
```

## Overview

Defaults to [`false`](https://developer.apple.com/documentation/swift/false). If [`true`](https://developer.apple.com/documentation/swift/true), table rows near the top of the screen shrink so that the curved corners don’t clip them. Typically, this property has no effect when the status bar is visible. It also has no effect on Apple Watch Series 3 or earlier.

## See Also

- [func scrollToRow(at: Int)](scrolltorow(at:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetable/scrolltorow(at:)))
- [var curvesAtBottom: Bool](curvesatbottom.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetable/curvesatbottom))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetable/curvesattop)*