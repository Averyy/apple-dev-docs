# overscanCompensation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

For an external screen, this property sets the desired technique to compensate for overscan.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS

## Declaration

```swift
var overscanCompensation: UIScreen.OverscanCompensation { get set }
```

```objc
@property (nonatomic) UIScreenOverscanCompensation overscanCompensation;
```

#### Discussion

Some external displays may be unable to reliably display all of the pixels to the user. To compensate, choose one of the techniques described in the  [`UIScreen.OverscanCompensation`](./overscancompensation-swift.enum.md) enumeration.

## See Also

### Managing overscan compensation
- [var overscanCompensationInsets: UIEdgeInsets](./overscancompensationinsets.md)
  The edge inset values needed to avoid clipping the rectangle.
- [UIScreen.OverscanCompensation](./overscancompensation-swift.enum.md)
  Describes different techniques for compensating for pixel loss at the edge of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation-swift.property)*