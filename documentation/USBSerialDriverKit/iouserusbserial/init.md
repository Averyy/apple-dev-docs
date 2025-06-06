# init

**Framework**: Usbserialdriverkit  
**Kind**: method

Handles the basic initialization of the service.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
bool init();
```

#### Return Value

`YES` if initialization is successful, or `NO` if an error occurred.

#### Discussion

The system calls this method shortly after it instantiates your `IOUserUSBSerial` subclass, and before it calls the [`Start`](https://developer.apple.com/documentation/SerialDriverKit/IOUserSerial/Start) method of your service. Limit the work you do in this method to simple tasks that must occur before your service starts. For example, use this method to allocate memory for your `ivars` structure.

Always call `super` at the beginning of your implementation of this method.

## See Also

- [Start](iouserusbserial/start.md)
  Starts the service for the specified provider.
- [Stop](iouserusbserial/stop.md)
  Stops the service that matches the specified provider.
- [free](iouserusbserial/free.md)
  Performs any final cleanup for the service.
- [initWith](iouserusbserial/initwith.md)
  Initializes the private data structures associated with this class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbserialdriverkit/iouserusbserial/init)*