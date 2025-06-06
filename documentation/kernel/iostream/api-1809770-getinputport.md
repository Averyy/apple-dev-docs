# getInputPort

**Framework**: Kernel  
**Kind**: instm

Get the Mach port used to receive notifications from user space that a buffer has been added to the input queue.

## Declaration

```swift
virtual mach_port_t getInputPort(
 void);
```

## See Also

- [getOutputPort](iostream/1809774-getoutputport.md)
  Get the Mach port used to send notifications to user space that a buffer has been added to the output queue.
- [sendOutputNotification](iostream/1809783-sendoutputnotification.md)
  Send a notification to the user client that data is available for reading on the output queue. This will result in the user's output handler being called, if they registered one.
- [setInputPort](iostream/1809793-setinputport.md)
  Set the Mach port used to receive notifications from user space that a buffer has been added to the input queue.
- [setOutputPort](iostream/1809801-setoutputport.md)
  Set the Mach port used to send notifications to user space that a buffer has been added to the output queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809770-getinputport)*