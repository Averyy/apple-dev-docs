# topCandidates(_:)

**Framework**: Vision  
**Kind**: method

Requests the  top candidates for a recognized text string.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func topCandidates(_ maxCandidateCount: Int) -> [VNRecognizedText]
```

#### Return Value

An array of the  top candidates, sorted by decreasing confidence score.

#### Discussion

This function returns no more than  candidates, but it may return fewer than  candidates.

## Parameters

- `maxCandidateCount`: The maximum number of candidates to return. This can’t exceed 10.

## See Also

- [class VNRecognizedText](vnrecognizedtext.md)
  Text recognized in an image through a text recognition request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedtextobservation/topcandidates(_:))*