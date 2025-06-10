# convertCursorImage

**Framework**: Kernel  
**Kind**: instm

Utility method of IOFramebuffer to convert cursor image to a hardware cursor format.

## Declaration

```swift
virtual bool convertCursorImage(
 void *cursorImage, 
 IOHardwareCursorDescriptor *description, 
 IOHardwareCursorInfo *cursor );
```

#### Return_value

a bool indicating the conversion was successful.

#### Overview

IOFramebuffer subclasses may implement hardware cursor functionality, if so they should pass the cursor image given by the setCursorImage() method, with a description of their hardware cursor format, to this helper function to this routine to convert the image to one suitable for the hardware.

## Parameters

- `cursorImage`: Opaque cursor parameter from the setCursorImage() call.
- `description`: Describes the cursor format supported by the driver.
- `cursor`: Structure describing the drivers allocated buffer to receive the converted image.

## See Also

- [connectFlags](ioframebuffer/1812972-connectflags.md)
  Return display sense information for legacy Apple sensing.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioframebuffer/1812983-convertcursorimage)*