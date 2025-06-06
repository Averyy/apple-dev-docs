# MDQuerySetSortComparatorBlock(_:_:)

**Framework**: Core Services  
**Kind**: func

Sets the block used to sort the results of an MDQuery.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func MDQuerySetSortComparatorBlock(_ query: MDQuery!, _ comparator: ((UnsafePointer<Unmanaged<CFTypeRef>?>?, UnsafePointer<Unmanaged<CFTypeRef>?>?) -> CFComparisonResult)!)
```

#### Discussion

You may set the comparator block as many times as you like, even while the query is executing. Whenever the comparator block is set, all results are re-sorted using the new comparator block before the function returns. The block can be NULL to cancel custom sorting and revert to the default sorting.

The default sort provided by [`MDQueryCreate(_:_:_:_:)`](1413029-mdquerycreate.md) is an ascending sort. Strings are compared using [`CFStringCompare(_:_:_:)`](https://developer.apple.com/documentation/corefoundation/cfstringcompare(_:_:_:)) with the options [`compareNonliteral`](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/comparenonliteral) | [`compareLocalized`](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/comparelocalized) | [`compareNumerically`](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/comparenumerically). `CFDataRefs` are compared by using `memcmp()` of the data pointers.

## Parameters

- `query`: The query.
- `comparator`: The block may be   to cancel any custom comparator. 

## See Also

- [func MDQueryCopyValuesOfAttribute(MDQuery!, CFString!) -> CFArray!](1413105-mdquerycopyvaluesofattribute.md)
  Returns the list of values from the results of the query for the specified attribute.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413021-mdquerysetsortcomparatorblock)*