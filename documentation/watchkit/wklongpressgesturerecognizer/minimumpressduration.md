# minimumPressDuration

**Framework**: Watchkit  
**Kind**: property

The minimum amount of time (in seconds) that the user’s fingers must be touching the interface object.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var minimumPressDuration: CFTimeInterval { get set }
```

## Overview

The default value of this property is `0.5` seconds, but you can change this value when configuring the gesture recognizer in Interface Builder.

## See Also

- [var numberOfTapsRequired: Int](numberoftapsrequired.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer/numberoftapsrequired))
- [var allowableMovement: CGFloat](allowablemovement.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer/allowablemovement))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer/minimumpressduration)*