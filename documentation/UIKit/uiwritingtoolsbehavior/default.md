# UIWritingToolsBehavior.default

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

An option to let the system determine the best way to enable writing tools for the view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.4+

## Declaration

```swift
case `default`
```

```c
UIWritingToolsBehaviorDefault
```

## Discussion

The system chooses a complete, limited, or none experience based on the device-level support for the feature.

## See Also

### Getting the writing tools behaviors
- [UIWritingToolsBehavior.none](./none.md)
  An option to prevent the writing tools from modifying the text in the view.
- [UIWritingToolsBehavior.complete](./complete.md)
  An option to provide the complete writing tools experience for the text view.
- [UIWritingToolsBehavior.limited](./limited.md)
  An option to provide a limited, overlay-panel experience for the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolsbehavior/default)*