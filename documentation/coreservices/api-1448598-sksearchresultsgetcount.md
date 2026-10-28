# SKSearchResultsGetCount

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Gets the total number of found items in a search.

**Availability**:
- macOS 10.3+ - Deprecated in 10.4

> **Deprecated**: Use [`SKSearchCreate`](./api-1443079-sksearchcreate.md) instead.

## Declaration

```c
CFIndex SKSearchResultsGetCount(SKSearchResultsRef inSearchResults);
```

## Return Value

A CFIndex object containing the total number of found items in a search.

## Parameters

- `inSearchResults`: A search results object containing the results of a query.

## See Also

### Legacy Support for Synchronous Searching
- [SKSearchGroupCreate](./api-1448627-sksearchgroupcreate.md)
  Creates a search group as an array of references to indexes.
- [SKSearchGroupCopyIndexes](./api-1448615-sksearchgroupcopyindexes.md)
  Obtains the indexes for a search group.
- [SKSearchGroupGetTypeID](./api-1448637-sksearchgroupgettypeid.md)
  Deprecated. Use asynchronous searching with SKSearchCreate instead, which does not employ search groups.
- [SKSearchResultsCreateWithDocuments](./api-1448629-sksearchresultscreatewithdocumen.md)
  Finds documents similar to given example documents.
- [SKSearchResultsGetInfoInRange](./api-1448618-sksearchresultsgetinfoinrange.md)
  Extracts information from a Search Kit query result.
- [SKSearchResultsCopyMatchingTerms](./api-1448612-sksearchresultscopymatchingterms.md)
  Obtains the terms in a document that match a query.
- [SKSearchResultsGetTypeID](./api-1448603-sksearchresultsgettypeid.md)
  Gets the type identifier for Search Kit search results.
- [SKSearchResultsCreateWithQuery](./api-1448610-sksearchresultscreatewithquery.md)
  Queries the indexes in a search group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448598-sksearchresultsgetcount)*