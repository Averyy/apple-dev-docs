# setDefaultResult()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the text paste item’s value to the default value based on the item provider’s data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setDefaultResult()
```

```objc
- (void) setDefaultResult;
```

## Discussion

You call this method, as a fallback, for any items you don’t handle. Setting the default result when the item provider’s data isn’t supported is the same as calling the [`setNoResult()`](./setnoresult%28%29.md) method.

## See Also

### Setting a text paste item’s result value
- [func setResult(string: String)](./setresult%28string%29.md)
  Sets a text paste item’s textual value to a specified plaintext string from the item provider.
- [func setResult(attributedString: NSAttributedString)](./setresult%28attributedstring%29.md)
  Sets a text paste item’s textual value to a specified attributed string from the item provider.
- [func setResult(attachment: NSTextAttachment)](./setresult%28attachment%29.md)
  Sets a text paste item’s attachment value to a specified value.
- [func setNoResult()](./setnoresult%28%29.md)
  Sets the text paste item’s textual value to not include data from the item provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextpasteitem/setdefaultresult())*