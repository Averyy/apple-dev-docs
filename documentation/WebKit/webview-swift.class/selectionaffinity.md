# selectionAffinity

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The current selection affinity.

**Availability**:
- macOS

## Declaration

```swift
var selectionAffinity: NSSelectionAffinity { get }
```

```objc
@property (nonatomic, readonly) NSSelectionAffinity selectionAffinity;
```

## Discussion

For example, if text wraps across line boundaries, the value of this property indicates whether or not the insertion point appears after the last charactrer of the first line or before the first character of the following line.

## See Also

### Selecting Content in the Document
- [var selectedDOMRange: DOMRange!](./selecteddomrange.md)
  The range of the current selection.
- [func setSelectedDOMRange(DOMRange!, affinity: NSSelectionAffinity)](./setselecteddomrange%28_,affinity%29.md)
  Selects a range of nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/selectionaffinity)*