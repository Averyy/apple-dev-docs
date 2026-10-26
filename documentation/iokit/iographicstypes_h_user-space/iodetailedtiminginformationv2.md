# IODetailedTimingInformationV2

**Framework**: IOKit  
**Kind**: tag

A structure defining the detailed timing information of a display mode.

## Declaration

```c
struct IODetailedTimingInformationV2 {
   UInt32 __reservedA[3]; // Init to 0
   UInt32 horizontalScaledInset; // pixels
   UInt32 verticalScaledInset; // lines
   UInt32 scalerFlags;
   UInt32 horizontalScaled;
   UInt32 verticalScaled;
   UInt32 signalConfig;
   UInt32 signalLevels;
   UInt64 pixelClock; // Hz
   UInt64 minPixelClock; // Hz - With error what is slowest actual clock
   UInt64 maxPixelClock; // Hz - With error what is fasted actual clock
   UInt32 horizontalActive; // pixels
   UInt32 horizontalBlanking; // pixels
   UInt32 horizontalSyncOffset; // pixels
   UInt32 horizontalSyncPulseWidth; // pixels
   UInt32 verticalActive; // lines
   UInt32 verticalBlanking; // lines
   UInt32 verticalSyncOffset; // lines
   UInt32 verticalSyncPulseWidth; // lines
   UInt32 horizontalBorderLeft; // pixels
   UInt32 horizontalBorderRight; // pixels
   UInt32 verticalBorderTop; // lines
   UInt32 verticalBorderBottom; // lines
   UInt32 horizontalSyncConfig;
   UInt32 horizontalSyncLevel; // Future use (init to 0)
   UInt32 verticalSyncConfig;
   UInt32 verticalSyncLevel; // Future use (init to 0)
   UInt32 numLinks;
   UInt32 __reservedB[7]; // Init to 0
};
```

#### Overview

This structure is used by IOFramebuffer to define detailed timing information for a display mode. The VESA EDID document has more information.

## Topics

### Fields
- [__reservedA](./iodetailedtiminginformationv2/api-2587781-_reserveda.md)
  Set to zero.
- [horizontalScaledInset](../iodetailedtiminginformationv2/api-1505675-horizontalscaledinset.md)
  If the mode is scaled, sets the number of active pixels to remove the left and right edges in order to display an underscanned image.
- [verticalScaledInset](../iodetailedtiminginformationv2/api-1505081-verticalscaledinset.md)
  If the mode is scaled, sets the number of active lines to remove the top and bottom edges in order to display an underscanned image.
- [scalerFlags](../iodetailedtiminginformationv2/api-1505247-scalerflags.md)
  If the mode is scaled, kIOScaleStretchToFit may be set to allow stretching. kIOScaleRotateFlags is mask which may have the value given by kIOScaleRotate90, kIOScaleRotate180, kIOScaleRotate270 to display a rotated framebuffer.
- [horizontalScaled](../iodetailedtiminginformationv2/api-1505336-horizontalscaled.md)
  If the mode is scaled, sets the size of the image before scaling or rotation.
- [verticalScaled](../iodetailedtiminginformationv2/api-1505368-verticalscaled.md)
  If the mode is scaled, sets the size of the image before scaling or rotation.
- [signalConfig](../iodetailedtiminginformationv2/api-1505078-signalconfig.md)
  Information about display setup.
- [signalLevels](../iodetailedtiminginformationv2/api-1505108-signallevels.md)
  Specifies the signal level. 
- [pixelClock](../iodetailedtiminginformationv2/api-1505625-pixelclock.md)
  Pixel clock frequency in Hz.
- [minPixelClock](../iodetailedtiminginformationv2/api-1506146-minpixelclock.md)
  Minimum pixel clock frequency in Hz, with error.
- [maxPixelClock](../iodetailedtiminginformationv2/api-1505269-maxpixelclock.md)
  Maximum pixel clock frequency in Hz, with error.
- [horizontalActive](../iodetailedtiminginformationv2/api-1505825-horizontalactive.md)
  Pixel clocks per line.
- [horizontalBlanking](../iodetailedtiminginformationv2/api-1505116-horizontalblanking.md)
  Blanking clocks per line.
- [horizontalSyncOffset](../iodetailedtiminginformationv2/api-1505654-horizontalsyncoffset.md)
  First clock of horizontal sync.
- [horizontalSyncPulseWidth](../iodetailedtiminginformationv2/api-1505982-horizontalsyncpulsewidth.md)
  Width of horizontal sync.
- [verticalActive](../iodetailedtiminginformationv2/api-1505884-verticalactive.md)
  Number of lines per frame.
- [verticalBlanking](../iodetailedtiminginformationv2/api-1505807-verticalblanking.md)
  Blanking lines per frame.
- [verticalSyncOffset](../iodetailedtiminginformationv2/api-1506166-verticalsyncoffset.md)
  First line of vertical sync.
- [verticalSyncPulseWidth](../iodetailedtiminginformationv2/api-1505756-verticalsyncpulsewidth.md)
  Height of vertical sync.
- [horizontalBorderLeft](../iodetailedtiminginformationv2/api-1506121-horizontalborderleft.md)
  Number of pixels in left horizontal border.
- [horizontalBorderRight](../iodetailedtiminginformationv2/api-1505214-horizontalborderright.md)
  Number of pixels in right horizontal border.
- [verticalBorderTop](../iodetailedtiminginformationv2/api-1505205-verticalbordertop.md)
  Number of lines in top vertical border.
- [verticalBorderBottom](../iodetailedtiminginformationv2/api-1506113-verticalborderbottom.md)
  Number of lines in bottom vertical border.
- [horizontalSyncConfig](../iodetailedtiminginformationv2/api-1505470-horizontalsyncconfig.md)
  kIOSyncPositivePolarity for positive polarity horizontal sync (0 for negative).
- [horizontalSyncLevel](../iodetailedtiminginformationv2/api-1505554-horizontalsynclevel.md)
  Zero.
- [verticalSyncConfig](../iodetailedtiminginformationv2/api-1506078-verticalsyncconfig.md)
  kIOSyncPositivePolarity for positive polarity vertical sync (0 for negative).
- [verticalSyncLevel](../iodetailedtiminginformationv2/api-1505614-verticalsynclevel.md)
  Zero.
- [numLinks](../iodetailedtiminginformationv2/api-1505253-numlinks.md)
  number of links to be used by a dual link timing, if zero, assume one link.
- [__reservedB](./iodetailedtiminginformationv2/api-2587782-_reservedb.md)
  Reserved set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iographicstypes_h_user-space/iodetailedtiminginformationv2)*