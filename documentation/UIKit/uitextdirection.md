# UITextDirection

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

The direction of the text.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
struct UITextDirection
```

```c
typedef NSInteger UITextDirection;
```

#### Overview

This parameter is used in methods declared by the [`UITextInputTokenizer`](./uitextinputtokenizer.md) protocol. This general direction type subsumes constants of the [`UITextStorageDirection`](./uitextstoragedirection.md) and [`UITextLayoutDirection`](./uitextlayoutdirection.md) types.

## Topics

### Text direction types
- [static func layout(UITextLayoutDirection) -> UITextDirection](./uitextdirection/layout%28_%29.md)
  Specifies the direction of text layout.
- [static func storage(UITextStorageDirection) -> UITextDirection](./uitextdirection/storage%28_%29.md)
  Specifies the direction of text storage.
### Initializers
- [init(rawValue: Int)](./uitextdirection/init%28rawvalue%29.md)
  Creates a text direction with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum UITextStorageDirection](./uitextstoragedirection.md)
  The direction of text storage.
- [enum UITextLayoutDirection](./uitextlayoutdirection.md)
  The direction of text layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdirection)*