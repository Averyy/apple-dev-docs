# MDQueryStop(_:)

**Framework**: Core Services  
**Kind**: func

Stops the query from generating more results. 

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDQueryStop(_ query: MDQuery!)
```

#### Discussion

Queries may be executed only once and cannot be restarted. The query will first complete processing any unprocessed results.do. That may trigger a progress notification, so be aware of that if you are stopping a query from within your progress note handler; that is, during this function, a recursive progress and/or finished notification might occur, which might recursively call your notification handler. It is safe to call this function recursively. You would call this function to stop a query that is generating way too many results to be useful, but still want to access the results that have come in so far. If a query is stopped before the gathering phase finishes, it will not report itself as finished, nor will it send out a finished notification.

## Parameters

- `query`: The query.

## See Also

- [func MDQueryExecute(MDQuery!, CFOptionFlags) -> Bool](1413099-mdqueryexecute.md)
  Run the query, and populate the query with the results. 
- [func MDQueryDisableUpdates(MDQuery!)](1413041-mdquerydisableupdates.md)
  Disables updates to the query result list.
- [func MDQueryEnableUpdates(MDQuery!)](1413066-mdqueryenableupdates.md)
  Enables updates to the query result list.
- [func MDQueryIsGatheringComplete(MDQuery!) -> Bool](1413032-mdqueryisgatheringcomplete.md)
  Returns true if the first phase of a query, the initial result gathering, has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413077-mdquerystop)*