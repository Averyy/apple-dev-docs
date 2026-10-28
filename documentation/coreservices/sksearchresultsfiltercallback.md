# SKSearchResultsFilterCallBack

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Deprecated. Use `SKSearchCreate` and `SKSearchFindMatches` instead, which do not use a callback.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```swift
typealias SKSearchResultsFilterCallBack = (SKIndex?, SKDocument?, UnsafeMutableRawPointer?) -> DarwinBoolean
```

```c
typedef Boolean (*SKSearchResultsFilterCallBack)(SKIndexRef inIndex, SKDocumentRef inDocument, void *inContext);
```

## Return Value

A Boolean value of `true` for a successful search hit, or `false` otherwise.

## Discussion

Deprecated. Defines a pointer to a search-results filtering callback function for hit testing and processing during a search. Use this callback function to perform custom filtering on the search hits returned by the [`SKSearchResultsCreateWithQuery`](./api-1448610-sksearchresultscreatewithquery.md) and [`SKSearchResultsCreateWithDocuments`](./api-1448629-sksearchresultscreatewithdocumen.md) functions. Return `true` to keep this document URL object (SKDocumentRef) in the results, `false` to filter it out.

## Parameters

- `inIndex`: The index you are searching.
- `inDocument`: The document URL object within the index you are searching.
- `inContext`: An application-specified context which you set when calling [`SKSearchResultsCreateWithQuery`](./api-1448610-sksearchresultscreatewithquery.md) or [`SKSearchResultsCreateWithDocuments`](./api-1448629-sksearchresultscreatewithdocumen.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/sksearchresultsfiltercallback)*