# free

**Framework**: Usbserialdriverkit  
**Kind**: method

Performs any final cleanup for the service.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
void free();
```

#### Discussion

Use this method to deallocate any memory associated with your service, or perform other cleanup tasks. The system calls this method at some point after it calls your service’s [`Stop`](https://developer.apple.com/documentation/SerialDriverKit/IOUserSerial/Stop) method.

Always call `super` at the end of your implementation of this method.

## See Also

- [init](iouserusbserial/init.md)
  Handles the basic initialization of the service.
- [Start](iouserusbserial/start.md)
  Starts the service for the specified provider.
- [Stop](iouserusbserial/stop.md)
  Stops the service that matches the specified provider.
- [initWith](iouserusbserial/initwith.md)
  Initializes the private data structures associated with this class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbserialdriverkit/iouserusbserial/free)*