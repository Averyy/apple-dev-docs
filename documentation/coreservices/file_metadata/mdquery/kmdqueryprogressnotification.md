# kMDQueryProgressNotification

**Framework**: Core Services

Indicates that a query’s results list has change during the initial result-gathering phase of a query.

#### Overview

New items are typically added during this phase, however it is possible for items to be removed or updated, if the original file is changed. The info dictionary of the notification can contain `kMDQueryUpdateChangedItems` and `kMDQueryUpdateRemovedItems` keys.

For performance reasons added results are not indicated in progress notifications, to avoid the cost of creating the result objects.

This notification is only sent to the application’s notification center.

## Topics

### Constants
- [let kMDQueryProgressNotification: CFString!](kmdqueryprogressnotification.md)
  Notification posted to indicate that a change has occurred to the query’s results list during the initial result-gathering phase of execution.

## See Also

- [kMDQueryDidFinishNotification](file_metadata/mdquery/kmdquerydidfinishnotification.md)
  Indicates that a query has finished with the initial result-gathering phase.
- [kMDQueryDidUpdateNotification](file_metadata/mdquery/kmdquerydidupdatenotification.md)
  Indicates that a query’s results list has change during the live-update phase of a query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/file_metadata/mdquery/kmdqueryprogressnotification)*