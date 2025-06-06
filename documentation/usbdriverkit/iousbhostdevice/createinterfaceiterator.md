# CreateInterfaceIterator

**Framework**: USBDriverKit  
**Kind**: method

Creates an iterator to get the list of interfaces from the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t CreateInterfaceIterator(uintptr_t * ref);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Use this method to create an iterator for the [`IOUSBHostInterface`](iousbhostinterface.md) children belonging to this device. Pass the value you receive in the `ref` parameter to the [`CopyInterface`](iousbhostdevice/copyinterface.md) method when fetching the interfaces.

## Parameters

- `ref`: A pointer to a variable. On return, this variable contains an opaque iterator reference.

## See Also

- [CopyInterface](iousbhostdevice/copyinterface.md)
  Gets the next host interface child associated with this device.
- [DestroyInterfaceIterator](iousbhostdevice/destroyinterfaceiterator.md)
  Destroys an interface iterator that you created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/createinterfaceiterator)*