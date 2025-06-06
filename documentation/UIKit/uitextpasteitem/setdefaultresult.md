# setDefaultResult()

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Sets the text paste item’s value to the default value based on the item provider’s data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setDefaultResult()
```

#### Discussion

You call this method, as a fallback, for any items you don’t handle. Setting the default result when the item provider’s data isn’t supported is the same as calling the [`setNoResult()`](uitextpasteitem/setnoresult().md) method.

## See Also

- [func setResult(string: String)](uitextpasteitem/setresult(string:).md)
  Sets a text paste item’s textual value to a specified plaintext string from the item provider.
- [func setResult(attributedString: NSAttributedString)](uitextpasteitem/setresult(attributedstring:).md)
  Sets a text paste item’s textual value to a specified attributed string from the item provider.
- [func setResult(attachment: NSTextAttachment)](uitextpasteitem/setresult(attachment:).md)
  Sets a text paste item’s attachment value to a specified value.
- [func setNoResult()](uitextpasteitem/setnoresult.md)
  Sets the text paste item’s textual value to not include data from the item provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextpasteitem/setdefaultresult())*