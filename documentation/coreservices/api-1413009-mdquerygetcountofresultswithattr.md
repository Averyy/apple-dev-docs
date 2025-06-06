# MDQueryGetCountOfResultsWithAttributeValue(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Returns the number of results which have the given attribute and attribute value.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDQueryGetCountOfResultsWithAttributeValue(_ query: MDQuery!, _ name: CFString!, _ value: CFTypeRef!) -> CFIndex
```

#### Return_value

The number of results containing that attribute and value.

#### Discussion

This count may change over time if the query allows live-updates.

## Parameters

- `query`: The query.
- `name`: The attribute name to return the result count of. If the attribute is not one of those requested in the   parameter, the behavior is undefined.
- `value`: The attribute value for which to return the number of results with that value. This parameter may be  , in which case the number of results that do not contain the specified attribute is returned.

## See Also

- [func MDQueryCopyValuesOfAttribute(MDQuery!, CFString!) -> CFArray!](1413105-mdquerycopyvaluesofattribute.md)
  Returns the list of values from the results of the query for the specified attribute.
- [func MDQueryGetAttributeValueOfResultAtIndex(MDQuery!, CFString!, CFIndex) -> UnsafeMutableRawPointer!](1413046-mdquerygetattributevalueofresult.md)
  Returns the value of the named attribute for the result at the given index.
- [func MDQueryGetIndexOfResult(MDQuery!, UnsafeRawPointer!) -> CFIndex](1413093-mdquerygetindexofresult.md)
  Returns the current index of the given result.
- [func MDQueryGetResultAtIndex(MDQuery!, CFIndex) -> UnsafeRawPointer!](1413055-mdquerygetresultatindex.md)
  Returns the current result at the given index.
- [func MDQueryGetResultCount(MDQuery!) -> CFIndex](1413008-mdquerygetresultcount.md)
  Returns the number of results currently collected by the query. 
- [func MDQuerySetSortComparatorBlock(MDQuery!, ((UnsafePointer<Unmanaged<CFTypeRef>?>?, UnsafePointer<Unmanaged<CFTypeRef>?>?) -> CFComparisonResult)!)](1413021-mdquerysetsortcomparatorblock.md)
  Sets the block used to sort the results of an MDQuery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413009-mdquerygetcountofresultswithattr)*