# Measuring the GPU’s use of memory bandwidth

**Framework**: Xcode

Check whether your Metal app correctly reads and writes to memory by measuring the GPU’s memory bandwidth.

#### Overview

The Instruments developer tool and the Metal debugger’s Performance timeline provide bandwidth counters (see [`Analyzing the performance of your Metal app`](analyzing-the-performance-of-your-metal-app.md) and [`Analyzing Apple GPU performance using a visual timeline`](analyzing-apple-gpu-performance-using-a-visual-timeline.md), respectively). The GPU bandwidth counters measure how much, in gigabytes per second, the GPU reads and writes, or  memory.

You may want your app to use a high amount of bandwidth for some activities — such as copying data quickly to save time — and lower bandwidth for others to save energy or to let the CPU and other processes access memory. If the GPU’s memory bandwidth usage is high when you don’t expect it to be, it may impede the CPU’s memory accesses.

You can reduce a GPU’s memory bandwidth with the following strategies in your passes:

- Read only the data your pass needs.
- Write only the data that a subsequent pass needs.
- Load and store only the attachments that a render pass needs.
- Create textures that use only the appropriate [`MTLTextureUsage`](https://developer.apple.com/documentation/Metal/MTLTextureUsage) attributes.

Metal can reduce your app’s memory bandwidth by optimizing the memory accesses to your textures that have the correct usage attributes. To set a texture’s usage appropriately, configure an [`MTLTextureDescriptor`](https://developer.apple.com/documentation/Metal/MTLTextureDescriptor) instance’s [`usage`](https://developer.apple.com/documentation/Metal/MTLTextureDescriptor/usage) property and create a texture with it.

Buffer and texture operations can also increase your app’s memory bandwidth. To check whether the limiter counters for buffer or texture operations are too high, and to learn what you can do to reduce their impact, see [`Reducing shader bottlenecks`](reducing-shader-bottlenecks.md).

> 💡 **Tip**: The Dependencies viewer in the Metal debugger can help you find opportunities to reduce memory bandwidth in your render and compute passes. See [`Analyzing resource dependencies`](analyzing-resource-dependencies.md).

## See Also

- [Finding your Metal app’s GPU occupancy](finding-your-metal-apps-gpu-occupancy.md)
  Understand the GPU usage for executing shaders by using occupancy.
- [Reducing shader bottlenecks](reducing-shader-bottlenecks.md)
  Identify and minimize congestion points in a GPU’s subsystems by checking its limiter and utilization counters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/measuring-the-gpus-use-of-memory-bandwidth)*