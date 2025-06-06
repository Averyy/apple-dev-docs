# Multiprocessing Services

**Framework**: Core Services

Support multitasking in your app.

#### Overview

Multiprocessing Services is an API that lets you create preemptive tasks in your application that can run on one or more microprocessors. Unlike the cooperative threads created by the Thread Manager, Multiprocessing Services automatically divides processor time among the available tasks, so that no particular task can monopolize the system. This document is relevant to you if you want to add multitasking capability to your Mac OS applications.

In macOS, Carbon supports Multiprocessing Services with the following restrictions:

- Debugging functions are not implemented. Use the mach APIs provided by the system to implement debugging services.
- Opaque notification IDs are local to your process; they are not globally addressable across processes.
- Global memory allocation is not supported.

##### 1674081

You can determine which system software calls are preemptively-safe for Multiprocessing Services by using the preemptive function attribute selectors defined in the Gestalt Manager. For more information, see [`Gestalt Manager`](carbon_core/gestalt_manager.md).

## Topics

### Result Codes
- [var kMPIterationEndErr: Int](kmpiterationenderr.md)
- [var kMPPrivilegedErr: Int](kmpprivilegederr.md)
- [var kMPProcessCreatedErr: Int](kmpprocesscreatederr.md)
- [var kMPProcessTerminatedErr: Int](kmpprocessterminatederr.md)
- [var kMPTaskCreatedErr: Int](kmptaskcreatederr.md)
- [var kMPTaskBlockedErr: Int](kmptaskblockederr.md)
  The desired task is blocked.
- [var kMPTaskStoppedErr: Int](kmptaskstoppederr.md)
  The desired task is stopped.
- [var kMPDeletedErr: Int](kmpdeletederr.md)
  The desired notification the function was waiting upon was deleted.
- [var kMPTimeoutErr: Int](kmptimeouterr.md)
  The designated timeout interval passed before the function could take action.
- [var kMPInsufficientResourcesErr: Int](kmpinsufficientresourceserr.md)
  Could not complete task due to unavailable Multiprocessing Services resources. Note that many functions return this value as a general error when the desired action could not be performed.
- [var kMPInvalidIDErr: Int](kmpinvalididerr.md)
  Invalid ID value. For example, an invalid message queue ID was passed to `MPNotifyQueue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/carbon_core/multiprocessing_services)*