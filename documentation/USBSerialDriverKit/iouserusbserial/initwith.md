# initWith

**Framework**: USBSerialDriverKit  
**Kind**: method  
**Role**: Instance Method

Initializes the private data structures associated with this class.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual bool initWith(IOBufferMemoryDescriptor *ifmd);
```

#### Return Value

`YES` if initialization succeeded, or `NO` if it didn’t.

#### Discussion

Do not override or call this method. Instead, override the [`init`](./init.md) method and use it to allocate memory for your driver’s data structures.

## Parameters

- `ifmd`: The memory buffer to use for interrupt-related data.

## See Also

### Configuring the Service
- [init](./init.md)
  Handles the basic initialization of the service.
- [Start](./start.md)
  Starts the service for the specified provider.
- [Stop](./stop.md)
  Stops the service that matches the specified provider.
- [free](./free.md)
  Performs any final cleanup for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbserialdriverkit/iouserusbserial/initwith)*