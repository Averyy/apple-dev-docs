# setSelectedDOMRange(_:affinity:)

**Framework**: WebKit  
**Kind**: method

Selects a range of nodes.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setSelectedDOMRange(_ range: DOMRange!, affinity selectionAffinity: NSSelectionAffinity)
```

## Parameters

- `range`: The range of nodes to select. If   is  , the current selection is cleared. This method raises a   if the range has been detached or refers to nodes not displayed by the receiver.
- `selectionAffinity`: See the   property for information on selection affinity.

## See Also

- [func editableDOMRange(for: NSPoint) -> DOMRange!](webview-swift.class/editabledomrange(for:).md)
  Returns the editable DOM object located at a given point.
- [var selectedDOMRange: DOMRange!](webview-swift.class/selecteddomrange.md)
  The range of the current selection.
- [var selectionAffinity: NSSelectionAffinity](webview-swift.class/selectionaffinity.md)
  The current selection affinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/setselecteddomrange(_:affinity:))*