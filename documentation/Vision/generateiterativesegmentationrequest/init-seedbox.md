# init(seedBox:_:)

**Framework**: Vision  
**Kind**: init

Instantiates with a seed box.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(seedBox: NormalizedRect, _ revision: GenerateIterativeSegmentationRequest.Revision? = nil)
```

#### Discussion

No result will be produced if the box is outside of the `regionOfInterest`. By default, the `regionOfInterest` is the whole image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateiterativesegmentationrequest/init(seedbox:_:))*