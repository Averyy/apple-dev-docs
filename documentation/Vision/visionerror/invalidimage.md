# VisionError.invalidImage(_:)

**Framework**: Vision  
**Kind**: case

An error that indicates the input image is invalid.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
case invalidImage(String)
```

#### Discussion

This error occurs when you pass an invalid image to an operation, like passing an image with no dimensions.

## See Also

- [VisionError.invalidArgument(_:)](visionerror/invalidargument(_:).md)
  An error that indicates a request has an invalid value.
- [VisionError.invalidFormat(_:)](visionerror/invalidformat(_:).md)
  An error that indicates a request has data that’s formatted incorrectly.
- [VisionError.invalidModel(_:)](visionerror/invalidmodel(_:).md)
  An error that indicates the Core ML model isn’t compatible with the request.
- [VisionError.invalidOperation(_:)](visionerror/invalidoperation(_:).md)
  An error that indicates an app requests an unsupported operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/visionerror/invalidimage(_:))*