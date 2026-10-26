# MPWaitOnSemaphore

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Waits on a semaphore

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPWaitOnSemaphore(MPSemaphoreID semaphore, Duration timeout);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

#### Discussion

If the value of the semaphore is greater than zero, the value is decremented and the function returns with `noErr`. Otherwise, the task is blocked awaiting a signal until the specified timeout is exceeded.

If you call this function from a cooperative task, you should specify only `kDurationImmediate` for the timeout length; other waits will cause the task to block. 

Also see the function  [`MPSignalSemaphore`](./api-1585713-mpsignalsemaphore.md). 

## Parameters

- `semaphore`: The ID of the semaphore you want to wait on. 
- `timeout`: The maximum time the function should wait before timing out. See [Timer Duration Constants](./api-1585641-timer_duration_constants.md) for a list of constants you can use to specify the wait interval. 

## See Also

### Creating and Handling Semaphores
- [MPCreateSemaphore](./api-1585569-mpcreatesemaphore.md)
  Creates a semaphore.
- [MPDeleteSemaphore](./api-1585586-mpdeletesemaphore.md)
  Removes a semaphore. 
- [MPSignalSemaphore](./api-1585713-mpsignalsemaphore.md)
  Signals a semaphore. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585722-mpwaitonsemaphore)*