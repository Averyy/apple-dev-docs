# init(requestRevision:boundingBox:roll:yaw:pitch:)

**Framework**: Vision  
**Kind**: init

Creates an observation that contains the roll, yaw, and pitch of the face.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(requestRevision: Int, boundingBox: CGRect, roll: NSNumber?, yaw: NSNumber?, pitch: NSNumber?)
```

## Parameters

- `requestRevision`: The revision of the request.
- `boundingBox`: The bounding rectangle of the detected face landmark.
- `roll`: The rotational angle of the face landmark around the z-axis.
- `yaw`: The rotational angle of the face landmark around the y-axis.
- `pitch`: The rotational angle of the face landmark around the x-axis.

## See Also

- [convenience init(requestRevision: Int, boundingBox: CGRect, roll: NSNumber?, yaw: NSNumber?)](vnfaceobservation/init(requestrevision:boundingbox:roll:yaw:).md)
  Creates an observation that contains the roll and yaw of the face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfaceobservation/init(requestrevision:boundingbox:roll:yaw:pitch:))*