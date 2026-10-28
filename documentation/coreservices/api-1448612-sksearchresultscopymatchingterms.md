# SKSearchResultsCopyMatchingTerms

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Obtains the terms in a document that match a query.

**Availability**:
- macOS 10.3+ - Deprecated in 10.4

> **Deprecated**: Use [`SKSearchCreate`](./api-1443079-sksearchcreate.md) instead.

## Declaration

```c
CFArrayRef SKSearchResultsCopyMatchingTerms(SKSearchResultsRef inSearchResults, CFIndex inItem);
```

## Return Value

A CFArray object containing term IDs.

## Discussion

When using a prefix search, or a search for which the user entered more than one word, there may be multiple terms that match the query. This function returns an array of the term IDs corresponding to these matches.

For example, a user could enter ‘App’ when performing a prefix search. If a document represented in the search group contains the words ‘Apple,’ ‘application,’ and ‘appendectomy,’ the IDs for all of these terms would then appear in the CFArray object that `SKSearchResultsCopyMatchingTerms` returns.

See [`SKSearchResultsCreateWithQuery`](./api-1448610-sksearchresultscreatewithquery.md) for a description of how to perform a search and get search results. See [`SKSearchResultsGetInfoInRange`](./api-1448618-sksearchresultsgetinfoinrange.md) for how to extract information, including document URL objects, from a search result. See [`SKSearchType`](./sksearchtype.md) for a description of the various categories of search.

## Parameters

- `inSearchResults`: The search results to examine.
- `inItem`: An integer that corresponds to a document URL object (SKDocumentRef) in the search results. A value of ‘1’ identifies the first document URL object in the search results, a value of ‘2’ identifies the second, and so on. 

  If you’ve created the search results using [`SKSearchResultsCreateWithQuery`](./api-1448610-sksearchresultscreatewithquery.md), the document URL objects are sorted in ranking order with the top-ranked one first. See [`SKSearchResultsGetInfoInRange`](./api-1448618-sksearchresultsgetinfoinrange.md) for a description of how to get a particular document URL object, or set of them, from a search result.

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
- [SKSearchResultsGetCount](./api-1448598-sksearchresultsgetcount.md)
  Gets the total number of found items in a search.
- [SKSearchResultsGetTypeID](./api-1448603-sksearchresultsgettypeid.md)
  Gets the type identifier for Search Kit search results.
- [SKSearchResultsCreateWithQuery](./api-1448610-sksearchresultscreatewithquery.md)
  Queries the indexes in a search group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448612-sksearchresultscopymatchingterms)*