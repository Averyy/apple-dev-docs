# init(frameAnalysisSpacing:completionHandler:)

**Framework**: Vision  
**Kind**: init

Initializes a video-based request.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(frameAnalysisSpacing: CMTime, completionHandler: VNRequestCompletionHandler? = nil)
```

## Parameters

- `frameAnalysisSpacing`: A   value that indicates the duration between analysis operations. Increase this value to reduce the number of frames analyzed on slower devices. Set this argument to   to analyze all frames.
- `completionHandler`: A closure that’s invoked after the request has completed its processing. The system invokes the completion handler on the same dispatch queue as the request performs its processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnstatefulrequest/init(frameanalysisspacing:completionhandler:))*