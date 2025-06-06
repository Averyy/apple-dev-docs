# MDQuerySetMaxCount(_:_:)

**Framework**: Core Services  
**Kind**: func

Sets the maximum number of results returned.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func MDQuerySetMaxCount(_ query: MDQuery!, _ size: CFIndex)
```

#### Discussion

This must be called before the query is executed.

## Parameters

- `query`: The query.
- `size`: The maximum number of return results.

## See Also

- [func MDQueryGetBatchingParameters(MDQuery!) -> MDQueryBatchingParams](1413006-mdquerygetbatchingparameters.md)
  Returns the current parameters that control the batching of progress notifications.
- [func MDQuerySetBatchingParameters(MDQuery!, MDQueryBatchingParams)](1413103-mdquerysetbatchingparameters.md)
  Set the query batching parameters.
- [func MDQueryCopyValueListAttributes(MDQuery!) -> CFArray!](1413071-mdquerycopyvaluelistattributes.md)
  Returns the list of attribute names for which values are being collected by the query.
- [func MDQueryCopySortingAttributes(MDQuery!) -> CFArray!](1413059-mdquerycopysortingattributes.md)
  Returns the list of attribute names used to sort the results.
- [func MDQueryCopyQueryString(MDQuery!) -> CFString!](1413004-mdquerycopyquerystring.md)
  Returns the query string of the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413085-mdquerysetmaxcount)*