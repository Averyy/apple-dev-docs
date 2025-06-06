# Finding your Metal app’s GPU occupancy

**Framework**: Xcode

Understand the GPU usage for executing shaders by using occupancy.

#### Overview

A GPU has a maximum number of threads that it can execute at the same time.  is a measurement of how much of this capacity the GPU is using. GPUs create new threads when they have commands with more threads to dispatch and enough internal resources. It’s generally better to have higher occupancy when the app is making efficient use of the GPU.

The sum of these percentages is the total percentage of the GPU’s capacity in use.

You can get shader occupancy counters in Instruments and in the Metal debugger’s Performance timeline. For more information, see [`Analyzing the performance of your Metal app`](analyzing-the-performance-of-your-metal-app.md) and [`Analyzing Apple GPU performance using a visual timeline`](analyzing-apple-gpu-performance-using-a-visual-timeline.md).

##### Determine Whether Your App Has Low Gpu Occupancy

Your app may have low occupancy when the overall occupancy measurements aren’t approaching 100%. Each shader has a maximum theoretical occupancy, depending on the amount of internal resources it consumes on the device. You can get this information for each shader in the Performance timeline.

Neither high nor low occupancy is automatically an indicator of a problem. For example, a low vertex shader occupancy may be OK if your fragment shaders are running concurrently with high occupancy. Ultimately, you need to correlate occupancy measurements with measurements from other counters or other Metal tools to determine a problem.

When overall occupancy is low, it likely means one of the following is true:

- Your shaders have exhausted some internal resources, such as thread, threadgroup, or imageblock memory, preventing the GPU from creating more threads.
- Your shaders are simple enough that threads finish executing faster than the GPU can create new ones.
- Your app is rendering to a small area inside the render targets, or dispatching very small compute grids, such that the GPU runs out of threads to create.

For more information on the Performance timeline, see [`Analyzing Apple GPU performance using a visual timeline`](analyzing-apple-gpu-performance-using-a-visual-timeline.md).

##### Determine the Impact on Your App

If you’re seeing overall low occupancy, your next step is to determine whether it’s negatively impacting your app. If an examination of the limiter counters also shows low values, the GPU is executing very little work.

When overall occupancy is high, the GPU is executing many threads to hide instruction latency. High occupancy is generally good because you want to use the GPU to its full potential. However, it’s also possible that your shaders aren’t using the GPU efficiently. Optimizing them can make more of the GPU’s capacity available for other GPU commands.

In rare cases, when overall occupancy is very high, the GPU may execute its workload poorly because threads are competing for space in the GPU’s memory caches (also known as ). In that case, you may need to scale back the amount of work you’re sending to the GPU or change how it accesses (reads or writes) memory. For example, you might try the following:

- Reduce the number of memory accesses.
- Reduce how much memory you access.
- Change the temporal or spatial access patterns you use when accessing memory.

The memory read or write limiter counters may provide more insight into whether your app has a problem. For more information, see [`Reducing shader bottlenecks`](reducing-shader-bottlenecks.md). In addition, use the other counters to determine how effectively you’re using the GPU and where it spends the most time.

## See Also

- [Reducing shader bottlenecks](reducing-shader-bottlenecks.md)
  Identify and minimize congestion points in a GPU’s subsystems by checking its limiter and utilization counters.
- [Measuring the GPU’s use of memory bandwidth](measuring-the-gpus-use-of-memory-bandwidth.md)
  Check whether your Metal app correctly reads and writes to memory by measuring the GPU’s memory bandwidth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/finding-your-metal-apps-gpu-occupancy)*