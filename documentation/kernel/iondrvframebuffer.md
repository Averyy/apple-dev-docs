# IONDRVFramebuffer

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IONDRVFramebuffer : IOFramebuffer
```

## Topics

### Instance Methods
- [- checkDriver](./iondrvframebuffer/api-1580204-checkdriver.md)
- [- connectFlags](./iondrvframebuffer/api-1580167-connectflags.md)
- [- createI2C](./iondrvframebuffer/api-1580201-createi2c.md)
- [- displayI2CPower](./iondrvframebuffer/api-1580240-displayi2cpower.md)
- [- doControl](./iondrvframebuffer/api-1580206-docontrol.md)
- [- doDriverIO](./iondrvframebuffer/api-1580192-dodriverio.md)
- [- doI2CRequest](./iondrvframebuffer/api-1580209-doi2crequest.md)
- [- doStatus](./iondrvframebuffer/api-1580237-dostatus.md)
- [- enableController](./iondrvframebuffer/api-1580230-enablecontroller.md)
- [- findVRAM](./iondrvframebuffer/api-1580185-findvram.md)
- [- free](./iondrvframebuffer/api-1580247-free.md)
- [- getApertureRange](./iondrvframebuffer/api-1580217-getaperturerange.md)
- [- getAppleSense](./iondrvframebuffer/api-1580171-getapplesense.md)
- [- getAttribute](./iondrvframebuffer/api-1580231-getattribute.md)
- [- getAttributeForConnection](./iondrvframebuffer/api-1580225-getattributeforconnection.md)
- [- getConnectionCount](./iondrvframebuffer/api-1580212-getconnectioncount.md)
- [- getCurrentConfiguration](./iondrvframebuffer/api-1580246-getcurrentconfiguration.md)
- [- getCurrentDisplayMode](./iondrvframebuffer/api-1580219-getcurrentdisplaymode.md)
- [- getDDCBlock](./iondrvframebuffer/api-1580194-getddcblock.md)
- [- getDisplayModeCount](./iondrvframebuffer/api-1580178-getdisplaymodecount.md)
- [- getDisplayModes](./iondrvframebuffer/api-1580180-getdisplaymodes.md)
- [- getInformationForDisplayMode](./iondrvframebuffer/api-1580197-getinformationfordisplaymode.md)
- [- getMetaClass](./iondrvframebuffer/api-1580193-getmetaclass.md)
- [- getOnlineState](./iondrvframebuffer/api-1580227-getonlinestate.md)
- [- getPixelFormats](./iondrvframebuffer/api-1580183-getpixelformats.md)
- [- getPixelFormatsForDisplayMode](./iondrvframebuffer/api-1580242-getpixelformatsfordisplaymode.md)
- [- getPixelInformation](./iondrvframebuffer/api-1580236-getpixelinformation.md)
- [- getResInfoForArbMode](./iondrvframebuffer/api-1580213-getresinfoforarbmode.md)
- [- getResInfoForDetailed](./iondrvframebuffer/api-1580181-getresinfofordetailed.md)
- [- getResInfoForMode](./iondrvframebuffer/api-1580190-getresinfoformode.md)
- [- getStartupDisplayMode](./iondrvframebuffer/api-1580184-getstartupdisplaymode.md)
- [- getTimingInfoForDisplayMode](./iondrvframebuffer/api-1580218-gettiminginfofordisplaymode.md)
- [- getVRAMRange](./iondrvframebuffer/api-1580166-getvramrange.md)
- [- hasDDCConnect](./iondrvframebuffer/api-1580214-hasddcconnect.md)
- [- initForPM](./iondrvframebuffer/api-1580177-initforpm.md)
- [- initialPowerStateForDomainState](./iondrvframebuffer/api-1580238-initialpowerstatefordomainstate.md)
- [- isConsoleDevice](./iondrvframebuffer/api-1580211-isconsoledevice.md)
- [- iterateAllModes](./iondrvframebuffer/api-1580244-iterateallmodes.md)
- [- makeSubRange](./iondrvframebuffer/api-1580203-makesubrange.md)
- [- mapDepthIndex](./iondrvframebuffer/api-1580222-mapdepthindex.md)
- [- maxCapabilityForDomainState](./iondrvframebuffer/api-1580191-maxcapabilityfordomainstate.md)
- [- ndrvGetSetFeature](./iondrvframebuffer/api-1580224-ndrvgetsetfeature.md)
- [- ndrvSetDisplayPowerState](./iondrvframebuffer/api-1580229-ndrvsetdisplaypowerstate.md)
- [- ndrvSetPowerState](./iondrvframebuffer/api-1580174-ndrvsetpowerstate.md)
- [- ndrvUpdatePowerState](./iondrvframebuffer/api-1580168-ndrvupdatepowerstate.md)
- [- powerStateForDomainState](./iondrvframebuffer/api-1580173-powerstatefordomainstate.md)
- [- probe](./iondrvframebuffer/api-1580172-probe.md)
- [- processConnectChange](./iondrvframebuffer/api-1580170-processconnectchange.md)
- [- registerForInterruptType](./iondrvframebuffer/api-1580221-registerforinterrupttype.md)
- [- requestProbe](./iondrvframebuffer/api-1580234-requestprobe.md)
- [- searchOfflineMode](./iondrvframebuffer/api-1580241-searchofflinemode.md)
- [- setApertureEnable](./iondrvframebuffer/api-1580228-setapertureenable.md)
- [- setAttribute](./iondrvframebuffer/api-1580232-setattribute.md)
- [- setAttributeForConnection](./iondrvframebuffer/api-1580223-setattributeforconnection.md)
- [- setCLUTWithEntries](./iondrvframebuffer/api-1580175-setclutwithentries.md)
- [- setConnectionFlags](./iondrvframebuffer/api-1580202-setconnectionflags.md)
- [- setCursorImage](./iondrvframebuffer/api-1580243-setcursorimage.md)
- [- setCursorState](./iondrvframebuffer/api-1580208-setcursorstate.md)
- [- setDetailedTiming](./iondrvframebuffer/api-1580188-setdetailedtiming.md)
- [- setDetailedTimings](./iondrvframebuffer/api-1580186-setdetailedtimings.md)
- [- setDisplayMode](./iondrvframebuffer/api-1580199-setdisplaymode.md)
- [- setGammaTable](./iondrvframebuffer/api-1580226-setgammatable.md)
- [- setInfoProperties](./iondrvframebuffer/api-1580176-setinfoproperties.md)
- [- setInterruptState](./iondrvframebuffer/api-1580200-setinterruptstate.md)
- [- setMirror](./iondrvframebuffer/api-1580215-setmirror.md)
- [- setProperties](./iondrvframebuffer/api-1580210-setproperties.md)
- [- setStartupDisplayMode](./iondrvframebuffer/api-1580182-setstartupdisplaymode.md)
- [- setupForCurrentConfig](./iondrvframebuffer/api-1580233-setupforcurrentconfig.md)
- [- start](./iondrvframebuffer/api-1580198-start.md)
- [- stop](./iondrvframebuffer/api-1580189-stop.md)
- [- undefinedSymbolHandler](./iondrvframebuffer/api-1580205-undefinedsymbolhandler.md)
- [- unregisterInterrupt](./iondrvframebuffer/api-1580179-unregisterinterrupt.md)
- [- validateDetailedTiming](./iondrvframebuffer/api-1580207-validatedetailedtiming.md)
- [- validateDisplayMode](./iondrvframebuffer/api-1580196-validatedisplaymode.md)
### Type Methods
- [+ VSLDisposeInterruptService](./iondrvframebuffer/api-1580216-vsldisposeinterruptservice.md)
- [+ VSLDoInterruptService](./iondrvframebuffer/api-1580235-vsldointerruptservice.md)
- [+ VSLNewInterruptService](./iondrvframebuffer/api-1580195-vslnewinterruptservice.md)
- [+ VSLPrepareCursorForHardwareCursor](./iondrvframebuffer/api-1580220-vslpreparecursorforhardwarecurso.md)
- [+ extControl](./iondrvframebuffer/api-1580169-extcontrol.md)
- [+ extStatus](./iondrvframebuffer/api-1580239-extstatus.md)

## Relationships

### Inherits From
- [IOFramebuffer](./ioframebuffer.md)

## See Also

### Devices
- [IOFramebuffer](./ioframebuffer.md)
  The base class for graphics devices to be made available as part of the desktop.
- [IOGraphicsDevice](./iographicsdevice.md)
- [IOFBCursorControlAttribute](./iofbcursorcontrolattribute.md)
- [IOFBCursorControlCallouts](./iofbcursorcontrolcallouts.md)
- [IOTVector](./iotvector.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iondrvframebuffer)*