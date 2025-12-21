# Improving your app’s rendering efficiency

**Framework**: Xcode

Optimize view updates by minimizing unnecessary redraws and using efficient update strategies.

#### Overview

Redrawing views unnecessarily, or performing complicated updates, can increase power consumption by the CPU and GPU. Additionally, inefficient view updates can contribute to hangs and hitches in your app, degrading a person’s experience when they use your app. For more information, see [`Understanding user interface responsiveness`](understanding-user-interface-responsiveness.md).

##### Improve Swiftui Performance

Profile your app with the SwiftUI instrument to identify long-running view body updates and frequent view updates in your app, and reorganize your views to avoid these. For more information, see [`Understanding and improving SwiftUI performance`](understanding-and-improving-swiftui-performance.md).

##### Limit the Frame Rate and Duration of Animations

Use animations to communicate changes and updates in your app, and pause or stop them when the update completes. For more information, see [`Foundations > Motion`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/motion) in the Human Interface Guidelines.

For situations where you need precise control over an animation’s behavior, use [`Core Animation`](https://developer.apple.com/documentation/QuartzCore) to provide hints to the system about the preferred frame rates for animations, and to control animation duration. Higher frame rates cause the system to use more power. For more information, see [`Optimizing ProMotion refresh rates for iPhone 13 Pro and iPad Pro`](https://developer.apple.com/documentation/QuartzCore/optimizing-promotion-refresh-rates-for-iphone-13-pro-and-ipad-pro).

##### Update Views Efficiently

Identify when your app updates regions of the screen by choosing Debug > View Debugging > Rendering > Flash Updated Regions in Xcode while it’s running your app. Regions of your app’s display that flash — indicating a screen update — but that don’t noticably change visually indicate unnecessary screen use, and potentially unneccessary computations to prepare the update.

When you need to update a view, calculate the smallest region that needs updating and pass that to [`setNeedsDisplay(_:)`](https://developer.apple.com/documentation/UIKit/UIView/setNeedsDisplay(_:)) (UIKit) or [`setNeedsDisplay(_:)`](https://developer.apple.com/documentation/AppKit/NSView/setNeedsDisplay(_:)) (AppKit), so the system only updates the changed region. Avoid view layouts where updating one layer requires the system to redraw other overlapping layers.

Pay particular attention to the regions you update in views that appear under [`Liquid Glass`](https://developer.apple.com/documentation/TechnologyOverviews/liquid-glass) effects, as the system performs additional calculations to update the Liquid Glass appearance when your app updates screen regions around the Liquid Glass effect.

##### Minimize Complex Effects

When you adopt [`Liquid Glass`](https://developer.apple.com/documentation/TechnologyOverviews/liquid-glass), use [`GlassEffectContainer`](https://developer.apple.com/documentation/SwiftUI/GlassEffectContainer) to combine Liquid Glass effects in multiple views. For more information, see [`Applying Liquid Glass to custom views`](https://developer.apple.com/documentation/SwiftUI/Applying-Liquid-Glass-to-custom-views).

Be careful when grouping views that are spatially distant from each other, as it can cause unnecessary updates. For example, grouping two buttons that are at the top and bottom of the screen respectively means that any change in the middle of the screen causes the system to update both buttons. Use the Flash Updated Regions tool, described in [`Update views efficiently`](improving-your-app-s-rendering-efficiency#Update-views-efficiently.md) above, to assess screen updates due to [`GlassEffectContainer`](https://developer.apple.com/documentation/SwiftUI/GlassEffectContainer) extents.

Prefer simple backgrounds — for example, solid colors — to complex effects like [`UIVisualEffectView`](https://developer.apple.com/documentation/UIKit/UIVisualEffectView).

##### Use Recommended Apis for Media Playback

Where possible, use [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) to play media assets, as it’s optimized to efficiently render audio and video. If you need to use lower-level APIs, measure your app’s power use, and choose the most efficient approach that supports your app’s features. For example, [`AVSampleBufferDisplayLayer`](https://developer.apple.com/documentation/AVFoundation/AVSampleBufferDisplayLayer) typically uses less power to play a video than [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer).

When you use [`VTDecompressionSession`](https://developer.apple.com/documentation/VideoToolbox/VTDecompressionSession-api-collection) to decode video frames that you display in an [`AVSampleBufferDisplayLayer`](https://developer.apple.com/documentation/AVFoundation/AVSampleBufferDisplayLayer), pass [`kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey) as an image buffer attribute to [`VTDecompressionSessionCreate(allocator:formatDescription:decoderSpecification:imageBufferAttributes:decompressionSessionOut:)`](https://developer.apple.com/documentation/VideoToolbox/VTDecompressionSessionCreate(allocator:formatDescription:decoderSpecification:imageBufferAttributes:decompressionSessionOut:)) so that Video Toolbox chooses the most efficient pixel format:

```swift
_ = VTDecompressionSessionCreate(allocator: nil,
                                 formatDescription: formatDescription,
                                 decoderSpecification: nil,
                                 imageBufferAttributes: [kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey],
                                 decompressionSessionOut: &decompressionSession)
```

##### Reduce Average Pixel Luminance in Your App

Brighter pixels use more power than darker pixels, so the lower the average pixel luminance of views in your app, the less energy the system uses powering the display. Support Dark Mode in your app and reduce the overall brightness of the display when someone enables this setting. For more information, see [`Supporting Dark Mode in your interface`](https://developer.apple.com/documentation/UIKit/supporting-dark-mode-in-your-interface).

Measure the average pixel luminance of views in your app using Power Profiler. For more information, see [`Measuring your app’s power use with Power Profiler`](measuring-your-app-s-power-use-with-power-profiler.md). Use [`MXUnitAveragePixelLuminance`](https://developer.apple.com/documentation/MetricKit/MXUnitAveragePixelLuminance) to gather metrics about the pixel luminosity.

## See Also

- [Reducing power usage when capturing media](reducing-power-usage-when-capturing-media.md)
  Optimize device camera power usage by stopping sessions when not needed and choosing appropriate video formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/improving-your-app-s-rendering-efficiency)*