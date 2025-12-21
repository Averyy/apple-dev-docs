# presentationIntent

**Framework**: UIKit  
**Kind**: property

implies `RichText`, `List`, and `Table`, and Writing Tools may provide text with presentation intent attributes. Writing Tools will use `NSPresentationIntent` instead of `NSTextList` and `NSTextTable` to represent lists and tables.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
static var presentationIntent: UIWritingToolsResultOptions { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolsresultoptions/presentationintent)*