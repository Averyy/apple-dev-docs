# init(layoutManager:range:unifyRects:)

**Framework**: UIKit  
**Kind**: init

Returns an initialized renderer of a text drag preview with the specified layout manager, range, and rectangle detection behavior.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(layoutManager: NSLayoutManager, range: NSRange, unifyRects: Bool)
```

#### Return Value

A renderer of a text drag preview using the specified layout manager, range, and detection behavior.

## Parameters

- `layoutManager`: The layout manager that renders the preview.
- `range`: The range to render the preview.
- `unifyRects`: A Boolean value that indicates whether the vertical position and height of the detection rectangles adjust to touch each other. If  , the  ,  , and   properties adjust; otherwise, they don’t. The default value is  .

## See Also

- [convenience init(layoutManager: NSLayoutManager, range: NSRange)](uitextdragpreviewrenderer/init(layoutmanager:range:).md)
  Initializes and returns a text drag preview renderer with the specified layout managers and range to render the text drag preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdragpreviewrenderer/init(layoutmanager:range:unifyrects:))*