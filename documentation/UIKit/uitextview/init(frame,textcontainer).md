# init(frame:textContainer:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a new text view with the specified text container.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(frame: CGRect, textContainer: NSTextContainer?)
```

```objc
- (instancetype) initWithFrame:(CGRect) frame textContainer:(NSTextContainer *) textContainer;
```

#### Return Value

An initialized text view.

#### Discussion

This is the designated initializer for `UITextView` objects.

## Parameters

- `frame`: The frame rectangle of the text view.
- `textContainer`: The text container to use for the receiver (can be `nil`).

## See Also

### Initializing the text view
- [convenience init(usingTextLayoutManager: Bool)](./init%28usingtextlayoutmanager%29.md)
  Creates a new text view, with or without a text layout manager depending on the Boolean value you specify.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a text view from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/init(frame:textcontainer:))*