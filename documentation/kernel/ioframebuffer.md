# IOFramebuffer

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

The base class for graphics devices to be made available as part of the desktop.

**Availability**:
- macOS 10.0+

> **Deprecated**: The IOFramebuffer class only enables simple framebuffer operation, which is not sufficient for the full macOS user experience. This class is not intended for use by third-party device drivers and is documented for informational purposes only.

## Declaration

```cpp
class IOFramebuffer : IOGraphicsDevice
```

#### Overview

The IOFramebuffer base class defines APIs used to publish a linear framebuffer device. Device driver writers should subclass this class to provide a X native driver. macOS will also utilize 'ndrv' drivers via a subclass of IOFramebuffer IONDRVFramebuffer that does not require device driver writers to provide a X native driver.

There are no in kernel clients of IOFramebuffer aside from rudimentary console and panic UI supported by the IOFramebuffer class. The IOFramebuffer class provides the IOUserClient implementation to allow the CoreGraphics server to provide the user accessible interface to all displays on a macOS system, and this is further layered underneath application frameworks. Device driver writers should not need any knowledge of this part of the interfaces. Similarly the instance variables of IOFramebuffer are mostly used for cursor rendering which is handled by the IOFramebuffer class, and should be avoided by subclass implementors. Only IOFramebuffer methods with header documentation in this header are designed for subclasses to implement.

IOFramebuffer provides simple framebuffer operation - acceleration for 2D, 3D and video may be provided by a separate implementation of the IOAccelerator class.

## Topics

### Miscellaneous
- [connectFlags](./ioframebuffer/api-1812972-connectflags.md)
  Return display sense information for legacy Apple sensing.
- [convertCursorImage](./ioframebuffer/api-1812983-convertcursorimage.md)
  Utility method of IOFramebuffer to convert cursor image to a hardware cursor format.
- [doI2CRequest](./ioframebuffer/api-1812996-doi2crequest.md)
  Carry out an I2C request.
- [enableController](./ioframebuffer/api-1813011-enablecontroller.md)
  Perform first time setup of the framebuffer.
- [flushCursor](./ioframebuffer/api-1813022-flushcursor.md)
  Perform any needed cache flushing after software cursor rendering.
- [getApertureRange](./ioframebuffer/api-1813036-getaperturerange.md)
  Return reference to IODeviceMemory object representing memory range of framebuffer.
- [getAppleSense](./ioframebuffer/api-1813053-getapplesense.md)
  Return display sense information for legacy Apple sensing.
- [getAttribute](./ioframebuffer/api-1813070-getattribute.md)
  Generic method to retrieve some attribute of the framebuffer device.
- [getAttributeForConnection](./ioframebuffer/api-1813093-getattributeforconnection.md)
  Generic method to retrieve some attribute of the framebuffer device, specific to one display connection.
- [getConnectionCount](./ioframebuffer/api-1813110-getconnectioncount.md)
  Reports the number of display connections the device supports, driven from one framebuffer.
- [getCurrentDisplayMode(IODisplayModeID *, IOIndex *)](./ioframebuffer/api-1813145-getcurrentdisplaymode.md)
  Return the framebuffers display mode and depth to be used during boot and at startup.
- [getDDCBlock](./ioframebuffer/api-1813183-getddcblock.md)
  Return display EDID data.
- [getDisplayModeCount](./ioframebuffer/api-1813210-getdisplaymodecount.md)
  Return the number of display modes the framebuffer supports.
- [getDisplayModes](./ioframebuffer/api-1813237-getdisplaymodes.md)
  Return the number of display modes the framebuffer supports.
- [getInformationForDisplayMode](./ioframebuffer/api-1813269-getinformationfordisplaymode.md)
  Return information about a given display mode.
- [getPixelFormats](./ioframebuffer/api-1813303-getpixelformats.md)
  List the pixel formats the framebuffer supports.
- [getPixelFormatsForDisplayMode](./ioframebuffer/api-1813329-getpixelformatsfordisplaymode.md)
  Obsolete.
- [getPixelInformation](./ioframebuffer/api-1813353-getpixelinformation.md)
  Return information about the framebuffer format for a given display mode and depth.
- [getStartupDisplayMode](./ioframebuffer/api-1813382-getstartupdisplaymode.md)
  Return the framebuffers display mode and depth to be used during boot and at startup.
- [getTimingInfoForDisplayMode](./ioframebuffer/api-1813413-gettiminginfofordisplaymode.md)
  Returns a timing description for a display mode.
- [getVRAMRange](./ioframebuffer/api-1813443-getvramrange.md)
  Return reference to IODeviceMemory object representing memory range of all the cards vram.
- [handleEvent](./ioframebuffer/api-1813481-handleevent.md)
  Notify IOFramebuffer superclass code of events.
- [hasDDCConnect](./ioframebuffer/api-1813510-hasddcconnect.md)
  Return display DDC connect state.
- [readDDCClock](./ioframebuffer/api-1813550-readddcclock.md)
  Reads the input state of the I2C clock line on a bus.
- [readDDCData](./ioframebuffer/api-1813593-readddcdata.md)
  Reads the input state of the I2C data line on a bus.
- [registerForInterruptType](./ioframebuffer/api-1813622-registerforinterrupttype.md)
  Set callbacks for driver to call on interrupt events.
- [setApertureEnable](./ioframebuffer/api-1813646-setapertureenable.md)
  Enable an aperture on the framebuffer (usually unimplemented, no OS usage).
- [setAttribute](./ioframebuffer/api-1813661-setattribute.md)
  Generic method to set some attribute of the framebuffer device.
- [setAttributeForConnection](./ioframebuffer/api-1813672-setattributeforconnection.md)
  Generic method to set some attribute of the framebuffer device, specific to one display connection.
- [setCLUTWithEntries](./ioframebuffer/api-1813680-setclutwithentries.md)
  Set the color lookup table to be used by the framebuffer in indexed modes.
- [setCurrentDisplayMode](./ioframebuffer/api-1813685-setcurrentdisplaymode.md)
  Set the framebuffers current display mode and depth.
- [setCursorImage](./ioframebuffer/api-1813692-setcursorimage.md)
  Set a new image for the hardware cursor.
- [setCursorState](./ioframebuffer/api-1813699-setcursorstate.md)
  Set a new position and visibility for the hardware cursor.
- [setDDCClock](./ioframebuffer/api-1813707-setddcclock.md)
  Sets the state of the I2C clock line on a bus.
- [setDDCData](./ioframebuffer/api-1813718-setddcdata.md)
  Sets the state of the I2C data line on a bus.
- [setDetailedTimings](./ioframebuffer/api-1813724-setdetailedtimings.md)
  Installs an array of OS programmed detailed timings to be made available by the driver.
- [setDisplayMode](./ioframebuffer/api-1813732-setdisplaymode.md)
  Set the framebuffers current display mode and depth.
- [setGammaTable](./ioframebuffer/api-1813739-setgammatable.md)
  Set the gamma table to be used by the framebuffer.
- [setInterruptState](./ioframebuffer/api-1813744-setinterruptstate.md)
  Enable or disable a callback previously installed by registerForInterruptType().
- [setStartupDisplayMode](./ioframebuffer/api-1813749-setstartupdisplaymode.md)
  Set the framebuffers display mode and depth to be used during boot and at startup.
- [unregisterInterrupt(void *)](./ioframebuffer/api-1813753-unregisterinterrupt.md)
  Remove a callback previously installed by registerForInterruptType().
- [unregisterInterrupt(void *, UInt32)](./ioframebuffer/api-1813757-unregisterinterrupt.md)
  Enable or disable a callback previously installed by registerForInterruptType().
- [validateDetailedTiming](./ioframebuffer/api-1813761-validatedetailedtiming.md)
  Reports whether a detailed timing is able to be programmed with the device.
### DataTypes
- [ExpansionData](./ioservice/expansiondata.md)
### Instance Variables
- [reserved](./ioframebuffer/reserved.md)
### Instance Methods
- [- addFramebufferNotification](./ioframebuffer/api-1397685-addframebuffernotification.md)
- [- addFramebufferNotificationWithOptions](./ioframebuffer/api-2880391-addframebuffernotificationwithop.md)
- [- attach](./ioframebuffer/api-2887410-attach.md)
- [- callPlatformFunction](./ioframebuffer/api-1397717-callplatformfunction.md)
- [- close](./ioframebuffer/api-1397604-close.md)
- [- connectFlags](./ioframebuffer/api-1397650-connectflags.md)
- [- convertCursorImage](./ioframebuffer/api-1397625-convertcursorimage.md)
- [- deliverFramebufferNotification](./ioframebuffer/api-1397663-deliverframebuffernotification.md)
- [- diagnoseReport](./ioframebuffer/api-2870089-diagnosereport.md)
- [- didTerminate](./ioframebuffer/api-2870091-didterminate.md)
- [- doI2CRequest](./ioframebuffer/api-1397655-doi2crequest.md)
- [- enableController](./ioframebuffer/api-1397497-enablecontroller.md)
- [- enableDDCRaster](./ioframebuffer/api-1397636-enableddcraster.md)
- [- flushCursor](./ioframebuffer/api-1397507-flushcursor.md)
- [- free](./ioframebuffer/api-1397623-free.md)
- [- getAggressiveness](./ioframebuffer/api-1397520-getaggressiveness.md)
- [- getApertureRange](./ioframebuffer/api-1397597-getaperturerange.md)
- [- getAppleSense](./ioframebuffer/api-1397564-getapplesense.md)
- [- getAttribute](./ioframebuffer/api-1397532-getattribute.md)
- [- getAttributeExt](./ioframebuffer/api-1397574-getattributeext.md)
- [- getAttributeForConnection](./ioframebuffer/api-1397509-getattributeforconnection.md)
- [- getAttributeForConnectionExt](./ioframebuffer/api-1397547-getattributeforconnectionext.md)
- [- getBoundingRect](./ioframebuffer/api-1397576-getboundingrect.md)
- [- getConnectionCount](./ioframebuffer/api-1397501-getconnectioncount.md)
- [- getControllerWorkLoop](./ioframebuffer/api-1397632-getcontrollerworkloop.md)
- [- getCurrentDisplayMode](./ioframebuffer/api-1397549-getcurrentdisplaymode.md)
- [- getDDCBlock](./ioframebuffer/api-1397555-getddcblock.md)
- [- getDisplayModeCount](./ioframebuffer/api-1397671-getdisplaymodecount.md)
- [- getDisplayModes](./ioframebuffer/api-1397527-getdisplaymodes.md)
- [- getGraphicsSystemWorkLoop](./ioframebuffer/api-1397681-getgraphicssystemworkloop.md)
- [- getInformationForDisplayMode](./ioframebuffer/api-1397524-getinformationfordisplaymode.md)
- [- getMetaClass](./ioframebuffer/api-1397505-getmetaclass.md)
- [- getNotificationSemaphore](./ioframebuffer/api-1397669-getnotificationsemaphore.md)
- [- getPixelFormats](./ioframebuffer/api-1397479-getpixelformats.md)
- [- getPixelFormatsForDisplayMode](./ioframebuffer/api-1397499-getpixelformatsfordisplaymode.md)
- [- getPixelInformation](./ioframebuffer/api-1397562-getpixelinformation.md)
- [- getStartupDisplayMode](./ioframebuffer/api-1397608-getstartupdisplaymode.md)
- [- getTimingInfoForDisplayMode](./ioframebuffer/api-1397648-gettiminginfofordisplaymode.md)
- [- getVBLTime](./ioframebuffer/api-1397691-getvbltime.md)
- [- getVRAMRange](./ioframebuffer/api-1397512-getvramrange.md)
- [- getWorkLoop](./ioframebuffer/api-1397659-getworkloop.md)
- [- handleEvent](./ioframebuffer/api-1397606-handleevent.md)
- [- hasDDCConnect](./ioframebuffer/api-1397618-hasddcconnect.md)
- [- hideCursor](./ioframebuffer/api-1397570-hidecursor.md)
- [- isConsoleDevice](./ioframebuffer/api-1397489-isconsoledevice.md)
- [- message](./ioframebuffer/api-2870087-message.md)
- [- moveCursor](./ioframebuffer/api-1397679-movecursor.md)
- [- newUserClient](./ioframebuffer/api-1397536-newuserclient.md)
- [- open](./ioframebuffer/api-1397518-open.md)
- [- powerStateDidChangeTo](./ioframebuffer/api-1397584-powerstatedidchangeto.md)
- [- powerStateWillChangeTo](./ioframebuffer/api-1397665-powerstatewillchangeto.md)
- [- readDDCClock](./ioframebuffer/api-1397472-readddcclock.md)
- [- readDDCData](./ioframebuffer/api-1397689-readddcdata.md)
- [- registerForInterruptType](./ioframebuffer/api-1397721-registerforinterrupttype.md)
- [- requestProbe](./ioframebuffer/api-1397594-requestprobe.md)
- [- requestTerminate](./ioframebuffer/api-1397614-requestterminate.md)
- [- resetCursor](./ioframebuffer/api-1397542-resetcursor.md)
- [- resetLimitState](./ioframebuffer/api-2923479-resetlimitstate.md)
- [- sendLimitState](./ioframebuffer/api-2923478-sendlimitstate.md)
- [- serializeInfo](./ioframebuffer/api-1397667-serializeinfo.md)
- [- setAggressiveness](./ioframebuffer/api-1397491-setaggressiveness.md)
- [- setApertureEnable](./ioframebuffer/api-1397719-setapertureenable.md)
- [- setAttribute](./ioframebuffer/api-1397610-setattribute.md)
- [- setAttributeExt](./ioframebuffer/api-1397560-setattributeext.md)
- [- setAttributeForConnection](./ioframebuffer/api-1397529-setattributeforconnection.md)
- [- setAttributeForConnectionExt](./ioframebuffer/api-1397697-setattributeforconnectionext.md)
- [- setBackingFramebuffer](./ioframebuffer/api-1397592-setbackingframebuffer.md)
- [- setCLUTWithEntries](./ioframebuffer/api-1397460-setclutwithentries.md)
- [- setCursorImage](./ioframebuffer/api-1397616-setcursorimage.md)
- [- setCursorState](./ioframebuffer/api-1397475-setcursorstate.md)
- [- setDDCClock](./ioframebuffer/api-1397553-setddcclock.md)
- [- setDDCData](./ioframebuffer/api-1397450-setddcdata.md)
- [- setDetailedTimings](./ioframebuffer/api-1397715-setdetailedtimings.md)
- [- setDisplayMode](./ioframebuffer/api-1397588-setdisplaymode.md)
- [- setGammaTable](./ioframebuffer/api-1397522-setgammatable.md)
- [- setInterruptState](./ioframebuffer/api-1397677-setinterruptstate.md)
- [- setNumber](./ioframebuffer/api-1397709-setnumber.md)
- [- setPowerState](./ioframebuffer/api-1397723-setpowerstate.md)
- [- setProperties](./ioframebuffer/api-3194323-setproperties.md)
- [- setStartupDisplayMode](./ioframebuffer/api-1397705-setstartupdisplaymode.md)
- [- setupForCurrentConfig](./ioframebuffer/api-1397568-setupforcurrentconfig.md)
- [- showCursor](./ioframebuffer/api-1397470-showcursor.md)
- [- start](./ioframebuffer/api-1397551-start.md)
- [- stop](./ioframebuffer/api-1397578-stop.md)
- [- switchBackingFramebuffer](./ioframebuffer/api-1397481-switchbackingframebuffer.md)
- [- terminate](./ioframebuffer/api-2870090-terminate.md)
- [- unregisterInterrupt](./ioframebuffer/api-1397462-unregisterinterrupt.md)
- [- validateDetailedTiming](./ioframebuffer/api-1397713-validatedetailedtiming.md)
- [- willTerminate](./ioframebuffer/api-2870088-willterminate.md)
### Type Methods
- [+ handleVBL](./ioframebuffer/api-3656573-handlevbl.md)
- [+ initialize](./ioframebuffer/api-1397628-initialize.md)

## Relationships

### Inherits From
- [IOGraphicsDevice](./iographicsdevice.md)

## See Also

### Devices
- [IONDRVFramebuffer](./iondrvframebuffer.md)
- [IOGraphicsDevice](./iographicsdevice.md)
- [IOFBCursorControlAttribute](./iofbcursorcontrolattribute.md)
- [IOFBCursorControlCallouts](./iofbcursorcontrolcallouts.md)
- [IOTVector](./iotvector.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioframebuffer)*