# CopyInterface

**Framework**: USBDriverKit  
**Kind**: method

Gets the next host interface child associated with this device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t CopyInterface(uintptr_t ref, IOUSBHostInterface * * interface);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Keep calling this method until the value in the interface parameter is `NULL`.

## Parameters

- `ref`: The opaque iterator reference you received from the   method.
- `interface`: A pointer to a variable. On output, this variable contains a pointer to the next   object. When there are no more iterfaces, this method assigns   to the variable.

## See Also

- [CreateInterfaceIterator](iousbhostdevice/createinterfaceiterator.md)
  Creates an iterator to get the list of interfaces from the device.
- [DestroyInterfaceIterator](iousbhostdevice/destroyinterfaceiterator.md)
  Destroys an interface iterator that you created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/copyinterface)*