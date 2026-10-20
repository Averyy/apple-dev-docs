# roll

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The roll angle of a face in radians.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var roll: NSNumber? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSNumber * roll;
```

#### Discussion

This value indicates the rotational angle of the face around the z-axis.

If the request doesn’t calculate the angle, the value is `nil`.

## See Also

### Determining Facial Orientation
- [var yaw: NSNumber?](./yaw.md)
  The yaw angle of a face in radians.
- [var pitch: NSNumber?](./pitch.md)
  The pitch angle of a face in radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfaceobservation/roll)*