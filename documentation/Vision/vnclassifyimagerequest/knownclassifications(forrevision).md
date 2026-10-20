# knownClassifications(forRevision:)

**Framework**: Vision  
**Kind**: method  
**Role**: Type Method

Requests the collection of classifications that the Vision framework recognizes.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.15+ - Deprecated in 12.0
- tvOS 13.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`supportedIdentifiers()`](./supportedidentifiers%28%29.md) instead.

## Declaration

```swift
class func knownClassifications(forRevision requestRevision: Int) throws -> [VNClassificationObservation]
```

```objc
+ (NSArray<VNClassificationObservation *> *) knownClassificationsForRevision:(NSUInteger) requestRevision error:(NSError **) error;
```

#### Return Value

An array of classifications for the revision, or `nil` if an error occurs.

## Parameters

- `requestRevision`: The revision of the request for which to report classifications.

## See Also

### Accessing Results
- [func supportedIdentifiers() throws -> [String]](./supportedidentifiers%28%29.md)
  Returns the classification identifiers that the request supports in its current configuration.
- [var results: [VNClassificationObservation]?](./results.md)
  The results of the image classification request.
- [class VNClassificationObservation](../vnclassificationobservation.md)
  An object that represents classification information that an image-analysis request produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnclassifyimagerequest/knownclassifications(forrevision:))*