# selectedDOMRange

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The range of the current selection.

**Availability**:
- macOS

## Declaration

```swift
var selectedDOMRange: DOMRange! { get }
```

```objc
@property (nonatomic, strong, readonly) DOMRange * selectedDOMRange;
```

## Discussion

`nil` if nothing is selected.

## See Also

### Related Documentation
- [func editableDOMRange(for: NSPoint) -> DOMRange!](./editabledomrange%28for%29.md)
  Returns the editable DOM object located at a given point.
### Selecting Content in the Document
- [func setSelectedDOMRange(DOMRange!, affinity: NSSelectionAffinity)](./setselecteddomrange%28_,affinity%29.md)
  Selects a range of nodes.
- [var selectionAffinity: NSSelectionAffinity](./selectionaffinity.md)
  The current selection affinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/selecteddomrange)*