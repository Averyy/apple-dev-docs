# IOUSBAbortOptions

**Framework**: USBDriverKit  
**Kind**: enum  
**Role**: Enumeration

Options to use when aborting an I/O request.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
enum IOUSBAbortOptions : unsigned int;
```

## Topics

### Getting the Options
- [kIOUSBAbortAsynchronous](./iousbabortoptions/kiousbabortasynchronous.md)
  Enqueue the abort request and return immediately.
- [kIOUSBAbortSynchronous](./iousbabortoptions/kiousbabortsynchronous.md)
  Enqueue the abort request and wait for it to finish.

## See Also

### Aborting I/O Requests
- [Abort](./iousbhostpipe/abort.md)
  Aborts all of the pipe’s pending I/O requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbabortoptions)*