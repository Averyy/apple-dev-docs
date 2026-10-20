# IOHIDElement

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.1

## Declaration

```cpp
class IOHIDElement : OSCollection
```

## Topics

### Instance Methods
- [- conformsTo](../HIDDriverKit/iohidelement/conformsto.md)
- [- getChildElements](../HIDDriverKit/iohidelement/getchildelements.md)
- [- getCollectionType](../HIDDriverKit/iohidelement/getcollectiontype.md)
- [- getCookie](../HIDDriverKit/iohidelement/getcookie.md)
- [- getDataValue](./iohidelement/api-1426875-getdatavalue.md)
- [- getDataValue](../HIDDriverKit/iohidelement/getdatavalue.md)
  Gets the data value.
- [- getFlags](../HIDDriverKit/iohidelement/getflags.md)
- [- getLogicalMax](../HIDDriverKit/iohidelement/getlogicalmax.md)
- [- getLogicalMin](../HIDDriverKit/iohidelement/getlogicalmin.md)
- [- getMetaClass](./iohidelement/api-1426853-getmetaclass.md)
- [- getParentElement](../HIDDriverKit/iohidelement/getparentelement.md)
- [- getPhysicalMax](../HIDDriverKit/iohidelement/getphysicalmax.md)
- [- getPhysicalMin](../HIDDriverKit/iohidelement/getphysicalmin.md)
- [- getReportCount](../HIDDriverKit/iohidelement/getreportcount.md)
- [- getReportID](../HIDDriverKit/iohidelement/getreportid.md)
- [- getReportSize](../HIDDriverKit/iohidelement/getreportsize.md)
- [- getReportType](./iohidelement/api-4077796-getreporttype.md)
- [- getScaledFixedValue](../HIDDriverKit/iohidelement/getscaledfixedvalue.md)
  Returns a fixed number that represents the scaled version of the element’s logical value.
- [- getScaledFixedValue](./iohidelement/api-3516592-getscaledfixedvalue.md)
- [- getScaledValue](../HIDDriverKit/iohidelement/getscaledvalue.md)
  Returns a scaled version of the logical value.
- [- getTimeStamp](../HIDDriverKit/iohidelement/gettimestamp.md)
- [- getType](../HIDDriverKit/iohidelement/gettype.md)
- [- getUnit](../HIDDriverKit/iohidelement/getunit.md)
  Returns the units that you use to interpret the element’s value.
- [- getUnitExponent](../HIDDriverKit/iohidelement/getunitexponent.md)
  Returns the exponent that you use to interpret the element’s value.
- [- getUsage](../HIDDriverKit/iohidelement/getusage.md)
- [- getUsagePage](../HIDDriverKit/iohidelement/getusagepage.md)
- [- getValue](./iohidelement/api-1426860-getvalue.md)
- [- getValue](../HIDDriverKit/iohidelement/getvalue.md)
  Gets the logical value that the device reported.
- [- isVariableSize](./iohidelement/api-2870278-isvariablesize.md)
- [- setCalibration](./iohidelement/api-1426877-setcalibration.md)
- [- setDataValue](../HIDDriverKit/iohidelement/setdatavalue.md)
  Sets the data value of the element.
- [- setValue](../HIDDriverKit/iohidelement/setvalue.md)
  Sets the value of the element.
- [- setValue](./iohidelement/api-3656574-setvalue.md)

## Relationships

### Inherits From
- [OSCollection](./oscollection.md)

## See Also

### IOKit
- [IOUSBDevice](./iousbdevice.md)
  An input/output service object that represents a device on the USB bus.
- [IOUSBInterface](./iousbinterface.md)
  An object that represents an interface of a device on the USB bus.
- [IOOFPathMatching](./api-1575304-ioofpathmatching.md)
- [IOUSBHostInterface](./iousbhostinterface.md)
- [IOUSBHostDevice](./iousbhostdevice.md)
- [IOUSBHostPipe](./iousbhostpipe.md)
- [IOUSBHostIOSource](./iousbhostiosource.md)
- [IOUSBHostStream](./iousbhoststream.md)
- [IOHIDEventDriver](./iohideventdriver.md)
- [IOHIDEventService](./iohideventservice.md)
  IOService represents an device or OS service in IOKit and DriverKit.
- [IOHIDInterface](./iohidinterface.md)
  IOService represents an device or OS service in IOKit and DriverKit.
- [IOHIDSystem](./iohidsystem.md)
- [IOHIKeyboardMapper](./iohikeyboardmapper.md)
- [IOHIKeyboard](./iohikeyboard.md)
- [IOHIPointing](./iohipointing.md)
- [IOHIDevice](./iohidevice.md)
- [IOHIDWorkLoop](./iohidworkloop.md)
- [IOEthernetInterface](./ioethernetinterface.md)
  The Ethernet interface object.
- [IOEthernetController](./ioethernetcontroller.md)
  Abstract superclass for Ethernet controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohidelement)*