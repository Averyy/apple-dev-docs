# kMDQueryDidUpdateNotification

**Framework**: Core Services

Indicates that a query’s results list has change during the live-update phase of a query.

#### Overview

The info dictionary of the notification can contain `kMDQueryUpdateAddedItems`, `kMDQueryUpdateChangedItems`, and `kMDQueryUpdateRemovedItems` keys. 

This notification is only sent to the application’s notification center.

## Topics

### Constants
- [let kMDQueryDidUpdateNotification: CFString!](kmdquerydidupdatenotification.md)
  Notification posted to indicate that a change has occurred to the query’s results list during the live-update phase of a query’s execution.

## See Also

- [kMDQueryDidFinishNotification](file_metadata/mdquery/kmdquerydidfinishnotification.md)
  Indicates that a query has finished with the initial result-gathering phase.
- [kMDQueryProgressNotification](file_metadata/mdquery/kmdqueryprogressnotification.md)
  Indicates that a query’s results list has change during the initial result-gathering phase of a query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/file_metadata/mdquery/kmdquerydidupdatenotification)*