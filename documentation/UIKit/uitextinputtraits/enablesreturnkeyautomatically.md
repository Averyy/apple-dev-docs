# enablesReturnKeyAutomatically

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the system automatically enables the Return key when the user enters text.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
optional var enablesReturnKeyAutomatically: Bool { get set }
```

#### Discussion

The default value for this property is [`false`](https://developer.apple.com/documentation/Swift/false). If you set it to [`true`](https://developer.apple.com/documentation/Swift/true), the keyboard disables the Return key when the text entry area contains no text. As soon as the user enters some text, the Return key is automatically enabled.

## See Also

- [var isSecureTextEntry: Bool](uitextinputtraits/issecuretextentry.md)
  A Boolean value that indicates whether a text object disables copying, and in some cases, prevents recording/broadcasting and also hides the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtraits/enablesreturnkeyautomatically)*