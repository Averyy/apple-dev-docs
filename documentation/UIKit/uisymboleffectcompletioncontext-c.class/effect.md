# effect

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The symbol effect that completed.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly, nullable) NSSymbolEffect * effect;
```

## Discussion

For a symbol effect completion, this property may not be the same instance as the original effect.

For a content transition completion, this property is `nil.`

## See Also

### Determining completion status
- [contentTransition](./contenttransition.md)
  The symbol content transition that completed.
- [finished](./finished.md)
  A Boolean value that indicates whether the symbol effect finished completely.
- [sender](./sender.md)
  The object, an image view or bar button item, that received the symbol effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisymboleffectcompletioncontext-c.class/effect)*