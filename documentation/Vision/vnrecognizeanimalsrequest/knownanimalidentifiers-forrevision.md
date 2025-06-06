# knownAnimalIdentifiers(forRevision:)

**Framework**: Vision  
**Kind**: method

Returns a list of animal identifiers the recognition algorithm supports for the specified revision.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func knownAnimalIdentifiers(forRevision requestRevision: Int) throws -> [VNAnimalIdentifier]
```

#### Return Value

The animal identifiers.

## Parameters

- `requestRevision`: The revision of the animal recognition request.

## See Also

- [func supportedIdentifiers() throws -> [VNAnimalIdentifier]](vnrecognizeanimalsrequest/supportedidentifiers.md)
  Returns the identifiers of the animals that the request detects.
- [struct VNAnimalIdentifier](vnanimalidentifier.md)
  An animal identifier string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizeanimalsrequest/knownanimalidentifiers(forrevision:))*