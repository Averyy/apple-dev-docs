# UITextPlaceholder

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A placeholder object that reserves visual space in a text input view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITextPlaceholder
```

```objc
@interface UITextPlaceholder : NSObject
```

## Topics

### Accessing the selection rectangles
- [var rects: [UITextSelectionRect]](./uitextplaceholder/rects.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Managing placeholders
- [func insertTextPlaceholder(with: CGSize) -> UITextPlaceholder](./uitextinput/inserttextplaceholder%28with%29.md)
  Inserts a placeholder object to reserve visual space during text input.
- [func remove(UITextPlaceholder)](./uitextinput/remove%28_%29.md)
  Removes a placeholder object from the text input view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextplaceholder)*