# MDQueryCopySortingAttributes(_:)

**Framework**: Core Services  
**Kind**: func

Returns the list of attribute names used to sort the results.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDQueryCopySortingAttributes(_ query: MDQuery!) -> CFArray!
```

#### Return_value

A CFArrayRef containing the attribute names used to sort the query results.

## Parameters

- `query`: The query.

## See Also

- [func MDQuerySetMaxCount(MDQuery!, CFIndex)](1413085-mdquerysetmaxcount.md)
  Sets the maximum number of results returned.
- [func MDQueryGetBatchingParameters(MDQuery!) -> MDQueryBatchingParams](1413006-mdquerygetbatchingparameters.md)
  Returns the current parameters that control the batching of progress notifications.
- [func MDQuerySetBatchingParameters(MDQuery!, MDQueryBatchingParams)](1413103-mdquerysetbatchingparameters.md)
  Set the query batching parameters.
- [func MDQueryCopyValueListAttributes(MDQuery!) -> CFArray!](1413071-mdquerycopyvaluelistattributes.md)
  Returns the list of attribute names for which values are being collected by the query.
- [func MDQueryCopyQueryString(MDQuery!) -> CFString!](1413004-mdquerycopyquerystring.md)
  Returns the query string of the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413059-mdquerycopysortingattributes)*