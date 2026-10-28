# tokens

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The collection of tokens in the search text field.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var tokens: [UISearchToken] { get set }
```

```objc
@property (nonatomic, copy) NSArray<UISearchToken *> * tokens;
```

## Discussion

Use this property to access existing tokens, or to replace all tokens at once. To convert text in the search field into a token, use [`replaceTextualPortion(of:with:at:)`](./replacetextualportion%28of,with,at%29.md).

## See Also

### Adding and removing tokens
- [func insertToken(UISearchToken, at: Int)](./inserttoken%28_,at%29.md)
  Adds a search token at a specific index.
- [func removeToken(at: Int)](./removetoken%28at%29.md)
  Removes a particular search token from the search text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfield/tokens)*