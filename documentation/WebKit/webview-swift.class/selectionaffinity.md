# selectionAffinity

**Framework**: WebKit  
**Kind**: property

The current selection affinity.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var selectionAffinity: NSSelectionAffinity { get }
```

#### Discussion

For example, if text wraps across line boundaries, the value of this property indicates whether or not the insertion point appears after the last charactrer of the first line or before the first character of the following line.

## See Also

- [var selectedDOMRange: DOMRange!](webview-swift.class/selecteddomrange.md)
  The range of the current selection.
- [func setSelectedDOMRange(DOMRange!, affinity: NSSelectionAffinity)](webview-swift.class/setselecteddomrange(_:affinity:).md)
  Selects a range of nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/selectionaffinity)*