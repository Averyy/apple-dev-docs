# MPCreateSemaphore

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a semaphore.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPCreateSemaphore(MPSemaphoreCount maximumValue, MPSemaphoreCount initialValue, MPSemaphoreID *semaphore);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

#### Discussion

If you want to create a binary semaphore, you can call the macro `MPCreateBinarySemaphore (MPSemaphoreID *semaphore)` instead, which simply calls `MPCreateSemaphore` with both `maximumValue` and `initialValue` set to 1.

Also see the function  [`MPDeleteSemaphore`](./api-1585586-mpdeletesemaphore.md). 

## Parameters

- `maximumValue`: The maximum allowed value of the semaphore. 
- `initialValue`: The initial value of the semaphore.
- `semaphore`: On return, `semaphore` contains the ID of the newly–created semaphore. 

## See Also

### Creating and Handling Semaphores
- [MPDeleteSemaphore](./api-1585586-mpdeletesemaphore.md)
  Removes a semaphore. 
- [MPSignalSemaphore](./api-1585713-mpsignalsemaphore.md)
  Signals a semaphore. 
- [MPWaitOnSemaphore](./api-1585722-mpwaitonsemaphore.md)
  Waits on a semaphore


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585569-mpcreatesemaphore)*