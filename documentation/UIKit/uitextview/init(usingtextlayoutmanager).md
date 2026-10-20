# init(usingTextLayoutManager:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a new text view, with or without a text layout manager depending on the Boolean value you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(usingTextLayoutManager: Bool)
```

```objc
+ (instancetype) textViewUsingTextLayoutManager:(BOOL) usingTextLayoutManager;
```

## Parameters

- `usingTextLayoutManager`: A Boolean value that indicates whether the framework should create the text view with an [`NSTextLayoutManager`](../nstextlayoutmanager.md).

## See Also

### Initializing the text view
- [init(frame: CGRect, textContainer: NSTextContainer?)](./init%28frame,textcontainer%29.md)
  Creates a new text view with the specified text container.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a text view from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/init(usingtextlayoutmanager:))*