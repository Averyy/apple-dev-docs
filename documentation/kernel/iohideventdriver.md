# IOHIDEventDriver

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.12.2+ - Deprecated in 10.15.1

## Declaration

```cpp
class IOHIDEventDriver : IOHIDEventService
```

## Topics

### Instance Methods
- [- checkGameControllerElement](./iohideventdriver/api-1528396-checkgamecontrollerelement.md)
- [- checkMultiAxisElement](./iohideventdriver/api-1528393-checkmultiaxiselement.md)
- [- conformTo](./iohideventdriver/api-2765566-conformto.md)
- [- copyEvent](./iohideventdriver/api-2967287-copyevent.md)
- [- copyMatchingEvent](./iohideventdriver/api-3081665-copymatchingevent.md)
- [- createDigitizerTransducerEventForReport](./iohideventdriver/api-2765564-createdigitizertransducereventfo.md)
- [- didTerminate](./iohideventdriver/api-1528375-didterminate.md)
- [- dispatchEvent](./iohideventdriver/api-2765568-dispatchevent.md)
- [- free](./iohideventdriver/api-1528363-free.md)
- [- getBlessedUsagePairs](./iohideventdriver/api-3042840-getblessedusagepairs.md)
- [- getButtonStateFromElements](./iohideventdriver/api-3753515-getbuttonstatefromelements.md)
- [- getCountryCode](./iohideventdriver/api-1528357-getcountrycode.md)
- [- getElementValue](./iohideventdriver/api-1528377-getelementvalue.md)
- [- getLocationID](./iohideventdriver/api-1528339-getlocationid.md)
- [- getManufacturer](./iohideventdriver/api-1528395-getmanufacturer.md)
- [- getMetaClass](./iohideventdriver/api-1528381-getmetaclass.md)
- [- getProduct](./iohideventdriver/api-1528374-getproduct.md)
- [- getProductID](./iohideventdriver/api-1528319-getproductid.md)
- [- getReportElements](./iohideventdriver/api-1528369-getreportelements.md)
- [- getSerialNumber](./iohideventdriver/api-1528329-getserialnumber.md)
- [- getTransport](./iohideventdriver/api-1528347-gettransport.md)
- [- getVendorID](./iohideventdriver/api-1528335-getvendorid.md)
- [- getVendorIDSource](./iohideventdriver/api-1528328-getvendoridsource.md)
- [- getVersion](./iohideventdriver/api-1528380-getversion.md)
- [- handleAccelReport](./iohideventdriver/api-2967288-handleaccelreport.md)
- [- handleBiometricReport](./iohideventdriver/api-2824266-handlebiometricreport.md)
- [- handleBootPointingReport](./iohideventdriver/api-1528386-handlebootpointingreport.md)
- [- handleCompassReport](./iohideventdriver/api-2967289-handlecompassreport.md)
- [- handleDeviceOrientationReport](./iohideventdriver/api-2967290-handledeviceorientationreport.md)
- [- handleDigitizerCollectionReport](./iohideventdriver/api-2765567-handledigitizercollectionreport.md)
- [- handleDigitizerReport](./iohideventdriver/api-1528385-handledigitizerreport.md)
- [- handleDigitizerTransducerReport](./iohideventdriver/api-1528321-handledigitizertransducerreport.md)
- [- handleGameControllerReport](./iohideventdriver/api-1528404-handlegamecontrollerreport.md)
- [- handleGyroReport](./iohideventdriver/api-2967291-handlegyroreport.md)
- [- handleInterruptReport](./iohideventdriver/api-1528364-handleinterruptreport.md)
- [- handleKeboardReport](./iohideventdriver/api-1528336-handlekeboardreport.md)
- [- handleMultiAxisPointerReport](./iohideventdriver/api-1528370-handlemultiaxispointerreport.md)
- [- handlePhaseReport](./iohideventdriver/api-3603593-handlephasereport.md)
- [- handleProximityReport](./iohideventdriver/api-3698195-handleproximityreport.md)
- [- handleRelativeReport](./iohideventdriver/api-1528361-handlerelativereport.md)
- [- handleScrollReport](./iohideventdriver/api-1528390-handlescrollreport.md)
- [- handleStart](./iohideventdriver/api-1528338-handlestart.md)
- [- handleStop](./iohideventdriver/api-1528345-handlestop.md)
- [- handleTemperatureReport](./iohideventdriver/api-2967292-handletemperaturereport.md)
- [- handleUnicodeGestureCandidateReport](./iohideventdriver/api-1528350-handleunicodegesturecandidaterep.md)
- [- handleUnicodeGestureReport](./iohideventdriver/api-1528340-handleunicodegesturereport.md)
- [- handleUnicodeLegacyReport](./iohideventdriver/api-1528379-handleunicodelegacyreport.md)
- [- handleUnicodeReport](./iohideventdriver/api-1528351-handleunicodereport.md)
- [- handleVendorMessageReport](./iohideventdriver/api-2765563-handlevendormessagereport.md)
- [- init](./iohideventdriver/api-1528326-init.md)
- [- parseAccelElement](./iohideventdriver/api-2967293-parseaccelelement.md)
- [- parseBiometricElement](./iohideventdriver/api-2824267-parsebiometricelement.md)
- [- parseCompassElement](./iohideventdriver/api-2967294-parsecompasselement.md)
- [- parseDeviceOrientationElement](./iohideventdriver/api-2967295-parsedeviceorientationelement.md)
- [- parseDigitizerElement](./iohideventdriver/api-1528330-parsedigitizerelement.md)
- [- parseDigitizerTransducerElement](./iohideventdriver/api-1528355-parsedigitizertransducerelement.md)
- [- parseElements](./iohideventdriver/api-1528391-parseelements.md)
- [- parseGameControllerElement](./iohideventdriver/api-1528399-parsegamecontrollerelement.md)
- [- parseGestureUnicodeElement](./iohideventdriver/api-1528372-parsegestureunicodeelement.md)
- [- parseGyroElement](./iohideventdriver/api-2967296-parsegyroelement.md)
- [- parseKeyboardElement](./iohideventdriver/api-1528398-parsekeyboardelement.md)
- [- parseLEDElement](./iohideventdriver/api-1528312-parseledelement.md)
- [- parseLegacyUnicodeElement](./iohideventdriver/api-1528313-parselegacyunicodeelement.md)
- [- parseMultiAxisElement](./iohideventdriver/api-1528401-parsemultiaxiselement.md)
- [- parsePhaseElement](./iohideventdriver/api-3603594-parsephaseelement.md)
- [- parseProximityElement](./iohideventdriver/api-3698196-parseproximityelement.md)
- [- parseRelativeElement](./iohideventdriver/api-1528354-parserelativeelement.md)
- [- parseScrollElement](./iohideventdriver/api-1528353-parsescrollelement.md)
- [- parseSensorPropertyElement](./iohideventdriver/api-2967297-parsesensorpropertyelement.md)
- [- parseTemperatureElement](./iohideventdriver/api-2967298-parsetemperatureelement.md)
- [- parseUnicodeElement](./iohideventdriver/api-1528323-parseunicodeelement.md)
- [- parseVendorMessageElement](./iohideventdriver/api-2765561-parsevendormessageelement.md)
- [- processDigitizerElements](./iohideventdriver/api-1528383-processdigitizerelements.md)
- [- processGameControllerElements](./iohideventdriver/api-1528346-processgamecontrollerelements.md)
- [- processLEDElements](./iohideventdriver/api-3589475-processledelements.md)
- [- processMultiAxisElements](./iohideventdriver/api-1528387-processmultiaxiselements.md)
- [- processUnicodeElements](./iohideventdriver/api-1528358-processunicodeelements.md)
- [- serializeCharacterGestureState](./iohideventdriver/api-1528337-serializecharactergesturestate.md)
- [- serializeDebugState](./iohideventdriver/api-2765565-serializedebugstate.md)
- [- setAccelProperties](./iohideventdriver/api-2967299-setaccelproperties.md)
- [- setAccelerationProperties](./iohideventdriver/api-2765560-setaccelerationproperties.md)
- [- setBiometricProperties](./iohideventdriver/api-2824268-setbiometricproperties.md)
- [- setCompassProperties](./iohideventdriver/api-2967300-setcompassproperties.md)
- [- setDeviceOrientationProperties](./iohideventdriver/api-2967301-setdeviceorientationproperties.md)
- [- setDigitizerProperties](./iohideventdriver/api-1528341-setdigitizerproperties.md)
- [- setElementValue](./iohideventdriver/api-1528325-setelementvalue.md)
- [- setGameControllerProperties](./iohideventdriver/api-1528402-setgamecontrollerproperties.md)
- [- setGyroProperties](./iohideventdriver/api-2967302-setgyroproperties.md)
- [- setKeyboardProperties](./iohideventdriver/api-1528388-setkeyboardproperties.md)
- [- setLEDProperties](./iohideventdriver/api-1528317-setledproperties.md)
- [- setMultiAxisProperties](./iohideventdriver/api-1528333-setmultiaxisproperties.md)
- [- setProperties](./iohideventdriver/api-1528368-setproperties.md)
- [- setRelativeProperties](./iohideventdriver/api-1528332-setrelativeproperties.md)
- [- setScrollProperties](./iohideventdriver/api-1528316-setscrollproperties.md)
- [- setSensorProperties](./iohideventdriver/api-2967303-setsensorproperties.md)
- [- setSurfaceDimensions](./iohideventdriver/api-3516596-setsurfacedimensions.md)
- [- setTemperatureProperties](./iohideventdriver/api-2967304-settemperatureproperties.md)
- [- setUnicodeProperties](./iohideventdriver/api-1528314-setunicodeproperties.md)
- [- setVendorMessageProperties](./iohideventdriver/api-2765562-setvendormessageproperties.md)
### Type Methods
- [+ calibrateCenteredPreferredStateElement](./iohideventdriver/api-1528359-calibratecenteredpreferredstatee.md)
- [+ calibrateJustifiedPreferredStateElement](./iohideventdriver/api-1528342-calibratejustifiedpreferredstate.md)

## Relationships

### Inherits From
- [IOHIDEventService](./iohideventservice.md)

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
- [IOHIDEventService](./iohideventservice.md)
  IOService represents an device or OS service in IOKit and DriverKit.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohideventdriver)*