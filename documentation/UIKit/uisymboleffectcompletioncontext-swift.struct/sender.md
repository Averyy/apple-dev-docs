# sender

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The object, an image view or bar button item, that received the symbol effect.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS

## Declaration

```swift
@MainActor
weak var sender: AnyObject? { get }
```

## See Also

### Determining completion status
- [var effect: any SymbolEffect](./effect.md)
  The symbol effect that completed.
- [var isFinished: Bool](./isfinished.md)
  A Boolean value that indicates whether the symbol effect finished completely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisymboleffectcompletioncontext-swift.struct/sender)*