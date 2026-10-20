# characterOffset(of:within:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the character offset of a position in a document’s text that falls within a specified range.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func characterOffset(of position: UITextPosition, within range: UITextRange) -> Int
```

```objc
- (NSInteger) characterOffsetOfPosition:(UITextPosition *) position withinRange:(UITextRange *) range;
```

#### Return Value

The number of characters in a document’s text that occur between `position` and the beginning of `range`.

#### Discussion

You should implement this method if you don’t have a one-to-one correspondence between [`UITextPosition`](../uitextposition.md) objects within the given range and character offsets into a document string.

## Parameters

- `position`: An object that identifies a location in a document’s text.
- `range`: An object that specifies a range of text in a document.

## See Also

### Reconciling text position and character offset
- [func position(within: UITextRange, atCharacterOffset: Int) -> UITextPosition?](./position%28within,atcharacteroffset%29.md)
  Returns the position within a range of a document’s text that corresponds to the character offset from the start of that range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/characteroffset(of:within:))*