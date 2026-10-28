# SKSearchGroupCopyIndexes

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Obtains the indexes for a search group.

**Availability**:
- macOS 10.3+ - Deprecated in 10.4

> **Deprecated**: Use asynchronous searching with SKSearchCreate instead, which does not employ search groups.

## Declaration

```c
CFArrayRef SKSearchGroupCopyIndexes(SKSearchGroupRef inSearchGroup);
```

## Return Value

A CFArray object containing the indexes in the search group.

## Discussion

Although the search functions [`SKSearchResultsCreateWithQuery`](./api-1448610-sksearchresultscreatewithquery.md) and [`SKSearchResultsCreateWithDocuments`](./api-1448629-sksearchresultscreatewithdocumen.md) operate directly on search groups, many Search Kit functions, such as [`SKIndexCompact`](./api-1443628-skindexcompact.md), operate on one index at a time. When you want to examine or manage all the indexes in a search group, use `SKSearchGroupCopyIndexes` to get the search group’s list of indexes.

## Parameters

- `inSearchGroup`: The search group whose indexes you want to copy.

## See Also

### Legacy Support for Synchronous Searching
- [SKSearchGroupCreate](./api-1448627-sksearchgroupcreate.md)
  Creates a search group as an array of references to indexes.
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
- [SKSearchResultsCreateWithQuery](./api-1448610-sksearchresultscreatewithquery.md)
  Queries the indexes in a search group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448615-sksearchgroupcopyindexes)*