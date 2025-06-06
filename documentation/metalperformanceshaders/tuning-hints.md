# Tuning Hints

**Framework**: Metal Performance Shaders

#### Overview

The Metal Performance Shaders framework has been tuned for excellent performance across a diversity of devices and kernel parameters. The tuning process focuses on minimizing both CPU and GPU latency for back to back calls on the same command buffer. It is possible, however, to inadvertently undo this optimization effort by introducing costly operations into the pipeline around the kernel, leading to disappointing overall results.

Here are some elements of good practice to avoid common pitfalls:

1. Don’t wait for results to complete before enqueuing more work. There can be a significant delay (up to 2.5 ms) just to get an empty command buffer through the pipeline to where the [`waitUntilCompleted()`](https://developer.apple.com/documentation/metal/mtlcommandbuffer/waituntilcompleted()) method returns. Instead, start encoding the next command buffer(s) while you wait for the first one to complete. Enqueue them too, so they can start immediately after the previous one exits the GPU. Don’t wait for the CPU kernel to notice the first command buffer is done, start taking it apart, and eventually make a callback to the app before beginning work on encoding the next one. By allowing the CPU and GPU to work concurrently in this way, throughput can be enhanced by up to a factor of ten.
2. There is a large cost to allocating buffers and textures. The cost can swamp the CPU, preventing you from keeping the GPU busy. Try to preallocate and reuse the [`MTLResource`](https://developer.apple.com/documentation/metal/mtlresource) objects as much as possible.
3. There is a cost to switching between render and compute encoders. Each time a new render encoder is used, there can be a substantial GPU mode switch cost that may undermine your throughput. To avoid the cost, try to batch compute work together. Since making a new command buffer forces you to make a new command encoder too, try to do more work with fewer command buffers.
4. For some image operations, particularly those involving multiple passes (e.g. chaining multiple image filters together), performance can be improved by up to a factor of two by breaking the work into tiles of ~512 KB in size. Use the [`sourceRegion(destinationSize:)`](mpsunaryimagekernel/1618754-sourceregion.md) method to find the region needed for each tile.

## See Also

- [The MPSKernel Class](the_mpskernel_class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/tuning_hints)*