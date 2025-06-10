# OnQueue

**Framework**: Kernel  
**Kind**: instm

Returns a Boolean value that indicates whether the current thread matches the dispatch queue's thread. 

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
bool OnQueue(void);
```

#### Return_value

`true` if the current thread is the same thread that the dispatch queue is using to execute its task. 

#### Discussion

Use this method to determine if your code is running on the same thread as the current dispatch queue.

## See Also

- [IODispatchQueueName](../driverkit/iodispatchqueuename.md)
  A buffer for specifying the name of a dispatch queue.
- [- GetName](iodispatchqueue/3438194-getname.md)
  Returns the name of the queue as a C string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodispatchqueue/3438196-onqueue)*