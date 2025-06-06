# IOHIDElement

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.1

## Declaration

```swift
class IOHIDElement : OSCollection
```

## Topics

### Instance Methods
- [- conformsTo](../hiddriverkit/iohidelement/conformsto.md)
- [- getChildElements](../hiddriverkit/iohidelement/getchildelements.md)
- [- getCollectionType](../hiddriverkit/iohidelement/getcollectiontype.md)
- [- getCookie](../hiddriverkit/iohidelement/getcookie.md)
- [- getDataValue](iohidelement/1426875-getdatavalue.md)
- [- getDataValue](../hiddriverkit/iohidelement/getdatavalue.md)
  Gets the data value.
- [- getFlags](../hiddriverkit/iohidelement/getflags.md)
- [- getLogicalMax](../hiddriverkit/iohidelement/getlogicalmax.md)
- [- getLogicalMin](../hiddriverkit/iohidelement/getlogicalmin.md)
- [- getMetaClass](iohidelement/1426853-getmetaclass.md)
- [- getParentElement](../hiddriverkit/iohidelement/getparentelement.md)
- [- getPhysicalMax](../hiddriverkit/iohidelement/getphysicalmax.md)
- [- getPhysicalMin](../hiddriverkit/iohidelement/getphysicalmin.md)
- [- getReportCount](../hiddriverkit/iohidelement/getreportcount.md)
- [- getReportID](../hiddriverkit/iohidelement/getreportid.md)
- [- getReportSize](../hiddriverkit/iohidelement/getreportsize.md)
- [- getReportType](iohidelement/4077796-getreporttype.md)
- [- getScaledFixedValue](../hiddriverkit/iohidelement/getscaledfixedvalue.md)
  Returns a fixed number that represents the scaled version of the element’s logical value.
- [- getScaledFixedValue](iohidelement/3516592-getscaledfixedvalue.md)
- [- getScaledValue](../hiddriverkit/iohidelement/getscaledvalue.md)
  Returns a scaled version of the logical value.
- [- getTimeStamp](../hiddriverkit/iohidelement/gettimestamp.md)
- [- getType](../hiddriverkit/iohidelement/gettype.md)
- [- getUnit](../hiddriverkit/iohidelement/getunit.md)
  Returns the units that you use to interpret the element’s value.
- [- getUnitExponent](../hiddriverkit/iohidelement/getunitexponent.md)
  Returns the exponent that you use to interpret the element’s value.
- [- getUsage](../hiddriverkit/iohidelement/getusage.md)
- [- getUsagePage](../hiddriverkit/iohidelement/getusagepage.md)
- [- getValue](iohidelement/1426860-getvalue.md)
- [- getValue](../hiddriverkit/iohidelement/getvalue.md)
  Gets the logical value that the device reported.
- [- isVariableSize](iohidelement/2870278-isvariablesize.md)
- [- setCalibration](iohidelement/1426877-setcalibration.md)
- [- setDataValue](../hiddriverkit/iohidelement/setdatavalue.md)
  Sets the data value of the element.
- [- setValue](../hiddriverkit/iohidelement/setvalue.md)
  Sets the value of the element.
- [- setValue](iohidelement/3656574-setvalue.md)

## Relationships

### Inherits From
- [OSCollection](oscollection.md)

## See Also

- [IOUSBDevice](iousbdevice.md)
  An input/output service object that represents a device on the USB bus.
- [IOUSBInterface](iousbinterface.md)
  An object that represents an interface of a device on the USB bus.
- [IOOFPathMatching](1575304-ioofpathmatching.md)
- [IOUSBHostInterface](iousbhostinterface.md)
- [IOUSBHostDevice](iousbhostdevice.md)
- [IOUSBHostPipe](iousbhostpipe.md)
- [IOUSBHostIOSource](iousbhostiosource.md)
- [IOUSBHostStream](iousbhoststream.md)
- [IOHIDEventDriver](iohideventdriver.md)
- [IOHIDEventService](iohideventservice.md)
  IOService represents an device or OS service in IOKit and DriverKit.
- [IOHIDInterface](iohidinterface.md)
  IOService represents an device or OS service in IOKit and DriverKit.
- [IOHIDSystem](iohidsystem.md)
- [IOHIKeyboardMapper](iohikeyboardmapper.md)
- [IOHIKeyboard](iohikeyboard.md)
- [IOHIPointing](iohipointing.md)
- [IOHIDevice](iohidevice.md)
- [IOHIDWorkLoop](iohidworkloop.md)
- [IOEthernetInterface](ioethernetinterface.md)
  The Ethernet interface object.
- [IOEthernetController](ioethernetcontroller.md)
  Abstract superclass for Ethernet controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohidelement)*