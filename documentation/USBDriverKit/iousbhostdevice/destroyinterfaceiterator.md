# DestroyInterfaceIterator

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Destroys an interface iterator that you created.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t DestroyInterfaceIterator(uintptr_t ref);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Parameters

- `ref`: An opaque iterator reference that you created using the [`CreateInterfaceIterator`](./createinterfaceiterator.md) method.

## See Also

### Iterating Over the Device Interfaces
- [CreateInterfaceIterator](./createinterfaceiterator.md)
  Creates an iterator to get the list of interfaces from the device.
- [CopyInterface](./copyinterface.md)
  Gets the next host interface child associated with this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/destroyinterfaceiterator)*