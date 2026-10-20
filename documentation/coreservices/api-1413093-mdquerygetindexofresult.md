# MDQueryGetIndexOfResult(_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the current index of the given result.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDQueryGetIndexOfResult(_ query: MDQuery!, _ result: UnsafeRawPointer!) -> CFIndex
```

```c
CFIndex MDQueryGetIndexOfResult(MDQueryRef query, const void *result);
```

#### Return Value

The index of the given result, or `kCFNotFound` if the value is not one of the query's existing results. If you provided a custom result creation function result, the result will be objects created by that function.

#### Discussion

If a result-create function has been set, and the equal callback is non-`NULL`, it will be used to test the query's results against the candidate result. 

Note that the index of a result can change over time if the query allows live-updates.

## Parameters

- `query`: The query.
- `result`: The result object to search for. If a custom create-result function has been set and this parameter is not a valid result object that the provided callbacks can handle, the behavior is undefined. If a custom create-result function has not been set this parameter must be a valid MDItemRef.

## See Also

### Getting Query Result Values
- [func MDQueryCopyValuesOfAttribute(MDQuery!, CFString!) -> CFArray!](./api-1413105-mdquerycopyvaluesofattribute.md)
  Returns the list of values from the results of the query for the specified attribute.
- [func MDQueryGetAttributeValueOfResultAtIndex(MDQuery!, CFString!, CFIndex) -> UnsafeMutableRawPointer!](./api-1413046-mdquerygetattributevalueofresult.md)
  Returns the value of the named attribute for the result at the given index.
- [func MDQueryGetCountOfResultsWithAttributeValue(MDQuery!, CFString!, CFTypeRef!) -> CFIndex](./api-1413009-mdquerygetcountofresultswithattr.md)
  Returns the number of results which have the given attribute and attribute value.
- [func MDQueryGetResultAtIndex(MDQuery!, CFIndex) -> UnsafeRawPointer!](./api-1413055-mdquerygetresultatindex.md)
  Returns the current result at the given index.
- [func MDQueryGetResultCount(MDQuery!) -> CFIndex](./api-1413008-mdquerygetresultcount.md)
  Returns the number of results currently collected by the query. 
- [func MDQuerySetSortComparatorBlock(MDQuery!, ((UnsafePointer<Unmanaged<CFTypeRef>?>?, UnsafePointer<Unmanaged<CFTypeRef>?>?) -> CFComparisonResult)!)](./api-1413021-mdquerysetsortcomparatorblock.md)
  Sets the block used to sort the results of an MDQuery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413093-mdquerygetindexofresult)*