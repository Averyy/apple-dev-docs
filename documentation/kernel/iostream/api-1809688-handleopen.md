# handleOpen

**Framework**: Kernel  
**Kind**: instm

The handleOpen() method relies on the default IOService behavior to ensure that only one client has the stream open at a time. The shared input and output queues are created at open time.

## Declaration

```swift
virtual bool handleOpen(
 IOService *forClient, 
 IOOptionBits options, 
 void *arg );
```

## Parameters

- `options`: 
- `arg`: 

## See Also

- [handleClose](iostream/1809680-handleclose.md)
  The handleClose method destroys the shared input and output queues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809688-handleopen)*