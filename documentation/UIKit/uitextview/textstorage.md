# textStorage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The text storage object holding the text that displays in the text view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var textStorage: NSTextStorage { get }
```

```objc
@property (nonatomic, strong, readonly) NSTextStorage * textStorage;
```

#### Discussion

This property is a convenience accessor that provides access through the text container.

## See Also

### Accessing TextKit Objects
- [var textLayoutManager: NSTextLayoutManager?](./textlayoutmanager.md)
  The text layout manager that lays out text for the text view’s text container.
- [var layoutManager: NSLayoutManager](./layoutmanager.md)
  The layout manager that lays out text for the text view’s text container.
- [var textContainer: NSTextContainer](./textcontainer.md)
  The text container object that defines the area where text displays in the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/textstorage)*