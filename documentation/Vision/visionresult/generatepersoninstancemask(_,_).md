# VisionResult.generatePersonInstanceMask(_:_:)

**Framework**: Vision  
**Kind**: case  
**Role**: Case

A result from performing a generate person instance mask request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
case generatePersonInstanceMask(GeneratePersonInstanceMaskRequest, InstanceMaskObservation?)
```

## See Also

### Getting the image sequence result
- [case generatePersonSegmentation(GeneratePersonSegmentationRequest, PixelBufferObservation)](./generatepersonsegmentation%28_,_%29.md)
  A result from performing a generate person segmentation request.
- [case detectDocumentSegmentation(DetectDocumentSegmentationRequest, DetectedDocumentObservation?)](./detectdocumentsegmentation%28_,_%29.md)
  A result from performing a detect document segmentation request.
- [case generateIterativeSegmentation(GenerateIterativeSegmentationRequest, PixelBufferObservation?)](./generateiterativesegmentation%28_,_%29.md)
- [case recognizeDocuments(RecognizeDocumentsRequest, [DocumentObservation])](./recognizedocuments%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/visionresult/generatepersoninstancemask(_:_:))*