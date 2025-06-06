# SKSearchResultsFilterCallBack

**Framework**: Core Services  
**Kind**: tdef

Deprecated. Use `SKSearchCreate` and `SKSearchFindMatches` instead, which do not use a callback.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```swift
typealias SKSearchResultsFilterCallBack = (SKIndex?, SKDocument?, UnsafeMutableRawPointer?) -> DarwinBoolean
```

#### Return_value

A Boolean value of `true` for a successful search hit, or `false` otherwise.

#### Discussion

Deprecated. Defines a pointer to a search-results filtering callback function for hit testing and processing during a search. Use this callback function to perform custom filtering on the search hits returned by the [`SKSearchResultsCreateWithQuery`](1448610-sksearchresultscreatewithquery.md) and [`SKSearchResultsCreateWithDocuments`](1448629-sksearchresultscreatewithdocumen.md) functions. Return `true` to keep this document URL object (SKDocumentRef) in the results, `false` to filter it out.

## Parameters

- `inIndex`: The index you are searching.
- `inDocument`: The document URL object within the index you are searching.
- `inContext`: An application-specified context which you set when calling   or  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/sksearchresultsfiltercallback)*