# init(layoutManager:range:unifyRects:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Returns an initialized renderer of a text drag preview with the specified layout manager, range, and rectangle detection behavior.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(layoutManager: NSLayoutManager, range: NSRange, unifyRects: Bool)
```

```objc
- (instancetype) initWithLayoutManager:(NSLayoutManager *) layoutManager range:(NSRange) range unifyRects:(BOOL) unifyRects;
```

#### Return Value

A renderer of a text drag preview using the specified layout manager, range, and detection behavior.

## Parameters

- `layoutManager`: The layout manager that renders the preview.
- `range`: The range to render the preview.
- `unifyRects`: A Boolean value that indicates whether the vertical position and height of the detection rectangles adjust to touch each other. If `true`, the [`firstLineRect`](./firstlinerect.md), [`bodyRect`](./bodyrect.md), and [`lastLineRect`](./lastlinerect.md) properties adjust; otherwise, they don’t. The default value is `true`.

## See Also

### Initializing a text drag preview renderer
- [convenience init(layoutManager: NSLayoutManager, range: NSRange)](./init%28layoutmanager,range%29.md)
  Initializes and returns a text drag preview renderer with the specified layout managers and range to render the text drag preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdragpreviewrenderer/init(layoutmanager:range:unifyrects:))*