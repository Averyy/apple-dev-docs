# objectBounds()

**Framework**: Watchkit  
**Kind**: method

Returns the dimensions of the interface object (measured in points) associated with the gesture recognizer.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func objectBounds() -> CGRect
```

## Overview

The bounding rectangle of the interface object to which the gesture recognizer is attached.

## Discussion

You attach a gesture recognizer to a specific element in your storyboard file. At runtime, you use this property to get the dimensions of that element.

## See Also

- [func locationInObject() -> CGPoint](locationinobject().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/locationinobject()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/objectbounds())*