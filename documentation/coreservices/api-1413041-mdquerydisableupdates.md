# MDQueryDisableUpdates(_:)

**Framework**: Core Services  
**Kind**: func

Disables updates to the query result list.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDQueryDisableUpdates(_ query: MDQuery!)
```

#### Discussion

This function should be called before iterating over query results that could change due to live-updates. The disabled state is a counter and disabling can be done recursively and from different threads.

## Parameters

- `query`: The query.

## See Also

- [func MDQueryExecute(MDQuery!, CFOptionFlags) -> Bool](1413099-mdqueryexecute.md)
  Run the query, and populate the query with the results. 
- [func MDQueryStop(MDQuery!)](1413077-mdquerystop.md)
  Stops the query from generating more results. 
- [func MDQueryEnableUpdates(MDQuery!)](1413066-mdqueryenableupdates.md)
  Enables updates to the query result list.
- [func MDQueryIsGatheringComplete(MDQuery!) -> Bool](1413032-mdqueryisgatheringcomplete.md)
  Returns true if the first phase of a query, the initial result gathering, has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413041-mdquerydisableupdates)*