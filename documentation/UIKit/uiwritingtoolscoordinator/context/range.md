# range

**Framework**: UIKit  
**Kind**: property

The unique identifier of the context object.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
var range: NSRange { get }
```

## Mentions

- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)

#### Discussion

The [`UIWritingToolsCoordinator.Context`](uiwritingtoolscoordinator/context.md) object initializes the value of this property at creation time. Use this value to identify the context object within your app.

## See Also

- [var attributedString: NSAttributedString](uiwritingtoolscoordinator/context/attributedstring.md)
  The portion of your view’s text to evaluate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/context/range)*