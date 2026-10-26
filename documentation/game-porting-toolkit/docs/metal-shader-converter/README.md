---
source: game-porting-toolkit
framework: game-porting-toolkit
url: https://github.com/apple/game-porting-toolkit/blob/main/docs/metal-shader-converter/README.md
---

# Metal Shader Converter integration guides

Metal Shader Converter converts shader intermediate representations in LLVM IR bytecode (DXIL) into a form suitable to be loaded into Metal. It is available both as a standalone executable (`metal-shaderconverter`) and as a dynamic library (`libmetalirconverter`); all functionality in the library is also available from the executable.

These guides break the material into standalone, task-focused documents. Start with [Get started](getting-started.md) for orientation, then jump to the guide for your task.

## Guides

| Guide | Covers |
|---|---|
| [Get started](getting-started.md) | Introduction, changelog, system requirements, download. |
| [Compiling shaders](compiling-shaders.md) | Converting DXIL→metallib via the CLI or library, creating a `MTLLibrary`, multithreading, offline GPU binaries (`metal-tt`), and carrying/stripping debug information. |
| [Binding model](binding-model.md) | Top-level Argument Buffer, root signatures vs automatic linear layout, resource encoding, synchronization (bump allocator, `setBytes`), indirect resources, texture arrays, NaN/Inf, samplers. |
| [Pipeline setup](pipeline-setup.md) | Vertex attribute fetch (Metal vertex fetch and separate stage-in), the companion header, adopting Metal-language features in HLSL (function constants, framebuffer fetch), hybrid pipelines, and runtime feature toggles (dual-source blending, sample mask, raster order views). |
| [Reflection](reflection.md) | Offline reflection JSON per shader stage and library reflection via `IRObjectGetReflection`. |
| [Porting complex pipelines](porting-complex-pipelines.md) | Geometry/tessellation emulation, amplification/mesh shaders, append/consume buffers, unbounded arrays, dynamic resources, inline ray tracing, and ray tracing pipelines (with performance considerations). |
| [Performance](performance.md) | Codegen compatibility flags, layout trade-offs, deployment targets, occupancy, execution overlap, and input IR quality. |
| [Reference](reference.md) | Feature support matrix, standalone code snippets, and complete sample programs. |

## Suggested reading paths

- **First time converting a shader:** [Get started](getting-started.md) → [Compiling shaders](compiling-shaders.md) → [Binding model](binding-model.md) → [Pipeline setup](pipeline-setup.md).
- **Porting a renderer:** [Binding model](binding-model.md) → [Reflection](reflection.md) → [Porting complex pipelines](porting-complex-pipelines.md) → [Performance](performance.md).
- **Ray tracing:** [Compiling shaders](compiling-shaders.md) → [Porting complex pipelines](porting-complex-pipelines.md#converting-and-running-ray-tracing-pipelines).

## The companion header

Several guides reference `metal_irconverter_runtime.h`, a lightweight, header-only library that accompanies Metal Shader Converter and helps with common tasks (encoding resources into descriptor tables, and emulating geometry/tessellation pipelines via Metal mesh shaders). See [Pipeline setup → The Metal Shader Converter companion header](pipeline-setup.md#the-metal-shader-converter-companion-header) for setup.

---

Code snippets in these guides are Copyright (C) 2023-2026 Apple Inc., licensed under the Apache License, Version 2.0.
