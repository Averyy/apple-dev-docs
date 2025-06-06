# MDQueryIsGatheringComplete(_:)

**Framework**: Core Services  
**Kind**: func

Returns true if the first phase of a query, the initial result gathering, has finished.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDQueryIsGatheringComplete(_ query: MDQuery!) -> Bool
```

#### Return_value

Returns `TRUE` if the first phase of a query has completed, otherwise `FALSE`.

## Parameters

- `query`: The query.

## See Also

- [func MDQueryExecute(MDQuery!, CFOptionFlags) -> Bool](1413099-mdqueryexecute.md)
  Run the query, and populate the query with the results. 
- [func MDQueryStop(MDQuery!)](1413077-mdquerystop.md)
  Stops the query from generating more results. 
- [func MDQueryDisableUpdates(MDQuery!)](1413041-mdquerydisableupdates.md)
  Disables updates to the query result list.
- [func MDQueryEnableUpdates(MDQuery!)](1413066-mdqueryenableupdates.md)
  Enables updates to the query result list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413032-mdqueryisgatheringcomplete)*