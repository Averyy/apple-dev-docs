# textualRange

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The range of the field’s text content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var textualRange: UITextRange { get }
```

```objc
@property (nonatomic, readonly) UITextRange * textualRange;
```

#### Discussion

Both tokens and text are included in the range from [`beginningOfDocument`](../uitextinput/beginningofdocument.md) to [`endOfDocument`](../uitextinput/endofdocument.md). This property provides convenient access to just the text.

## See Also

### Converting text into tokens
- [func replaceTextualPortion(of: UITextRange, with: UISearchToken, at: Int)](./replacetextualportion%28of,with,at%29.md)
  Converts text in a search field into a search token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfield/textualrange)*