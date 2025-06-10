# Create

**Framework**: Kernel  
**Kind**: clm

Creates a new dispatch queue object.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
static kern_return_t Create(const char *name, uint64_t options, uint64_t priority, IODispatchQueue **queue);
```

#### Return_value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. For a list of error codes, see `Error Codes`. 

#### Discussion

Creates a new dispatch queue object. All queues are currently serial, executing one block at time in FIFO order. The new object has retain count of 1 and should be released by the caller.

## Parameters

- `options`: No options are currently defined. Specify   for this parameter.
- `priority`: No priorities are currently defined. Specify   for this parameter.

## See Also

- [- init](iodispatchqueue/3438198-init.md)
  Initializes the dispatch queue object.
- [- free](iodispatchqueue/3438197-free.md)
  Performs any final cleanup for the dispatch queue object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodispatchqueue/3438189-create)*