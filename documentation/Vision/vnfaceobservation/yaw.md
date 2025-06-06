# yaw

**Framework**: Vision  
**Kind**: property

The yaw angle of a face in radians.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var yaw: NSNumber? { get }
```

#### Discussion

This value indicates the rotational angle of the face around the y-axis.

If the request doesn’t calculate the angle, the value is `nil.`

## See Also

- [var roll: NSNumber?](vnfaceobservation/roll.md)
  The roll angle of a face in radians.
- [var pitch: NSNumber?](vnfaceobservation/pitch.md)
  The pitch angle of a face in radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfaceobservation/yaw)*