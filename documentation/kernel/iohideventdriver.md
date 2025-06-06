# IOHIDEventDriver

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.12.2+ - Deprecated in 10.15.1

## Declaration

```swift
class IOHIDEventDriver : IOHIDEventService
```

## Topics

### Instance Methods
- [- checkGameControllerElement](iohideventdriver/1528396-checkgamecontrollerelement.md)
- [- checkMultiAxisElement](iohideventdriver/1528393-checkmultiaxiselement.md)
- [- conformTo](iohideventdriver/2765566-conformto.md)
- [- copyEvent](iohideventdriver/2967287-copyevent.md)
- [- copyMatchingEvent](iohideventdriver/3081665-copymatchingevent.md)
- [- createDigitizerTransducerEventForReport](iohideventdriver/2765564-createdigitizertransducereventfo.md)
- [- didTerminate](iohideventdriver/1528375-didterminate.md)
- [- dispatchEvent](iohideventdriver/2765568-dispatchevent.md)
- [- free](iohideventdriver/1528363-free.md)
- [- getBlessedUsagePairs](iohideventdriver/3042840-getblessedusagepairs.md)
- [- getButtonStateFromElements](iohideventdriver/3753515-getbuttonstatefromelements.md)
- [- getCountryCode](iohideventdriver/1528357-getcountrycode.md)
- [- getElementValue](iohideventdriver/1528377-getelementvalue.md)
- [- getLocationID](iohideventdriver/1528339-getlocationid.md)
- [- getManufacturer](iohideventdriver/1528395-getmanufacturer.md)
- [- getMetaClass](iohideventdriver/1528381-getmetaclass.md)
- [- getProduct](iohideventdriver/1528374-getproduct.md)
- [- getProductID](iohideventdriver/1528319-getproductid.md)
- [- getReportElements](iohideventdriver/1528369-getreportelements.md)
- [- getSerialNumber](iohideventdriver/1528329-getserialnumber.md)
- [- getTransport](iohideventdriver/1528347-gettransport.md)
- [- getVendorID](iohideventdriver/1528335-getvendorid.md)
- [- getVendorIDSource](iohideventdriver/1528328-getvendoridsource.md)
- [- getVersion](iohideventdriver/1528380-getversion.md)
- [- handleAccelReport](iohideventdriver/2967288-handleaccelreport.md)
- [- handleBiometricReport](iohideventdriver/2824266-handlebiometricreport.md)
- [- handleBootPointingReport](iohideventdriver/1528386-handlebootpointingreport.md)
- [- handleCompassReport](iohideventdriver/2967289-handlecompassreport.md)
- [- handleDeviceOrientationReport](iohideventdriver/2967290-handledeviceorientationreport.md)
- [- handleDigitizerCollectionReport](iohideventdriver/2765567-handledigitizercollectionreport.md)
- [- handleDigitizerReport](iohideventdriver/1528385-handledigitizerreport.md)
- [- handleDigitizerTransducerReport](iohideventdriver/1528321-handledigitizertransducerreport.md)
- [- handleGameControllerReport](iohideventdriver/1528404-handlegamecontrollerreport.md)
- [- handleGyroReport](iohideventdriver/2967291-handlegyroreport.md)
- [- handleInterruptReport](iohideventdriver/1528364-handleinterruptreport.md)
- [- handleKeboardReport](iohideventdriver/1528336-handlekeboardreport.md)
- [- handleMultiAxisPointerReport](iohideventdriver/1528370-handlemultiaxispointerreport.md)
- [- handlePhaseReport](iohideventdriver/3603593-handlephasereport.md)
- [- handleProximityReport](iohideventdriver/3698195-handleproximityreport.md)
- [- handleRelativeReport](iohideventdriver/1528361-handlerelativereport.md)
- [- handleScrollReport](iohideventdriver/1528390-handlescrollreport.md)
- [- handleStart](iohideventdriver/1528338-handlestart.md)
- [- handleStop](iohideventdriver/1528345-handlestop.md)
- [- handleTemperatureReport](iohideventdriver/2967292-handletemperaturereport.md)
- [- handleUnicodeGestureCandidateReport](iohideventdriver/1528350-handleunicodegesturecandidaterep.md)
- [- handleUnicodeGestureReport](iohideventdriver/1528340-handleunicodegesturereport.md)
- [- handleUnicodeLegacyReport](iohideventdriver/1528379-handleunicodelegacyreport.md)
- [- handleUnicodeReport](iohideventdriver/1528351-handleunicodereport.md)
- [- handleVendorMessageReport](iohideventdriver/2765563-handlevendormessagereport.md)
- [- init](iohideventdriver/1528326-init.md)
- [- parseAccelElement](iohideventdriver/2967293-parseaccelelement.md)
- [- parseBiometricElement](iohideventdriver/2824267-parsebiometricelement.md)
- [- parseCompassElement](iohideventdriver/2967294-parsecompasselement.md)
- [- parseDeviceOrientationElement](iohideventdriver/2967295-parsedeviceorientationelement.md)
- [- parseDigitizerElement](iohideventdriver/1528330-parsedigitizerelement.md)
- [- parseDigitizerTransducerElement](iohideventdriver/1528355-parsedigitizertransducerelement.md)
- [- parseElements](iohideventdriver/1528391-parseelements.md)
- [- parseGameControllerElement](iohideventdriver/1528399-parsegamecontrollerelement.md)
- [- parseGestureUnicodeElement](iohideventdriver/1528372-parsegestureunicodeelement.md)
- [- parseGyroElement](iohideventdriver/2967296-parsegyroelement.md)
- [- parseKeyboardElement](iohideventdriver/1528398-parsekeyboardelement.md)
- [- parseLEDElement](iohideventdriver/1528312-parseledelement.md)
- [- parseLegacyUnicodeElement](iohideventdriver/1528313-parselegacyunicodeelement.md)
- [- parseMultiAxisElement](iohideventdriver/1528401-parsemultiaxiselement.md)
- [- parsePhaseElement](iohideventdriver/3603594-parsephaseelement.md)
- [- parseProximityElement](iohideventdriver/3698196-parseproximityelement.md)
- [- parseRelativeElement](iohideventdriver/1528354-parserelativeelement.md)
- [- parseScrollElement](iohideventdriver/1528353-parsescrollelement.md)
- [- parseSensorPropertyElement](iohideventdriver/2967297-parsesensorpropertyelement.md)
- [- parseTemperatureElement](iohideventdriver/2967298-parsetemperatureelement.md)
- [- parseUnicodeElement](iohideventdriver/1528323-parseunicodeelement.md)
- [- parseVendorMessageElement](iohideventdriver/2765561-parsevendormessageelement.md)
- [- processDigitizerElements](iohideventdriver/1528383-processdigitizerelements.md)
- [- processGameControllerElements](iohideventdriver/1528346-processgamecontrollerelements.md)
- [- processLEDElements](iohideventdriver/3589475-processledelements.md)
- [- processMultiAxisElements](iohideventdriver/1528387-processmultiaxiselements.md)
- [- processUnicodeElements](iohideventdriver/1528358-processunicodeelements.md)
- [- serializeCharacterGestureState](iohideventdriver/1528337-serializecharactergesturestate.md)
- [- serializeDebugState](iohideventdriver/2765565-serializedebugstate.md)
- [- setAccelProperties](iohideventdriver/2967299-setaccelproperties.md)
- [- setAccelerationProperties](iohideventdriver/2765560-setaccelerationproperties.md)
- [- setBiometricProperties](iohideventdriver/2824268-setbiometricproperties.md)
- [- setCompassProperties](iohideventdriver/2967300-setcompassproperties.md)
- [- setDeviceOrientationProperties](iohideventdriver/2967301-setdeviceorientationproperties.md)
- [- setDigitizerProperties](iohideventdriver/1528341-setdigitizerproperties.md)
- [- setElementValue](iohideventdriver/1528325-setelementvalue.md)
- [- setGameControllerProperties](iohideventdriver/1528402-setgamecontrollerproperties.md)
- [- setGyroProperties](iohideventdriver/2967302-setgyroproperties.md)
- [- setKeyboardProperties](iohideventdriver/1528388-setkeyboardproperties.md)
- [- setLEDProperties](iohideventdriver/1528317-setledproperties.md)
- [- setMultiAxisProperties](iohideventdriver/1528333-setmultiaxisproperties.md)
- [- setProperties](iohideventdriver/1528368-setproperties.md)
- [- setRelativeProperties](iohideventdriver/1528332-setrelativeproperties.md)
- [- setScrollProperties](iohideventdriver/1528316-setscrollproperties.md)
- [- setSensorProperties](iohideventdriver/2967303-setsensorproperties.md)
- [- setSurfaceDimensions](iohideventdriver/3516596-setsurfacedimensions.md)
- [- setTemperatureProperties](iohideventdriver/2967304-settemperatureproperties.md)
- [- setUnicodeProperties](iohideventdriver/1528314-setunicodeproperties.md)
- [- setVendorMessageProperties](iohideventdriver/2765562-setvendormessageproperties.md)
### Type Methods
- [+ calibrateCenteredPreferredStateElement](iohideventdriver/1528359-calibratecenteredpreferredstatee.md)
- [+ calibrateJustifiedPreferredStateElement](iohideventdriver/1528342-calibratejustifiedpreferredstate.md)

## Relationships

### Inherits From
- [IOHIDEventService](iohideventservice.md)

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
- [IOHIDEventService](iohideventservice.md)
  IOService represents an device or OS service in IOKit and DriverKit.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohideventdriver)*