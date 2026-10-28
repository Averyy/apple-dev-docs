# Create

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

Creates a new dispatch queue object.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

*DriverKit*

```c
static kern_return_t Create(const IODispatchQueueName name, uint64_t options, uint64_t priority, IODispatchQueue **queue);
```

*macOS*

```c
static kern_return_t Create(const char *name, uint64_t options, uint64_t priority, IODispatchQueue **queue);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md). 

## Discussion

Creates a new dispatch queue object. All queues are currently serial, executing one block at time in FIFO order. The new object has retain count of 1 and should be released by the caller.

## Parameters

- `options`: No options are currently defined. Specify `0` for this parameter.
- `priority`: No priorities are currently defined. Specify `0` for this parameter.

## See Also

### Creating a Dispatch Queue
- [- init](./api-3438198-init.md)
  Initializes the dispatch queue object.
- [- free](./api-3438197-free.md)
  Performs any final cleanup for the dispatch queue object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodispatchqueue/3438189-create)*