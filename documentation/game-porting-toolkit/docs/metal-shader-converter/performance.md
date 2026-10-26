---
source: game-porting-toolkit
framework: game-porting-toolkit
url: https://github.com/apple/game-porting-toolkit/blob/main/docs/metal-shader-converter/performance.md
---

# Performance tips

> Part of the [Metal Shader Converter integration guides](README.md).

This guide collects general guidance for getting the best runtime and build-time performance from converted shaders. For ray-tracing-specific tuning, see [Performance considerations for ray tracing pipelines](porting-complex-pipelines.md#performance-considerations-for-ray-tracing-pipelines).

## Codegen compatibility flags

Compiler compatibility flags allow you to tailor code generation to the specific requirements of your shaders. You typically enable compatibility flags to support a broader set of features and behaviors (such as out-of-bounds reads) when your shader needs them to operate correctly. These flags, however, carry a performance cost.

Always use the minimum set of compatibility flags your shader needs to attain the highest runtime performance for IR code you compile. By default, all compatibility flags are disabled.

You control the compatibility flags by calling the `IRCompilerSetCompatibilityFlags` API in the Metal Shader Converter library. The expected parameter is a 64-bit bitmask of flags to enable. Refer to the library's header file for a list of all flags.

You may also control the compatibility flags from the command line. Consult `metal-shaderconverter --help` for a list of all flags.

## Automatic linear resource layout vs explicit root signatures

Root signatures provide maximum flexibility when laying out resources in your shader's top-level Argument Buffer, enabling advanced features such as bindless resources. This flexibility, however, comes at the cost of increased indirection.

Favor using a linear resource binding model for shaders that don't require the flexibility of root signatures. This binding model provides a top-level Argument Buffer layout that references resources through a single indirection, improving resource access times.

See [Binding model](binding-model.md) for details on both layouts.

## Minimum OS deployment target and minimum GPU

Metal Shader Converter may be able to produce more optimal output when targeting newer GPU families and operating system versions.

Use function `IRCompilerSetMinimumGPUFamily()` to specify the minimum GPU target and `IRCompilerSetMinimumDeploymentTarget()` to specify the OS and minimum build version your IR needs to support.

Metal Shader Converter vends these functions via the command line switches `--minimum-gpu-family`, and `deployment-os` alongside `--minimum-os-build-version`.

## Top-level argument buffers and GPU occupancy

Shader code produced by Metal Shader Converter relies on Argument Buffers to bind resources to pipeline states. Using Argument Buffers to access resources may result in higher register pressure, reducing theoretical shader occupancy when compared to directly binding resources to pipeline slots.

## Top-level argument buffers and shader execution overlap

The root signature binding model allows you to specify and reference resource (descriptor) tables to Metal and reference them from multiple top-level Argument Buffers without rebinding linked resources multiple times. This may lead to lower CPU times due to reducing the calls into the Metal command encoder.

However, be mindful of potential data dependencies introduced between passes by referencing common resources, which may reduce GPU work overlap and increase the wall clock execution time of your workload.

Consider a compute shader that writes into a texture that a fragment shader subsequently samples. You place this texture in a texture table and reference it from a top-level Argument Buffer available to both the compute dispatch and the draw call.

If the texture is a tracked resource, and the vertex stage is able to access this texture through its top-level Argument Buffer, Metal needs to serialize the GPU execution of the compute dispatch and the vertex stage, even when no race condition exists and these two stages can theoretically overlap.

When you use the root signature binding model and share resources via top-level Argument Buffers, use the Metal System Trace in Instruments to evaluate the overlap. Instruments gives you insights you can use to fine-tune your workload dependencies and maximize shader execution overlap.

## Input IR quality influences output IR performance

Metal Shader Converter transforms IR directly based on its input. Suboptimal input IR influences the output of Metal Shader Converter, and may reduce runtime performance of shader pipelines. Always use the best possible input IR as input to Metal Shader Converter.

For best results, avoid intermediate tools that transform the input IR from other formats and provide Metal Shader Converter with IR as close to the source language as possible.

## Root signature validation flags

This flag doesn't affect Metal IR runtime performance. When you instruct Metal Shader Converter to generate a hierarchical resource layout via root signatures, by default Metal Shader Converter performs validation checks on your root signature descriptor and produces an error message when it detects issues.

After you've verified your root signatures are correct, you can disable all validation flags to prevent Metal Shader Converter from performing these checks at compilation time.

## Related guides

- [Binding model](binding-model.md) — linear layout vs root signatures, and synchronization strategies.
- [Compiling shaders](compiling-shaders.md) — debug information and offline GPU binary generation.
- [Porting complex pipelines](porting-complex-pipelines.md#performance-considerations-for-ray-tracing-pipelines) — ray-tracing-specific performance tuning.
