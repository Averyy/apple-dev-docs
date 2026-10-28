# knownAnimalIdentifiers(forRevision:)

**Framework**: Vision  
**Kind**: method  
**Role**: Type Method

Returns a list of animal identifiers the recognition algorithm supports for the specified revision.

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
class func knownAnimalIdentifiers(forRevision requestRevision: Int) throws -> [VNAnimalIdentifier]
```

```objc
+ (NSArray<NSString *> *) knownAnimalIdentifiersForRevision:(NSUInteger) requestRevision error:(NSError **) error;
```

## Return Value

The animal identifiers.

## Parameters

- `requestRevision`: The revision of the animal recognition request.

## See Also

### Identifying Animals
- [func supportedIdentifiers() throws -> [VNAnimalIdentifier]](./supportedidentifiers%28%29.md)
  Returns the identifiers of the animals that the request detects.
- [struct VNAnimalIdentifier](../vnanimalidentifier.md)
  An animal identifier string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizeanimalsrequest/knownanimalidentifiers(forrevision:))*