---
source: game-porting-toolkit
framework: game-porting-toolkit
url: https://github.com/apple/game-porting-toolkit/blob/main/docs/metal-shader-converter/binding-model.md
---

# The Metal Shader Converter binding model

> Part of the [Metal Shader Converter integration guides](README.md).

This guide explains how shaders converted by Metal Shader Converter bind their resources at runtime: the top-level Argument Buffer, root signatures versus the automatic linear layout, resource encoding, synchronization, and the Metal-specific constraints you need to observe. For pipeline wiring (vertex fetch, hybrid pipelines, runtime feature toggles), see [Pipeline setup](pipeline-setup.md).

## The top-level Argument Buffer

In order to use the Metal IR, you bind global shader resources to your pipeline states via a "top-level" Argument Buffer. Metal Shader Converter offers two mechanisms to control the layout of the resource handles in the top-level Argument Buffer: an explicit mode via root signatures, and an automatic "linear" layout.

The top-level Argument Buffer is a resource shared between the CPU and GPU and, as such, you need to coordinate access to its memory to avoid race conditions. See [Top-level Argument Buffer synchronization](#top-level-argument-buffer-synchronization) below for best practices.

## Explicit layout via root signatures

Use root signatures for maximum flexibility at resource binding time.

When you provide a root signature, or the input IR embeds one, Metal Shader Converter generates a layout for the top-level Argument Buffer that matches your specification. In particular, root signatures allow you to define the following resources in the top-level Argument Buffer:

- Inline constant data ("root constants") of arbitrary size.
- Pointers to Metal resources ("root arguments"). Pointers are 64-bit unsigned values corresponding to the `gpuAddress` or `resourceID` of the resource to reference. Note: textures need to always be placed in descriptor tables.
- Pointers to a resource table ("descriptor table"). In Metal you implement this table via Argument Buffers. Each entry in the table consists of three 64-bit unsigned values: a buffer GPU address, a texture handle, and flags. Use `IRDescriptorTableEntry` in the runtime companion header to correctly calculate offsets and cast pointer types.

After Metal Shader Converter generates its output IR, calculate the offsets of each resource in the top-level Argument Buffer by taking the size of the root constants in bytes (if present), and adding the resource index multiplied by `sizeof(uint64_t)`, while observing that Metal Shader Converter adds padding to achieve the correct alignment for each resource type:

- Pointers: 8-byte alignment.
- 32-bit constants: 4-byte alignment.

When you use root signatures, you need to supply `SamplerState` objects in a descriptor table. Metal Shader Converter doesn't support providing samplers in the top-level argument buffer in this mode.

Use the explicit layout approach when porting root signatures or when your game uses bindless resources.

## Automatic linear layout

When you don't provide a root signature to the Metal Shader Converter at conversion time, and the input IR doesn't embed one, Metal Shader Converter automatically generates a linear layout of resources into the top-level Argument Buffer.

This is a simple layout where the top-level Argument Buffer directly references each resource through a small resource descriptor. Just like descriptor tables, each entry in the Argument Buffer consists of three `uint64_t` parameters.

If you use `libmetalirconverter`, you can reflect the Argument Buffer offsets using function:

```c
void IRShaderReflectionGetResourceLocations(
                       IRShaderReflection* reflection,
                       IRResourceLocation* resourceLocations);
```

Alternatively, if you use Metal Shader Converter as a standalone tool, it conveniently writes resource locations into a reflection JSON file when you provide argument `--output-reflection-file`.

The order in which Metal Shader Converter places your resources in the top-level Argument Buffer is implementation-specific. Always reference the offline reflection data to correctly determine resource offsets. See [Reflection](reflection.md).

The runtime companion header provides a helper struct and functions you can use to encode your resources into this Argument Buffer. These helpers start with the prefix `IRDescriptorTable`.

Use the automatic layout mechanism when you don't need to produce a resource hierarchy and your game doesn't use bindless resources.

Because this mechanism avoids one level of indirection, it may provide a performance advantage compared to the explicit layout approach.

## Resource encoding

When you use root descriptors for your top-level Argument Buffer, you encode resource references into it by writing 64-bit GPU addresses (or Metal resource IDs) at their corresponding offsets within the Argument Buffer.

In addition to root resources, the top-level Argument Buffer may reference "descriptor tables" that you need to encode using a specific format.

This specific format also applies to resources the top-level Argument Buffer directly references when you generate an automatic linear layout of resources (i.e., when you do not provide a root signature to Metal Shader Converter).

The Metal Shader Converter companion header provides helper functions to help you encode resources into descriptor tables. Use functions `IRDescriptorTableSetBuffer()`, `IRDescriptorTableSetTexture()`, and `IRDescriptorTableSetSampler()` to encode resource references into descriptor tables, depending on the resource type to encode.

You may also implement this encoding yourself without using the runtime header. In this case, resource "descriptors" in descriptor tables always consist of three 64-bit unsigned ints representing the GPU address (for buffers and acceleration structures), the texture resource ID (for textures and sampler bindings), and metadata flags (64 bits) representing:

- For buffers:
    - The buffer length stored in the low 32 bits.
    - A texture buffer view offset stored in 2 bytes left-shifted 32 bits. Metal requires texture buffer views to be aligned to 16 bytes. This offset represents the padding necessary to achieve this alignment.
    - Whether the buffer is a typed buffer (`1`) or not (`0`) in the high bit.
- For textures:
    - The min LOD clamp in the low 32 bits.
    - 0 in the high 32 bits.
- For samplers, the LOD bias as a 32-bit floating point number.

For a worked example of encoding a descriptor table, and full root signature listings (C++ and JSON), see [Reference](reference.md).

## Top-level Argument Buffer synchronization

The top-level Argument Buffer is a shared resource that the CPU and GPU both may access simultaneously, and as such, you need to coordinate access to its memory to avoid race conditions.

In the Metal execution model, you first encode the work to perform into a command buffer, and then the GPU carries out your commands later, after you commit it. If each draw call modifies the top-level Argument Buffer as a shared resource, when the GPU executes your commands, only the last modification to the Argument Buffer is visible to the pipeline.

Furthermore, when your application handles multiple frames in flight, the CPU could overwrite memory locations the GPU is reading from.

To avoid these situations, you can provide each draw call with its own top-level Argument Buffer. While you can manage these as discrete or `MTLHeap`-based allocations, it would necessitate having one Argument Buffer per draw call and for each frame in flight. This can become challenging to manage and carry CPU overhead to orchestrate at runtime.

To properly synchronize access without the need to serialize CPU and GPU work, you can use a bump allocator backed by a `MTLBuffer`, or the Metal `setBytes` family of functions.

### Bump allocator

For the best frame encoding performance, implement a bump allocator backed by a `MTLBuffer`.

To achieve this, you first allocate a buffer large enough to contain the data for your frame or render pass. Store an offset tracker alongside this buffer.

When you need to obtain memory, reserve a pointer into the buffer contents at the free offset, and increase the offset's value by the size of the data to write. When binding buffers to Metal Shader Converter pipelines, ensure addresses align to 8 bytes. Repeat the process for each piece of data.

To bind the data to your pipeline, use the `setBuffer:offset:atIndex:` family of functions, with the appropriate offset. Repeat the process for each buffer to write.

Using this technique, and keeping one buffer for each frame in flight, you can completely avoid race conditions without the cost of synchronization primitives.

The [Reference](reference.md#c-bump-allocator) guide presents a simple bump allocator implementation in C++.

### SetBytes functions

You may alternatively leverage the `setBytes:` family of functions in Metal's command encoders (such as `setVertexBytes:offset:index` and `setFragmentBytes:offset:index`) to provide your Argument Buffer as inline data in the `MTLCommandBuffer`.

When using the `setBytes:` family of functions, Metal immediately performs a `memcpy` of your Argument Buffer in the CPU timeline, preserving its contents.

The cost of the `memcpy` operation is linear on the size of your top-level Argument Buffer (smaller buffers are faster to copy), and Metal limits the size of each draw call data to 4KB (per draw call).

In some implementations, Metal may have to allocate a buffer to back the `memcpy` operation, which can add significant CPU overhead to your frame encoding time. For CPU-intensive scenarios, favor using a bump allocator instead.

Follow these steps when moving from a slot-based binding model to the top-level Argument Buffer model via `setBytes`:

1. Write your resource GPU addresses and handles into a CPU struct matching the Argument Buffer's layout.
2. Use the `setBytes:` family of functions to have Metal snapshot your CPU struct into an inline "buffer" at slot `kIRArgumentBufferBindPoint` (`2`).
3. Issue the appropriate `useResource` and `useHeap` calls to signal resource residency (and dependencies) to Metal.

## Other important considerations

### Indirect resources

As with any other Argument Buffers, you need to inform Metal of all resources referenced through the top-level Argument Buffer via the `useResource:usage:` and `useResource:usage:stages:` methods for compute and render pipelines respectively. For read-only `MTLHeap`-backed resources, you may alternatively use `useHeap:`. Resource tables may in turn reference other resources. You need to also call the `useResource:` or `useHeap:` methods to make them resident.

### Texture arrays

HLSL shaders may legally treat textures as texture arrays and vice-versa, and prior to Metal Shader Converter 3.0, it was required that you allocate all Metal texture resources as a texture array — `MTLTextureType2DArray`. With Metal Shader Converter 3.0, this is no longer required, and more importantly, it is no longer the default behavior.

The following table shows the appropriate Metal texture type you need to use for each HLSL texture type when converting shaders with Metal Shader Converter 3.0 or older.

| HLSL | Metal (shader converter 3.0) | Metal (shader converter 2.x) | Mechanism |
|---|---|---|---|
| 1D Texture | 2D Texture | 2D Texture Array | Allocation or texture view |
| 1D Texture Array | 2D Texture Array | 2D Texture Array | |
| 2D Texture | 2D Texture | 2D Texture Array | |
| 2D Texture Array | 2D Texture Array | 2D Texture Array | |
| Cube | Cube | Cube Array | |
| Cube Array | Cube Array | Cube Array | |
| 1D Multisampled Texture | 2D Multisampled Texture | 2D Multisampled Texture Array | |
| 1D Multisampled Texture Array | 2D Multisampled Texture Array | 2D Multisampled Texture Array | |
| 2D Multisampled Texture | 2D Multisampled Texture | 2D Multisampled Texture Array | |
| 2D Multisampled Texture Array | 2D Multisampled Texture Array | 2D Multisampled Texture Array | |
| 3D textures | No change | No change | |

With this change in behavior, you have two options to ensure backward compatibility with your existing Metal Shader Converter apps:

1. Set the new compatibility flag, `IRCompatibilityFlagForceTextureArray`, on `IRCompiler` instances. If using the `metal-shaderconverter` command line tool, add the command option `--forceTextureArray`.
2. At app compile-time, conditionally set the appropriate texture type depending on the Metal Shader Converter version — using the macro `IR_VERSION_MAJOR`:

```c
#if IR_VERSION_MAJOR < 3
textureDesc.textureType = MTLTextureType2DArray;
#else
textureDesc.textureType = MTLTextureType2D;
#endif
```

### NaN/Inf optimization

By default, Metal optimizes floating-point operations under the assumption that their operands are neither NaN nor Inf, which unlocks more aggressive arithmetic simplifications and instruction selection. Prior to Metal Shader Converter 4.0, this optimization was disabled in IR generated by Metal Shader Converter. With Metal Shader Converter 4.0, NaN/Inf optimization is enabled by default to match Metal's default behavior, improving the runtime performance of converted shaders.

If your shaders rely on the strict propagation of NaN or Inf values, set the new compatibility flag, `IRCompatibilityFlagDisableNanInfOptimization`, on `IRCompiler` instances to restore the pre-4.0 behavior. If using the `metal-shaderconverter` command line tool, add the command option `--disableNanInfOptimization`. Apply this flag selectively to shaders known to be sensitive to NaN/Inf handling, so the rest of your pipeline benefits from the new default.

### Sampler state objects

Metal needs to know at resource creation time if your game intends to reference a sampler through an Argument Buffer.

Set the `supportArgumentBuffers` property of the `MTLSamplerDescriptor` to `YES` in order to create sampler state objects that you can bind to Metal Shader Converter pipelines.

Starting in macOS 15 and iOS 18, the Metal debug layer asserts when you obtain the GPU address of a sampler state object that doesn't support argument buffers.

## Related guides

- [Pipeline setup](pipeline-setup.md) — vertex attribute fetch, hybrid pipelines, and runtime feature toggles.
- [Reflection](reflection.md) — determining resource offsets from reflection data.
- [Porting complex pipelines](porting-complex-pipelines.md) — descriptor heaps for dynamic resources, unbounded arrays, and append/consume buffers.
- [Reference](reference.md) — descriptor table encoding example, root signature listings, and a C++ bump allocator.
