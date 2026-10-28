# getTimingInfoForDisplayMode

**Framework**: Kernel  
**Kind**: instm

Returns a timing description for a display mode.

## Declaration

```cpp
virtual IOReturn getTimingInfoForDisplayMode( 
 IODisplayModeIDdisplayMode,
 IOTimingInformation *info );
```

## Return Value

an IOReturn code. A return other than kIOReturnSuccess will prevent the system from using the device.

## Overview

IOFramebuffer subclasses should implement this method to return timing information for a display mode. This allows the OS to enable display modes based on its knowledge of the connected display type. Two types of timing information are defined, by Apple defined constant, or by a detailed description of the timing parameters of the mode.

## Parameters

- `displayMode`: A display mode ID representing the mode to examine.
- `info`: The driver returns the information for the display mode in this structure.

  If the mode has an Apple defined constant, such as timingVESA_1024x768_75hz, it should be returned in the appleTimingID field. Otherwise the field should be set to timingInvalid.

  If the driver is able to supply detailed timing information, it should return it in the detailedInfo.v2 field of the structure, otherwise the driver should clear the kIODetailedTimingValid flag from the flags field.

  The IODetailedTimingInformationV2 structure is documented in IOGraphicsTypes.h

## See Also

### Miscellaneous
- [connectFlags](./api-1812972-connectflags.md)
  Return display sense information for legacy Apple sensing.
- [convertCursorImage](./api-1812983-convertcursorimage.md)
  Utility method of IOFramebuffer to convert cursor image to a hardware cursor format.
- [doI2CRequest](./api-1812996-doi2crequest.md)
  Carry out an I2C request.
- [enableController](./api-1813011-enablecontroller.md)
  Perform first time setup of the framebuffer.
- [flushCursor](./api-1813022-flushcursor.md)
  Perform any needed cache flushing after software cursor rendering.
- [getApertureRange](./api-1813036-getaperturerange.md)
  Return reference to IODeviceMemory object representing memory range of framebuffer.
- [getAppleSense](./api-1813053-getapplesense.md)
  Return display sense information for legacy Apple sensing.
- [getAttribute](./api-1813070-getattribute.md)
  Generic method to retrieve some attribute of the framebuffer device.
- [getAttributeForConnection](./api-1813093-getattributeforconnection.md)
  Generic method to retrieve some attribute of the framebuffer device, specific to one display connection.
- [getConnectionCount](./api-1813110-getconnectioncount.md)
  Reports the number of display connections the device supports, driven from one framebuffer.
- [getCurrentDisplayMode(IODisplayModeID *, IOIndex *)](./api-1813145-getcurrentdisplaymode.md)
  Return the framebuffers display mode and depth to be used during boot and at startup.
- [getDDCBlock](./api-1813183-getddcblock.md)
  Return display EDID data.
- [getDisplayModeCount](./api-1813210-getdisplaymodecount.md)
  Return the number of display modes the framebuffer supports.
- [getDisplayModes](./api-1813237-getdisplaymodes.md)
  Return the number of display modes the framebuffer supports.
- [getInformationForDisplayMode](./api-1813269-getinformationfordisplaymode.md)
  Return information about a given display mode.
- [getPixelFormats](./api-1813303-getpixelformats.md)
  List the pixel formats the framebuffer supports.
- [getPixelFormatsForDisplayMode](./api-1813329-getpixelformatsfordisplaymode.md)
  Obsolete.
- [getPixelInformation](./api-1813353-getpixelinformation.md)
  Return information about the framebuffer format for a given display mode and depth.
- [getStartupDisplayMode](./api-1813382-getstartupdisplaymode.md)
  Return the framebuffers display mode and depth to be used during boot and at startup.
- [getVRAMRange](./api-1813443-getvramrange.md)
  Return reference to IODeviceMemory object representing memory range of all the cards vram.
- [handleEvent](./api-1813481-handleevent.md)
  Notify IOFramebuffer superclass code of events.
- [hasDDCConnect](./api-1813510-hasddcconnect.md)
  Return display DDC connect state.
- [readDDCClock](./api-1813550-readddcclock.md)
  Reads the input state of the I2C clock line on a bus.
- [readDDCData](./api-1813593-readddcdata.md)
  Reads the input state of the I2C data line on a bus.
- [registerForInterruptType](./api-1813622-registerforinterrupttype.md)
  Set callbacks for driver to call on interrupt events.
- [setApertureEnable](./api-1813646-setapertureenable.md)
  Enable an aperture on the framebuffer (usually unimplemented, no OS usage).
- [setAttribute](./api-1813661-setattribute.md)
  Generic method to set some attribute of the framebuffer device.
- [setAttributeForConnection](./api-1813672-setattributeforconnection.md)
  Generic method to set some attribute of the framebuffer device, specific to one display connection.
- [setCLUTWithEntries](./api-1813680-setclutwithentries.md)
  Set the color lookup table to be used by the framebuffer in indexed modes.
- [setCurrentDisplayMode](./api-1813685-setcurrentdisplaymode.md)
  Set the framebuffers current display mode and depth.
- [setCursorImage](./api-1813692-setcursorimage.md)
  Set a new image for the hardware cursor.
- [setCursorState](./api-1813699-setcursorstate.md)
  Set a new position and visibility for the hardware cursor.
- [setDDCClock](./api-1813707-setddcclock.md)
  Sets the state of the I2C clock line on a bus.
- [setDDCData](./api-1813718-setddcdata.md)
  Sets the state of the I2C data line on a bus.
- [setDetailedTimings](./api-1813724-setdetailedtimings.md)
  Installs an array of OS programmed detailed timings to be made available by the driver.
- [setDisplayMode](./api-1813732-setdisplaymode.md)
  Set the framebuffers current display mode and depth.
- [setGammaTable](./api-1813739-setgammatable.md)
  Set the gamma table to be used by the framebuffer.
- [setInterruptState](./api-1813744-setinterruptstate.md)
  Enable or disable a callback previously installed by registerForInterruptType().
- [setStartupDisplayMode](./api-1813749-setstartupdisplaymode.md)
  Set the framebuffers display mode and depth to be used during boot and at startup.
- [unregisterInterrupt(void *)](./api-1813753-unregisterinterrupt.md)
  Remove a callback previously installed by registerForInterruptType().
- [unregisterInterrupt(void *, UInt32)](./api-1813757-unregisterinterrupt.md)
  Enable or disable a callback previously installed by registerForInterruptType().
- [validateDetailedTiming](./api-1813761-validatedetailedtiming.md)
  Reports whether a detailed timing is able to be programmed with the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioframebuffer/1813413-gettiminginfofordisplaymode)*