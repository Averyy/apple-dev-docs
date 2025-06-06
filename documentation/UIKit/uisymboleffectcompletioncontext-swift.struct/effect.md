# effect

**Framework**: UIKit  
**Kind**: property

The symbol effect that completed.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
@MainActor
var effect: any SymbolEffect { get }
```

#### Discussion

For a symbol effect completion, this property may not be the same instance as the original effect.

For a content transition completion, this property is `nil.`

## See Also

- [var isFinished: Bool](uisymboleffectcompletioncontext-swift.struct/isfinished.md)
  A Boolean value that indicates whether the symbol effect finished completely.
- [var sender: AnyObject?](uisymboleffectcompletioncontext-swift.struct/sender.md)
  The object, an image view or bar button item, that received the symbol effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisymboleffectcompletioncontext-swift.struct/effect)*