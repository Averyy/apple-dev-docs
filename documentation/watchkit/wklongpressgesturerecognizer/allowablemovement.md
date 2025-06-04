# allowableMovement

**Framework**: Watchkit  
**Kind**: property

The maximum movement of the finger on the interface object that allows the gesture to be recognized.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var allowableMovement: CGFloat { get set }
```

## Overview

The allowable movement is measured in points. The default value of this property is `10`, but you can change this value when configuring the gesture recognizer in Interface Builder.

## See Also

- [var minimumPressDuration: CFTimeInterval](minimumpressduration.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer/minimumpressduration))
- [var numberOfTapsRequired: Int](numberoftapsrequired.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer/numberoftapsrequired))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer/allowablemovement)*