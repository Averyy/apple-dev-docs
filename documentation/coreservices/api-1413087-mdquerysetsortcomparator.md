# MDQuerySetSortComparator(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Sets the function used to sort the results of an MDQuery.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDQuerySetSortComparator(_ query: MDQuery!, _ comparator: MDQuerySortComparatorFunction!, _ context: UnsafeMutableRawPointer!)
```

## Parameters

- `query`: The query.
- `comparator`: The callback function the MDQuery uses to sort the results list. This parameter may be   which cancels previous sort comparator settings. If a function is specified and is not of type   or does not behave as a   must, the behavior is undefined.
- `context`: A pointer-sized user-defined value, that is passed as the third parameter to the create function. MDQuery does not use this value, does not retain the context in any way, and requires that the context be valid for the lifetime of the query. If the context is not what is expected by the create function, the behavior is undefined.

## See Also

- [func MDQuerySetCreateResultFunction(MDQuery!, MDQueryCreateResultFunction!, UnsafeMutableRawPointer!, UnsafePointer<CFArrayCallBacks>!)](1413064-mdquerysetcreateresultfunction.md)
  Sets the function used to create the result objects of the MDQuery.
- [func MDQuerySetCreateValueFunction(MDQuery!, MDQueryCreateValueFunction!, UnsafeMutableRawPointer!, UnsafePointer<CFArrayCallBacks>!)](1413017-mdquerysetcreatevaluefunction.md)
  Sets the function used to create the value objects of the MDQuery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413087-mdquerysetsortcomparator)*