# IODetailedTimingInformationV2

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
typedef struct IODetailedTimingInformationV2 {
    ...
} IODetailedTimingInformationV2;
```

## Topics

### Instance Properties
- [bitsPerColorComponent](./iodetailedtiminginformationv2/api-2937879-bitspercolorcomponent.md)
- [colorimetry](./iodetailedtiminginformationv2/api-2937850-colorimetry.md)
- [dscCompressedBitsPerPixel](./iodetailedtiminginformationv2/api-3131301-dsccompressedbitsperpixel.md)
- [dscSliceHeight](./iodetailedtiminginformationv2/api-3131302-dscsliceheight.md)
- [dscSliceWidth](./iodetailedtiminginformationv2/api-3131303-dscslicewidth.md)
- [dynamicRange](./iodetailedtiminginformationv2/api-2937839-dynamicrange.md)
- [horizontalActive](./iodetailedtiminginformationv2/api-1505825-horizontalactive.md)
  Pixel clocks per line.
- [horizontalBlanking](./iodetailedtiminginformationv2/api-1505116-horizontalblanking.md)
  Blanking clocks per line.
- [horizontalBorderLeft](./iodetailedtiminginformationv2/api-1506121-horizontalborderleft.md)
  Number of pixels in left horizontal border.
- [horizontalBorderRight](./iodetailedtiminginformationv2/api-1505214-horizontalborderright.md)
  Number of pixels in right horizontal border.
- [horizontalScaled](./iodetailedtiminginformationv2/api-1505336-horizontalscaled.md)
  If the mode is scaled, sets the size of the image before scaling or rotation.
- [horizontalScaledInset](./iodetailedtiminginformationv2/api-1505675-horizontalscaledinset.md)
  If the mode is scaled, sets the number of active pixels to remove the left and right edges in order to display an underscanned image.
- [horizontalSyncConfig](./iodetailedtiminginformationv2/api-1505470-horizontalsyncconfig.md)
  kIOSyncPositivePolarity for positive polarity horizontal sync (0 for negative).
- [horizontalSyncLevel](./iodetailedtiminginformationv2/api-1505554-horizontalsynclevel.md)
  Zero.
- [horizontalSyncOffset](./iodetailedtiminginformationv2/api-1505654-horizontalsyncoffset.md)
  First clock of horizontal sync.
- [horizontalSyncPulseWidth](./iodetailedtiminginformationv2/api-1505982-horizontalsyncpulsewidth.md)
  Width of horizontal sync.
- [maxPixelClock](./iodetailedtiminginformationv2/api-1505269-maxpixelclock.md)
  Maximum pixel clock frequency in Hz, with error.
- [minPixelClock](./iodetailedtiminginformationv2/api-1506146-minpixelclock.md)
  Minimum pixel clock frequency in Hz, with error.
- [numLinks](./iodetailedtiminginformationv2/api-1505253-numlinks.md)
  number of links to be used by a dual link timing, if zero, assume one link.
- [pixelClock](./iodetailedtiminginformationv2/api-1505625-pixelclock.md)
  Pixel clock frequency in Hz.
- [pixelEncoding](./iodetailedtiminginformationv2/api-2937889-pixelencoding.md)
- [scalerFlags](./iodetailedtiminginformationv2/api-1505247-scalerflags.md)
  If the mode is scaled, kIOScaleStretchToFit may be set to allow stretching. kIOScaleRotateFlags is mask which may have the value given by kIOScaleRotate90, kIOScaleRotate180, kIOScaleRotate270 to display a rotated framebuffer.
- [signalConfig](./iodetailedtiminginformationv2/api-1505078-signalconfig.md)
  Information about display setup.
- [signalLevels](./iodetailedtiminginformationv2/api-1505108-signallevels.md)
  Specifies the signal level. 
- [verticalActive](./iodetailedtiminginformationv2/api-1505884-verticalactive.md)
  Number of lines per frame.
- [verticalBlanking](./iodetailedtiminginformationv2/api-1505807-verticalblanking.md)
  Blanking lines per frame.
- [verticalBlankingExtension](./iodetailedtiminginformationv2/api-2870095-verticalblankingextension.md)
- [verticalBlankingMaxShrinkPerFrame](./iodetailedtiminginformationv2/api-3753269-verticalblankingmaxshrinkperfram.md)
- [verticalBlankingMaxStretchPerFrame](./iodetailedtiminginformationv2/api-3753270-verticalblankingmaxstretchperfra.md)
- [verticalBorderBottom](./iodetailedtiminginformationv2/api-1506113-verticalborderbottom.md)
  Number of lines in bottom vertical border.
- [verticalBorderTop](./iodetailedtiminginformationv2/api-1505205-verticalbordertop.md)
  Number of lines in top vertical border.
- [verticalScaled](./iodetailedtiminginformationv2/api-1505368-verticalscaled.md)
  If the mode is scaled, sets the size of the image before scaling or rotation.
- [verticalScaledInset](./iodetailedtiminginformationv2/api-1505081-verticalscaledinset.md)
  If the mode is scaled, sets the number of active lines to remove the top and bottom edges in order to display an underscanned image.
- [verticalSyncConfig](./iodetailedtiminginformationv2/api-1506078-verticalsyncconfig.md)
  kIOSyncPositivePolarity for positive polarity vertical sync (0 for negative).
- [verticalSyncLevel](./iodetailedtiminginformationv2/api-1505614-verticalsynclevel.md)
  Zero.
- [verticalSyncOffset](./iodetailedtiminginformationv2/api-1506166-verticalsyncoffset.md)
  First line of vertical sync.
- [verticalSyncPulseWidth](./iodetailedtiminginformationv2/api-1505756-verticalsyncpulsewidth.md)
  Height of vertical sync.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iodetailedtiminginformationv2)*