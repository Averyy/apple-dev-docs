# IOHIDValueGetTypeID

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Returns the type identifier of all IOHIDValue instances.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```c
CFTypeID IOHIDValueGetTypeID(void);
```

## See Also

### Miscellaneous
- [IOHIDValueCreateWithBytes](./api-1433290-iohidvaluecreatewithbytes.md)
  Creates a new element value using byte data.
- [IOHIDValueCreateWithBytesNoCopy](./api-1433287-iohidvaluecreatewithbytesnocopy.md)
  Creates a new element value using byte data without performing a copy.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1433293-iohidvaluegettypeid)*