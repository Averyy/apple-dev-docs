# SKSearchResultsCreateWithDocuments

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Finds documents similar to given example documents.

**Availability**:
- macOS 10.3+ - Deprecated in 10.4

> **Deprecated**: Use [`SKSearchCreate`](./api-1443079-sksearchcreate.md) instead.

## Declaration

```c
SKSearchResultsRef SKSearchResultsCreateWithDocuments(SKSearchGroupRef inSearchGroup, CFArrayRef inExampleDocuments, CFIndex inMaxFoundDocuments, void *inContext, SKSearchResultsFilterCallBack inFilterCallBack);
```

#### Return Value

A search results object containing a list of document URL objects (SKDocumentRefs) representing documents similar to the example documents.

#### Discussion

This function searches the on-disk indexes in a search group for document URL objects (SKDocumentRefs) representing documents similar to those provided as examples. Build the search group in three steps:

1. Collect the index IDs from the search groups you want to search: for each search group, call the [`SKSearchGroupCopyIndexes`](./api-1448615-sksearchgroupcopyindexes.md) function.
2. Add the document URL objects representing the example documents to a memory-based index (if they’re not already in an index) by calling [`SKIndexCreateWithMutableData`](./api-1447500-skindexcreatewithmutabledata.md), and get that index’s ID.
3. Create a new search group that contains the indexes to search, and also containing the example-documents index, using [`SKSearchGroupCreate`](./api-1448627-sksearchgroupcreate.md).

Before invoking a search, call [`SKIndexFlush`](./api-1450667-skindexflush.md) on all indexes in the search group to ensure that changes to the indexes have been written to disk.

Once you’ve obtained the results of a search, get the specifics—including which documents match the user’s similarity query, and the ranking scores for each document—by calling [`SKSearchResultsGetInfoInRange`](./api-1448618-sksearchresultsgetinfoinrange.md).

When your application no longer needs the search result, dispose of it by calling [`CFRelease`](../CoreFoundation/cfrelease.md).

## Parameters

- `inSearchGroup`: A search group containing the indexes which, in turn, contain the document URL objects (SKDocumentRefs) representing the documents you want to search by similarity. The search group must also contains the indexes that contain the textual content of the example documents.
- `inExampleDocuments`: An array of document URL objects (SKDocumentRefs), each representing an example document.
- `inMaxFoundDocuments`: The maximum number of found items to return. Your application must pass in a positive value.
- `inContext`: An application-specified context for use by the [`SKSearchResultsFilterCallBack`](./sksearchresultsfiltercallback.md) callback function. Can be `NULL`.
- `inFilterCallBack`: A callback function for hit testing during searching—see [`SKSearchResultsFilterCallBack`](./sksearchresultsfiltercallback.md). In a similarity search, your application would typically use this function to exclude the example documents from the search results. This parameter can be `NULL`, in which case your application receives the returned results directly and without any custom postprocessing.

## See Also

### Legacy Support for Synchronous Searching
- [SKSearchGroupCreate](./api-1448627-sksearchgroupcreate.md)
  Creates a search group as an array of references to indexes.
- [SKSearchGroupCopyIndexes](./api-1448615-sksearchgroupcopyindexes.md)
  Obtains the indexes for a search group.
- [SKSearchGroupGetTypeID](./api-1448637-sksearchgroupgettypeid.md)
  Deprecated. Use asynchronous searching with SKSearchCreate instead, which does not employ search groups.
- [SKSearchResultsGetInfoInRange](./api-1448618-sksearchresultsgetinfoinrange.md)
  Extracts information from a Search Kit query result.
- [SKSearchResultsCopyMatchingTerms](./api-1448612-sksearchresultscopymatchingterms.md)
  Obtains the terms in a document that match a query.
- [SKSearchResultsGetCount](./api-1448598-sksearchresultsgetcount.md)
  Gets the total number of found items in a search.
- [SKSearchResultsGetTypeID](./api-1448603-sksearchresultsgettypeid.md)
  Gets the type identifier for Search Kit search results.
- [SKSearchResultsCreateWithQuery](./api-1448610-sksearchresultscreatewithquery.md)
  Queries the indexes in a search group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448629-sksearchresultscreatewithdocumen)*