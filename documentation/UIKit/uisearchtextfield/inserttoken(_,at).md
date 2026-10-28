# insertToken(_:at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds a search token at a specific index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func insertToken(_ token: UISearchToken, at tokenIndex: Int)
```

```objc
- (void) insertToken:(UISearchToken *) token atIndex:(NSInteger) tokenIndex;
```

## Discussion

If you’re converting part of the search field’s text into a token, use [`replaceTextualPortion(of:with:at:)`](./replacetextualportion%28of,with,at%29.md).

## Parameters

- `token`: The search token to be inserted.
- `tokenIndex`: Within the [`tokens`](./tokens.md) array, the index at which to insert the token.

## See Also

### Adding and removing tokens
- [var tokens: [UISearchToken]](./tokens.md)
  The collection of tokens in the search text field.
- [func removeToken(at: Int)](./removetoken%28at%29.md)
  Removes a particular search token from the search text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfield/inserttoken(_:at:))*