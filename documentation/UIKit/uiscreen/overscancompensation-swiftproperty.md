# overscanCompensation

**Framework**: UIKit  
**Kind**: property

For an external screen, this property sets the desired technique to compensate for overscan.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var overscanCompensation: UIScreen.OverscanCompensation { get set }
```

#### Discussion

Some external displays may be unable to reliably display all of the pixels to the user. To compensate, choose one of the techniques described in the  [`UIScreen.OverscanCompensation`](uiscreen/overscancompensation-swift.enum.md) enumeration.

## See Also

- [var overscanCompensationInsets: UIEdgeInsets](uiscreen/overscancompensationinsets.md)
  The edge inset values needed to avoid clipping the rectangle.
- [UIScreen.OverscanCompensation](uiscreen/overscancompensation-swift.enum.md)
  Describes different techniques for compensating for pixel loss at the edge of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation-swift.property)*