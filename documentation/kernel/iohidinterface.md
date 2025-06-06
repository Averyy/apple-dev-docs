# IOHIDInterface

**Framework**: Kernel  
**Kind**: cl

IOService represents an device or OS service in IOKit and DriverKit.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.2

## Declaration

```swift
class IOHIDInterface : IOService
```

#### Overview

IOKit provides driver lifecycle management through the IOService APIs.  Drivers and devices are represented as subclasses of IOService.

## Topics

### Miscellaneous
- [free](iohidinterface/1812725-free.md)
  Free the IOHIDInterface object.
- [init](iohidinterface/1812739-init.md)
  Initialize an IOHIDInterface object.
- [matchPropertyTable](iohidinterface/1812756-matchpropertytable.md)
  Called by the provider during a match
- [start](iohidinterface/1812781-start.md)
  Start up the driver using the given provider.
### Callbacks
- [CompletionAction](iohidinterface/completionaction.md)
- [InterruptReportAction](iohidinterface/interruptreportaction.md)
  Callback to handle an asynchronous report received from the HID device.
- [IOHIDInterface::CompletionAction](iohidinterface/iohidinterface_completionaction.md)
- [IOHIDInterface::InterruptReportAction](iohidinterface/iohidinterface_interruptreportaction.md)
  Callback to handle an asynchronous report received from the HID device.
### Instance Variables
- [_reserved](iohidinterface/reserved.md)
### Instance Methods
- [- AddReportToPool](iohidinterface/3294546-addreporttopool.md)
- [- AddReportToPool_Impl](iohidinterface/3294547-addreporttopool_impl.md)
- [- Close](iohidinterface/3294549-close.md)
- [- Close_Impl](iohidinterface/3294550-close_impl.md)
- [- Dispatch](iohidinterface/3294552-dispatch.md)
- [- GetElementValues](iohidinterface/3294553-getelementvalues.md)
- [- GetElementValues_Impl](iohidinterface/3294554-getelementvalues_impl.md)
- [- GetReport](iohidinterface/3294556-getreport.md)
- [- GetReport_Impl](iohidinterface/3294557-getreport_impl.md)
- [- GetSupportedCookies](iohidinterface/3294559-getsupportedcookies.md)
- [- GetSupportedCookies_Impl](iohidinterface/3294560-getsupportedcookies_impl.md)
- [- HandleReportPrivate](iohidinterface/3294562-handlereportprivate.md)
- [- Open](iohidinterface/3294563-open.md)
- [- Open_Impl](iohidinterface/3294564-open_impl.md)
- [- ReportAvailable](iohidinterface/3294566-reportavailable.md)
- [- SendDebugBuffer](iohidinterface/3787569-senddebugbuffer.md)
- [- SendDebugBuffer_Impl](iohidinterface/3787570-senddebugbuffer_impl.md)
- [- SetElementValues](iohidinterface/3294568-setelementvalues.md)
- [- SetElementValues_Impl](iohidinterface/3294569-setelementvalues_impl.md)
- [- SetReport](iohidinterface/3294571-setreport.md)
- [- SetReport_Impl](iohidinterface/3294572-setreport_impl.md)
- [- addReportToPoolGated](iohidinterface/3294574-addreporttopoolgated.md)
- [- close](iohidinterface/1545711-close.md)
- [- createElements](iohidinterface/3294576-createelements.md)
- [- createMatchingElements](iohidinterface/1545731-creatematchingelements.md)
- [- free](../hiddriverkit/iohidinterface/free.md)
- [- getCountryCode](iohidinterface/1545717-getcountrycode.md)
- [- getLocationID](iohidinterface/1545716-getlocationid.md)
- [- getManufacturer](iohidinterface/1545718-getmanufacturer.md)
- [- getMaxReportSize](iohidinterface/1545712-getmaxreportsize.md)
- [- getMetaClass](iohidinterface/1545732-getmetaclass.md)
- [- getProduct](iohidinterface/1545707-getproduct.md)
- [- getProductID](iohidinterface/1545701-getproductid.md)
- [- getReport](iohidinterface/1545729-getreport.md)
- [- getReport](iohidinterface/3516593-getreport.md)
- [- getReportInterval](iohidinterface/1545710-getreportinterval.md)
- [- getSerialNumber](iohidinterface/1545720-getserialnumber.md)
- [- getTransport](iohidinterface/1545700-gettransport.md)
- [- getVendorID](iohidinterface/1545713-getvendorid.md)
- [- getVendorIDSource](iohidinterface/1545703-getvendoridsource.md)
- [- getVersion](iohidinterface/1545705-getversion.md)
- [- handleReport](iohidinterface/1545706-handlereport.md)
- [- handleReportGated](iohidinterface/3294577-handlereportgated.md)
- [- init](iohidinterface/1545733-init.md)
  Initializes IOHIDInterface object.
- [- matchPropertyTable](iohidinterface/1545727-matchpropertytable.md)
- [- message](iohidinterface/1545719-message.md)
- [- open](iohidinterface/1545722-open.md)
- [- openGated](iohidinterface/3294578-opengated.md)
- [- serializeDebugState](iohidinterface/3787572-serializedebugstate.md)
- [- setProperty](iohidinterface/3516594-setproperty.md)
- [- setReport](iohidinterface/1545724-setreport.md)
- [- setReport](iohidinterface/3516595-setreport.md)
- [- start](iohidinterface/1545702-start.md)
- [- stop](iohidinterface/1545726-stop.md)
### Type Methods
- [+ AddReportToPool_Invoke](iohidinterface/3294548-addreporttopool_invoke.md)
- [+ Close_Invoke](iohidinterface/3294551-close_invoke.md)
- [+ GetElementValues_Invoke](iohidinterface/3294555-getelementvalues_invoke.md)
- [+ GetReport_Invoke](iohidinterface/3294558-getreport_invoke.md)
- [+ GetSupportedCookies_Invoke](iohidinterface/3294561-getsupportedcookies_invoke.md)
- [+ Open_Invoke](iohidinterface/3294565-open_invoke.md)
- [+ ReportAvailable_Invoke](iohidinterface/4520007-reportavailable_invoke.md)
- [+ ReportAvailable_Invoke](iohidinterface/4520008-reportavailable_invoke.md)
- [+ SendDebugBuffer_Invoke](iohidinterface/3787571-senddebugbuffer_invoke.md)
- [+ SetElementValues_Invoke](iohidinterface/3294570-setelementvalues_invoke.md)
- [+ SetReport_Invoke](iohidinterface/3294573-setreport_invoke.md)
- [+ withElements](iohidinterface/1545728-withelements.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

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
- [IOHIDSystem](iohidsystem.md)
- [IOHIKeyboardMapper](iohikeyboardmapper.md)
- [IOHIKeyboard](iohikeyboard.md)
- [IOHIPointing](iohipointing.md)
- [IOHIDevice](iohidevice.md)
- [IOHIDElement](iohidelement.md)
- [IOHIDWorkLoop](iohidworkloop.md)
- [IOEthernetInterface](ioethernetinterface.md)
  The Ethernet interface object.
- [IOEthernetController](ioethernetcontroller.md)
  Abstract superclass for Ethernet controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohidinterface)*