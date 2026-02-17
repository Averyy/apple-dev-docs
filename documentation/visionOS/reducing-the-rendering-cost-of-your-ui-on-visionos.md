# Reducing the rendering cost of your UI on visionOS

**Framework**: visionOS

Optimize your 2D user interface rendering on visionOS.

#### Overview

Provide an enjoyable experience and maintain a sense of immersion on Apple Vision Pro by minimizing visual choppiness and interaction latency. Performance bottlenecks that prevent timely rendering and responsive feedback interfere with the spatial experience overall and can cause disorientation or discomfort if they persist over an extended period of time. Your app’s processing and its views have an impact on the work the system does and its ability to meet rendering deadlines. To address bottlenecks in your SwiftUI or UIKit interfaces, first analyze your apps performance, then implement some of the following strategies to reduce CPU and GPU overhead. For more information on performance analysis, see [`Analyzing the performance of your visionOS app`](analyzing-the-performance-of-your-visionos-app.md).

##### Minimize Transparency in Overlapping Views

If you have overlapping UI windows, avoid adding translucency to them. In SwiftUI, avoid setting the value of your view’s [`opacity(_:)`](https://developer.apple.com/documentation/SwiftUI/View/opacity(_:)) below 1. In UIKit, avoid setting the value of your view’s [`alpha`](https://developer.apple.com/documentation/UIKit/UIView/alpha) below 1. Subviews inherit `alpha`.

When a view with transparent pixels overlaps another view, the system performs extra work to composite those views together. The GPU always renders foreground content, but when foreground content is transparent the GPU also renders the UI behind it. When the foreground content is fully opaque, the GPU doesn’t do this rendering.

The Translucent UI Meshes metric in the Core Animation section of the RealityKit Metrics instrument timeline helps you identify translucent UI content your app uses:

![An Instrument window shows profile data from the RealityKit Trace template. The top of the window displays the RealityKit Metrics instrument timeline with a graph of Translucent UI Meshes. The detail view at the bottom of the window displays a summary of the average, minimum, and maximum number of meshes that include transparency.](https://docs-assets.developer.apple.com/published/1941c8f9cc272bb7fa65a8cf9e77a623/translucent-ui-meshes-metric%402x.png)

Other visual effects that involve , the need to draw pixels multiple times to produce a final result, also increase rendering work. In the Shared Space, overdraw can result from interactions with the content from other apps, so minimizing translucent content might have a greater impact. For design guidance, see [`Windows`](https://developer.apple.com/design/Human-Interface-Guidelines/windows#visionOS). Visual effects can also cause offscreen passes. To reduce offscreen passes, see [`Reducing the rendering cost of your UI on visionOS`](reducing-the-rendering-cost-of-your-UI-on-visionOS#Reduce-redraw-and-offscreen-rendering.md).

##### Reduce the Size of Static Ui Views

To lower the GPU overhead of static UI content, reduce the size of UI elements in your view hierarchy. Making your UI content appear larger in a space requires rendering more pixels which requires more rendering work. People still have control over re-sizing content, so use sizes that are large enough for people to be comfortable interacting with, but not so large that they require unnecessary demand from the GPU.

To identify areas in your app where rendering your static UI content creates a lot of overhead for the GPU, check the RealityKit Metrics instrument for 3D Render GPU bottlenecks. Content you display in 2D windows still renders in a space with a 3D mesh. If you expect people to frequently launch multiple windows, account for the rendering cost of this in your design and profile your app with multiple windows open. For design guidance, see [`Spatial layout`](https://developer.apple.com/design/Human-Interface-Guidelines/spatial-layout).

##### Consider the Impact of Dynamic Content Scaling

The system can provide sharper visuals from any angle and distance by altering the resolution of text or vector-based UI content based on where people are looking. Doing so requires drawing content more frequently and at potentially higher scales. SwiftUI and UIKit views enable this by default. To opt in with your custom Core Animation or Core Graphics rendering, enable the [`wantsDynamicContentScaling`](https://developer.apple.com/documentation/QuartzCore/CALayer/wantsDynamicContentScaling) property of any [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer) object. Consider the performance and memory trade-offs and profile your app with this feature on and off to determine if the cost is worth the quality improvement.

For more information on dynamic content scaling, see [`Drawing sharp layer-based content in visionOS`](drawing-sharp-layer-based-content.md) and the section on Dynamic content scaling in the video [`Explore rendering for spatial computing`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10095/?time=793).

##### Reduce Redraw and Offscreen Rendering

The performance cost of numerous redraws and offscreen render passes adds up. Offscreen passes can also contribute to additional overdraw. Some complex renderers require offscreen passes but you can avoid them in many cases. Learn more about offscreen render passes in [`Customizing render pass setup`](https://developer.apple.com/documentation/Metal/customizing-render-pass-setup). To reduce the number of redraw and offscreen render passes your app performs:

- Lower the update rates of animations.
- Pause or stop animations.
- Reduce the number of different views your app uses.
- Avoid layouts that require redrawing overlapping layers when redrawing a different layer.
- Use more efficient alternatives than [`UIVisualEffectView`](https://developer.apple.com/documentation/UIKit/UIVisualEffectView). For example, use background colors in your SwiftUI and UIKit apps.

Similar to other Apple platforms, app updates done in response to input events, timed animations, or other sources initiate UI redraw work in the render server. On visionOS, dynamic content scaling can cause redraw to be frequent in the absence of these updates. This makes it more important to reduce updates and animation timers.

To reduce the cost of redraws and render passes:

- Avoid large layers that might require redrawing a large number of pixels.
- Minimize your use of vector-based media content during active scrolling and animated interactions. Animating large vector-based media content is often expensive.
- Reduce the resolution, type, and number of images in your content that scrolls or animates during interactions.

The number of offscreen render passes can negatively impact performance. Visual effects, like shadows, masking, rounded rectangles, blurs, and vibrancy increase the number of offscreen passes the system requires to render your content.

To identify frequent or expensive UI redraws, check the RealityKit Metrics instrument for Core Animation Encoding (CPU), Core Animation GPU (GPU), Core Animation Server Update (CPU), and Core Animation Client Commit (CPU) bottlenecks.

Minimize view layouts and updates in your SwiftUI, UIKit, or custom Core Animation and Core Graphics rendering when you see a bottleneck related to UI redraw to make your app more efficient for the system to render.

![An Instruments window shows profile data from the RealityKit Trace template. The top of the window displays the RealityKit Metrics instrument timeline which includes a graphs of Offscreen Prepares and Render Passes. The detail view at the bottom of the window displays a summary of the average, minimum, and maximum number for each of these metrics.](https://docs-assets.developer.apple.com/published/74a0b812b098c3fcac0f04d4398fdea3/offscreen-prepares-render-passes-metrics%402x.png)

Review the Offscreen Prepares and Render Passes metrics in the Core Animation Render section of the RealityKit Metrics Instrument to identify the number of potential offscreen render passes and total render passes the render server does on behalf of your app. The section includes metrics on render passes for both offscreen visual effects and for each region of UI content to redraw.

To learn more about these offscreen passes, watch the video [`Demystify and eliminate hitches in the render phase`](https://developer.apple.comhttps://developer.apple.com/videos/play/tech-talks/10857).

##### Avoid Expensive Updates on the Main Thread

To avoid visible hitches and delays while people scroll and resize, reduce time consuming layout and view creations that occur on the app’s main thread. The SwiftUI Instrument template includes the View Body, View Properties, Core Animation Commits, Time Profiler, and Hangs instruments. Use the data these instruments collect to debug expensive commits and updates on your app’s main thread. The Core Animation Commits and Hangs instruments can help you locate areas of expensive work and updates on the app’s main thread that cause rendering delays:

![A screenshot that contains part of an Instruments trace document. It displays a vertical stack of timelines for the View Body, View Properties, Core Animation Commits, Time Profiler, and Hangs instruments. The Core Animation instrument is highlighted with an overlay and includes four blocks that represent Core Animation commit times. The first block starting from the left is orange, the next block is red, and the final two blocks are green. Below the timeline is an an outline view containing a Summary information for the Core Animation Commits instrument. The Hangs instrument is also highlighted with an overlay and includes a single block labeled Brief Unresponsiveness. Below the timeline is an an outline view containing a Summary information for the Hangs instrument.](https://docs-assets.developer.apple.com/published/873da8f3bd40380b133d056257ec2103/core-animation-commits-and-hangs-instruments%402x.png)

To learn more about analyzing Hangs with Instruments, watch [`Analyze hangs with Instruments`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10248).

The View Body and View Properties instruments provide metrics on the number of view body creations and property updates that occur:

![A screenshot that contains part of an Instruments trace document. It displays a vertical stack of timelines for View Body, View Properties, Core Animation Commits, and Time Profiler instruments. The View Properties instrument is highlighted with an overlay and includes a graph visualizing Updates metrics. Below the timeline is an an outline view containing a Summary information for the View Properties instrument. The View Body instrument is also highlighted with an overlay and includes graphs visualizing metrics for RealityKit_SwiftUI, StopwatchSupport, SwiftUI, and you app. Below the timeline is an an outline view containing a Summary information for the View Body instrument.](https://docs-assets.developer.apple.com/published/51c7b3489b5244ce39252b2f6be29fe7/view-properties-and-view-body-instruments%402x.png)

For debugging purposes, you can add a call to the internal method `Self._printChanges()` from the body of the view to log information about the property that caused the view to update.

```swift
var body: some View {
    let _ = Self._printChanges()
    // View code 
}
```

###### Related Articles

###### Related Videos


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/reducing-the-rendering-cost-of-your-ui-on-visionos)*