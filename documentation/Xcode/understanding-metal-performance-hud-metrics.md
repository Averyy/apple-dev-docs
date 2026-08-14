# Understanding the Metal Performance HUD metrics

**Framework**: Xcode

Learn what each of the metrics reported by the heads-up display indicates.

#### Overview

The Metal Performance HUD provides a variety of performance metrics to help you spot performance issues, or find the perfect scope to capture in Xcode (see [`Capturing a Metal workload in Xcode`](capturing-a-metal-workload-in-xcode.md)) or in Instruments (see [`Analyzing the performance of your Metal app`](analyzing-the-performance-of-your-metal-app.md)).

> **Note**:  To learn more about how to customize the Metal Performance HUD and enable various metrics, see [`Customizing the Metal Performance HUD`](customizing-metal-performance-hud.md).

Below is a complete list of the Metal Performance HUD metrics:

- **Metal Device**: Shows the name of the [`MTLDevice`](https://developer.apple.com/documentation/metal/mtldevice).
- **Rosetta Info**: Shows the active architecture (x86_64) if the app runs through the Rosetta translation layer.
- **Layer Size and Composition**: Shows the size of the layer and the present mode (direct or composited).
- **Layer Scale and Pixel Format**: Shows the content scale factor and pixel format of the layer.
- **Memory**: Shows the current amount of memory the process is using, and the [`currentAllocatedSize`](https://developer.apple.com/documentation/metal/mtldevice/currentallocatedsize) of the `MTLDevice`.
- **Thermal State**: Shows the current [`thermalState`](https://developer.apple.com/documentation/foundation/processinfo/thermalstate-swift.property) of the machine.
- **Screen Refresh Rate**: Shows the current refresh rate of the display your app is on.
- **Game Mode**: Shows the state of Game Mode (on or off).
- **FPS**: Shows the rolling average of frames per second for the past 120 frames. FPS is calculated by dividing 1 second with the frame interval.
- **FPS Graph**: Shows a chart graphing the FPS for the past 120 frames.
- **Frame Number**: Shows the current frame number. In most cases this is the number of drawable presents since the app launch or last metric reset. This value counts interpolated frames when you enable frame interpolation.
- **GPU Time**: Shows the rolling average of GPU time for the past 120 frames. GPU time is calculated using the [`gpuStartTime`](https://developer.apple.com/documentation/metal/mtlcommandbuffer/gpustarttime) and  [`gpuEndTime`](https://developer.apple.com/documentation/metal/mtlcommandbuffer/gpuendtime) of the command buffers that get scheduled by Metal for each frame.
- **Present Delay**: Shows the rolling average of present delay for the past 120 frames. Present delay is the interval between the time when you call `presentDrawable` to the time when the drawable hits the display.
- **Frame Interval**: Shows the rolling average of the on-glass time difference between two consecutive `MTLDrawables` for the past 120 frames.
- **Frame Interval Graph**: Shows a chart graphing the frame interval for the past 120 frames.
- **Frame Interval Histogram**: Shows a bucketed frame interval with a bar chart. The bucket size is the display refresh rate.
- **Command Buffer and Encoder Count**: Shows the number of scheduled command buffers and encoders, and their CPU encoding time for the last frame. The CPU time for encoders is the interval between the allocation of command encoder to the end of encoding.
- **Shader Compiler**: Shows the shader compiler activity including number of pipeline states, number of cached shaders, and number of compiled shaders and compilation time. Below the number of compiled shaders is a graph showing the compilation time for the past 120 frames.
- **Disk Usage**: Shows the disk bytes read, written, and logical writes as reported by system usage. To learn more, see [`rusage_info_current`](https://developer.apple.com/documentation/kernel/rusage_info_current).

> ❗ **Important**:  The metrics below require that you enable the encoder GPU time tracking feature. To learn more, see [`Customizing the Metal Performance HUD`](customizing-metal-performance-hud.md).

- **Encoder Time and GPU Timeline**: Shows encoder GPU times for each type of encoder, and a GPU timeline graph. The GPU timeline shows the encoder durations on the GPU for the past three frames every second.
- **Top Labeled Command Buffers**: Shows the most GPU-intensive command buffers with a [`label`](https://developer.apple.com/documentation/metal/mtlcommandbuffer/label) and excludes command buffers without a label.
- **Top Labeled Encoders**: Shows the most GPU-intensive encoders with a [`label`](https://developer.apple.com/documentation/metal/mtlcommandencoder/label) and excludes command encoders without a label.

> ❗ **Important**:  The metrics below only appear when you use specific MetalFX effects in your app. To learn more about MetalFX, see [`MetalFX`](https://developer.apple.com/documentation/metalfx).

- **MetalFX Scaling**: Shows the scaling method of MetalFX (temporal, spatial, or denoising).
- **MetalFX Scaling Input Resolution**: Shows the input resolution of MetalFX scaling.
- **MetalFX Scaling Target Resolution**: Shows the target resolution of MetalFX scaling.
- **MetalFX Exposure**: Shows the exposure of the MetalFX effect.
- **MetalFX Frame Interpolator**: Shows the state of MetalFX frame interpolation (on or off).

> ❗ **Important**:  The metrics below only appear when you evaluate your game through the Game Porting Toolkit evaluation environment. To learn more, see [`Game Porting Toolkit`](https://developer.apple.comhttps://developer.apple.com/games/game-porting-toolkit/).

- **GPTk Draw (GSTS)**: Shows the number of draw calls (`DrawInstanced`, `DrawIndexedInstanced`, `DrawInstancedIndirect`, and `DrawIndexedInstandedIndirect`) with a geometry stage and a tessellation stage.
- **GPTk Draw (TS)**: Shows the number of draw calls (`DrawInstanced`, `DrawIndexedInstanced`, `DrawInstancedIndirect`, and `DrawIndexedInstandedIndirect`) with a tessellation stage.
- **GPTk Draw (GS)**: Shows the number of draw calls (`DrawInstanced`, `DrawIndexedInstanced`, `DrawInstancedIndirect`, and `DrawIndexedInstandedIndirect`) with a geometry stage.
- **GPTk Draw**: Shows the number of draw calls (`DrawInstanced`, `DrawIndexedInstanced`, `DrawInstancedIndirect`, and `DrawIndexedInstandedIndirect`) that don’t use a geometry stage or a tessellation stage.
- **GPTk Execute Indirect**: Shows the number of indirect draw calls or dispatches (`DrawInstancedIndirect`, `DrawIndexedInstandedIndirect`, and `DispatchIndirect`) .
- **GPTk Dispatch**: Shows the number of dispatches (`Dispatch`).
- **GPTk Dispatch Mesh**: Shows the number of draw calls or dispatches (`DrawInstanced`, `DrawIndexedInstanced`, `DrawInstancedIndirect`, `DrawIndexedInstandedIndirect`, `Dispatch`, and `DispatchIndirect`) with a mesh stage.
- **GPTk Copy Resource**: Shows the number of resource copies (`CopyResource`, `CopyBufferRegion`, `UpdateSubResource`, `CopySubResourceRegion`, and `CopyTextureRegion`).
- **GPTk Clear Resource**: Shows the number of clears commands (`ClearRenderTargetView`, `ClearDepthStencilView`, and `ClearUnorderedAccessView`).
- **GPTk Refit BVH**: Shows the number of BVH refits.
- **GPTk Build BVH**: Shows the number of BVH builds.
- **GPTk Display Rays**: Shows the number of ray dispatches.
- **GPTk Ray Query**: Shows the number of ray queries.

## See Also

- [Inspecting live resources at runtime](inspecting-live-resources-at-runtime.md)
  Validate your resources by viewing the contents of your textures and buffers while debugging your Metal app.
- [Validating your app’s Metal API usage](validating-your-apps-metal-api-usage.md)
  Catch runtime issues in your Metal app using API Validation.
- [Validating your app’s Metal shader usage](validating-your-apps-metal-shader-usage.md)
  Catch common shader runtime issues using Shader Validation.
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