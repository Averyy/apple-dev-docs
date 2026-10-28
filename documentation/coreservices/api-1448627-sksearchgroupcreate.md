# SKSearchGroupCreate

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a search group as an array of references to indexes.

**Availability**:
- macOS 10.3+ - Deprecated in 10.4

> **Deprecated**: Use asynchronous searching with SKSearchCreate instead, which does not employ search groups.

## Declaration

```c
SKSearchGroupRef SKSearchGroupCreate(CFArrayRef inArrayOfInIndexes);
```

## Return Value

An SKSearchGroup opaque type.

## Discussion

Creates a search group as an array of references to indexes.

You create a search group to search one or more indexes, and then typically use the resulting `SKSearchGroupRef` opaque type with [`SKSearchResultsCreateWithQuery`](./api-1448610-sksearchresultscreatewithquery.md) or [`SKSearchResultsCreateWithDocuments`](./api-1448629-sksearchresultscreatewithdocumen.md).

When your application no longer needs the search group, dispose of it by calling [`CFRelease`](../CoreFoundation/cfrelease.md).

## Parameters

- `inArrayOfInIndexes`: A CFArray object containing the indexes to put into the search group.

## See Also

### Legacy Support for Synchronous Searching
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
- [SKSearchResultsCreateWithQuery](./api-1448610-sksearchresultscreatewithquery.md)
  Queries the indexes in a search group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448627-sksearchgroupcreate)*