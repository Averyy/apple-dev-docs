# moveDragCaret(to:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Moves the drag caret that indicates the destination of a drag operation to a given point.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
func moveDragCaret(to point: NSPoint)
```

```objc
- (void) moveDragCaretToPoint:(NSPoint) point;
```

## Parameters

- `point`: The point to move the drag caret to.

## See Also

### Dragging
- [func element(at: NSPoint) -> [AnyHashable : Any]!](./element%28at%29.md)
  Returns a dictionary description of the element at a given point in the receiver’s coordinates.
- [func removeDragCaret()](./removedragcaret%28%29.md)
  Removes the drag caret that indicates the destination of a drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/movedragcaret(to:))*