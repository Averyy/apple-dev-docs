# Query Result Change Keys

**Framework**: Core Services  
**Role**: API Collection

Specify the items that have changed in the query results.

## Topics

### Constants
- [let kMDQueryUpdateAddedItems: CFString!](../../kmdqueryupdateaddeditems.md)
  An array that identifies the items that have been added to the query results. This list only contains result objects that have previously been created, result objects that have not been created are not included.
- [let kMDQueryUpdateChangedItems: CFString!](../../kmdqueryupdatechangeditems.md)
  An array that identifies the items that have changed in the query results. This list only contains result objects that have previously been created, result objects that have not been created are not included.
- [let kMDQueryUpdateRemovedItems: CFString!](../../kmdqueryupdateremoveditems.md)
  An array that identifies the items that have been removed from the query results. This list only contains result objects that have previously been created, result objects that have not been created are not included.

## See Also

### Notification Info Keys
- [Query Search Scope Keys](./query_search_scope_keys.md)
  Specify the scope of a query’s search.
- [Result Relevance Sorting Key](./result_relevance_sorting_key.md)
  Key used in a user notification’s description dictionary that indicates the relevance of a result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/file_metadata/mdquery/query_result_change_keys)*