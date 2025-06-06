# MDQueryCopyValuesOfAttribute(_:_:)

**Framework**: Core Services  
**Kind**: func

Returns the list of values from the results of the query for the specified attribute.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDQueryCopyValuesOfAttribute(_ query: MDQuery!, _ name: CFString!) -> CFArray!
```

#### Return_value

A CFArrayRef containing the value objects for the specified attribute. The array contents are not ordered and contain only one occurrence of each value. The array contents may change over time if the query is configured for live-updates.

## Parameters

- `query`: The query.
- `name`: The attribute name to return the value of. If the attribute is not one of those requested when the query was created the behavior is undefined

## See Also

- [func MDQueryGetAttributeValueOfResultAtIndex(MDQuery!, CFString!, CFIndex) -> UnsafeMutableRawPointer!](1413046-mdquerygetattributevalueofresult.md)
  Returns the value of the named attribute for the result at the given index.
- [func MDQueryGetCountOfResultsWithAttributeValue(MDQuery!, CFString!, CFTypeRef!) -> CFIndex](1413009-mdquerygetcountofresultswithattr.md)
  Returns the number of results which have the given attribute and attribute value.
- [func MDQueryGetIndexOfResult(MDQuery!, UnsafeRawPointer!) -> CFIndex](1413093-mdquerygetindexofresult.md)
  Returns the current index of the given result.
- [func MDQueryGetResultAtIndex(MDQuery!, CFIndex) -> UnsafeRawPointer!](1413055-mdquerygetresultatindex.md)
  Returns the current result at the given index.
- [func MDQueryGetResultCount(MDQuery!) -> CFIndex](1413008-mdquerygetresultcount.md)
  Returns the number of results currently collected by the query. 
- [func MDQuerySetSortComparatorBlock(MDQuery!, ((UnsafePointer<Unmanaged<CFTypeRef>?>?, UnsafePointer<Unmanaged<CFTypeRef>?>?) -> CFComparisonResult)!)](1413021-mdquerysetsortcomparatorblock.md)
  Sets the block used to sort the results of an MDQuery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413105-mdquerycopyvaluesofattribute)*