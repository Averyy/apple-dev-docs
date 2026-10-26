# IOHIDValueCreateWithBytesNoCopy

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Creates a new element value using byte data without performing a copy.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```c
IOHIDValueRef IOHIDValueCreateWithBytesNoCopy(CFAllocatorRef allocator, IOHIDElementRef element, uint64_t timeStamp, const uint8_t *bytes, CFIndex length);
```

#### Return Value

Returns a reference to a new IOHIDValueRef.

#### Discussion

The timestamp value passed should represent OS AbsoluteTime, not CFAbsoluteTime. To obtain the OS AbsoluteTime, please reference the APIs declared in <mach/mach_time.h>

## Parameters

- `allocator`: The CFAllocator which should be used to allocate memory for the value. This parameter may be NULL in which case the current default CFAllocator is used. If this reference is not a valid CFAllocator, the behavior is undefined.
- `element`: IOHIDElementRef associated with this value.
- `timeStamp`: OS absolute time timestamp for this value.
- `bytes`: Pointer to a buffer of uint8_t to be referenced by this object.
- `length`: Number of bytes in the passed buffer.

## See Also

### Miscellaneous
- [IOHIDValueCreateWithBytes](./api-1433290-iohidvaluecreatewithbytes.md)
  Creates a new element value using byte data.
- [IOHIDValueCreateWithIntegerValue](./api-1433294-iohidvaluecreatewithintegervalue.md)
  Creates a new element value using an integer value.
- [IOHIDValueGetBytePtr](./api-1433292-iohidvaluegetbyteptr.md)
  Returns a byte pointer to the value contained in this IOHIDValueRef.
- [IOHIDValueGetElement](./api-1433285-iohidvaluegetelement.md)
  Returns the element value associated with this IOHIDValueRef.
- [IOHIDValueGetIntegerValue](./api-1433289-iohidvaluegetintegervalue.md)
  Returns an integer representaion of the value contained in this IOHIDValueRef.
- [IOHIDValueGetLength](./api-1433291-iohidvaluegetlength.md)
  Returns the size, in bytes, of the value contained in this IOHIDValueRef.
- [IOHIDValueGetScaledValue](./api-1433288-iohidvaluegetscaledvalue.md)
  Returns an scaled representaion of the value contained in this IOHIDValueRef based on the scale type.
- [IOHIDValueGetTimeStamp](./api-1433286-iohidvaluegettimestamp.md)
  Returns the timestamp value contained in this IOHIDValueRef.
- [IOHIDValueGetTypeID](./api-1433293-iohidvaluegettypeid.md)
  Returns the type identifier of all IOHIDValue instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1433287-iohidvaluecreatewithbytesnocopy)*