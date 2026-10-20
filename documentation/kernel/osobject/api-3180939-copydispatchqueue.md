# CopyDispatchQueue

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
virtual kern_return_t CopyDispatchQueue(const IODispatchQueueName name, IODispatchQueue **queue);
```

*macOS*

```cpp
kern_return_t CopyDispatchQueue(const char *name, IODispatchQueue **queue, OSDispatchMethod supermethod);
```

## See Also

### Managing an Object's Dispatch Queue
- [- SetDispatchQueue](./api-3180942-setdispatchqueue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osobject/3180939-copydispatchqueue)*