# init(layoutManager:range:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a text drag preview renderer with the specified layout managers and range to render the text drag preview.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
convenience init(layoutManager: NSLayoutManager, range: NSRange)
```

```objc
- (instancetype) initWithLayoutManager:(NSLayoutManager *) layoutManager range:(NSRange) range;
```

## Return Value

A renderer of a text drag preview using the specified layout manager and range.

## Parameters

- `layoutManager`: The layout manager that renders the text drag preview.
- `range`: The range to render the text drag preview.

## See Also

### Initializing a text drag preview renderer
- [init(layoutManager: NSLayoutManager, range: NSRange, unifyRects: Bool)](./init%28layoutmanager,range,unifyrects%29.md)
  Returns an initialized renderer of a text drag preview with the specified layout manager, range, and rectangle detection behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdragpreviewrenderer/init(layoutmanager:range:))*