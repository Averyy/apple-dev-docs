# GetName

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Returns the name of the queue as a C string.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```c
const char * GetName(void);
```

## Return Value

A C-string pointer to the queue's internal storage.

## Discussion

Returns a pointer to the queue's name. This string is valid only while the queue is retained.

## See Also

### Getting Queue Information
- [- OnQueue](./api-3438196-onqueue.md)
  Returns a Boolean value that indicates whether the current thread matches the dispatch queue's thread. 
- [IODispatchQueueName](../../DriverKit/iodispatchqueuename.md)
  A buffer for specifying the name of a dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodispatchqueue/3438194-getname)*