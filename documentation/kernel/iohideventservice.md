# IOHIDEventService

**Framework**: Kernel  
**Kind**: cl

IOService represents an device or OS service in IOKit and DriverKit.

**Availability**:
- macOS 10.12.2+ - Deprecated in 10.15.2

## Declaration

```swift
class IOHIDEventService : IOService
```

#### Overview

IOKit provides driver lifecycle management through the IOService APIs.  Drivers and devices are represented as subclasses of IOService.

## Topics

### Miscellaneous
- [dispatchDigitizerEvent](iohideventservice/1812711-dispatchdigitizerevent.md)
  Dispatch tablet events without orientation
- [dispatchDigitizerEventWithPolarOrientation](iohideventservice/1812728-dispatchdigitizereventwithpolaro.md)
  Dispatch tablet events with polar orientation
- [dispatchDigitizerEventWithTiltOrientation](iohideventservice/1812735-dispatchdigitizereventwithtiltor.md)
  Dispatch tablet events with tilt orientation
- [dispatchMultiAxisPointerEvent](iohideventservice/1812745-dispatchmultiaxispointerevent.md)
  Dispatch multi-axis pointer event
- [handleClose](iohideventservice/1812757-handleclose.md)
  Handle a client close on the interface.
- [handleIsOpen](iohideventservice/1812770-handleisopen.md)
  Query whether a client has an open on the interface.
- [handleOpen](iohideventservice/1812786-handleopen.md)
  Handle a client open on the interface.
- [handleStart](iohideventservice/1812803-handlestart.md)
  Prepare the hardware and driver to support I/O operations.
- [handleStop](iohideventservice/1812816-handlestop.md)
  Quiesce the hardware and stop the driver.
### Instance Variables
- [_reserved](iohideventservice/reserved.md)
### Instance Methods
- [- CopyEvent](iohideventservice/3753516-copyevent.md)
- [- CreateAction_CopyEvent](iohideventservice/3753519-createaction_copyevent.md)
- [- CreateAction_SetLED](iohideventservice/3869767-createaction_setled.md)
- [- CreateAction_SetUserProperties](iohideventservice/3753520-createaction_setuserproperties.md)
- [- Dispatch](iohideventservice/3294579-dispatch.md)
- [- EventAvailable](iohideventservice/3294592-eventavailable.md)
- [- EventAvailable_Impl](iohideventservice/3294593-eventavailable_impl.md)
- [- SetEventMemory](iohideventservice/3294598-seteventmemory.md)
- [- SetEventMemory_Impl](iohideventservice/3294599-seteventmemory_impl.md)
- [- SetLED](iohideventservice/3294601-setled.md)
- [- SetLEDAction](iohideventservice/3869768-setledaction.md)
- [- SetLEDState](iohideventservice/3869771-setledstate.md)
- [- SetLEDState_Impl](iohideventservice/3869772-setledstate_impl.md)
- [- SetLED_Impl](iohideventservice/3294602-setled_impl.md)
- [- SetProperties_Impl](iohideventservice/3753521-setproperties_impl.md)
- [- SetUserProperties](iohideventservice/3753522-setuserproperties.md)
- [- Start_Impl](iohideventservice/3753525-start_impl.md)
- [- Stop_Impl](iohideventservice/3753526-stop_impl.md)
- [- calculateStandardType](iohideventservice/1558595-calculatestandardtype.md)
- [- close](iohideventservice/2765595-close.md)
- [- closeForClient](iohideventservice/2873398-closeforclient.md)
- [- completeCopyEvent](iohideventservice/3753527-completecopyevent.md)
- [- completeSetLED](iohideventservice/3869774-completesetled.md)
- [- completeSetProperties](iohideventservice/3753528-completesetproperties.md)
- [- copyEvent](iohideventservice/2765598-copyevent.md)
- [- copyEventForClient](iohideventservice/2870306-copyeventforclient.md)
- [- copyMatchingEvent](iohideventservice/3081666-copymatchingevent.md)
- [- copyPropertyForClient](iohideventservice/2870303-copypropertyforclient.md)
- [- determineResolution](iohideventservice/1558613-determineresolution.md)
- [- dispatchAbsolutePointerEvent](iohideventservice/1558604-dispatchabsolutepointerevent.md)
- [- dispatchBiometricEvent](iohideventservice/2824240-dispatchbiometricevent.md)
- [- dispatchDigitizerEvent](iohideventservice/1558608-dispatchdigitizerevent.md)
- [- dispatchDigitizerEventWithOrientation](iohideventservice/1558596-dispatchdigitizereventwithorient.md)
- [- dispatchDigitizerEventWithPolarOrientation](iohideventservice/1558555-dispatchdigitizereventwithpolaro.md)
- [- dispatchDigitizerEventWithTiltOrientation](iohideventservice/1558617-dispatchdigitizereventwithtiltor.md)
- [- dispatchEvent](iohideventservice/2765586-dispatchevent.md)
  Dispatches an event.
- [- dispatchExtendedGameControllerEvent](iohideventservice/2765592-dispatchextendedgamecontrollerev.md)
- [- dispatchExtendedGameControllerEventWithOptionalBottomButtons](iohideventservice/4316297-dispatchextendedgamecontrollerev.md)
- [- dispatchExtendedGameControllerEventWithOptionalButtons](iohideventservice/4077797-dispatchextendedgamecontrollerev.md)
- [- dispatchExtendedGameControllerEventWithThumbstickButtons](iohideventservice/3037457-dispatchextendedgamecontrollerev.md)
- [- dispatchKeyboardEvent](iohideventservice/1558606-dispatchkeyboardevent.md)
- [- dispatchKeyboardEvent](iohideventservice/3603595-dispatchkeyboardevent.md)
- [- dispatchMultiAxisPointerEvent](iohideventservice/1558594-dispatchmultiaxispointerevent.md)
- [- dispatchRelativePointerEvent](iohideventservice/1558568-dispatchrelativepointerevent.md)
- [- dispatchRelativePointerEventWithFixed](iohideventservice/2765608-dispatchrelativepointereventwith.md)
- [- dispatchScrollWheelEvent](iohideventservice/1558590-dispatchscrollwheelevent.md)
- [- dispatchScrollWheelEventWithFixed](iohideventservice/2765602-dispatchscrollwheeleventwithfixe.md)
- [- dispatchStandardGameControllerEvent](iohideventservice/2765589-dispatchstandardgamecontrollerev.md)
- [- dispatchTabletPointerEvent](iohideventservice/1558562-dispatchtabletpointerevent.md)
- [- dispatchTabletProximityEvent](iohideventservice/1558586-dispatchtabletproximityevent.md)
- [- dispatchUnicodeEvent](iohideventservice/1558582-dispatchunicodeevent.md)
- [- free](../hiddriverkit/iohideventservice/free.md)
- [- getCountryCode](iohideventservice/1558585-getcountrycode.md)
- [- getDeviceUsagePairs](iohideventservice/1558559-getdeviceusagepairs.md)
- [- getElementValue](iohideventservice/1558578-getelementvalue.md)
- [- getLocationID](iohideventservice/1558611-getlocationid.md)
- [- getManufacturer](iohideventservice/1558618-getmanufacturer.md)
- [- getMetaClass](iohideventservice/1558610-getmetaclass.md)
- [- getPrimaryUsage](iohideventservice/2765606-getprimaryusage.md)
- [- getPrimaryUsagePage](iohideventservice/2765591-getprimaryusagepage.md)
- [- getProduct](iohideventservice/1558580-getproduct.md)
- [- getProductID](iohideventservice/1558553-getproductid.md)
- [- getReportElements](iohideventservice/1558589-getreportelements.md)
- [- getReportInterval](iohideventservice/1558574-getreportinterval.md)
- [- getSerialNumber](iohideventservice/1558549-getserialnumber.md)
- [- getTransport](iohideventservice/1558583-gettransport.md)
- [- getVendorID](iohideventservice/1558584-getvendorid.md)
- [- getVendorIDSource](iohideventservice/1558609-getvendoridsource.md)
- [- getVersion](iohideventservice/1558588-getversion.md)
- [- handleClose](iohideventservice/1558561-handleclose.md)
- [- handleCopyMatchingEvent](iohideventservice/3753529-handlecopymatchingevent.md)
- [- handleCopyMatchingEvent_Impl](iohideventservice/3753530-handlecopymatchingevent_impl.md)
- [- handleIsOpen](iohideventservice/1558571-handleisopen.md)
- [- handleOpen](iohideventservice/1558591-handleopen.md)
- [- handleStart](iohideventservice/1558579-handlestart.md)
- [- handleStop](iohideventservice/1558563-handlestop.md)
- [- init](iohideventservice/1558615-init.md)
- [- isPowerButtonNmiEnabled](iohideventservice/3578268-ispowerbuttonnmienabled.md)
- [- matchPropertyTable](iohideventservice/1558551-matchpropertytable.md)
- [- message](iohideventservice/3075121-message.md)
- [- multiAxisTimerCallback](iohideventservice/1558558-multiaxistimercallback.md)
- [- newConsumerShim](iohideventservice/1558554-newconsumershim.md)
- [- newKeyboardShim](iohideventservice/1558598-newkeyboardshim.md)
- [- newUserClient](iohideventservice/2765583-newuserclient.md)
- [- open](iohideventservice/2765582-open.md)
- [- openForClient](iohideventservice/2870305-openforclient.md)
- [- parseSupportedElements](iohideventservice/1558557-parsesupportedelements.md)
- [- processTabletElement](iohideventservice/1558600-processtabletelement.md)
- [- readyForReports](iohideventservice/1558607-readyforreports.md)
- [- setElementValue](iohideventservice/1558603-setelementvalue.md)
- [- setProperties](iohideventservice/1558565-setproperties.md)
- [- setPropertiesForClient](iohideventservice/2870304-setpropertiesforclient.md)
- [- setSystemProperties](iohideventservice/1558547-setsystemproperties.md)
- [- start](iohideventservice/1558564-start.md)
- [- stop](iohideventservice/1558597-stop.md)
- [- supportsHeadset](iohideventservice/3019360-supportsheadset.md)
### Type Methods
- [+ CopyEvent_Invoke](iohideventservice/4520009-copyevent_invoke.md)
- [+ CopyEvent_Invoke](iohideventservice/4520010-copyevent_invoke.md)
- [+ EventAvailable_Invoke](iohideventservice/3294594-eventavailable_invoke.md)
- [+ SetEventMemory_Invoke](iohideventservice/3294600-seteventmemory_invoke.md)
- [+ SetLEDAction_Invoke](iohideventservice/4520011-setledaction_invoke.md)
- [+ SetLEDAction_Invoke](iohideventservice/4520012-setledaction_invoke.md)
- [+ SetLEDState_Invoke](iohideventservice/3869773-setledstate_invoke.md)
- [+ SetLED_Invoke](iohideventservice/3294603-setled_invoke.md)
- [+ SetUserProperties_Invoke](iohideventservice/4520013-setuserproperties_invoke.md)
- [+ SetUserProperties_Invoke](iohideventservice/4520014-setuserproperties_invoke.md)
- [+ debugActionNMI](iohideventservice/2765593-debugactionnmi.md)
- [+ debugActionSysdiagnose](iohideventservice/2765590-debugactionsysdiagnose.md)
- [+ handleCopyMatchingEvent_Invoke](iohideventservice/3753531-handlecopymatchingevent_invoke.md)
- [+ powerButtonNMI](iohideventservice/3578269-powerbuttonnmi.md)

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
- [IOHIDInterface](iohidinterface.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohideventservice)*