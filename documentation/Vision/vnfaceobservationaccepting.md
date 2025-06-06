# VNFaceObservationAccepting

**Framework**: Vision  
**Kind**: protocol

An image analysis request that operates on face observations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol VNFaceObservationAccepting : NSObjectProtocol
```

#### Overview

This protocol allows you to provide an input collection of [`VNFaceObservation`](vnfaceobservation.md) objects as part of a request. Request objects adopt this protocol to request additional information about detected faces, such as facial landmarks.

## Topics

### Providing Face Observations
- [var inputFaceObservations: [VNFaceObservation]?](vnfaceobservationaccepting/inputfaceobservations.md)
  An array of [`VNFaceObservation`](vnfaceobservation.md) objects to process as part of the request.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [VNDetectFaceCaptureQualityRequest](vndetectfacecapturequalityrequest.md)
- [VNDetectFaceLandmarksRequest](vndetectfacelandmarksrequest.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfaceobservationaccepting)*