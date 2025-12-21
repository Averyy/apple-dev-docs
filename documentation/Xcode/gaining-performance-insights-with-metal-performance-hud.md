# Gaining performance insights with the Metal Performance HUD

**Framework**: Xcode

Catch potential performance issues while your app runs using the Metal heads-up display.

#### Overview

To help you optimize performance, the Metal Performance HUD analyzes your app’s Metal API call patterns and automatically flags potential issues. This analysis is available for both native apps and Windows games running through the evaluation environment. Each insight offers links to documentation detailing the issue and outlining methods for resolution.

You can also generate a performance report covering a specific duration to gain deeper insight into your app’s performance during that timeframe. For more information, see [`Generating performance reports with the Metal Performance HUD`](generating-performance-reports-with-metal-performance-hud.md)

Turn on performance insights by setting the `MTL_HUD_INSIGHTS_ENABLED` environment variable to `1`, or through the configuration panel on macOS. See [`Customizing the Metal Performance HUD`](customizing-metal-performance-hud.md) for more details.

```None
export MTL_HUD_INSIGHTS_ENABLED=1
```

![A screenshot showing the Metal Performance HUD insights panel on macOS.](https://docs-assets.developer.apple.com/published/67130492a96d630cbb1c505541a03d6b/metal-hud-config-insights%402x.png)

##### Analyze and Interpret Performance Insights

When performance insights are active, the Metal Performance HUD collects Metal API statistics for every frame. If a pattern suggesting a potential performance issue on Apple GPUs occurs in at least half the frames over a set duration (the default time is 5 seconds), an insight overlay appears alongside the main overlay.

![A screenshot showing a performance insight reported by the Metal Performance HUD.](https://docs-assets.developer.apple.com/published/869904f59e81bc4fb46c5a77e0aab695/metal-hud-app-perf-insights%402x.png)

The HUD identifies four major issue types for native apps and specific D3D12 API usage issues from the Game Porting Toolkit, discussed below.

An excessive number of encoders per frame can be a performance bottleneck on Apple GPUs. The Metal Performance HUD assists in optimizing performance by examining sequential render command encoders to find those with similar color attachments. These encoders are prime candidates for merging by adopting the color attachment mapping feature in Metal 4. Color attachment mapping allows you to define the relationship between logical and physical color attachments for draw operations, thereby allowing a single encoder to utilize a diverse set of color attachments. To learn more, see [`Understanding the Metal 4 core API`](https://developer.apple.com/documentation/Metal/understanding-the-metal-4-core-api).

When the HUD detects this insight, it includes a complete encoding table in the performance report to help you locate these specific encoders. To learn more, see [`Generating performance reports with the Metal Performance HUD`](generating-performance-reports-with-metal-performance-hud.md).

![A screenshot showing the frame encoding table in the performance report.](https://docs-assets.developer.apple.com/published/b163658a4b0f9e914ac3023e2ef9cb32/metal-hud-report-encoding-table%402x.png)

Frequent encoder switching due to resource copies with blit command encoders is another area for potential optimization. This pattern splits the current render or compute encoder into multiple encoders. You can mitigate this overhead by batching resource updates or by adopting Metal 4 command encoding, where blit commands are part of compute command encoders.

Serial, blocking shader compilation during runtime often causes stutters. Metal 4 mitigates this with new shader compilation methods that allow for finer-grained control and increased parallelization.

When the app spends most of the frame interval encoding GPU work, there can be a CPU bottleneck. With Metal 4, you can have more explicit control of command encoding and improve the CPU performance when encoding. See [`Understanding the Metal 4 core API`](https://developer.apple.com/documentation/Metal/understanding-the-metal-4-core-api) for more information.

> ❗ **Important**:  The insights below only appear in the Game Porting Toolkit evaluation environment.

In D3D12, resource barriers are often too coarse, which can lead to oversynchronization when running applications through the Game Porting Toolkit evaluation environment. When porting to Metal, you can use more fine-grained synchronization primitives such as [`MTLFence`](https://developer.apple.com/documentation/Metal/MTLFence) and [`MTLEvent`](https://developer.apple.com/documentation/Metal/MTLEvent) to improve performance.

Apple GPU doesn’t support tessellation and geometry stages directly and needs to be emulated. You can adopt mesh shaders as an alternative to improve performance.

## See Also

- [Inspecting live resources at runtime](inspecting-live-resources-at-runtime.md)
  Validate your resources by viewing the contents of your textures and buffers while debugging your Metal app.
- [Validating your app’s Metal API usage](validating-your-apps-metal-api-usage.md)
  Catch runtime issues in your Metal app using API Validation.
- [Validating your app’s Metal shader usage](validating-your-apps-metal-shader-usage.md)
  Catch common shader runtime issues using Shader Validation while your app is running.
- [Monitoring your Metal app’s graphics performance](monitoring-your-metal-apps-graphics-performance.md)
  Catch performance issues using the Metal Performance HUD while your app runs.
- [Customizing the Metal Performance HUD](customizing-metal-performance-hud.md)
  Modify the appearance of your Metal heads-up display to monitor your graphics performance.
- [Understanding the Metal Performance HUD metrics](understanding-metal-performance-hud-metrics.md)
  Learn what each of the metrics reported by the heads-up display indicates.
- [Generating performance reports with the Metal Performance HUD](generating-performance-reports-with-metal-performance-hud.md)
  Record your app’s performance using the heads-up display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/gaining-performance-insights-with-metal-performance-hud)*