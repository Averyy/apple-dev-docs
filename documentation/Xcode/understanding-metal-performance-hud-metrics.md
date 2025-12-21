# Understanding the Metal Performance HUD metrics

**Framework**: Xcode

Learn what each of the metrics reported by the heads-up display indicates.

#### Overview

The Metal Performance HUD provides a variety of performance metrics to help you spot performance issues, or find the perfect scope to capture in Xcode (see [`Capturing a Metal workload in Xcode`](capturing-a-metal-workload-in-xcode.md)) or in Instruments (see [`Analyzing the performance of your Metal app`](analyzing-the-performance-of-your-metal-app.md)).

> **Note**:  To learn more about how to customize the Metal Performance HUD and enable various metrics, see [`Customizing the Metal Performance HUD`](customizing-metal-performance-hud.md).

Below is a complete list of the Metal Performance HUD metrics:

> ❗ **Important**:  The metrics below require that you enable the encoder GPU time tracking feature. To learn more, see [`Customizing the Metal Performance HUD`](customizing-metal-performance-hud.md).

> ❗ **Important**:  The metrics below only appear when you use specific MetalFX effects in your app. To learn more about MetalFX, see [`MetalFX`](https://developer.apple.com/documentation/MetalFX).

> ❗ **Important**:  The metrics below only appear when you evaluate your game through the Game Porting Toolkit evaluation environment. To learn more, see [`Game Porting Toolkit`](https://developer.apple.comhttps://developer.apple.com/games/game-porting-toolkit/).

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
- [Gaining performance insights with the Metal Performance HUD](gaining-performance-insights-with-metal-performance-hud.md)
  Catch potential performance issues while your app runs using the Metal heads-up display.
- [Generating performance reports with the Metal Performance HUD](generating-performance-reports-with-metal-performance-hud.md)
  Record your app’s performance using the heads-up display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/understanding-metal-performance-hud-metrics)*