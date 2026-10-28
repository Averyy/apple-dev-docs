# RegisterService

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Starts the registration process for the service and performs any additional matching.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
virtual kern_return_t RegisterService(void);
```

*macOS*

```cpp
kern_return_t RegisterService(OSDispatchMethod supermethod);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md). 

## Discussion

After setting up your service in your custom [`Start`](./api-3180710-start.md) method, call this method to let the system know your service is running. 

## See Also

### Registering the Service with IOKit
- [- SetName](../../DriverKit/ioservice/setname.md)
  Sets the name of the service in the system's registry.
- [- GetRegistryEntryID](./api-3180698-getregistryentryid.md)
  Returns the registry ID for the current service. 
- [IOServiceName](../../DriverKit/ioservicename.md)
  A string type for setting the name of the service in the system's registry. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservice/3180701-registerservice)*