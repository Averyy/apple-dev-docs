# start

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The start of a range of text.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var start: UITextPosition { get }
```

```objc
@property (nonatomic, readonly) UITextPosition * start;
```

#### Discussion

Compute and store in this property the UITextPosition object representing the start of a range of text.

## See Also

### Defining Ranges of Text
- [var end: UITextPosition](./end.md)
  The end of the range of text.
- [var isEmpty: Bool](./isempty.md)
  A Boolean value that indicates whether the range of text represented by the receiver is zero-length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextrange/start)*