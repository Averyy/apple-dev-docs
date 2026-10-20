# pitch

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The pitch angle of a face in radians.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var pitch: NSNumber? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSNumber * pitch;
```

#### Discussion

This value indicates the rotational angle of the face around the x-axis.

If the request doesn’t calculate the angle, the value is `nil`.

## See Also

### Determining Facial Orientation
- [var roll: NSNumber?](./roll.md)
  The roll angle of a face in radians.
- [var yaw: NSNumber?](./yaw.md)
  The yaw angle of a face in radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfaceobservation/pitch)*