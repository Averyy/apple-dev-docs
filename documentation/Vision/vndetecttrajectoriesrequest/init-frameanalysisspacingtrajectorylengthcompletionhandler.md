# init(frameAnalysisSpacing:trajectoryLength:completionHandler:)

**Framework**: Vision  
**Kind**: init

Creates a new request to detect trajectories.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(frameAnalysisSpacing: CMTime, trajectoryLength: Int, completionHandler: VNRequestCompletionHandler? = nil)
```

## Parameters

- `frameAnalysisSpacing`: A   value that indicates the duration between analysis operations. Increase this value to reduce the number of frames analyzed on slower devices. Set this argument to   to analyze all frames.
- `trajectoryLength`: The number of points required to analyze to determine that a shape follows a parabolic path. This argument value must be at least 5.
- `completionHandler`: A closure that’s invoked after the request completes its processing. The system invokes the completion handler on the same dispatch queue that the request uses to perform its processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecttrajectoriesrequest/init(frameanalysisspacing:trajectorylength:completionhandler:))*