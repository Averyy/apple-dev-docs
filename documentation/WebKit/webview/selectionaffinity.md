# selectionAffinity

**Framework**: Webkit  
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

- [var selectedDOMRange: DOMRange!](webview/selecteddomrange.md)
  The range of the current selection.
- [func setSelectedDOMRange(DOMRange!, affinity: NSSelectionAffinity)](webview/setselecteddomrange(_:affinity:).md)
  Selects a range of nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/selectionaffinity)*