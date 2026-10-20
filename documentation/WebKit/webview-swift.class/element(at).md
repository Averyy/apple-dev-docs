# element(at:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns a dictionary description of the element at a given point in the receiver’s coordinates.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
func element(at point: NSPoint) -> [AnyHashable : Any]!
```

```objc
- (NSDictionary *) elementAtPoint:(NSPoint) point;
```

#### Return Value

A dictionary description of the element at `point` in the receiver’s coordinates.

## Parameters

- `point`: The point to represent as a dictionary.

## See Also

### Dragging
- [func moveDragCaret(to: NSPoint)](./movedragcaret%28to%29.md)
  Moves the drag caret that indicates the destination of a drag operation to a given point.
- [func removeDragCaret()](./removedragcaret%28%29.md)
  Removes the drag caret that indicates the destination of a drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/element(at:))*