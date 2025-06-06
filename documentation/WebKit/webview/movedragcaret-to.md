# moveDragCaret(to:)

**Framework**: Webkit  
**Kind**: method

Moves the drag caret that indicates the destination of a drag operation to a given point.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func moveDragCaret(to point: NSPoint)
```

## Parameters

- `point`: The point to move the drag caret to.

## See Also

- [func element(at: NSPoint) -> [AnyHashable : Any]!](webview/element(at:).md)
  Returns a dictionary description of the element at a given point in the receiver’s coordinates.
- [func removeDragCaret()](webview/removedragcaret.md)
  Removes the drag caret that indicates the destination of a drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/movedragcaret(to:))*