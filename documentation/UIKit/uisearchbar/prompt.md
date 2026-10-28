# prompt

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A single line of text displayed at the top of the search bar.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var prompt: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * prompt;
```

## Discussion

The default value is `nil`.

## See Also

### Getting the search text
- [var placeholder: String?](./placeholder.md)
  The string to display when there’s no other text in the text field.
- [var text: String?](./text.md)
  The current or starting search text.
- [var searchTextField: UISearchTextField](./searchtextfield.md)
  The text field that the user enters a search query into.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/prompt)*