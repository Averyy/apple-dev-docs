# Create

**Framework**: Kernel  
**Kind**: clm

Creates a dispatch source that you use as a shared-memory data queue.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
static kern_return_t Create(uint64_t queueByteCount, IODispatchQueue *queue, IODataQueueDispatchSource **source);
```

#### Return_value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. See `Error Codes`. 

## Parameters

- `queueByteCount`: The size of the queue in bytes.
- `queue`: The dispatch queue to use for executing tasks. Note that the   and   handlers execute on the queue set for the target method of the associated   object, not this queue.
- `source`: A variable for storing the resulting dispatch source object. On success, the returned object has a retain count of 1, and you must release it when finished. 

## See Also

- [- init](iodataqueuedispatchsource/3438187-init.md)
  Handles the basic initialization of the dispatch source.
- [- free](iodataqueuedispatchsource/3438186-free.md)
  Performs any final cleanup for the data-queue dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueuedispatchsource/3438177-create)*