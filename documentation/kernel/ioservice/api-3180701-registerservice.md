# RegisterService

**Framework**: Kernel  
**Kind**: instm

Starts the registration process for the service and performs any additional matching.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
kern_return_t RegisterService(OSDispatchMethod supermethod);
```

#### Return_value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes). 

#### Discussion

After setting up your service in your custom [`Start`](ioservice/3180710-start.md) method, call this method to let the system know your service is running. 

## See Also

- [- SetName](../driverkit/ioservice/setname.md)
  Sets the name of the service in the system's registry.
- [- GetRegistryEntryID](ioservice/3180698-getregistryentryid.md)
  Returns the registry ID for the current service. 
- [IOServiceName](../driverkit/ioservicename.md)
  A string type for setting the name of the service in the system's registry. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservice/3180701-registerservice)*