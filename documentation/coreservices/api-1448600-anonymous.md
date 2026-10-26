# Anonymous

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kSKSearchOptionDefault](./api-1448600-anonymous/ksksearchoptiondefault.md)
- [kSKSearchOptionFindSimilar](./api-1448600-anonymous/ksksearchoptionfindsimilar.md)
  This option alters query behavior so that Search Kit returns references to documents that are similar to an example text string. When this option is specified, Search Kit ignores all query operators.
- [kSKSearchOptionNoRelevanceScores](./api-1448600-anonymous/ksksearchoptionnorelevancescores.md)
  This option saves time during a search by suppressing the computation of relevance scores.
- [kSKSearchOptionSpaceMeansOR](./api-1448600-anonymous/ksksearchoptionspacemeansor.md)
  This option alters query behavior so that spaces are interpreted as Boolean `OR` operators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448600-anonymous)*