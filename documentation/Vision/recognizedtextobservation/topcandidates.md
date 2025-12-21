# topCandidates(_:)

**Framework**: Vision  
**Kind**: method

Requests the top candidates for a recognized text string.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func topCandidates(_ maxCandidateCount: Int) -> [RecognizedText]
```

## Parameters

- `maxCandidateCount`: The maximum number of candidates to return, up to  .

## See Also

- [struct RecognizedText](recognizedtext.md)
  Text recognized in an image through a text recognition request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedtextobservation/topcandidates(_:))*