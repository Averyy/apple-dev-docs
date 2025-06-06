# SKSearchType

**Framework**: Core Services  
**Kind**: struct

Search Kit ignores the constants in this group. Use asynchronous searching with `SKSearchCreate` instead, which uses query syntax to determine search type.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```swift
struct SKSearchType
```

#### Overview

In releases of macOS prior to version 10.4, these constants specify the category of search to perform. Starting with OS X v10.4, use asynchronous searching with `SKSearchCreate` instead, which uses query syntax to determine search type.

In older versions of macOS, these constants specify the various search types you can use with `SKSearchResultsCreateWithQuery`. Each of these specifies a set of ranked search hits. The `kSKSearchRanked` and `kSKSearchPrefixRanked` constants can be used for all index types. The `kSKSearchBooleanRanked` and `kSKSearchRequiredRanked` constants cannot be used for vector indexes. 

## Topics

### Constants
- [var kSKSearchRanked: SKSearchType](ksksearchranked.md)
  Deprecated. Specifies a basic ranked search.
- [var kSKSearchBooleanRanked: SKSearchType](ksksearchbooleanranked.md)
  Deprecated. Specifies a query that can include Boolean operators including `'|'`, `'&'`, `'!'`, `'('`, and `')'`.
- [var kSKSearchRequiredRanked: SKSearchType](ksksearchrequiredranked.md)
  Deprecated. Specifies a query that can include required (`'+'`) or excluded (`'-'`) terms.
- [var kSKSearchPrefixRanked: SKSearchType](ksksearchprefixranked.md)
  Deprecated. Specifies a prefix-based search, which matches terms that begin with the query string.
### Initializers
- [init(UInt32)](sksearchtype/1449367-init.md)
- [init(rawValue: UInt32)](sksearchtype/1448964-init.md)
### Instance Properties
- [var rawValue: UInt32](sksearchtype/1445786-rawvalue.md)

## Relationships

### Conforms To
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/sksearchtype)*