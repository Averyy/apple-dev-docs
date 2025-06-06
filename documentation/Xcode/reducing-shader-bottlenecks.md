# Reducing shader bottlenecks

**Framework**: Xcode

Identify and minimize congestion points in a GPU’s subsystems by checking its limiter and utilization counters.

#### Overview

A GPU can typically run subtasks at the same time by dispatching them to various subsystems that specialize in different operations, such as memory accesses, math and logic operations, and pixel rasterization. However, the code in an app’s GPU functions (shaders functions and compute kernels) can force some of these subsystems to stall, or wait for either itself to finish an operation or until another subsystem is ready.

The GPU driver publishes its subsystems’ work time and stall times with counters that you can monitor to see how much time those subsystems spend working versus stalling:

- A  counter shows how much time the GPU subsystem is doing work, excluding stall time.
- A  counter shows how much time the GPU spends doing work, including stall time.

Use the following counters as clues to help you identify which GPU subsystems might be a bottleneck at runtime:

| Counter | Limiter counter | Utilization counter | Description |
| --- | --- | --- | --- |
| GPU memory read | Yes | No | Measures the percentage of the GPU’s peak memory read performance. See [`Measuring the GPU’s use of memory bandwidth`](measuring-the-gpus-use-of-memory-bandwidth.md). |
| GPU memory write | Yes | No | Measures the percentage of the GPU’s peak memory write performance. See [`Measuring the GPU’s use of memory bandwidth`](measuring-the-gpus-use-of-memory-bandwidth.md). |
| Memory managament unit (MMU) | Yes | Yes | Measures the time the GPU spends in the memory management unit. |
| Last level cache | Yes | Yes | Measures the time the GPU spends on requests to the highest-level GPU cache. |
| Tile memory read | Yes | Yes | Tile memory is local to the GPU and is synonymous with threadgroup memory and imageblock memory. |
| Tile memory write | Yes | Yes | Tile memory is local to the GPU and is synonymous with threadgroup memory and imageblock memory. |
| Arithmetic logic unit (ALU) | Yes | Yes | Measures the time the GPU spends on arithmetic, logic, and bitwise operations. |
| F16 | No | Yes | Measures the time the GPU spends on 16-bit floating-point operations. |
| F32 | No | Yes | Measures the time the GPU spends on 32-bit floating-point operations. |
| Texture sampling | Yes | Yes | Measures the time the GPU spends on sampling textures. |
| Texture filtering | Yes | No | Measures the time the GPU spends on running texture-filtering operations. |
| Texture read cache | Yes | No | Measures the time the GPU spends in the texture read cache. |
| Texture write | Yes | Yes | Measures the time the GPU spends on writing textures. |
| Buffer read | Yes | Yes | Measures the time the GPU spends reading data from buffers. |
| Buffer write | Yes | Yes | Measures the time the GPU spends writing data to buffers, including any time a GPU function writes to memory in the device address space. |
| Fragment shader input interpolation | Yes | Yes | Measures the time the GPU spends on interpolating inputs to a fragment shader. |

You can monitor the utilization and limiter counters in Instruments’s Metal system trace and in the Metal debugger’s Performance timeline. For more information, see [`Analyzing the performance of your Metal app`](analyzing-the-performance-of-your-metal-app.md) and [`Analyzing Apple GPU performance using a visual timeline`](analyzing-apple-gpu-performance-using-a-visual-timeline.md).

To relieve pressure on specific GPU subsystems and help the GPU run commands more quickly, you can adjust how your GPU functions operate and use resources. Most code adjustments typically belong to several strategies that include the following:

- Reducing the number of operations
- Moving work to another subsystem that’s working less
- Reducing the image quality or mathematical precision of the work
- Accessing memory in ways that improve GPU memory cache hits

Some adjustments have a trade-off, such as reducing image quality or mathematical precision, and it’s up to you to decide which adjustments are worth it for your app.

> 💡 **Tip**: Discover which adjustments yield better performance by experimenting with your app.

Discover which adjustments yield better performance by experimenting with your app.

##### Reduce the Workload of the Arithmetic Logic Unit

The arithmetic logic unit (ALU) handles your code’s arithmetic, logic, and bitwise operations. If the counters indicate the ALU may be a bottleneck, you can try each of the following adjustments and evaluate any changes:

- Replace formulas with approximations.
- Replace floating-point values with with half-floats if they have enough range and precision for your calculations.
- Compile your GPU functions to use the `-ffast-math` Metal compiler flag, which enables optimizations that run faster, but may introduce precision errors (see section 1.5 in the [`Metal Shading Language Specification`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf)).
- Replace complex calculations with lookup tables or textures.

These adjustments reduce the ALU’s workload by making the work simpler or by shifting work to another subsystem, such as a texture sampler. For example, you might eliminate a noise calculation function by creating a noise texture and sampling from it each time your code needs a value.

##### Reduce the Workload for Texture Operations

The GPU reads texture data for each color attachment of a render pass when you set its [`loadAction`](https://developer.apple.com/documentation/Metal/MTLRenderPassAttachmentDescriptor/loadAction) property to [`MTLLoadAction.load`](https://developer.apple.com/documentation/Metal/MTLLoadAction/load), and each time a GPU function reads, gathers, or samples a texture. Textures that have larger dimensions, or use larger pixel formats, consume more memory and typically increase the amount of data the GPU reads to sample the texture.

If the counters indicate the texture  operations may be a bottleneck, you can try the following adjustments and evaluate any changes in your app’s performance:

- Sample from a mipmap for any textures your app uses with a minification filter.
- Select bilinear filtering instead of trilinear filtering.
- Calculate values that are less expensive to compute within the GPU function than reading from a texture.
- Work with textures that have smaller dimensions or use smaller pixel formats.
- Replace reading or sampling single-channel textures with gather operations, which use the GPU more efficiently.

Similarly, the GPU saves texture data for each color attachment of a render pass when you set its [`storeAction`](https://developer.apple.com/documentation/Metal/MTLRenderPassAttachmentDescriptor/storeAction) property to [`MTLStoreAction.store`](https://developer.apple.com/documentation/Metal/MTLStoreAction/store), and each time a GPU function explicitly writes to a texture.

If the counters indicate the texture  operations may be a bottleneck, you can try the following adjustments and evaluate any changes in your app’s performance:

- Work with textures that have smaller dimensions or use smaller pixel formats.
- Reduce the number of samples for multisample antialiasing (MSAA).
- Render fewer very small triangles, especially if you’re applying MSAA as well.
- Modify textures that cluster writes in space or time (higher spatial or temporal locality), which the GPU can coalesce into fewer write transactions to memory.

##### Reduce the Workload for Buffer Operations

The write operation counters measure the time your GPU functions store data to memory in the GPU device’s address space. The read operation counters measure the time your GPU functions fetch data from memory in both the device’s address space and the constants’ address space.

GPU functions can increase the read-and-write activity when they use a lot of thread memory or access it with . This can happen when a function needs to store more data than can fit in the GPU’s registers, which forces the GPU to store data to device memory and then read it at a later time.

If the counters indicate the buffer  or  operations may be a bottleneck, you can try the following adjustments and evaluate any changes in your app’s performance:

- Pack data into buffers more tightly.
- Pack scalar values with SIMD types, such as the `float4` SIMD type instead of four separate `float` values.
- Use smaller data types, such as the `packed_half3` type for positional data instead of `float4`.
- Avoid implementations that randomly index into thread-scoped arrays, which may give the compiler the flexibility to better optimize the GPU function.

For the buffer  operations, you can also try to read data from textures instead of buffers to share some of the workload with another subsystem. For the buffer  operations, try to reduce the number of atomic writes your GPU function makes to device memory.

##### Reduce the Workload for Threadgroup and Imageblock Operations

Apple silicon GPUs use threadgroup memory and imageblock memory (called  collectively) that consists of a local, unified set of high-performance storage within the GPU itself.

You access this high-speed memory when you write to threadgroup memory in a compute shader, write to a pixel in an imageblock, use blending in a render pass, or write data to a color attachment from a fragment shader.

Your app accesses this high-speed memory during a render pass that applies blending, and when:

- A GPU function reads or writes imageblock data
- A fragment shader reads from or writes to a color attachment
- A compute kernel reads from or writes to threadgroup memory

If the counters indicate the threadgroup and imageblock  or  operations may be a bottleneck, you can try the following adjustments in your compute kernels and evaluate any changes in your app’s performance:

- Align threadgroup memory allocations to a 16-byte boundary.
- Reduce a kernel’s atomic reads from or writes to threadgroup memory.
- Reorder your memory access patterns so that neighboring threads in a quad group write (or read) to neighboring elements in threadgroup memory.

For the threadgroup and imageblock  operations, you can also try removing accesses to the same memory location from multiple threads in the same threadgroup.

##### Reduce the Workload for Fragment Input Interpolation

During a render pass, a GPU interpolates the vertex stage’s output data before sending it to the fragment stage. If the counters indicate fragment input interpolation may be a bottleneck, you can try reducing the number of vertex attributes the fragment shader uses.

##### Reduce the Workload of the Last Level Cache

The last level cache counters measure how much time the GPU spends processing requests in the highest-level GPU cache. A higher value here may indicate that your shaders are requesting a lot of data that isn’t present in the cache.

> 💡 **Tip**: Check and improve any bottlenecks in the texture and the buffer operations before trying the adjustments below.

Check and improve any bottlenecks in the texture and the buffer operations before trying the adjustments below.

If the counters indicate the last level cache may be a bottleneck, you can try the following adjustments and evaluate any changes in your app’s performance:

- Reduce the size of the datasets your GPU functions work with.
- Use compressed pixel formats for the textures that your GPU functions only read or sample from.
- Reduce the number of atomic reads from and writes to device memory by storing intermediate results in threadgroup memory and using atomic operations there instead.
- Access memory that clusters reads in space or time (higher spatial or temporal locality), which can reduce cache misses and the subsystem’s workload.

## See Also

- [Finding your Metal app’s GPU occupancy](finding-your-metal-apps-gpu-occupancy.md)
  Understand the GPU usage for executing shaders by using occupancy.
- [Measuring the GPU’s use of memory bandwidth](measuring-the-gpus-use-of-memory-bandwidth.md)
  Check whether your Metal app correctly reads and writes to memory by measuring the GPU’s memory bandwidth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/reducing-shader-bottlenecks)*