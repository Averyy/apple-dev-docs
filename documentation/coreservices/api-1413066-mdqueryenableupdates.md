# MDQueryEnableUpdates(_:)

**Framework**: Core Services  
**Kind**: func

Enables updates to the query result list.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDQueryEnableUpdates(_ query: MDQuery!)
```

#### Discussion

This function should be called when finished iterating through the list of results. Live-updates to the query results will continue when all the disables have been matched by a corresponding enable.

## Parameters

- `query`:  The query.

## See Also

- [func MDQueryExecute(MDQuery!, CFOptionFlags) -> Bool](1413099-mdqueryexecute.md)
  Run the query, and populate the query with the results. 
- [func MDQueryStop(MDQuery!)](1413077-mdquerystop.md)
  Stops the query from generating more results. 
- [func MDQueryDisableUpdates(MDQuery!)](1413041-mdquerydisableupdates.md)
  Disables updates to the query result list.
- [func MDQueryIsGatheringComplete(MDQuery!) -> Bool](1413032-mdqueryisgatheringcomplete.md)
  Returns true if the first phase of a query, the initial result gathering, has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413066-mdqueryenableupdates)*