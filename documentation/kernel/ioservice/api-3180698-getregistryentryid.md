# GetRegistryEntryID

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Returns the registry ID for the current service. 

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
virtual kern_return_t GetRegistryEntryID(uint64_t *registryEntryID);
```

*macOS*

```cpp
kern_return_t GetRegistryEntryID(uint64_t *registryEntryID, OSDispatchMethod supermethod);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md). 

## Parameters

- `registryEntryID`: A pointer to an integer that, on return, contains the registry ID for the service. It is a programmer error to specify `NULL` or an invalid pointer for this parameter.

## See Also

### Registering the Service with IOKit
- [- RegisterService](./api-3180701-registerservice.md)
  Starts the registration process for the service and performs any additional matching.
- [- SetName](../../DriverKit/ioservice/setname.md)
  Sets the name of the service in the system's registry.
- [IOServiceName](../../DriverKit/ioservicename.md)
  A string type for setting the name of the service in the system's registry. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservice/3180698-getregistryentryid)*