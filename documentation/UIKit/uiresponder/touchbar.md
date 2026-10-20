# touchBar

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The Touch Bar object for the responder.

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
var touchBar: NSTouchBar? { get set }
```

```objc
@property (nonatomic, strong, readwrite, nullable) NSTouchBar * touchBar;
```

#### Discussion

This property’s default value — on devices with a Touch Bar — is the [`NSTouchBar`](../../AppKit/nstouchbar.md) instance that the responder’s [`makeTouchBar()`](./maketouchbar%28%29.md) method returns. Otherwise, the default value is `nil`.

## See Also

### Managing the Touch Bar
- [func makeTouchBar() -> NSTouchBar?](./maketouchbar%28%29.md)
  Asks the receiving responder to create and configure a Touch Bar object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/touchbar)*