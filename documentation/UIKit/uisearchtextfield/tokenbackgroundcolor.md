# tokenBackgroundColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The background color for all tokens in the search text field.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var tokenBackgroundColor: UIColor! { get set }
```

```objc
@property (nonatomic, strong, null_resettable) UIColor * tokenBackgroundColor;
```

#### Discussion

If you set this property to `nil`, the search field reverts to the default token background color.

## See Also

### Customizing token behavior
- [func tokens(in: UITextRange) -> [UISearchToken]](./tokens%28in%29.md)
  Returns the search field’s tokens that are within a given range.
- [func positionOfToken(at: Int) -> UITextPosition](./positionoftoken%28at%29.md)
  Converts a token index into a text position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfield/tokenbackgroundcolor)*