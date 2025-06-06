# touchBar

**Framework**: UIKit  
**Kind**: property

The Touch Bar object for the responder.

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
@MainActor
var touchBar: NSTouchBar? { get set }
```

#### Discussion

This property’s default value — on devices with a Touch Bar — is the [`NSTouchBar`](https://developer.apple.com/documentation/AppKit/NSTouchBar) instance that the responder’s [`makeTouchBar()`](uiresponder/maketouchbar().md) method returns. Otherwise, the default value is `nil`.

## See Also

- [func makeTouchBar() -> NSTouchBar?](uiresponder/maketouchbar.md)
  Asks the receiving responder to create and configure a Touch Bar object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/touchbar)*