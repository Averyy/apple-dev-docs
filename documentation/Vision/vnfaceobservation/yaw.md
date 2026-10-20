# yaw

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, strong, readonly, nullable) NSNumber * yaw;
```

#### Discussion

This value indicates the rotational angle of the face around the y-axis.

If the request doesn’t calculate the angle, the value is `nil`.

## See Also

### Determining Facial Orientation
- [var roll: NSNumber?](./roll.md)
  The roll angle of a face in radians.
- [var pitch: NSNumber?](./pitch.md)
  The pitch angle of a face in radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfaceobservation/yaw)*