# SKSearchResultsRef

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Deprecated. Use asynchronous searching with SKSearchCreate instead, which does not employ search groups.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
typedef struct __SKSearchResults *SKSearchResultsRef;
```

#### Discussion

Defines an opaque data type representing the result of a search. To perform a query and generate search results, use [`SKSearchResultsCreateWithQuery`](./api-1448610-sksearchresultscreatewithquery.md) or [`SKSearchResultsCreateWithDocuments`](./api-1448629-sksearchresultscreatewithdocumen.md). To examine the result of a search, use [`SKSearchResultsGetInfoInRange`](./api-1448618-sksearchresultsgetinfoinrange.md). For other operations on search results, see [Legacy Support for Synchronous Searching](./search_kit.md#1655799).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/sksearchresultsref)*