# MDQueryGetResultCount(_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the number of results currently collected by the query. 

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDQueryGetResultCount(_ query: MDQuery!) -> CFIndex
```

```c
CFIndex MDQueryGetResultCount(MDQueryRef query);
```

## Return Value

The number of results in the query.

## Discussion

Note that the number of results in a query will change over time as the query's result list is updated.

## Parameters

- `query`: The query.

## See Also

### Getting Query Result Values
- [func MDQueryCopyValuesOfAttribute(MDQuery!, CFString!) -> CFArray!](./api-1413105-mdquerycopyvaluesofattribute.md)
  Returns the list of values from the results of the query for the specified attribute.
- [func MDQueryGetAttributeValueOfResultAtIndex(MDQuery!, CFString!, CFIndex) -> UnsafeMutableRawPointer!](./api-1413046-mdquerygetattributevalueofresult.md)
  Returns the value of the named attribute for the result at the given index.
- [func MDQueryGetCountOfResultsWithAttributeValue(MDQuery!, CFString!, CFTypeRef!) -> CFIndex](./api-1413009-mdquerygetcountofresultswithattr.md)
  Returns the number of results which have the given attribute and attribute value.
- [func MDQueryGetIndexOfResult(MDQuery!, UnsafeRawPointer!) -> CFIndex](./api-1413093-mdquerygetindexofresult.md)
  Returns the current index of the given result.
- [func MDQueryGetResultAtIndex(MDQuery!, CFIndex) -> UnsafeRawPointer!](./api-1413055-mdquerygetresultatindex.md)
  Returns the current result at the given index.
- [func MDQuerySetSortComparatorBlock(MDQuery!, ((UnsafePointer<Unmanaged<CFTypeRef>?>?, UnsafePointer<Unmanaged<CFTypeRef>?>?) -> CFComparisonResult)!)](./api-1413021-mdquerysetsortcomparatorblock.md)
  Sets the block used to sort the results of an MDQuery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413008-mdquerygetresultcount)*