# MDQueryCopyValueListAttributes(_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the list of attribute names for which values are being collected by the query.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDQueryCopyValueListAttributes(_ query: MDQuery!) -> CFArray!
```

```c
CFArrayRef MDQueryCopyValueListAttributes(MDQueryRef query);
```

#### Return Value

A CFArrayRef containing the attribute names of the collected values.

## Parameters

- `query`: The query.

## See Also

### Getting and Setting Query Parameters
- [func MDQuerySetMaxCount(MDQuery!, CFIndex)](./api-1413085-mdquerysetmaxcount.md)
  Sets the maximum number of results returned.
- [func MDQueryGetBatchingParameters(MDQuery!) -> MDQueryBatchingParams](./api-1413006-mdquerygetbatchingparameters.md)
  Returns the current parameters that control the batching of progress notifications.
- [func MDQuerySetBatchingParameters(MDQuery!, MDQueryBatchingParams)](./api-1413103-mdquerysetbatchingparameters.md)
  Set the query batching parameters.
- [func MDQueryCopySortingAttributes(MDQuery!) -> CFArray!](./api-1413059-mdquerycopysortingattributes.md)
  Returns the list of attribute names used to sort the results.
- [func MDQueryCopyQueryString(MDQuery!) -> CFString!](./api-1413004-mdquerycopyquerystring.md)
  Returns the query string of the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413071-mdquerycopyvaluelistattributes)*