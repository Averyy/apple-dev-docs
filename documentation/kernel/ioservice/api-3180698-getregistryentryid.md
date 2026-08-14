# GetRegistryEntryID

**Framework**: Kernel  
**Kind**: instm

Returns the registry ID for the current service. 

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
kern_return_t GetRegistryEntryID(uint64_t *registryEntryID, OSDispatchMethod supermethod);
```

#### Return_value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes). 

## Parameters

- `registryEntryID`: A pointer to an integer that, on return, contains the registry ID for the service. It is a programmer error to specify `NULL` or an invalid pointer for this parameter.

## See Also

- [- RegisterService](ioservice/3180701-registerservice.md)
  Starts the registration process for the service and performs any additional matching.
- [- SetName](../driverkit/ioservice/setname.md)
  Sets the name of the service in the system's registry.
- [IOServiceName](../driverkit/ioservicename.md)
  A string type for setting the name of the service in the system's registry. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservice/3180698-getregistryentryid)*