# SKSearchOptions

**Framework**: Core Services  
**Kind**: tdef

Specifies the search options available for the [`SKSearchCreate(_:_:_:)`](1443079-sksearchcreate.md) function.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
typealias SKSearchOptions = UInt32
```

## Topics

### Constants
- [var kSKSearchOptionDefault: Int](ksksearchoptiondefault.md)
- [var kSKSearchOptionNoRelevanceScores: Int](ksksearchoptionnorelevancescores.md)
  This option saves time during a search by suppressing the computation of relevance scores.
- [var kSKSearchOptionSpaceMeansOR: Int](ksksearchoptionspacemeansor.md)
  This option alters query behavior so that spaces are interpreted as Boolean `OR` operators.
- [var kSKSearchOptionFindSimilar: Int](ksksearchoptionfindsimilar.md)
  This option alters query behavior so that Search Kit returns references to documents that are similar to an example text string. When this option is specified, Search Kit ignores all query operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/sksearchoptions)*