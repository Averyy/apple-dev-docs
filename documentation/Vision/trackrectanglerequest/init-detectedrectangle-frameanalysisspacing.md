# init(detectedRectangle:_:frameAnalysisSpacing:)

**Framework**: Vision  
**Kind**: init

Creates a rectangle tracking request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
init(detectedRectangle: any QuadrilateralProviding & VisionObservation, _ revision: TrackRectangleRequest.Revision? = nil, frameAnalysisSpacing: CMTime? = nil)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/trackrectanglerequest/init(detectedrectangle:_:frameanalysisspacing:))*