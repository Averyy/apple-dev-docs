# tokenBackgroundColor

**Framework**: UIKit  
**Kind**: property

The background color for all tokens in the search text field.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var tokenBackgroundColor: UIColor! { get set }
```

#### Discussion

If you set this property to `nil`, the search field reverts to the default token background color.

## See Also

- [func tokens(in: UITextRange) -> [UISearchToken]](uisearchtextfield/tokens(in:).md)
  Returns the search field’s tokens that are within a given range.
- [func positionOfToken(at: Int) -> UITextPosition](uisearchtextfield/positionoftoken(at:).md)
  Converts a token index into a text position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfield/tokenbackgroundcolor)*