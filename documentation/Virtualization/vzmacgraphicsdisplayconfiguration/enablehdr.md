# enableHDR

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the framework enables high dynamic range (HDR) support for the display.

**Availability**:
- macOS 27.3+ (Beta)

## Declaration

```swift
var enableHDR: Bool { get set }
```

```objc
@property BOOL enableHDR;
```

## Discussion

Setting this property to `YES` enables the framework to render HDR content when the display’s first responder view appears on an HDR capable display; otherwise, the framework maps the content to standard dynamic range (SDR). Defaults to `YES`. People may wish to set `enableHDR` to `NO` to reduce power consumption.

> ❗ **Important**: This capability requires a guest VM running macOS 27.3 or later; make sure your app informs people about the availability of this option and its effect on power use when they’re running macOS guests that support it.

Enabling HDR allows, but doesn’t guarantee, HDR output. The display shows SDR content when any of the following conditions are true: - The guest operating system doesn’t support HDR. - The host display the view appears on doesn’t support HDR, or provides only limited HDR headroom of less than or equal to `2.0`. *Headroom* is the ratio of the luminance of the screen’s brightest white to the luminance of SDR white, in the screen’s native color space.

On external HDR-capable host displays that don’t report brightness information the Virtualization framework needs for this feature, the view shows HDR content with a fixed brightness range instead of tracking the host display’s current brightness.

The framework reevaluates the display mode when the VM view moves to a different display on the host.

> **Note**:  It’s possible for a person to have multiple views open for the same VM. When multiple views are open, the framework selects the view that last became the first responder to be the main view, and the framework uses the properties of the display that view runs on (the “main” display) when a guest generates HDR content. Views not on the main display may look suboptimal, since a different display generated the HDR content. If the main display is an SDR display, the VM switches back to SDR.

## See Also

### Configuring the display properties
- [var heightInPixels: Int](./heightinpixels.md)
  The height of the display, in pixels.
- [var widthInPixels: Int](./widthinpixels.md)
  The width of the display, in pixels.
- [var pixelsPerInch: Int](./pixelsperinch.md)
  The pixel density in pixels per inch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacgraphicsdisplayconfiguration/enablehdr)*