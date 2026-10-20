# MDQuerySetBatchingParameters(_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Set the query batching parameters.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDQuerySetBatchingParameters(_ query: MDQuery!, _ params: MDQueryBatchingParams)
```

```c
void MDQuerySetBatchingParameters(MDQueryRef query, MDQueryBatchingParams params);
```

## Parameters

- `query`: The query.
- `params`: An MDQueryBatchingParams structure with the batching parameters to set.

## See Also

### Getting and Setting Query Parameters
- [func MDQuerySetMaxCount(MDQuery!, CFIndex)](./api-1413085-mdquerysetmaxcount.md)
  Sets the maximum number of results returned.
- [func MDQueryGetBatchingParameters(MDQuery!) -> MDQueryBatchingParams](./api-1413006-mdquerygetbatchingparameters.md)
  Returns the current parameters that control the batching of progress notifications.
- [func MDQueryCopyValueListAttributes(MDQuery!) -> CFArray!](./api-1413071-mdquerycopyvaluelistattributes.md)
  Returns the list of attribute names for which values are being collected by the query.
- [func MDQueryCopySortingAttributes(MDQuery!) -> CFArray!](./api-1413059-mdquerycopysortingattributes.md)
  Returns the list of attribute names used to sort the results.
- [func MDQueryCopyQueryString(MDQuery!) -> CFString!](./api-1413004-mdquerycopyquerystring.md)
  Returns the query string of the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413103-mdquerysetbatchingparameters)*