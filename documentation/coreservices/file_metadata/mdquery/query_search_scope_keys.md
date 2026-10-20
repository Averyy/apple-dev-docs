# Query Search Scope Keys

**Framework**: Core Services

Specify the scope of a query’s search.

#### Overview

These constants can be passed in the `scopeDirectories` array to the function `MDQuerySetSearchScope`.

## Topics

### Constants
- [let kMDQueryScopeHome: CFString!](kmdqueryscopehome.md)
  Specifies that the query should be restricted to the volume and directory that contains the current user’s home directory.
- [let kMDQueryScopeComputer: CFString!](kmdqueryscopecomputer.md)
  Specifies that the query should be restricted to all locally mounted volumes, plus the user’s home directory (which may be on a remote volume).
- [let kMDQueryScopeNetwork: CFString!](kmdqueryscopenetwork.md)
  Specifies that the query should include all user mounted remote volumes.
- [let kMDQueryScopeAllIndexed: CFString!](kmdqueryscopeallindexed.md)
  Specifies that the search should be restricted to indexed, locally mounted volumes and indexed user mounted remote volumes, plus the user's home directory.
- [let kMDQueryScopeComputerIndexed: CFString!](kmdqueryscopecomputerindexed.md)
  Specifies that the search should be restricted to indexed, locally mounted volumes, plus the user's home directory (which may be on a remote volume).
- [let kMDQueryScopeNetworkIndexed: CFString!](kmdqueryscopenetworkindexed.md)
  Specifies that the search should include indexed user mounted remote volumes.

## See Also

- [Query Result Change Keys](file_metadata/mdquery/query_result_change_keys.md)
  Specify the items that have changed in the query results.
- [Result Relevance Sorting Key](file_metadata/mdquery/result_relevance_sorting_key.md)
  Key used in a user notification’s description dictionary that indicates the relevance of a result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/file_metadata/mdquery/query_search_scope_keys)*