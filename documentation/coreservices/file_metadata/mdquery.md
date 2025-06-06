# MDQuery

**Framework**: Core Services

#### Overview

MDQuery is a CF-compliant object, follows the CF conventions,and can be used with the CF polymorphic functions, such as `CFRetain`.MDQuery encapsulates queries against the System store of the filemetadata. 

An MDQuery normally executes asynchronously and posts progressnotifications as the results are collected. During the gatheringphase the query results conform to the specified value lists andsorting.

MDQuery gathers results and processes updates only while thecurrent thread's run loop is running.

For functions that take an MDQueryRef parameter, if this parameteris not a valid MDQueryRef, the behavior is undefined. `NULL` isnot a valid MDQueryRef. 

For functions that take CF*Ref parameters, such as CFStringRefand CFArrayRef, if this parameter is not a valid CF object of thecorrect type, the behavior is undefined. `NULL` isnot a valid CF*Ref. 

## Topics

### Creating Queries
- [func MDQueryCreate(CFAllocator!, CFString!, CFArray!, CFArray!) -> MDQuery!](1413029-mdquerycreate.md)
  Creates a new query instance.
- [func MDQueryCreateSubset(CFAllocator!, MDQuery!, CFString!, CFArray!, CFArray!) -> MDQuery!](1413027-mdquerycreatesubset.md)
  Creates a new query that is a subset of the specified parentquery.
- [func MDQuerySetSearchScope(MDQuery!, CFArray!, OptionBits)](1413048-mdquerysetsearchscope.md)
  Sets the search scope for a query instance.
- [func MDQuerySetDispatchQueue(MDQuery!, dispatch_queue_t!)](1413019-mdquerysetdispatchqueue.md)
  Sets the dispatch queue on which query results will be delivered by MDQueryExecute.
### Getting and Setting Query Parameters
- [func MDQuerySetMaxCount(MDQuery!, CFIndex)](1413085-mdquerysetmaxcount.md)
  Sets the maximum number of results returned.
- [func MDQueryGetBatchingParameters(MDQuery!) -> MDQueryBatchingParams](1413006-mdquerygetbatchingparameters.md)
  Returns the current parameters that control the batching of progress notifications.
- [func MDQuerySetBatchingParameters(MDQuery!, MDQueryBatchingParams)](1413103-mdquerysetbatchingparameters.md)
  Set the query batching parameters.
- [func MDQueryCopyValueListAttributes(MDQuery!) -> CFArray!](1413071-mdquerycopyvaluelistattributes.md)
  Returns the list of attribute names for which values are being collected by the query.
- [func MDQueryCopySortingAttributes(MDQuery!) -> CFArray!](1413059-mdquerycopysortingattributes.md)
  Returns the list of attribute names used to sort the results.
- [func MDQueryCopyQueryString(MDQuery!) -> CFString!](1413004-mdquerycopyquerystring.md)
  Returns the query string of the query.
### Setting Callback Functions
- [func MDQuerySetCreateResultFunction(MDQuery!, MDQueryCreateResultFunction!, UnsafeMutableRawPointer!, UnsafePointer<CFArrayCallBacks>!)](1413064-mdquerysetcreateresultfunction.md)
  Sets the function used to create the result objects of the MDQuery.
- [func MDQuerySetSortComparator(MDQuery!, MDQuerySortComparatorFunction!, UnsafeMutableRawPointer!)](1413087-mdquerysetsortcomparator.md)
  Sets the function used to sort the results of an MDQuery.
- [func MDQuerySetCreateValueFunction(MDQuery!, MDQueryCreateValueFunction!, UnsafeMutableRawPointer!, UnsafePointer<CFArrayCallBacks>!)](1413017-mdquerysetcreatevaluefunction.md)
  Sets the function used to create the value objects of the MDQuery.
### Starting, Stopping and Pausing Queries
- [func MDQueryExecute(MDQuery!, CFOptionFlags) -> Bool](1413099-mdqueryexecute.md)
  Run the query, and populate the query with the results. 
- [func MDQueryStop(MDQuery!)](1413077-mdquerystop.md)
  Stops the query from generating more results. 
- [func MDQueryDisableUpdates(MDQuery!)](1413041-mdquerydisableupdates.md)
  Disables updates to the query result list.
- [func MDQueryEnableUpdates(MDQuery!)](1413066-mdqueryenableupdates.md)
  Enables updates to the query result list.
- [func MDQueryIsGatheringComplete(MDQuery!) -> Bool](1413032-mdqueryisgatheringcomplete.md)
  Returns true if the first phase of a query, the initial result gathering, has finished.
### Getting Query Result Values
- [func MDQueryCopyValuesOfAttribute(MDQuery!, CFString!) -> CFArray!](1413105-mdquerycopyvaluesofattribute.md)
  Returns the list of values from the results of the query for the specified attribute.
- [func MDQueryGetAttributeValueOfResultAtIndex(MDQuery!, CFString!, CFIndex) -> UnsafeMutableRawPointer!](1413046-mdquerygetattributevalueofresult.md)
  Returns the value of the named attribute for the result at the given index.
- [func MDQueryGetCountOfResultsWithAttributeValue(MDQuery!, CFString!, CFTypeRef!) -> CFIndex](1413009-mdquerygetcountofresultswithattr.md)
  Returns the number of results which have the given attribute and attribute value.
- [func MDQueryGetIndexOfResult(MDQuery!, UnsafeRawPointer!) -> CFIndex](1413093-mdquerygetindexofresult.md)
  Returns the current index of the given result.
- [func MDQueryGetResultAtIndex(MDQuery!, CFIndex) -> UnsafeRawPointer!](1413055-mdquerygetresultatindex.md)
  Returns the current result at the given index.
- [func MDQueryGetResultCount(MDQuery!) -> CFIndex](1413008-mdquerygetresultcount.md)
  Returns the number of results currently collected by the query. 
- [func MDQuerySetSortComparatorBlock(MDQuery!, ((UnsafePointer<Unmanaged<CFTypeRef>?>?, UnsafePointer<Unmanaged<CFTypeRef>?>?) -> CFComparisonResult)!)](1413021-mdquerysetsortcomparatorblock.md)
  Sets the block used to sort the results of an MDQuery.
### Getting the Type Identifier
- [func MDQueryGetTypeID() -> CFTypeID](1413037-mdquerygettypeid.md)
  Returns the type identifier of all MDQuery instances
### Callbacks
- [typealias MDQuerySortComparatorFunction](mdquerysortcomparatorfunction.md)
  Callback function used to sort the results of a query.
- [typealias MDQueryCreateResultFunction](mdquerycreateresultfunction.md)
  Callback function used to create the result objects stored and returned by a query.
- [typealias MDQueryCreateValueFunction](mdquerycreatevaluefunction.md)
  Callback function usedto create the value objects stored and returned by a query.
### Batching Parameters
- [struct MDQueryBatchingParams](mdquerybatchingparams.md)
  Structure containing the progress notification batchingparameters of a MDQuery.
### Miscellaneous
- [class MDQuery](mdquery.md)
  A reference to a MDQuery object.
### Query Option Flags
- [struct MDQueryOptionFlags](mdqueryoptionflags.md)
  Specify the execution mode for a query.
### Notifications
- [kMDQueryDidFinishNotification](file_metadata/mdquery/kmdquerydidfinishnotification.md)
  Indicates that a query has finished with the initial result-gathering phase.
- [kMDQueryDidUpdateNotification](file_metadata/mdquery/kmdquerydidupdatenotification.md)
  Indicates that a query’s results list has change during the live-update phase of a query.
- [kMDQueryProgressNotification](file_metadata/mdquery/kmdqueryprogressnotification.md)
  Indicates that a query’s results list has change during the initial result-gathering phase of a query.
### Notification Info Keys
- [Query Result Change Keys](file_metadata/mdquery/query_result_change_keys.md)
  Specify the items that have changed in the query results.
- [Query Search Scope Keys](file_metadata/mdquery/query_search_scope_keys.md)
  Specify the scope of a query’s search.
- [Result Relevance Sorting Key](file_metadata/mdquery/result_relevance_sorting_key.md)
  Key used in a user notification’s description dictionary that indicates the relevance of a result.

## See Also

- [Spotlight Overview](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MetadataIntro/MetadataIntro.html#//apple_ref/doc/uid/TP40001268)
- [File Metadata Search Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/Introduction.html#//apple_ref/doc/uid/TP40001841)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/file_metadata/mdquery)*