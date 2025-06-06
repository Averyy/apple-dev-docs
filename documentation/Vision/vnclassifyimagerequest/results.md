# results

**Framework**: Vision  
**Kind**: property

The results of the image classification request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var results: [VNClassificationObservation]? { get }
```

## See Also

- [func supportedIdentifiers() throws -> [String]](vnclassifyimagerequest/supportedidentifiers.md)
  Returns the classification identifiers that the request supports in its current configuration.
- [class VNClassificationObservation](vnclassificationobservation.md)
  An object that represents classification information that an image-analysis request produces.
- [class func knownClassifications(forRevision: Int) throws -> [VNClassificationObservation]](vnclassifyimagerequest/knownclassifications(forrevision:).md)
  Requests the collection of classifications that the Vision framework recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnclassifyimagerequest/results)*