# VNRequestTextRecognitionLevel

**Framework**: Vision  
**Kind**: enum

Constants that identify the performance and accuracy of the text recognition.

## Declaration

```swift
enum VNRequestTextRecognitionLevel
```

## Topics

### Recognition Levels
- [VNRequestTextRecognitionLevel.fast](vnrequesttextrecognitionlevel/fast.md)
  Fast text recognition returns results more quickly at the expense of accuracy.
- [VNRequestTextRecognitionLevel.accurate](vnrequesttextrecognitionlevel/accurate.md)
  Accurate text recognition takes more time to produce a more comprehensive result.
### Creating a Recognition Level
- [init?(rawValue: Int)](vnrequesttextrecognitionlevel/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var minimumTextHeight: Float](vnrecognizetextrequest/minimumtextheight.md)
  The minimum height, relative to the image height, of the text to recognize.
- [var recognitionLevel: VNRequestTextRecognitionLevel](vnrecognizetextrequest/recognitionlevel.md)
  A value that determines whether the request prioritizes accuracy or speed in text recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrequesttextrecognitionlevel)*