# MDQueryGetResultAtIndex(_:_:)

**Framework**: Core Services  
**Kind**: func

Returns the current result at the given index.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDQueryGetResultAtIndex(_ query: MDQuery!, _ idx: CFIndex) -> UnsafeRawPointer!
```

#### Return_value

Returns the MDItemRef currently at the given index, or if a result-creation function has been set, returns the result returned by that function.

#### Discussion

This function causes the result object to be created if it hasn't been created already. For performance reasons you should only request objects that you require. If possible, call this function to fetch only the results you need to display or otherwise process. 

Note that the index of a particular result can change over time if the query is configured to allow live-updates.

## Parameters

- `query`: The query.
- `idx`: The index into the query's result list. If the index is negative, or is equal to or larger than the current number of results in the query, the behavior is undefined.

## See Also

- [func MDQueryCopyValuesOfAttribute(MDQuery!, CFString!) -> CFArray!](1413105-mdquerycopyvaluesofattribute.md)
  Returns the list of values from the results of the query for the specified attribute.
- [func MDQueryGetAttributeValueOfResultAtIndex(MDQuery!, CFString!, CFIndex) -> UnsafeMutableRawPointer!](1413046-mdquerygetattributevalueofresult.md)
  Returns the value of the named attribute for the result at the given index.
- [func MDQueryGetCountOfResultsWithAttributeValue(MDQuery!, CFString!, CFTypeRef!) -> CFIndex](1413009-mdquerygetcountofresultswithattr.md)
  Returns the number of results which have the given attribute and attribute value.
- [func MDQueryGetIndexOfResult(MDQuery!, UnsafeRawPointer!) -> CFIndex](1413093-mdquerygetindexofresult.md)
  Returns the current index of the given result.
- [func MDQueryGetResultCount(MDQuery!) -> CFIndex](1413008-mdquerygetresultcount.md)
  Returns the number of results currently collected by the query. 
- [func MDQuerySetSortComparatorBlock(MDQuery!, ((UnsafePointer<Unmanaged<CFTypeRef>?>?, UnsafePointer<Unmanaged<CFTypeRef>?>?) -> CFComparisonResult)!)](1413021-mdquerysetsortcomparatorblock.md)
  Sets the block used to sort the results of an MDQuery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413055-mdquerygetresultatindex)*