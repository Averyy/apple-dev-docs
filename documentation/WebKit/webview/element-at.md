# element(at:)

**Framework**: Webkit  
**Kind**: method

Returns a dictionary description of the element at a given point in the receiver’s coordinates.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func element(at point: NSPoint) -> [AnyHashable : Any]!
```

#### Return Value

A dictionary description of the element at `point` in the receiver’s coordinates.

## Parameters

- `point`: The point to represent as a dictionary.

## See Also

- [func moveDragCaret(to: NSPoint)](webview/movedragcaret(to:).md)
  Moves the drag caret that indicates the destination of a drag operation to a given point.
- [func removeDragCaret()](webview/removedragcaret.md)
  Removes the drag caret that indicates the destination of a drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/element(at:))*