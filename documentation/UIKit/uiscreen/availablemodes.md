# availableModes

**Framework**: UIKit  
**Kind**: property

The display modes that can be associated with the screen.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var availableModes: [UIScreenMode] { get }
```

## Mentions

- [Presenting content on a connected display](presenting-content-on-a-connected-display.md)

#### Discussion

The array contains one or more [`UIScreenMode`](uiscreenmode.md) objects, each of which represents a display mode supported by the screen.

## See Also

- [var currentMode: UIScreenMode?](uiscreen/currentmode.md)
  The current screen mode associated with the screen.
- [var preferredMode: UIScreenMode?](uiscreen/preferredmode.md)
  The preferred display mode for the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/availablemodes)*