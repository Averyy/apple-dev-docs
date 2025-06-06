# kMPTaskStoppedErr

**Framework**: Core Services  
**Kind**: data

The desired task is stopped.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kMPTaskStoppedErr: Int { get }
```

## See Also

- [var kMPIterationEndErr: Int](kmpiterationenderr.md)
- [var kMPPrivilegedErr: Int](kmpprivilegederr.md)
- [var kMPProcessCreatedErr: Int](kmpprocesscreatederr.md)
- [var kMPProcessTerminatedErr: Int](kmpprocessterminatederr.md)
- [var kMPTaskCreatedErr: Int](kmptaskcreatederr.md)
- [var kMPTaskBlockedErr: Int](kmptaskblockederr.md)
  The desired task is blocked.
- [var kMPDeletedErr: Int](kmpdeletederr.md)
  The desired notification the function was waiting upon was deleted.
- [var kMPTimeoutErr: Int](kmptimeouterr.md)
  The designated timeout interval passed before the function could take action.
- [var kMPInsufficientResourcesErr: Int](kmpinsufficientresourceserr.md)
  Could not complete task due to unavailable Multiprocessing Services resources. Note that many functions return this value as a general error when the desired action could not be performed.
- [var kMPInvalidIDErr: Int](kmpinvalididerr.md)
  Invalid ID value. For example, an invalid message queue ID was passed to `MPNotifyQueue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kmptaskstoppederr)*