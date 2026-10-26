# SKSearchResultsGetInfoInRange

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Extracts information from a Search Kit query result.

**Availability**:
- macOS 10.3+ - Deprecated in 10.4

> **Deprecated**: Use [`SKSearchCreate`](./api-1443079-sksearchcreate.md) instead.

## Declaration

```c
CFIndex SKSearchResultsGetInfoInRange(SKSearchResultsRef inSearchResults, CFRange inRange, SKDocumentRef *outDocumentsArray, SKIndexRef *outIndexesArray, float *outScoresArray);
```

#### Return Value

The number of items returned—usually the same number as specified by the length item in the `inRange` parameter.

#### Discussion

This function provides results to its output parameters in the order in which they are found, to reduce latency and to support search-as-you-type functionality.

## Parameters

- `inSearchResults`: The search results whose information you want to extract.
- `inRange`: The starting ranking and total number of found items to obtain, specified as `(Location, Length)`. ‘Location’ specifies the starting item by ranking, with the top-ranked item having a location of 0. ‘Length’ specifies the total number of items to include in the results. For example, (0,1) indicates the first item, which is also the highest-ranking item. (1,1) indicates the second item, which is also the second-highest-ranking item. (0,5) means to get the first 5 items.
- `outDocumentsArray`: On output, points to an array of found document URL objects (SKDocumentRefs).
- `outIndexesArray`: On output, points to an array of indexes in which the found document URL objects reside. Can be `NULL` on input, provided that your application doesn’t need this information.
- `outScoresArray`: On output, points to an array of correspondence scores for found items. Can be `NULL` on input, provided that your application doesn’t need this information.

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
- [SKSearchResultsCopyMatchingTerms](./api-1448612-sksearchresultscopymatchingterms.md)
  Obtains the terms in a document that match a query.
- [SKSearchResultsGetCount](./api-1448598-sksearchresultsgetcount.md)
  Gets the total number of found items in a search.
- [SKSearchResultsGetTypeID](./api-1448603-sksearchresultsgettypeid.md)
  Gets the type identifier for Search Kit search results.
- [SKSearchResultsCreateWithQuery](./api-1448610-sksearchresultscreatewithquery.md)
  Queries the indexes in a search group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448618-sksearchresultsgetinfoinrange)*