# MDQuerySetSortComparatorBlock(_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Sets the block used to sort the results of an MDQuery.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func MDQuerySetSortComparatorBlock(_ query: MDQuery!, _ comparator: ((UnsafePointer<Unmanaged<CFTypeRef>?>?, UnsafePointer<Unmanaged<CFTypeRef>?>?) -> CFComparisonResult)!)
```

```c
void MDQuerySetSortComparatorBlock(MDQueryRef query, CFComparisonResult (^comparator)(const CFTypeRef attrs1[], const CFTypeRef attrs2[]));
```

#### Discussion

You may set the comparator block as many times as you like, even while the query is executing. Whenever the comparator block is set, all results are re-sorted using the new comparator block before the function returns. The block can be NULL to cancel custom sorting and revert to the default sorting.

The default sort provided by [`MDQueryCreate(_:_:_:_:)`](./api-1413029-mdquerycreate.md) is an ascending sort. Strings are compared using [`CFStringCompare(_:_:_:)`](../CoreFoundation/cfstringcompare%28_,_,_%29.md) with the options [`compareNonliteral`](../CoreFoundation/cfstringcompareflags/comparenonliteral.md) | [`compareLocalized`](../CoreFoundation/cfstringcompareflags/comparelocalized.md) | [`compareNumerically`](../CoreFoundation/cfstringcompareflags/comparenumerically.md). `CFDataRefs` are compared by using `memcmp()` of the data pointers.

## Parameters

- `query`: The query.
- `comparator`: The callback block the MDQuery will use to sort its results. The comparator may be called on multiple threads in parallel, and must be reentrant. To take advantage of parallel sorting, it is best to avoid any locking in the comparator.

  The block may be `NULL` to cancel any custom comparator. 

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
- [func MDQueryGetResultCount(MDQuery!) -> CFIndex](./api-1413008-mdquerygetresultcount.md)
  Returns the number of results currently collected by the query. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413021-mdquerysetsortcomparatorblock)*