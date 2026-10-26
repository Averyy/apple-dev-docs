# verticalBorderBottom

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Number of lines in bottom vertical border.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
UInt32 verticalBorderBottom;
```

## See Also

### Fields
- [__reservedA](../iographicstypes_h_user-space/iodetailedtiminginformationv2/api-2587781-_reserveda.md)
  Set to zero.
- [horizontalScaledInset](./api-1505675-horizontalscaledinset.md)
  If the mode is scaled, sets the number of active pixels to remove the left and right edges in order to display an underscanned image.
- [verticalScaledInset](./api-1505081-verticalscaledinset.md)
  If the mode is scaled, sets the number of active lines to remove the top and bottom edges in order to display an underscanned image.
- [scalerFlags](./api-1505247-scalerflags.md)
  If the mode is scaled, kIOScaleStretchToFit may be set to allow stretching. kIOScaleRotateFlags is mask which may have the value given by kIOScaleRotate90, kIOScaleRotate180, kIOScaleRotate270 to display a rotated framebuffer.
- [horizontalScaled](./api-1505336-horizontalscaled.md)
  If the mode is scaled, sets the size of the image before scaling or rotation.
- [verticalScaled](./api-1505368-verticalscaled.md)
  If the mode is scaled, sets the size of the image before scaling or rotation.
- [signalConfig](./api-1505078-signalconfig.md)
  Information about display setup.
- [signalLevels](./api-1505108-signallevels.md)
  Specifies the signal level. 
- [pixelClock](./api-1505625-pixelclock.md)
  Pixel clock frequency in Hz.
- [minPixelClock](./api-1506146-minpixelclock.md)
  Minimum pixel clock frequency in Hz, with error.
- [maxPixelClock](./api-1505269-maxpixelclock.md)
  Maximum pixel clock frequency in Hz, with error.
- [horizontalActive](./api-1505825-horizontalactive.md)
  Pixel clocks per line.
- [horizontalBlanking](./api-1505116-horizontalblanking.md)
  Blanking clocks per line.
- [horizontalSyncOffset](./api-1505654-horizontalsyncoffset.md)
  First clock of horizontal sync.
- [horizontalSyncPulseWidth](./api-1505982-horizontalsyncpulsewidth.md)
  Width of horizontal sync.
- [verticalActive](./api-1505884-verticalactive.md)
  Number of lines per frame.
- [verticalBlanking](./api-1505807-verticalblanking.md)
  Blanking lines per frame.
- [verticalSyncOffset](./api-1506166-verticalsyncoffset.md)
  First line of vertical sync.
- [verticalSyncPulseWidth](./api-1505756-verticalsyncpulsewidth.md)
  Height of vertical sync.
- [horizontalBorderLeft](./api-1506121-horizontalborderleft.md)
  Number of pixels in left horizontal border.
- [horizontalBorderRight](./api-1505214-horizontalborderright.md)
  Number of pixels in right horizontal border.
- [verticalBorderTop](./api-1505205-verticalbordertop.md)
  Number of lines in top vertical border.
- [horizontalSyncConfig](./api-1505470-horizontalsyncconfig.md)
  kIOSyncPositivePolarity for positive polarity horizontal sync (0 for negative).
- [horizontalSyncLevel](./api-1505554-horizontalsynclevel.md)
  Zero.
- [verticalSyncConfig](./api-1506078-verticalsyncconfig.md)
  kIOSyncPositivePolarity for positive polarity vertical sync (0 for negative).
- [verticalSyncLevel](./api-1505614-verticalsynclevel.md)
  Zero.
- [numLinks](./api-1505253-numlinks.md)
  number of links to be used by a dual link timing, if zero, assume one link.
- [__reservedB](../iographicstypes_h_user-space/iodetailedtiminginformationv2/api-2587782-_reservedb.md)
  Reserved set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iodetailedtiminginformationv2/1506113-verticalborderbottom)*