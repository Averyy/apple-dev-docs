# supportedIdentifiers()

**Framework**: Vision  
**Kind**: method

Returns the classification identifiers that the request supports in its current configuration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func supportedIdentifiers() throws -> [String]
```

#### Return Value

An array of supported identifiers.

## See Also

- [var results: [VNClassificationObservation]?](vnclassifyimagerequest/results.md)
  The results of the image classification request.
- [class VNClassificationObservation](vnclassificationobservation.md)
  An object that represents classification information that an image-analysis request produces.
- [class func knownClassifications(forRevision: Int) throws -> [VNClassificationObservation]](vnclassifyimagerequest/knownclassifications(forrevision:).md)
  Requests the collection of classifications that the Vision framework recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnclassifyimagerequest/supportedidentifiers())*