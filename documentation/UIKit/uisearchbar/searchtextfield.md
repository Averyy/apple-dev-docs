# searchTextField

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The text field that the user enters a search query into.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var searchTextField: UISearchTextField { get }
```

```objc
@property (nonatomic, readonly) UISearchTextField * searchTextField;
```

## Discussion

For details about interacting with the text field, accessing its content, and using tokens, see [`UISearchTextField`](../uisearchtextfield.md) and [`UISearchToken`](../uisearchtoken.md).

## See Also

### Getting the search text
- [var placeholder: String?](./placeholder.md)
  The string to display when there’s no other text in the text field.
- [var prompt: String?](./prompt.md)
  A single line of text displayed at the top of the search bar.
- [var text: String?](./text.md)
  The current or starting search text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/searchtextfield)*