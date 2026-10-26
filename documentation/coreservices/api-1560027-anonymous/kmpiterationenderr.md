# kMPIterationEndErr

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
kMPIterationEndErr = -29275
```

## See Also

### Result Codes
- [kMPPrivilegedErr](./kmpprivilegederr.md)
- [kMPProcessCreatedErr](./kmpprocesscreatederr.md)
- [kMPProcessTerminatedErr](./kmpprocessterminatederr.md)
- [kMPTaskCreatedErr](./kmptaskcreatederr.md)
- [kMPTaskBlockedErr](./kmptaskblockederr.md)
  The desired task is blocked.
- [kMPTaskStoppedErr](./kmptaskstoppederr.md)
  The desired task is stopped.
- [kMPDeletedErr](./kmpdeletederr.md)
  The desired notification the function was waiting upon was deleted.
- [kMPTimeoutErr](./kmptimeouterr.md)
  The designated timeout interval passed before the function could take action.
- [kMPInsufficientResourcesErr](./kmpinsufficientresourceserr.md)
  Could not complete task due to unavailable Multiprocessing Services resources. Note that many functions return this value as a general error when the desired action could not be performed.
- [kMPInvalidIDErr](./kmpinvalididerr.md)
  Invalid ID value. For example, an invalid message queue ID was passed to `MPNotifyQueue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1560027-anonymous/kmpiterationenderr)*