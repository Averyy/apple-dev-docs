# VNAnimalIdentifier

**Framework**: Vision  
**Kind**: struct

An animal identifier string.

## Declaration

```swift
struct VNAnimalIdentifier
```

## Topics

### Animals
- [static let cat: VNAnimalIdentifier](vnanimalidentifier/cat.md)
  An animal identifier for cats.
- [static let dog: VNAnimalIdentifier](vnanimalidentifier/dog.md)
  An animal identifier for dogs.
### Initializers
- [init(rawValue: String)](vnanimalidentifier/init(rawvalue:).md)
  Creates an identifier with a string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func supportedIdentifiers() throws -> [VNAnimalIdentifier]](vnrecognizeanimalsrequest/supportedidentifiers.md)
  Returns the identifiers of the animals that the request detects.
- [class func knownAnimalIdentifiers(forRevision: Int) throws -> [VNAnimalIdentifier]](vnrecognizeanimalsrequest/knownanimalidentifiers(forrevision:).md)
  Returns a list of animal identifiers the recognition algorithm supports for the specified revision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnanimalidentifier)*