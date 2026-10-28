# SKSearchGroupGetTypeID

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Deprecated. Use asynchronous searching with SKSearchCreate instead, which does not employ search groups.

**Availability**:
- macOS 10.3+ - Deprecated in 10.4

## Declaration

```c
CFTypeID SKSearchGroupGetTypeID(void);
```

## Return Value

A CFTypeID object containing the type identifier for the SKSearchGroup opaque type.

## Discussion

Gets the type identifier for Search Kit search groups.

Search Kit represents search groups with the [`SKSearchGroupRef`](./sksearchgroupref.md) opaque type. If your code needs to determine whether a particular data type is a search group, you can use this function along with the [`CFGetTypeID(_:)`](../CoreFoundation/cfgettypeid%28_%29.md) function and perform a comparison.

Never hard-code the search group type ID because it can change from one release of macOS to another.

## See Also

### Legacy Support for Synchronous Searching
- [SKSearchGroupCreate](./api-1448627-sksearchgroupcreate.md)
  Creates a search group as an array of references to indexes.
- [SKSearchGroupCopyIndexes](./api-1448615-sksearchgroupcopyindexes.md)
  Obtains the indexes for a search group.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448637-sksearchgroupgettypeid)*