# copyMatchingElements

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Obtains specific elements defined by the device.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.3+

## Declaration

```c
IOReturn (*copyMatchingElements)(void *self, CFDictionaryRef matchingDict, CFArrayRef *elements);
```

## Return Value

Returns an IOReturn code.

## Discussion

Using keys defined in IOHIDKeys.h for elements, create a matching dictonary containing items that you wish to search for. A null array indicates that no elements matching that criteria were found. Each item in the array is a reference to the same dictionary item that represents each element in the I/O Registry. It is up to the caller to release the returned array of elements.

## Parameters

- `matchingDict`: Dictionary containg key/value pairs to match on. Pass a null value to match on all elements.
- `elements`: Pointer to a CFArrayRef that will be returned by this method. It is up to the caller to release it when finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddeviceinterface122/1493276-copymatchingelements)*