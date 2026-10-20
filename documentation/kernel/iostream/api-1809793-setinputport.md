# setInputPort

**Framework**: Kernel  
**Kind**: instm

Set the Mach port used to receive notifications from user space that a buffer has been added to the input queue.

## Declaration

```cpp
virtual IOReturn setInputPort(
 mach_port_tport);
```

## Parameters

- `port`: 

## See Also

### Managing notification ports
- [getInputPort](./api-1809770-getinputport.md)
  Get the Mach port used to receive notifications from user space that a buffer has been added to the input queue.
- [getOutputPort](./api-1809774-getoutputport.md)
  Get the Mach port used to send notifications to user space that a buffer has been added to the output queue.
- [sendOutputNotification](./api-1809783-sendoutputnotification.md)
  Send a notification to the user client that data is available for reading on the output queue. This will result in the user's output handler being called, if they registered one.
- [setOutputPort](./api-1809801-setoutputport.md)
  Set the Mach port used to send notifications to user space that a buffer has been added to the output queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809793-setinputport)*