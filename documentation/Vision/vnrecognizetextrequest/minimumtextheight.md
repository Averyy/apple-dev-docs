# minimumTextHeight

**Framework**: Vision  
**Kind**: property

The minimum height, relative to the image height, of the text to recognize.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var minimumTextHeight: Float { get set }
```

#### Discussion

Specify a floating-point number relative to the image height. For example, to limit recognition to text that’s half of the image height, use `0.5`. Increasing the size reduces memory consumption and expedites recognition with the tradeoff of ignoring text smaller than the minimum height. The default value is 1/32, or `0.03125`.

## See Also

- [var recognitionLevel: VNRequestTextRecognitionLevel](vnrecognizetextrequest/recognitionlevel.md)
  A value that determines whether the request prioritizes accuracy or speed in text recognition.
- [enum VNRequestTextRecognitionLevel](vnrequesttextrecognitionlevel.md)
  Constants that identify the performance and accuracy of the text recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizetextrequest/minimumtextheight)*