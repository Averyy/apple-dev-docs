# knownClassifications(forRevision:)

**Framework**: Vision  
**Kind**: method

Requests the collection of classifications that the Vision framework recognizes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func knownClassifications(forRevision requestRevision: Int) throws -> [VNClassificationObservation]
```

#### Return Value

An array of classifications for the revision, or `nil` if an error occurs.

## Parameters

- `requestRevision`: The revision of the request for which to report classifications.

## See Also

- [func supportedIdentifiers() throws -> [String]](vnclassifyimagerequest/supportedidentifiers.md)
  Returns the classification identifiers that the request supports in its current configuration.
- [var results: [VNClassificationObservation]?](vnclassifyimagerequest/results.md)
  The results of the image classification request.
- [class VNClassificationObservation](vnclassificationobservation.md)
  An object that represents classification information that an image-analysis request produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnclassifyimagerequest/knownclassifications(forrevision:))*