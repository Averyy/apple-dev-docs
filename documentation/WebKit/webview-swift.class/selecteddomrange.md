# selectedDOMRange

**Framework**: WebKit  
**Kind**: property

The range of the current selection.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var selectedDOMRange: DOMRange! { get }
```

#### Discussion

`nil` if nothing is selected.

## See Also

- [func editableDOMRange(for: NSPoint) -> DOMRange!](webview-swift.class/editabledomrange(for:).md)
  Returns the editable DOM object located at a given point.
- [func setSelectedDOMRange(DOMRange!, affinity: NSSelectionAffinity)](webview-swift.class/setselecteddomrange(_:affinity:).md)
  Selects a range of nodes.
- [var selectionAffinity: NSSelectionAffinity](webview-swift.class/selectionaffinity.md)
  The current selection affinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/selecteddomrange)*