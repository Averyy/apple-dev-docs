# MDQueryCopyQueryString(_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the query string of the query.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDQueryCopyQueryString(_ query: MDQuery!) -> CFString!
```

```c
CFStringRef MDQueryCopyQueryString(MDQueryRef query);
```

## Return Value

A CFStringRef containing the query string.

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
- [func MDQueryCopyValueListAttributes(MDQuery!) -> CFArray!](./api-1413071-mdquerycopyvaluelistattributes.md)
  Returns the list of attribute names for which values are being collected by the query.
- [func MDQueryCopySortingAttributes(MDQuery!) -> CFArray!](./api-1413059-mdquerycopysortingattributes.md)
  Returns the list of attribute names used to sort the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413004-mdquerycopyquerystring)*