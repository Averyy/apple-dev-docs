# UIWritingToolsCoordinator.TextDecoration

**Framework**: UIKit  
**Kind**: enum

Use the `UIWritingToolsCoordinator.TextDecoration` constants to determine the type of decoration to be applied to a preview for grammar animation. The grammar animation needs previews of the text of the issue in two forms, without and with the grammar indication underline applied. If you use grammar animation, you must implement the delegate method [`writingToolsCoordinator(_:requestsPreviewFor:of:in:textDecoration:completion:)`](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:of:in:textdecoration:completion:).md) to provide both forms of previews, based on the specified decoration.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum TextDecoration
```

## Topics

### Enumeration Cases
- [UIWritingToolsCoordinator.TextDecoration.grammarUnderline](uiwritingtoolscoordinator/textdecoration/grammarunderline.md)
  Requests a preview of the text with the grammar indication underline.
- [UIWritingToolsCoordinator.TextDecoration.none](uiwritingtoolscoordinator/textdecoration/none.md)
  Requests a preview of the text without any additional decoration.
### Initializers
- [init?(rawValue: Int)](uiwritingtoolscoordinator/textdecoration/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textdecoration)*