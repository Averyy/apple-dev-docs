# IONDRVFramebuffer

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IONDRVFramebuffer : IOFramebuffer
```

## Topics

### Instance Methods
- [- checkDriver](iondrvframebuffer/1580204-checkdriver.md)
- [- connectFlags](iondrvframebuffer/1580167-connectflags.md)
- [- createI2C](iondrvframebuffer/1580201-createi2c.md)
- [- displayI2CPower](iondrvframebuffer/1580240-displayi2cpower.md)
- [- doControl](iondrvframebuffer/1580206-docontrol.md)
- [- doDriverIO](iondrvframebuffer/1580192-dodriverio.md)
- [- doI2CRequest](iondrvframebuffer/1580209-doi2crequest.md)
- [- doStatus](iondrvframebuffer/1580237-dostatus.md)
- [- enableController](iondrvframebuffer/1580230-enablecontroller.md)
- [- findVRAM](iondrvframebuffer/1580185-findvram.md)
- [- free](iondrvframebuffer/1580247-free.md)
- [- getApertureRange](iondrvframebuffer/1580217-getaperturerange.md)
- [- getAppleSense](iondrvframebuffer/1580171-getapplesense.md)
- [- getAttribute](iondrvframebuffer/1580231-getattribute.md)
- [- getAttributeForConnection](iondrvframebuffer/1580225-getattributeforconnection.md)
- [- getConnectionCount](iondrvframebuffer/1580212-getconnectioncount.md)
- [- getCurrentConfiguration](iondrvframebuffer/1580246-getcurrentconfiguration.md)
- [- getCurrentDisplayMode](iondrvframebuffer/1580219-getcurrentdisplaymode.md)
- [- getDDCBlock](iondrvframebuffer/1580194-getddcblock.md)
- [- getDisplayModeCount](iondrvframebuffer/1580178-getdisplaymodecount.md)
- [- getDisplayModes](iondrvframebuffer/1580180-getdisplaymodes.md)
- [- getInformationForDisplayMode](iondrvframebuffer/1580197-getinformationfordisplaymode.md)
- [- getMetaClass](iondrvframebuffer/1580193-getmetaclass.md)
- [- getOnlineState](iondrvframebuffer/1580227-getonlinestate.md)
- [- getPixelFormats](iondrvframebuffer/1580183-getpixelformats.md)
- [- getPixelFormatsForDisplayMode](iondrvframebuffer/1580242-getpixelformatsfordisplaymode.md)
- [- getPixelInformation](iondrvframebuffer/1580236-getpixelinformation.md)
- [- getResInfoForArbMode](iondrvframebuffer/1580213-getresinfoforarbmode.md)
- [- getResInfoForDetailed](iondrvframebuffer/1580181-getresinfofordetailed.md)
- [- getResInfoForMode](iondrvframebuffer/1580190-getresinfoformode.md)
- [- getStartupDisplayMode](iondrvframebuffer/1580184-getstartupdisplaymode.md)
- [- getTimingInfoForDisplayMode](iondrvframebuffer/1580218-gettiminginfofordisplaymode.md)
- [- getVRAMRange](iondrvframebuffer/1580166-getvramrange.md)
- [- hasDDCConnect](iondrvframebuffer/1580214-hasddcconnect.md)
- [- initForPM](iondrvframebuffer/1580177-initforpm.md)
- [- initialPowerStateForDomainState](iondrvframebuffer/1580238-initialpowerstatefordomainstate.md)
- [- isConsoleDevice](iondrvframebuffer/1580211-isconsoledevice.md)
- [- iterateAllModes](iondrvframebuffer/1580244-iterateallmodes.md)
- [- makeSubRange](iondrvframebuffer/1580203-makesubrange.md)
- [- mapDepthIndex](iondrvframebuffer/1580222-mapdepthindex.md)
- [- maxCapabilityForDomainState](iondrvframebuffer/1580191-maxcapabilityfordomainstate.md)
- [- ndrvGetSetFeature](iondrvframebuffer/1580224-ndrvgetsetfeature.md)
- [- ndrvSetDisplayPowerState](iondrvframebuffer/1580229-ndrvsetdisplaypowerstate.md)
- [- ndrvSetPowerState](iondrvframebuffer/1580174-ndrvsetpowerstate.md)
- [- ndrvUpdatePowerState](iondrvframebuffer/1580168-ndrvupdatepowerstate.md)
- [- powerStateForDomainState](iondrvframebuffer/1580173-powerstatefordomainstate.md)
- [- probe](iondrvframebuffer/1580172-probe.md)
- [- processConnectChange](iondrvframebuffer/1580170-processconnectchange.md)
- [- registerForInterruptType](iondrvframebuffer/1580221-registerforinterrupttype.md)
- [- requestProbe](iondrvframebuffer/1580234-requestprobe.md)
- [- searchOfflineMode](iondrvframebuffer/1580241-searchofflinemode.md)
- [- setApertureEnable](iondrvframebuffer/1580228-setapertureenable.md)
- [- setAttribute](iondrvframebuffer/1580232-setattribute.md)
- [- setAttributeForConnection](iondrvframebuffer/1580223-setattributeforconnection.md)
- [- setCLUTWithEntries](iondrvframebuffer/1580175-setclutwithentries.md)
- [- setConnectionFlags](iondrvframebuffer/1580202-setconnectionflags.md)
- [- setCursorImage](iondrvframebuffer/1580243-setcursorimage.md)
- [- setCursorState](iondrvframebuffer/1580208-setcursorstate.md)
- [- setDetailedTiming](iondrvframebuffer/1580188-setdetailedtiming.md)
- [- setDetailedTimings](iondrvframebuffer/1580186-setdetailedtimings.md)
- [- setDisplayMode](iondrvframebuffer/1580199-setdisplaymode.md)
- [- setGammaTable](iondrvframebuffer/1580226-setgammatable.md)
- [- setInfoProperties](iondrvframebuffer/1580176-setinfoproperties.md)
- [- setInterruptState](iondrvframebuffer/1580200-setinterruptstate.md)
- [- setMirror](iondrvframebuffer/1580215-setmirror.md)
- [- setProperties](iondrvframebuffer/1580210-setproperties.md)
- [- setStartupDisplayMode](iondrvframebuffer/1580182-setstartupdisplaymode.md)
- [- setupForCurrentConfig](iondrvframebuffer/1580233-setupforcurrentconfig.md)
- [- start](iondrvframebuffer/1580198-start.md)
- [- stop](iondrvframebuffer/1580189-stop.md)
- [- undefinedSymbolHandler](iondrvframebuffer/1580205-undefinedsymbolhandler.md)
- [- unregisterInterrupt](iondrvframebuffer/1580179-unregisterinterrupt.md)
- [- validateDetailedTiming](iondrvframebuffer/1580207-validatedetailedtiming.md)
- [- validateDisplayMode](iondrvframebuffer/1580196-validatedisplaymode.md)
### Type Methods
- [+ VSLDisposeInterruptService](iondrvframebuffer/1580216-vsldisposeinterruptservice.md)
- [+ VSLDoInterruptService](iondrvframebuffer/1580235-vsldointerruptservice.md)
- [+ VSLNewInterruptService](iondrvframebuffer/1580195-vslnewinterruptservice.md)
- [+ VSLPrepareCursorForHardwareCursor](iondrvframebuffer/1580220-vslpreparecursorforhardwarecurso.md)
- [+ extControl](iondrvframebuffer/1580169-extcontrol.md)
- [+ extStatus](iondrvframebuffer/1580239-extstatus.md)

## Relationships

### Inherits From
- [IOFramebuffer](ioframebuffer.md)

## See Also

- [IOFramebuffer](ioframebuffer.md)
  The base class for graphics devices to be made available as part of the desktop.
- [IOGraphicsDevice](iographicsdevice.md)
- [IOFBCursorControlAttribute](iofbcursorcontrolattribute.md)
- [IOFBCursorControlCallouts](iofbcursorcontrolcallouts.md)
- [IOTVector](iotvector.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iondrvframebuffer)*