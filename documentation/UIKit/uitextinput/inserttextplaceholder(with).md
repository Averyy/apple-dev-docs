# insertTextPlaceholder(with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Inserts a placeholder object to reserve visual space during text input.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func insertTextPlaceholder(with size: CGSize) -> UITextPlaceholder
```

```objc
- (UITextPlaceholder *) insertTextPlaceholderWithSize:(CGSize) size;
```

#### Return Value

The placeholder object that was inserted into the text input.

#### Discussion

If the `size.height` is less than or equal to zero, then the placeholder displays inline using the current line’s height.

If the `size.height` is greater than zero, then the text input treats the placeholder as a paragraph of height `size.height`.

## Parameters

- `size`: The size of the space to reserve.

## See Also

### Managing placeholders
- [func remove(UITextPlaceholder)](./remove%28_%29.md)
  Removes a placeholder object from the text input view.
- [class UITextPlaceholder](../uitextplaceholder.md)
  A placeholder object that reserves visual space in a text input view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/inserttextplaceholder(with:))*