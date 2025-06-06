# MDQueryGetAttributeValueOfResultAtIndex(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Returns the value of the named attribute for the result at the given index.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDQueryGetAttributeValueOfResultAtIndex(_ query: MDQuery!, _ name: CFString!, _ idx: CFIndex) -> UnsafeMutableRawPointer!
```

#### Return_value

The value of the attribute, or `NULL` if the attribute doesn't exist for the specified result.

## Parameters

- `query`: The query.
- `name`: The attribute name to return the values of. If the attribute is not one of those requested in the   or   parameters to one of the query creation functions, the result will be  .
- `idx`: The index into the query's result list. If the index is negative or is equal to or larger than the current number of results in the query, the behavior is undefined.

## See Also

- [func MDQueryCopyValuesOfAttribute(MDQuery!, CFString!) -> CFArray!](1413105-mdquerycopyvaluesofattribute.md)
  Returns the list of values from the results of the query for the specified attribute.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413046-mdquerygetattributevalueofresult)*