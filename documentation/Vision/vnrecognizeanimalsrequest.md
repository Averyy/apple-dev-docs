# VNRecognizeAnimalsRequest

**Framework**: Vision  
**Kind**: class  
**Role**: Class

A request that recognizes animals in an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class VNRecognizeAnimalsRequest
```

```objc
@interface VNRecognizeAnimalsRequest : VNImageBasedRequest
```

#### Overview

Use the [`knownAnimalIdentifiers(forRevision:)`](./vnrecognizeanimalsrequest/knownanimalidentifiers%28forrevision%29.md) method to determine which animals the request supports.

## Topics

### Accessing the Results
- [var results: [VNRecognizedObjectObservation]?](./vnrecognizeanimalsrequest/results.md)
  The results of the request to recognize animals.
### Identifying Animals
- [func supportedIdentifiers() throws -> [VNAnimalIdentifier]](./vnrecognizeanimalsrequest/supportedidentifiers%28%29.md)
  Returns the identifiers of the animals that the request detects.
- [struct VNAnimalIdentifier](./vnanimalidentifier.md)
  An animal identifier string.
- [class func knownAnimalIdentifiers(forRevision: Int) throws -> [VNAnimalIdentifier]](./vnrecognizeanimalsrequest/knownanimalidentifiers%28forrevision%29.md)
  Returns a list of animal identifiers the recognition algorithm supports for the specified revision.
### Identifying Request Revisions
- [var VNRecognizeAnimalsRequestRevision2: Int](./vnrecognizeanimalsrequestrevision2.md)
  A constant for specifying revision 2 of the animal recognition request.
- [var VNRecognizeAnimalsRequestRevision1: Int](./vnrecognizeanimalsrequestrevision1.md)
  A constant for specifying revision 1 of the animal recognition request.

## Relationships

### Inherits From
- [VNImageBasedRequest](./vnimagebasedrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizeanimalsrequest)*