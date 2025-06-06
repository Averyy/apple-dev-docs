# DestroyInterfaceIterator

**Framework**: USBDriverKit  
**Kind**: method

Destroys an interface iterator that you created.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t DestroyInterfaceIterator(uintptr_t ref);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

## Parameters

- `ref`: An opaque iterator reference that you created using the   method.

## See Also

- [CreateInterfaceIterator](iousbhostdevice/createinterfaceiterator.md)
  Creates an iterator to get the list of interfaces from the device.
- [CopyInterface](iousbhostdevice/copyinterface.md)
  Gets the next host interface child associated with this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/destroyinterfaceiterator)*