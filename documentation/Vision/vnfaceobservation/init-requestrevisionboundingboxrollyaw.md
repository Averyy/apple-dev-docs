# init(requestRevision:boundingBox:roll:yaw:)

**Framework**: Vision  
**Kind**: init

Creates an observation that contains the roll and yaw of the face.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(requestRevision: Int, boundingBox: CGRect, roll: NSNumber?, yaw: NSNumber?)
```

## Parameters

- `requestRevision`: The revision of the request.
- `boundingBox`: The bounding rectangle of the detected face landmark.
- `roll`: The rotational angle of the face landmark around the z-axis.
- `yaw`: The rotational angle of the face landmark around the y-axis.

## See Also

- [convenience init(requestRevision: Int, boundingBox: CGRect, roll: NSNumber?, yaw: NSNumber?, pitch: NSNumber?)](vnfaceobservation/init(requestrevision:boundingbox:roll:yaw:pitch:).md)
  Creates an observation that contains the roll, yaw, and pitch of the face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfaceobservation/init(requestrevision:boundingbox:roll:yaw:))*