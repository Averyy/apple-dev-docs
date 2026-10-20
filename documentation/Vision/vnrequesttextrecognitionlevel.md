# VNRequestTextRecognitionLevel

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

Constants that identify the performance and accuracy of the text recognition.

## Declaration

```swift
enum VNRequestTextRecognitionLevel
```

```c
enum VNRequestTextRecognitionLevel : NSInteger;
```

## Topics

### Recognition Levels
- [VNRequestTextRecognitionLevel.fast](./vnrequesttextrecognitionlevel/fast.md)
  Fast text recognition returns results more quickly at the expense of accuracy.
- [VNRequestTextRecognitionLevel.accurate](./vnrequesttextrecognitionlevel/accurate.md)
  Accurate text recognition takes more time to produce a more comprehensive result.
### Creating a Recognition Level
- [init?(rawValue: Int)](./vnrequesttextrecognitionlevel/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Customizing Recognition Constraints
- [var minimumTextHeight: Float](./vnrecognizetextrequest/minimumtextheight.md)
  The minimum height, relative to the image height, of the text to recognize.
- [var recognitionLevel: VNRequestTextRecognitionLevel](./vnrecognizetextrequest/recognitionlevel.md)
  A value that determines whether the request prioritizes accuracy or speed in text recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrequesttextrecognitionlevel)*