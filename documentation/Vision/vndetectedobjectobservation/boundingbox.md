# boundingBox

**Framework**: Vision  
**Kind**: property

The bounding box of the object that the request detects.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var boundingBox: CGRect { get }
```

#### Discussion

The system normalizes the coordinates to the dimensions of the processed image, with the origin at the lower-left corner of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectedobjectobservation/boundingbox)*