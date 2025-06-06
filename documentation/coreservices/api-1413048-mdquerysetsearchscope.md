# MDQuerySetSearchScope(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Sets the search scope for a query instance.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDQuerySetSearchScope(_ query: MDQuery!, _ scopeDirectories: CFArray!, _ scopeOptions: OptionBits)
```

#### Discussion

## Parameters

- `query`: The query object to modify.
- `scopeDirectories`: A CFArray of CFStringRef or CFURLRef objects which specify where to search. For convenience the  ,   and   constants may also be included in the array.
- `scopeOptions`: Additional options for modifying the search. Currently you must pass 0.

## See Also

- [func MDQueryCreate(CFAllocator!, CFString!, CFArray!, CFArray!) -> MDQuery!](1413029-mdquerycreate.md)
  Creates a new query instance.
- [func MDQueryCreateSubset(CFAllocator!, MDQuery!, CFString!, CFArray!, CFArray!) -> MDQuery!](1413027-mdquerycreatesubset.md)
  Creates a new query that is a subset of the specified parentquery.
- [func MDQuerySetDispatchQueue(MDQuery!, dispatch_queue_t!)](1413019-mdquerysetdispatchqueue.md)
  Sets the dispatch queue on which query results will be delivered by MDQueryExecute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413048-mdquerysetsearchscope)*