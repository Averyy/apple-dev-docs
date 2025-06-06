# locationInObject()

**Framework**: Watchkit  
**Kind**: method

Returns the point computed as the current position of the touch event.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func locationInObject() -> CGPoint
```

#### Return Value

A point in the local coordinate system of the associated interface object.

#### Discussion

If multiple touches were detected, this method returns the location of only the first one.

## See Also

- [func objectBounds() -> CGRect](wkgesturerecognizer/objectbounds.md)
  Returns the dimensions of the interface object (measured in points) associated with the gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/locationinobject())*