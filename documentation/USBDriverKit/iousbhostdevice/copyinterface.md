# CopyInterface

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the next host interface child associated with this device.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t CopyInterface(uintptr_t ref, IOUSBHostInterface **interface);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Discussion

Keep calling this method until the value in the interface parameter is `NULL`.

## Parameters

- `ref`: The opaque iterator reference you received from the [`CreateInterfaceIterator`](./createinterfaceiterator.md) method.
- `interface`: A pointer to a variable. On output, this variable contains a pointer to the next [`IOUSBHostInterface`](../iousbhostinterface.md) object. When there are no more iterfaces, this method assigns `NULL` to the variable.

## See Also

### Iterating Over the Device Interfaces
- [CreateInterfaceIterator](./createinterfaceiterator.md)
  Creates an iterator to get the list of interfaces from the device.
- [DestroyInterfaceIterator](./destroyinterfaceiterator.md)
  Destroys an interface iterator that you created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/copyinterface)*