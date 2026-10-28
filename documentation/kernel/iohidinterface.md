# IOHIDInterface

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

IOService represents an device or OS service in IOKit and DriverKit.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15.2

## Declaration

```cpp
class IOHIDInterface : IOService
```

## Overview

IOKit provides driver lifecycle management through the IOService APIs.  Drivers and devices are represented as subclasses of IOService.

## Topics

### Miscellaneous
- [free](./iohidinterface/api-1812725-free.md)
  Free the IOHIDInterface object.
- [init](./iohidinterface/api-1812739-init.md)
  Initialize an IOHIDInterface object.
- [matchPropertyTable](./iohidinterface/api-1812756-matchpropertytable.md)
  Called by the provider during a match
- [start](./iohidinterface/api-1812781-start.md)
  Start up the driver using the given provider.
### Callbacks
- [CompletionAction](./iohidinterface/completionaction.md)
- [InterruptReportAction](./iohidinterface/interruptreportaction.md)
  Callback to handle an asynchronous report received from the HID device.
- [IOHIDInterface::CompletionAction](./iohidinterface/iohidinterface_completionaction.md)
- [IOHIDInterface::InterruptReportAction](./iohidinterface/iohidinterface_interruptreportaction.md)
  Callback to handle an asynchronous report received from the HID device.
### Instance Variables
- [_reserved](./iohidinterface/reserved.md)
### Instance Methods
- [- AddReportToPool](./iohidinterface/api-3294546-addreporttopool.md)
- [- AddReportToPool_Impl](./iohidinterface/api-3294547-addreporttopool_impl.md)
- [- Close](./iohidinterface/api-3294549-close.md)
- [- Close_Impl](./iohidinterface/api-3294550-close_impl.md)
- [- Dispatch](./iohidinterface/api-3294552-dispatch.md)
- [- GetElementValues](./iohidinterface/api-3294553-getelementvalues.md)
- [- GetElementValues_Impl](./iohidinterface/api-3294554-getelementvalues_impl.md)
- [- GetReport](./iohidinterface/api-3294556-getreport.md)
- [- GetReport_Impl](./iohidinterface/api-3294557-getreport_impl.md)
- [- GetSupportedCookies](./iohidinterface/api-3294559-getsupportedcookies.md)
- [- GetSupportedCookies_Impl](./iohidinterface/api-3294560-getsupportedcookies_impl.md)
- [- HandleReportPrivate](./iohidinterface/api-3294562-handlereportprivate.md)
- [- Open](./iohidinterface/api-3294563-open.md)
- [- Open_Impl](./iohidinterface/api-3294564-open_impl.md)
- [- ReportAvailable](./iohidinterface/api-3294566-reportavailable.md)
- [- SendDebugBuffer](./iohidinterface/api-3787569-senddebugbuffer.md)
- [- SendDebugBuffer_Impl](./iohidinterface/api-3787570-senddebugbuffer_impl.md)
- [- SetElementValues](./iohidinterface/api-3294568-setelementvalues.md)
- [- SetElementValues_Impl](./iohidinterface/api-3294569-setelementvalues_impl.md)
- [- SetReport](./iohidinterface/api-3294571-setreport.md)
- [- SetReport_Impl](./iohidinterface/api-3294572-setreport_impl.md)
- [- addReportToPoolGated](./iohidinterface/api-3294574-addreporttopoolgated.md)
- [- close](./iohidinterface/api-1545711-close.md)
- [- createElements](./iohidinterface/api-3294576-createelements.md)
- [- createMatchingElements](./iohidinterface/api-1545731-creatematchingelements.md)
- [- free](../HIDDriverKit/iohidinterface/free.md)
- [- getCountryCode](./iohidinterface/api-1545717-getcountrycode.md)
- [- getLocationID](./iohidinterface/api-1545716-getlocationid.md)
- [- getManufacturer](./iohidinterface/api-1545718-getmanufacturer.md)
- [- getMaxReportSize](./iohidinterface/api-1545712-getmaxreportsize.md)
- [- getMetaClass](./iohidinterface/api-1545732-getmetaclass.md)
- [- getProduct](./iohidinterface/api-1545707-getproduct.md)
- [- getProductID](./iohidinterface/api-1545701-getproductid.md)
- [- getReport](./iohidinterface/api-1545729-getreport.md)
- [- getReport](./iohidinterface/api-3516593-getreport.md)
- [- getReportInterval](./iohidinterface/api-1545710-getreportinterval.md)
- [- getSerialNumber](./iohidinterface/api-1545720-getserialnumber.md)
- [- getTransport](./iohidinterface/api-1545700-gettransport.md)
- [- getVendorID](./iohidinterface/api-1545713-getvendorid.md)
- [- getVendorIDSource](./iohidinterface/api-1545703-getvendoridsource.md)
- [- getVersion](./iohidinterface/api-1545705-getversion.md)
- [- handleReport](./iohidinterface/api-1545706-handlereport.md)
- [- handleReportGated](./iohidinterface/api-3294577-handlereportgated.md)
- [- init](./iohidinterface/api-1545733-init.md)
  Initializes IOHIDInterface object.
- [- matchPropertyTable](./iohidinterface/api-1545727-matchpropertytable.md)
- [- message](./iohidinterface/api-1545719-message.md)
- [- open](./iohidinterface/api-1545722-open.md)
- [- openGated](./iohidinterface/api-3294578-opengated.md)
- [- serializeDebugState](./iohidinterface/api-3787572-serializedebugstate.md)
- [- setProperty](./iohidinterface/api-3516594-setproperty.md)
- [- setReport](./iohidinterface/api-1545724-setreport.md)
- [- setReport](./iohidinterface/api-3516595-setreport.md)
- [- start](./iohidinterface/api-1545702-start.md)
- [- stop](./iohidinterface/api-1545726-stop.md)
### Type Methods
- [+ AddReportToPool_Invoke](./iohidinterface/api-3294548-addreporttopool_invoke.md)
- [+ Close_Invoke](./iohidinterface/api-3294551-close_invoke.md)
- [+ GetElementValues_Invoke](./iohidinterface/api-3294555-getelementvalues_invoke.md)
- [+ GetReport_Invoke](./iohidinterface/api-3294558-getreport_invoke.md)
- [+ GetSupportedCookies_Invoke](./iohidinterface/api-3294561-getsupportedcookies_invoke.md)
- [+ Open_Invoke](./iohidinterface/api-3294565-open_invoke.md)
- [+ ReportAvailable_Invoke](./iohidinterface/api-4520007-reportavailable_invoke.md)
- [+ ReportAvailable_Invoke](./iohidinterface/api-4520008-reportavailable_invoke.md)
- [+ SendDebugBuffer_Invoke](./iohidinterface/api-3787571-senddebugbuffer_invoke.md)
- [+ SetElementValues_Invoke](./iohidinterface/api-3294570-setelementvalues_invoke.md)
- [+ SetReport_Invoke](./iohidinterface/api-3294573-setreport_invoke.md)
- [+ withElements](./iohidinterface/api-1545728-withelements.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

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
- [IOHIDSystem](./iohidsystem.md)
- [IOHIKeyboardMapper](./iohikeyboardmapper.md)
- [IOHIKeyboard](./iohikeyboard.md)
- [IOHIPointing](./iohipointing.md)
- [IOHIDevice](./iohidevice.md)
- [IOHIDElement](./iohidelement.md)
- [IOHIDWorkLoop](./iohidworkloop.md)
- [IOEthernetInterface](./ioethernetinterface.md)
  The Ethernet interface object.
- [IOEthernetController](./ioethernetcontroller.md)
  Abstract superclass for Ethernet controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohidinterface)*