# handleClose

**Framework**: Kernel  
**Kind**: instm

The handleClose method destroys the shared input and output queues.

## Declaration

```swift
virtual void handleClose(
 IOService *forClient, 
 IOOptionBits options );
```

## Parameters

- `options`: 

## See Also

- [handleOpen](iostream/1809688-handleopen.md)
  The handleOpen() method relies on the default IOService behavior to ensure that only one client has the stream open at a time. The shared input and output queues are created at open time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809680-handleclose)*