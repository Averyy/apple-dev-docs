# MPDeleteSemaphore

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Removes a semaphore. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPDeleteSemaphore(MPSemaphoreID semaphore);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

#### Discussion

Calling this function unblocks all tasks waiting on the semaphore and the tasks’ respective  [`MPWaitOnSemaphore`](./api-1585722-mpwaitonsemaphore.md)  calls will return with the result code `kMPDeletedErr`.

Also see the function  [`MPCreateSemaphore`](./api-1585569-mpcreatesemaphore.md). 

## Parameters

- `semaphore`: The ID of the semaphore you want to remove. 

## See Also

### Creating and Handling Semaphores
- [MPCreateSemaphore](./api-1585569-mpcreatesemaphore.md)
  Creates a semaphore.
- [MPSignalSemaphore](./api-1585713-mpsignalsemaphore.md)
  Signals a semaphore. 
- [MPWaitOnSemaphore](./api-1585722-mpwaitonsemaphore.md)
  Waits on a semaphore


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585586-mpdeletesemaphore)*