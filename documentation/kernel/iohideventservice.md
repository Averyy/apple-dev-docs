# IOHIDEventService

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

IOService represents an device or OS service in IOKit and DriverKit.

**Availability**:
- macOS 10.12.2+ - Deprecated in 10.15.2

## Declaration

```cpp
class IOHIDEventService : IOService
```

#### Overview

IOKit provides driver lifecycle management through the IOService APIs.  Drivers and devices are represented as subclasses of IOService.

## Topics

### Miscellaneous
- [dispatchDigitizerEvent](./iohideventservice/api-1812711-dispatchdigitizerevent.md)
  Dispatch tablet events without orientation
- [dispatchDigitizerEventWithPolarOrientation](./iohideventservice/api-1812728-dispatchdigitizereventwithpolaro.md)
  Dispatch tablet events with polar orientation
- [dispatchDigitizerEventWithTiltOrientation](./iohideventservice/api-1812735-dispatchdigitizereventwithtiltor.md)
  Dispatch tablet events with tilt orientation
- [dispatchMultiAxisPointerEvent](./iohideventservice/api-1812745-dispatchmultiaxispointerevent.md)
  Dispatch multi-axis pointer event
- [handleClose](./iohideventservice/api-1812757-handleclose.md)
  Handle a client close on the interface.
- [handleIsOpen](./iohideventservice/api-1812770-handleisopen.md)
  Query whether a client has an open on the interface.
- [handleOpen](./iohideventservice/api-1812786-handleopen.md)
  Handle a client open on the interface.
- [handleStart](./iohideventservice/api-1812803-handlestart.md)
  Prepare the hardware and driver to support I/O operations.
- [handleStop](./iohideventservice/api-1812816-handlestop.md)
  Quiesce the hardware and stop the driver.
### Instance Variables
- [_reserved](./iohideventservice/reserved.md)
### Instance Methods
- [- CopyEvent](./iohideventservice/api-3753516-copyevent.md)
- [- CreateAction_CopyEvent](./iohideventservice/api-3753519-createaction_copyevent.md)
- [- CreateAction_SetLED](./iohideventservice/api-3869767-createaction_setled.md)
- [- CreateAction_SetUserProperties](./iohideventservice/api-3753520-createaction_setuserproperties.md)
- [- Dispatch](./iohideventservice/api-3294579-dispatch.md)
- [- EventAvailable](./iohideventservice/api-3294592-eventavailable.md)
- [- EventAvailable_Impl](./iohideventservice/api-3294593-eventavailable_impl.md)
- [- SetEventMemory](./iohideventservice/api-3294598-seteventmemory.md)
- [- SetEventMemory_Impl](./iohideventservice/api-3294599-seteventmemory_impl.md)
- [- SetLED](./iohideventservice/api-3294601-setled.md)
- [- SetLEDAction](./iohideventservice/api-3869768-setledaction.md)
- [- SetLEDState](./iohideventservice/api-3869771-setledstate.md)
- [- SetLEDState_Impl](./iohideventservice/api-3869772-setledstate_impl.md)
- [- SetLED_Impl](./iohideventservice/api-3294602-setled_impl.md)
- [- SetProperties_Impl](./iohideventservice/api-3753521-setproperties_impl.md)
- [- SetUserProperties](./iohideventservice/api-3753522-setuserproperties.md)
- [- Start_Impl](./iohideventservice/api-3753525-start_impl.md)
- [- Stop_Impl](./iohideventservice/api-3753526-stop_impl.md)
- [- calculateStandardType](./iohideventservice/api-1558595-calculatestandardtype.md)
- [- close](./iohideventservice/api-2765595-close.md)
- [- closeForClient](./iohideventservice/api-2873398-closeforclient.md)
- [- completeCopyEvent](./iohideventservice/api-3753527-completecopyevent.md)
- [- completeSetLED](./iohideventservice/api-3869774-completesetled.md)
- [- completeSetProperties](./iohideventservice/api-3753528-completesetproperties.md)
- [- copyEvent](./iohideventservice/api-2765598-copyevent.md)
- [- copyEventForClient](./iohideventservice/api-2870306-copyeventforclient.md)
- [- copyMatchingEvent](./iohideventservice/api-3081666-copymatchingevent.md)
- [- copyPropertyForClient](./iohideventservice/api-2870303-copypropertyforclient.md)
- [- determineResolution](./iohideventservice/api-1558613-determineresolution.md)
- [- dispatchAbsolutePointerEvent](./iohideventservice/api-1558604-dispatchabsolutepointerevent.md)
- [- dispatchBiometricEvent](./iohideventservice/api-2824240-dispatchbiometricevent.md)
- [- dispatchDigitizerEvent](./iohideventservice/api-1558608-dispatchdigitizerevent.md)
- [- dispatchDigitizerEventWithOrientation](./iohideventservice/api-1558596-dispatchdigitizereventwithorient.md)
- [- dispatchDigitizerEventWithPolarOrientation](./iohideventservice/api-1558555-dispatchdigitizereventwithpolaro.md)
- [- dispatchDigitizerEventWithTiltOrientation](./iohideventservice/api-1558617-dispatchdigitizereventwithtiltor.md)
- [- dispatchEvent](./iohideventservice/api-2765586-dispatchevent.md)
  Dispatches an event.
- [- dispatchExtendedGameControllerEvent](./iohideventservice/api-2765592-dispatchextendedgamecontrollerev.md)
- [- dispatchExtendedGameControllerEventWithOptionalBottomButtons](./iohideventservice/api-4316297-dispatchextendedgamecontrollerev.md)
- [- dispatchExtendedGameControllerEventWithOptionalButtons](./iohideventservice/api-4077797-dispatchextendedgamecontrollerev.md)
- [- dispatchExtendedGameControllerEventWithThumbstickButtons](./iohideventservice/api-3037457-dispatchextendedgamecontrollerev.md)
- [- dispatchKeyboardEvent](./iohideventservice/api-1558606-dispatchkeyboardevent.md)
- [- dispatchKeyboardEvent](./iohideventservice/api-3603595-dispatchkeyboardevent.md)
- [- dispatchMultiAxisPointerEvent](./iohideventservice/api-1558594-dispatchmultiaxispointerevent.md)
- [- dispatchRelativePointerEvent](./iohideventservice/api-1558568-dispatchrelativepointerevent.md)
- [- dispatchRelativePointerEventWithFixed](./iohideventservice/api-2765608-dispatchrelativepointereventwith.md)
- [- dispatchScrollWheelEvent](./iohideventservice/api-1558590-dispatchscrollwheelevent.md)
- [- dispatchScrollWheelEventWithFixed](./iohideventservice/api-2765602-dispatchscrollwheeleventwithfixe.md)
- [- dispatchStandardGameControllerEvent](./iohideventservice/api-2765589-dispatchstandardgamecontrollerev.md)
- [- dispatchTabletPointerEvent](./iohideventservice/api-1558562-dispatchtabletpointerevent.md)
- [- dispatchTabletProximityEvent](./iohideventservice/api-1558586-dispatchtabletproximityevent.md)
- [- dispatchUnicodeEvent](./iohideventservice/api-1558582-dispatchunicodeevent.md)
- [- free](../HIDDriverKit/iohideventservice/free.md)
- [- getCountryCode](./iohideventservice/api-1558585-getcountrycode.md)
- [- getDeviceUsagePairs](./iohideventservice/api-1558559-getdeviceusagepairs.md)
- [- getElementValue](./iohideventservice/api-1558578-getelementvalue.md)
- [- getLocationID](./iohideventservice/api-1558611-getlocationid.md)
- [- getManufacturer](./iohideventservice/api-1558618-getmanufacturer.md)
- [- getMetaClass](./iohideventservice/api-1558610-getmetaclass.md)
- [- getPrimaryUsage](./iohideventservice/api-2765606-getprimaryusage.md)
- [- getPrimaryUsagePage](./iohideventservice/api-2765591-getprimaryusagepage.md)
- [- getProduct](./iohideventservice/api-1558580-getproduct.md)
- [- getProductID](./iohideventservice/api-1558553-getproductid.md)
- [- getReportElements](./iohideventservice/api-1558589-getreportelements.md)
- [- getReportInterval](./iohideventservice/api-1558574-getreportinterval.md)
- [- getSerialNumber](./iohideventservice/api-1558549-getserialnumber.md)
- [- getTransport](./iohideventservice/api-1558583-gettransport.md)
- [- getVendorID](./iohideventservice/api-1558584-getvendorid.md)
- [- getVendorIDSource](./iohideventservice/api-1558609-getvendoridsource.md)
- [- getVersion](./iohideventservice/api-1558588-getversion.md)
- [- handleClose](./iohideventservice/api-1558561-handleclose.md)
- [- handleCopyMatchingEvent](./iohideventservice/api-3753529-handlecopymatchingevent.md)
- [- handleCopyMatchingEvent_Impl](./iohideventservice/api-3753530-handlecopymatchingevent_impl.md)
- [- handleIsOpen](./iohideventservice/api-1558571-handleisopen.md)
- [- handleOpen](./iohideventservice/api-1558591-handleopen.md)
- [- handleStart](./iohideventservice/api-1558579-handlestart.md)
- [- handleStop](./iohideventservice/api-1558563-handlestop.md)
- [- init](./iohideventservice/api-1558615-init.md)
- [- isPowerButtonNmiEnabled](./iohideventservice/api-3578268-ispowerbuttonnmienabled.md)
- [- matchPropertyTable](./iohideventservice/api-1558551-matchpropertytable.md)
- [- message](./iohideventservice/api-3075121-message.md)
- [- multiAxisTimerCallback](./iohideventservice/api-1558558-multiaxistimercallback.md)
- [- newConsumerShim](./iohideventservice/api-1558554-newconsumershim.md)
- [- newKeyboardShim](./iohideventservice/api-1558598-newkeyboardshim.md)
- [- newUserClient](./iohideventservice/api-2765583-newuserclient.md)
- [- open](./iohideventservice/api-2765582-open.md)
- [- openForClient](./iohideventservice/api-2870305-openforclient.md)
- [- parseSupportedElements](./iohideventservice/api-1558557-parsesupportedelements.md)
- [- processTabletElement](./iohideventservice/api-1558600-processtabletelement.md)
- [- readyForReports](./iohideventservice/api-1558607-readyforreports.md)
- [- setElementValue](./iohideventservice/api-1558603-setelementvalue.md)
- [- setProperties](./iohideventservice/api-1558565-setproperties.md)
- [- setPropertiesForClient](./iohideventservice/api-2870304-setpropertiesforclient.md)
- [- setSystemProperties](./iohideventservice/api-1558547-setsystemproperties.md)
- [- start](./iohideventservice/api-1558564-start.md)
- [- stop](./iohideventservice/api-1558597-stop.md)
- [- supportsHeadset](./iohideventservice/api-3019360-supportsheadset.md)
### Type Methods
- [+ CopyEvent_Invoke](./iohideventservice/api-4520009-copyevent_invoke.md)
- [+ CopyEvent_Invoke](./iohideventservice/api-4520010-copyevent_invoke.md)
- [+ EventAvailable_Invoke](./iohideventservice/api-3294594-eventavailable_invoke.md)
- [+ SetEventMemory_Invoke](./iohideventservice/api-3294600-seteventmemory_invoke.md)
- [+ SetLEDAction_Invoke](./iohideventservice/api-4520011-setledaction_invoke.md)
- [+ SetLEDAction_Invoke](./iohideventservice/api-4520012-setledaction_invoke.md)
- [+ SetLEDState_Invoke](./iohideventservice/api-3869773-setledstate_invoke.md)
- [+ SetLED_Invoke](./iohideventservice/api-3294603-setled_invoke.md)
- [+ SetUserProperties_Invoke](./iohideventservice/api-4520013-setuserproperties_invoke.md)
- [+ SetUserProperties_Invoke](./iohideventservice/api-4520014-setuserproperties_invoke.md)
- [+ debugActionNMI](./iohideventservice/api-2765593-debugactionnmi.md)
- [+ debugActionSysdiagnose](./iohideventservice/api-2765590-debugactionsysdiagnose.md)
- [+ handleCopyMatchingEvent_Invoke](./iohideventservice/api-3753531-handlecopymatchingevent_invoke.md)
- [+ powerButtonNMI](./iohideventservice/api-3578269-powerbuttonnmi.md)

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
- [IOHIDInterface](./iohidinterface.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohideventservice)*