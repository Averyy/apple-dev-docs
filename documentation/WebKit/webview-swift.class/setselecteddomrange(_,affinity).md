# setSelectedDOMRange(_:affinity:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Selects a range of nodes.

**Availability**:
- macOS

## Declaration

```swift
func setSelectedDOMRange(_ range: DOMRange!, affinity selectionAffinity: NSSelectionAffinity)
```

```objc
- (void) setSelectedDOMRange:(DOMRange *) range affinity:(NSSelectionAffinity) selectionAffinity;
```

## Parameters

- `range`: The range of nodes to select. If `range` is `nil`, the current selection is cleared. This method raises a `DOMRangeExcepton` if the range has been detached or refers to nodes not displayed by the receiver.
- `selectionAffinity`: See the [`selectionAffinity`](./selectionaffinity.md) property for information on selection affinity.

## See Also

### Related Documentation
- [func editableDOMRange(for: NSPoint) -> DOMRange!](./editabledomrange%28for%29.md)
  Returns the editable DOM object located at a given point.
### Selecting Content in the Document
- [var selectedDOMRange: DOMRange!](./selecteddomrange.md)
  The range of the current selection.
- [var selectionAffinity: NSSelectionAffinity](./selectionaffinity.md)
  The current selection affinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/setselecteddomrange(_:affinity:))*