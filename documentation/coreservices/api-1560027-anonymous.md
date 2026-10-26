# Anonymous

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : int {
    ...
};
```

## Topics

### Constants
- [kMPBlueBlockingErr](./api-1560027-anonymous/kmpblueblockingerr.md)
- [kMPDeletedErr](./api-1560027-anonymous/kmpdeletederr.md)
  The desired notification the function was waiting upon was deleted.
- [kMPInsufficientResourcesErr](./api-1560027-anonymous/kmpinsufficientresourceserr.md)
  Could not complete task due to unavailable Multiprocessing Services resources. Note that many functions return this value as a general error when the desired action could not be performed.
- [kMPInvalidIDErr](./api-1560027-anonymous/kmpinvalididerr.md)
  Invalid ID value. For example, an invalid message queue ID was passed to `MPNotifyQueue`.
- [kMPIterationEndErr](./api-1560027-anonymous/kmpiterationenderr.md)
- [kMPPrivilegedErr](./api-1560027-anonymous/kmpprivilegederr.md)
- [kMPProcessCreatedErr](./api-1560027-anonymous/kmpprocesscreatederr.md)
- [kMPProcessTerminatedErr](./api-1560027-anonymous/kmpprocessterminatederr.md)
- [kMPTaskAbortedErr](./api-1560027-anonymous/kmptaskabortederr.md)
- [kMPTaskBlockedErr](./api-1560027-anonymous/kmptaskblockederr.md)
  The desired task is blocked.
- [kMPTaskCreatedErr](./api-1560027-anonymous/kmptaskcreatederr.md)
- [kMPTaskStoppedErr](./api-1560027-anonymous/kmptaskstoppederr.md)
  The desired task is stopped.
- [kMPTimeoutErr](./api-1560027-anonymous/kmptimeouterr.md)
  The designated timeout interval passed before the function could take action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1560027-anonymous)*