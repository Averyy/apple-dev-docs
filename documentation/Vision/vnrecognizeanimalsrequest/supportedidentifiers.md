# supportedIdentifiers()

**Framework**: Vision  
**Kind**: method

Returns the identifiers of the animals that the request detects.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func supportedIdentifiers() throws -> [VNAnimalIdentifier]
```

#### Return Value

The animal identifiers.

## See Also

- [struct VNAnimalIdentifier](vnanimalidentifier.md)
  An animal identifier string.
- [class func knownAnimalIdentifiers(forRevision: Int) throws -> [VNAnimalIdentifier]](vnrecognizeanimalsrequest/knownanimalidentifiers(forrevision:).md)
  Returns a list of animal identifiers the recognition algorithm supports for the specified revision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizeanimalsrequest/supportedidentifiers())*