# UAZoomChangeFocus(_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Tells the Universal Access zoom feature where it should focus.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func UAZoomChangeFocus(_ inRect: UnsafePointer<CGRect>!, _ inHighlightRect: UnsafePointer<CGRect>!, _ inType: UAZoomChangeFocusType) -> OSStatus
```

```c
OSStatus UAZoomChangeFocus(const CGRect *inRect, const CGRect *inHighlightRect, UAZoomChangeFocusType inType);
```

## Return Value

Returns `noErr` if there were no problems, if Universal Access Zoom is zoomed all the way out, or if the feature is off; returns `paramErr` if `inRect` is `NULL` or if `inType` is out of range.

## Discussion

This function tells Universal Access the frame of the element in focus and the part of the element that should be in focus.

## Parameters

- `inRect`: The frame of the element in focus, in global 72-dot-per-inch (dpi) coordinates.
- `inHighlightRect`: The frame of the highlighted part of the element in focus, in global 72 dpi coordinates. If the whole element is in focus, and not just a smaller part of it, pass the `inRect` parameter and pass `NULL` for `inHighlightRect`.
- `inType`: A value of type [`UAZoomChangeFocusType`](./uazoomchangefocustype.md).

## See Also

### Miscellaneous
- [func UAZoomEnabled() -> Bool](./api-1462288-uazoomenabled.md)
  Determines if the Universal Access zoom feature is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1458830-uazoomchangefocus)*