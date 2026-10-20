# init(requestRevision:boundingBox:roll:yaw:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates an observation that contains the roll and yaw of the face.

**Availability**:
- iOS 12.0+ - Deprecated in 15.0
- iPadOS 12.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.14+ - Deprecated in 12.0
- tvOS 12.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`init(requestRevision:boundingBox:roll:yaw:pitch:)`](./init%28requestrevision,boundingbox,roll,yaw,pitch%29.md)instead.

## Declaration

```swift
convenience init(requestRevision: Int, boundingBox: CGRect, roll: NSNumber?, yaw: NSNumber?)
```

```objc
+ (instancetype) faceObservationWithRequestRevision:(NSUInteger) requestRevision boundingBox:(CGRect) boundingBox roll:(NSNumber *) roll yaw:(NSNumber *) yaw;
```

## Parameters

- `requestRevision`: The revision of the request.
- `boundingBox`: The bounding rectangle of the detected face landmark.
- `roll`: The rotational angle of the face landmark around the z-axis.
- `yaw`: The rotational angle of the face landmark around the y-axis.

## See Also

### Creating an Observation
- [convenience init(requestRevision: Int, boundingBox: CGRect, roll: NSNumber?, yaw: NSNumber?, pitch: NSNumber?)](./init%28requestrevision,boundingbox,roll,yaw,pitch%29.md)
  Creates an observation that contains the roll, yaw, and pitch of the face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfaceobservation/init(requestrevision:boundingbox:roll:yaw:))*