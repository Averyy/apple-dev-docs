# SKSearchResultsCreateWithQuery

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Queries the indexes in a search group.

**Availability**:
- macOS 10.3+ - Deprecated in 10.4

> **Deprecated**: Use [`SKSearchCreate`](./api-1443079-sksearchcreate.md) instead.

## Declaration

```c
SKSearchResultsRef SKSearchResultsCreateWithQuery(SKSearchGroupRef inSearchGroup, CFStringRef inQuery, SKSearchType inSearchType, CFIndex inMaxFoundDocuments, void *inContext, SKSearchResultsFilterCallBack inFilterCallBack);
```

## Return Value

A search results object.

## Discussion

This function searches the on-disk indexes in a search group. Before invoking a search, call [`SKIndexFlush`](./api-1450667-skindexflush.md) on all indexes in the search group to ensure that changes to the indexes have been flushed to disk.

Once you’ve obtained the results of a search, get the specifics—including which documents match the user’s query, and the ranking scores for each document—by calling [`SKSearchResultsGetInfoInRange`](./api-1448618-sksearchresultsgetinfoinrange.md). You can extract other information by calling [`SKSearchResultsCopyMatchingTerms`](./api-1448612-sksearchresultscopymatchingterms.md) and [`SKSearchResultsGetCount`](./api-1448598-sksearchresultsgetcount.md).

When your application no longer needs the search result, dispose of it by calling [`CFRelease`](../CoreFoundation/cfrelease.md).

### Special Considerations

This deprecated function performs searches synchronously. Apple recommends using the asynchronous [`SKSearchCreate`](./api-1443079-sksearchcreate.md) function instead.

In the current implementation of Search Kit, unary Boolean operators are not implemented. A search, for example, for ‘not blue’, returns zero documents no matter what their content.

## Parameters

- `inSearchGroup`: The search group to query.
- `inQuery`: The query string to search for.
- `inSearchType`: The category of search to perform. See the [`SKSearchType`](./sksearchtype.md) enumeration for options.
- `inMaxFoundDocuments`: The maximum number of found items to return. Your application must pass in a positive integer value.
- `inContext`: An application-specified context for use by the [`SKSearchResultsFilterCallBack`](./sksearchresultsfiltercallback.md). Can be `NULL`, but if you want to use the callback you must supply a context.
- `inFilterCallBack`: A callback function for hit testing during searching. Can be `NULL`, in which case your application receives the returned results directly and without any custom postprocessing. If non-`NULL`, you must supply a context. See [`SKSearchResultsFilterCallBack`](./sksearchresultsfiltercallback.md).

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
- [SKSearchResultsGetCount](./api-1448598-sksearchresultsgetcount.md)
  Gets the total number of found items in a search.
- [SKSearchResultsGetTypeID](./api-1448603-sksearchresultsgettypeid.md)
  Gets the type identifier for Search Kit search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448610-sksearchresultscreatewithquery)*