# presentationIntent

**Framework**: UIKit  
**Kind**: property

implies `RichText`, `List`, and `Table`, and Writing Tools may provide text with presentation intent attributes. Writing Tools will use `NSPresentationIntent` instead of `NSTextList` and `NSTextTable` to represent lists and tables.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static var presentationIntent: UIWritingToolsResultOptions { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolsresultoptions/presentationintent)*