# IOFramebuffer

**Framework**: Kernel  
**Kind**: cl

The base class for graphics devices to be made available as part of the desktop.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOFramebuffer : IOGraphicsDevice
```

#### Overview

The IOFramebuffer base class defines APIs used to publish a linear framebuffer device. Device driver writers should subclass this class to provide a X native driver. macOS will also utilize 'ndrv' drivers via a subclass of IOFramebuffer IONDRVFramebuffer that does not require device driver writers to provide a X native driver.

There are no in kernel clients of IOFramebuffer aside from rudimentary console and panic UI supported by the IOFramebuffer class. The IOFramebuffer class provides the IOUserClient implementation to allow the CoreGraphics server to provide the user accessible interface to all displays on a macOS system, and this is further layered underneath application frameworks. Device driver writers should not need any knowledge of this part of the interfaces. Similarly the instance variables of IOFramebuffer are mostly used for cursor rendering which is handled by the IOFramebuffer class, and should be avoided by subclass implementors. Only IOFramebuffer methods with header documentation in this header are designed for subclasses to implement.

IOFramebuffer provides simple framebuffer operation - acceleration for 2D, 3D and video may be provided by a separate implementation of the IOAccelerator class.

## Topics

### Miscellaneous
- [connectFlags](ioframebuffer/1812972-connectflags.md)
  Return display sense information for legacy Apple sensing.
- [convertCursorImage](ioframebuffer/1812983-convertcursorimage.md)
  Utility method of IOFramebuffer to convert cursor image to a hardware cursor format.
- [doI2CRequest](ioframebuffer/1812996-doi2crequest.md)
  Carry out an I2C request.
- [enableController](ioframebuffer/1813011-enablecontroller.md)
  Perform first time setup of the framebuffer.
- [flushCursor](ioframebuffer/1813022-flushcursor.md)
  Perform any needed cache flushing after software cursor rendering.
- [getApertureRange](ioframebuffer/1813036-getaperturerange.md)
  Return reference to IODeviceMemory object representing memory range of framebuffer.
- [getAppleSense](ioframebuffer/1813053-getapplesense.md)
  Return display sense information for legacy Apple sensing.
- [getAttribute](ioframebuffer/1813070-getattribute.md)
  Generic method to retrieve some attribute of the framebuffer device.
- [getAttributeForConnection](ioframebuffer/1813093-getattributeforconnection.md)
  Generic method to retrieve some attribute of the framebuffer device, specific to one display connection.
- [getConnectionCount](ioframebuffer/1813110-getconnectioncount.md)
  Reports the number of display connections the device supports, driven from one framebuffer.
- [getCurrentDisplayMode(IODisplayModeID *, IOIndex *)](ioframebuffer/1813145-getcurrentdisplaymode.md)
  Return the framebuffers display mode and depth to be used during boot and at startup.
- [getDDCBlock](ioframebuffer/1813183-getddcblock.md)
  Return display EDID data.
- [getDisplayModeCount](ioframebuffer/1813210-getdisplaymodecount.md)
  Return the number of display modes the framebuffer supports.
- [getDisplayModes](ioframebuffer/1813237-getdisplaymodes.md)
  Return the number of display modes the framebuffer supports.
- [getInformationForDisplayMode](ioframebuffer/1813269-getinformationfordisplaymode.md)
  Return information about a given display mode.
- [getPixelFormats](ioframebuffer/1813303-getpixelformats.md)
  List the pixel formats the framebuffer supports.
- [getPixelFormatsForDisplayMode](ioframebuffer/1813329-getpixelformatsfordisplaymode.md)
  Obsolete.
- [getPixelInformation](ioframebuffer/1813353-getpixelinformation.md)
  Return information about the framebuffer format for a given display mode and depth.
- [getStartupDisplayMode](ioframebuffer/1813382-getstartupdisplaymode.md)
  Return the framebuffers display mode and depth to be used during boot and at startup.
- [getTimingInfoForDisplayMode](ioframebuffer/1813413-gettiminginfofordisplaymode.md)
  Returns a timing description for a display mode.
- [getVRAMRange](ioframebuffer/1813443-getvramrange.md)
  Return reference to IODeviceMemory object representing memory range of all the cards vram.
- [handleEvent](ioframebuffer/1813481-handleevent.md)
  Notify IOFramebuffer superclass code of events.
- [hasDDCConnect](ioframebuffer/1813510-hasddcconnect.md)
  Return display DDC connect state.
- [readDDCClock](ioframebuffer/1813550-readddcclock.md)
  Reads the input state of the I2C clock line on a bus.
- [readDDCData](ioframebuffer/1813593-readddcdata.md)
  Reads the input state of the I2C data line on a bus.
- [registerForInterruptType](ioframebuffer/1813622-registerforinterrupttype.md)
  Set callbacks for driver to call on interrupt events.
- [setApertureEnable](ioframebuffer/1813646-setapertureenable.md)
  Enable an aperture on the framebuffer (usually unimplemented, no OS usage).
- [setAttribute](ioframebuffer/1813661-setattribute.md)
  Generic method to set some attribute of the framebuffer device.
- [setAttributeForConnection](ioframebuffer/1813672-setattributeforconnection.md)
  Generic method to set some attribute of the framebuffer device, specific to one display connection.
- [setCLUTWithEntries](ioframebuffer/1813680-setclutwithentries.md)
  Set the color lookup table to be used by the framebuffer in indexed modes.
- [setCurrentDisplayMode](ioframebuffer/1813685-setcurrentdisplaymode.md)
  Set the framebuffers current display mode and depth.
- [setCursorImage](ioframebuffer/1813692-setcursorimage.md)
  Set a new image for the hardware cursor.
- [setCursorState](ioframebuffer/1813699-setcursorstate.md)
  Set a new position and visibility for the hardware cursor.
- [setDDCClock](ioframebuffer/1813707-setddcclock.md)
  Sets the state of the I2C clock line on a bus.
- [setDDCData](ioframebuffer/1813718-setddcdata.md)
  Sets the state of the I2C data line on a bus.
- [setDetailedTimings](ioframebuffer/1813724-setdetailedtimings.md)
  Installs an array of OS programmed detailed timings to be made available by the driver.
- [setDisplayMode](ioframebuffer/1813732-setdisplaymode.md)
  Set the framebuffers current display mode and depth.
- [setGammaTable](ioframebuffer/1813739-setgammatable.md)
  Set the gamma table to be used by the framebuffer.
- [setInterruptState](ioframebuffer/1813744-setinterruptstate.md)
  Enable or disable a callback previously installed by registerForInterruptType().
- [setStartupDisplayMode](ioframebuffer/1813749-setstartupdisplaymode.md)
  Set the framebuffers display mode and depth to be used during boot and at startup.
- [unregisterInterrupt(void *)](ioframebuffer/1813753-unregisterinterrupt.md)
  Remove a callback previously installed by registerForInterruptType().
- [unregisterInterrupt(void *, UInt32)](ioframebuffer/1813757-unregisterinterrupt.md)
  Enable or disable a callback previously installed by registerForInterruptType().
- [validateDetailedTiming](ioframebuffer/1813761-validatedetailedtiming.md)
  Reports whether a detailed timing is able to be programmed with the device.
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [reserved](ioframebuffer/reserved.md)
### Instance Methods
- [- addFramebufferNotification](ioframebuffer/1397685-addframebuffernotification.md)
- [- addFramebufferNotificationWithOptions](ioframebuffer/2880391-addframebuffernotificationwithop.md)
- [- attach](ioframebuffer/2887410-attach.md)
- [- callPlatformFunction](ioframebuffer/1397717-callplatformfunction.md)
- [- close](ioframebuffer/1397604-close.md)
- [- connectFlags](ioframebuffer/1397650-connectflags.md)
- [- convertCursorImage](ioframebuffer/1397625-convertcursorimage.md)
- [- deliverFramebufferNotification](ioframebuffer/1397663-deliverframebuffernotification.md)
- [- diagnoseReport](ioframebuffer/2870089-diagnosereport.md)
- [- didTerminate](ioframebuffer/2870091-didterminate.md)
- [- doI2CRequest](ioframebuffer/1397655-doi2crequest.md)
- [- enableController](ioframebuffer/1397497-enablecontroller.md)
- [- enableDDCRaster](ioframebuffer/1397636-enableddcraster.md)
- [- flushCursor](ioframebuffer/1397507-flushcursor.md)
- [- free](ioframebuffer/1397623-free.md)
- [- getAggressiveness](ioframebuffer/1397520-getaggressiveness.md)
- [- getApertureRange](ioframebuffer/1397597-getaperturerange.md)
- [- getAppleSense](ioframebuffer/1397564-getapplesense.md)
- [- getAttribute](ioframebuffer/1397532-getattribute.md)
- [- getAttributeExt](ioframebuffer/1397574-getattributeext.md)
- [- getAttributeForConnection](ioframebuffer/1397509-getattributeforconnection.md)
- [- getAttributeForConnectionExt](ioframebuffer/1397547-getattributeforconnectionext.md)
- [- getBoundingRect](ioframebuffer/1397576-getboundingrect.md)
- [- getConnectionCount](ioframebuffer/1397501-getconnectioncount.md)
- [- getControllerWorkLoop](ioframebuffer/1397632-getcontrollerworkloop.md)
- [- getCurrentDisplayMode](ioframebuffer/1397549-getcurrentdisplaymode.md)
- [- getDDCBlock](ioframebuffer/1397555-getddcblock.md)
- [- getDisplayModeCount](ioframebuffer/1397671-getdisplaymodecount.md)
- [- getDisplayModes](ioframebuffer/1397527-getdisplaymodes.md)
- [- getGraphicsSystemWorkLoop](ioframebuffer/1397681-getgraphicssystemworkloop.md)
- [- getInformationForDisplayMode](ioframebuffer/1397524-getinformationfordisplaymode.md)
- [- getMetaClass](ioframebuffer/1397505-getmetaclass.md)
- [- getNotificationSemaphore](ioframebuffer/1397669-getnotificationsemaphore.md)
- [- getPixelFormats](ioframebuffer/1397479-getpixelformats.md)
- [- getPixelFormatsForDisplayMode](ioframebuffer/1397499-getpixelformatsfordisplaymode.md)
- [- getPixelInformation](ioframebuffer/1397562-getpixelinformation.md)
- [- getStartupDisplayMode](ioframebuffer/1397608-getstartupdisplaymode.md)
- [- getTimingInfoForDisplayMode](ioframebuffer/1397648-gettiminginfofordisplaymode.md)
- [- getVBLTime](ioframebuffer/1397691-getvbltime.md)
- [- getVRAMRange](ioframebuffer/1397512-getvramrange.md)
- [- getWorkLoop](ioframebuffer/1397659-getworkloop.md)
- [- handleEvent](ioframebuffer/1397606-handleevent.md)
- [- hasDDCConnect](ioframebuffer/1397618-hasddcconnect.md)
- [- hideCursor](ioframebuffer/1397570-hidecursor.md)
- [- isConsoleDevice](ioframebuffer/1397489-isconsoledevice.md)
- [- message](ioframebuffer/2870087-message.md)
- [- moveCursor](ioframebuffer/1397679-movecursor.md)
- [- newUserClient](ioframebuffer/1397536-newuserclient.md)
- [- open](ioframebuffer/1397518-open.md)
- [- powerStateDidChangeTo](ioframebuffer/1397584-powerstatedidchangeto.md)
- [- powerStateWillChangeTo](ioframebuffer/1397665-powerstatewillchangeto.md)
- [- readDDCClock](ioframebuffer/1397472-readddcclock.md)
- [- readDDCData](ioframebuffer/1397689-readddcdata.md)
- [- registerForInterruptType](ioframebuffer/1397721-registerforinterrupttype.md)
- [- requestProbe](ioframebuffer/1397594-requestprobe.md)
- [- requestTerminate](ioframebuffer/1397614-requestterminate.md)
- [- resetCursor](ioframebuffer/1397542-resetcursor.md)
- [- resetLimitState](ioframebuffer/2923479-resetlimitstate.md)
- [- sendLimitState](ioframebuffer/2923478-sendlimitstate.md)
- [- serializeInfo](ioframebuffer/1397667-serializeinfo.md)
- [- setAggressiveness](ioframebuffer/1397491-setaggressiveness.md)
- [- setApertureEnable](ioframebuffer/1397719-setapertureenable.md)
- [- setAttribute](ioframebuffer/1397610-setattribute.md)
- [- setAttributeExt](ioframebuffer/1397560-setattributeext.md)
- [- setAttributeForConnection](ioframebuffer/1397529-setattributeforconnection.md)
- [- setAttributeForConnectionExt](ioframebuffer/1397697-setattributeforconnectionext.md)
- [- setBackingFramebuffer](ioframebuffer/1397592-setbackingframebuffer.md)
- [- setCLUTWithEntries](ioframebuffer/1397460-setclutwithentries.md)
- [- setCursorImage](ioframebuffer/1397616-setcursorimage.md)
- [- setCursorState](ioframebuffer/1397475-setcursorstate.md)
- [- setDDCClock](ioframebuffer/1397553-setddcclock.md)
- [- setDDCData](ioframebuffer/1397450-setddcdata.md)
- [- setDetailedTimings](ioframebuffer/1397715-setdetailedtimings.md)
- [- setDisplayMode](ioframebuffer/1397588-setdisplaymode.md)
- [- setGammaTable](ioframebuffer/1397522-setgammatable.md)
- [- setInterruptState](ioframebuffer/1397677-setinterruptstate.md)
- [- setNumber](ioframebuffer/1397709-setnumber.md)
- [- setPowerState](ioframebuffer/1397723-setpowerstate.md)
- [- setProperties](ioframebuffer/3194323-setproperties.md)
- [- setStartupDisplayMode](ioframebuffer/1397705-setstartupdisplaymode.md)
- [- setupForCurrentConfig](ioframebuffer/1397568-setupforcurrentconfig.md)
- [- showCursor](ioframebuffer/1397470-showcursor.md)
- [- start](ioframebuffer/1397551-start.md)
- [- stop](ioframebuffer/1397578-stop.md)
- [- switchBackingFramebuffer](ioframebuffer/1397481-switchbackingframebuffer.md)
- [- terminate](ioframebuffer/2870090-terminate.md)
- [- unregisterInterrupt](ioframebuffer/1397462-unregisterinterrupt.md)
- [- validateDetailedTiming](ioframebuffer/1397713-validatedetailedtiming.md)
- [- willTerminate](ioframebuffer/2870088-willterminate.md)
### Type Methods
- [+ handleVBL](ioframebuffer/3656573-handlevbl.md)
- [+ initialize](ioframebuffer/1397628-initialize.md)

## Relationships

### Inherits From
- [IOGraphicsDevice](iographicsdevice.md)

## See Also

- [IONDRVFramebuffer](iondrvframebuffer.md)
- [IOGraphicsDevice](iographicsdevice.md)
- [IOFBCursorControlAttribute](iofbcursorcontrolattribute.md)
- [IOFBCursorControlCallouts](iofbcursorcontrolcallouts.md)
- [IOTVector](iotvector.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioframebuffer)*