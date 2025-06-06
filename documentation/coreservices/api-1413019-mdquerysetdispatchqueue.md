# MDQuerySetDispatchQueue(_:_:)

**Framework**: Core Services  
**Kind**: func

Sets the dispatch queue on which query results will be delivered by MDQueryExecute.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func MDQuerySetDispatchQueue(_ query: MDQuery!, _ queue: dispatch_queue_t!)
```

#### Discussion

It is not advisable to change set dispatch queue after [`MDQueryExecute(_:_:)`](1413099-mdqueryexecute.md) has been called with the query. 

Setting the dispatch queue for a synchronous query ([`kMDQuerySynchronous`](kmdquerysynchronous.md)) has no effect.

## Parameters

- `query`: The query.
- `queue`: The dispatch queue on which results should be delivered.

## See Also

- [func MDQueryCreate(CFAllocator!, CFString!, CFArray!, CFArray!) -> MDQuery!](1413029-mdquerycreate.md)
  Creates a new query instance.
- [func MDQueryCreateSubset(CFAllocator!, MDQuery!, CFString!, CFArray!, CFArray!) -> MDQuery!](1413027-mdquerycreatesubset.md)
  Creates a new query that is a subset of the specified parentquery.
- [func MDQuerySetSearchScope(MDQuery!, CFArray!, OptionBits)](1413048-mdquerysetsearchscope.md)
  Sets the search scope for a query instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413019-mdquerysetdispatchqueue)*