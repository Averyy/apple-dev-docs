# IOHIDValueGetScaledValue

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Returns an scaled representaion of the value contained in this IOHIDValueRef based on the scale type.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```c
double_t IOHIDValueGetScaledValue(IOHIDValueRef value, IOHIDValueScaleType type);
```

#### Return Value

Returns an scaled floating point representation of the value.

#### Discussion

The scaled value is based on the range described by the scale type's min and max, such that:

scaledValue = ((value - min) * (scaledMax - scaledMin) / (max - min)) + scaledMin

**Note:**

There are currently two types of scaling that can be applied:

- **kIOHIDValueScaleTypePhysical**: Scales element value using the physical bounds of the device such that **scaledMin = physicalMin** and **scaledMax = physicalMax**.
- **kIOHIDValueScaleTypeCalibrated**: Scales element value such that **scaledMin = -1** and **scaledMax = 1**. This value will also take into account the calibration properties associated with this element.

## Parameters

- `value`: The value to be queried. If this parameter is not a valid IOHIDValueRef, the behavior is undefined.
- `type`: The type of scaling to be performed.

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
- [IOHIDValueGetTimeStamp](./api-1433286-iohidvaluegettimestamp.md)
  Returns the timestamp value contained in this IOHIDValueRef.
- [IOHIDValueGetTypeID](./api-1433293-iohidvaluegettypeid.md)
  Returns the type identifier of all IOHIDValue instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1433288-iohidvaluegetscaledvalue)*