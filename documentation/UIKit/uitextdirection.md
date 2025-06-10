# UITextDirection

**Framework**: UIKit  
**Kind**: struct

The direction of the text.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct UITextDirection
```

#### Overview

This parameter is used in methods declared by the [`UITextInputTokenizer`](uitextinputtokenizer.md) protocol. This general direction type subsumes constants of the [`UITextStorageDirection`](uitextstoragedirection.md) and [`UITextLayoutDirection`](uitextlayoutdirection.md) types.

## Topics

### Text direction types
- [static func layout(UITextLayoutDirection) -> UITextDirection](uitextdirection/layout(_:).md)
  Specifies the direction of text layout.
- [static func storage(UITextStorageDirection) -> UITextDirection](uitextdirection/storage(_:).md)
  Specifies the direction of text storage.
### Initializers
- [init(rawValue: Int)](uitextdirection/init(rawvalue:).md)
  Creates a text direction with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum UITextStorageDirection](uitextstoragedirection.md)
  The direction of text storage.
- [enum UITextLayoutDirection](uitextlayoutdirection.md)
  The direction of text layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdirection)*