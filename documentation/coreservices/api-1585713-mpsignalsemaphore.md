# MPSignalSemaphore

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Signals a semaphore. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPSignalSemaphore(MPSemaphoreID semaphore);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965). If the value of the semaphore was already at the maximum, `MPSignalSemaphore` returns `kInsufficientResourcesErr`.

#### Discussion

If tasks are waiting on the semaphore, the oldest (first queued) task is unblocked so that the corresponding  [`MPWaitOnSemaphore`](./api-1585722-mpwaitonsemaphore.md)  call for that task completes. Otherwise, if the value of the semaphore is not already equal to its maximum value, it is incremented by one.

Note that you can call this function from an interrupt handler. 

## Parameters

- `semaphore`: The ID of the semaphore you want to signal. 

## See Also

### Creating and Handling Semaphores
- [MPCreateSemaphore](./api-1585569-mpcreatesemaphore.md)
  Creates a semaphore.
- [MPDeleteSemaphore](./api-1585586-mpdeletesemaphore.md)
  Removes a semaphore. 
- [MPWaitOnSemaphore](./api-1585722-mpwaitonsemaphore.md)
  Waits on a semaphore


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585713-mpsignalsemaphore)*