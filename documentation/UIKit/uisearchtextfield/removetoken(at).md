# removeToken(at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes a particular search token from the search text field.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func removeToken(at tokenIndex: Int)
```

```objc
- (void) removeTokenAtIndex:(NSInteger) tokenIndex;
```

## Parameters

- `tokenIndex`: Within the [`tokens`](./tokens.md) array, the index of the token you want to remove.

## See Also

### Adding and removing tokens
- [var tokens: [UISearchToken]](./tokens.md)
  The collection of tokens in the search text field.
- [func insertToken(UISearchToken, at: Int)](./inserttoken%28_,at%29.md)
  Adds a search token at a specific index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfield/removetoken(at:))*