# init(trajectoryLength:_:frameAnalysisSpacing:)

**Framework**: Vision  
**Kind**: init

Creates a trajectory-detection request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
init(trajectoryLength: Int, _ revision: DetectTrajectoriesRequest.Revision? = nil, frameAnalysisSpacing: CMTime? = nil)
```

## Parameters

- `trajectoryLength`: The number of points required to analyze to determine that a shape follows a parabolic path. This argument value must be at least 5.
- `revision`: The specific algorithm or implementation revision that the system uses to perform the request.
- `frameAnalysisSpacing`: The duration between analysis operations. Increase this value to reduce the number of frames analyzed on slower devices. By default, Vision analyzes all frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detecttrajectoriesrequest/init(trajectorylength:_:frameanalysisspacing:))*