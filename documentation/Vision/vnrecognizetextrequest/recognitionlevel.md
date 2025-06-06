# recognitionLevel

**Framework**: Vision  
**Kind**: property

A value that determines whether the request prioritizes accuracy or speed in text recognition.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var recognitionLevel: VNRequestTextRecognitionLevel { get set }
```

## Mentions

- [Recognizing Text in Images](recognizing-text-in-images.md)

#### Discussion

The recognition level determines which techniques the request uses during the text recognition. Set this value to [`VNRequestTextRecognitionLevel.fast`](vnrequesttextrecognitionlevel/fast.md) to prioritize speed over accuracy, and to [`VNRequestTextRecognitionLevel.accurate`](vnrequesttextrecognitionlevel/accurate.md) for longer, more computationally intensive recognition.

## See Also

- [var minimumTextHeight: Float](vnrecognizetextrequest/minimumtextheight.md)
  The minimum height, relative to the image height, of the text to recognize.
- [enum VNRequestTextRecognitionLevel](vnrequesttextrecognitionlevel.md)
  Constants that identify the performance and accuracy of the text recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizetextrequest/recognitionlevel)*