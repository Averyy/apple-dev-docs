# SKSearchResultsGetTypeID

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Gets the type identifier for Search Kit search results.

**Availability**:
- macOS 10.3+ - Deprecated in 10.4

> **Deprecated**: Use [`SKSearchCreate`](./api-1443079-sksearchcreate.md) instead.

## Declaration

```c
CFTypeID SKSearchResultsGetTypeID(void);
```

## Return Value

A CFTypeID object containing the type identifier for the SKSearchResults opaque type.

## Discussion

Search Kit represents search results with search results objects ([`SKSearchResultsRef`](./sksearchresultsref.md) opaque types). If your code needs to determine whether a particular data type is a search result, you can use this function along with the [`CFGetTypeID(_:)`](../CoreFoundation/cfgettypeid%28_%29.md) function and perform a comparison.

Never hard-code the search result type ID because it can change from one release of macOS to another.

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
- [SKSearchResultsCreateWithQuery](./api-1448610-sksearchresultscreatewithquery.md)
  Queries the indexes in a search group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448603-sksearchresultsgettypeid)*