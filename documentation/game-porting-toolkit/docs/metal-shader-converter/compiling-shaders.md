---
source: game-porting-toolkit
framework: game-porting-toolkit
url: https://github.com/apple/game-porting-toolkit/blob/main/docs/metal-shader-converter/compiling-shaders.md
---

# Compiling shaders with Metal Shader Converter

> Part of the [Metal Shader Converter integration guides](README.md).

This guide covers converting shader IR (DXIL) into Metal libraries — using either the standalone executable or the dynamic library — and producing finalized GPU binaries offline. Once you have metallib files, see [Binding model](binding-model.md) and [Pipeline setup](pipeline-setup.md) for runtime integration.

## Converting IR

To convert shaders from DXIL to Metal IR, you use Metal Shader Converter as a standalone executable (`metal-shaderconverter`) or as a dynamic library (`libmetalirconverter`). Metal Shader Converter supports both Windows and macOS. `libmetalirconverter` supports Windows, macOS and iOS.

### Standalone executable

The Metal Shader Converter executable offers several options to customize code generation. In its most basic form, Metal Shader Converter takes a DXIL file as input and produces a metallib.

```
% metal-shaderconverter shader.dxil -o ./shader.metallib
```

By default, Metal Shader Converter generates metallib files that target the latest version of macOS at the time of release. You can inspect this version by running `metal-shaderconverter --version`. Make sure your Xcode is always up to date.

Run `metal-shaderconverter --help` to access all command-line options.

### Dynamic library

`libmetalirconverter` offers a C interface for easy integration into C, C++, Objective-C, and Swift codebases.

```c
IRCompiler* pCompiler = IRCompilerCreate();
IRCompilerSetEntryPointName(pCompiler, "MainVS");

IRObject* pDXIL = IRObjectCreateFromDXIL(bytecode, size, IRBytecodeOwnershipNone);

// Compile DXIL to Metal IR:
IRError* pError = nullptr;
IRObject* pOutIR = IRCompilerAllocCompileAndLink(pCompiler, NULL, pDXIL, &pError);

if (!pOutIR)
{
  // Inspect pError to determine cause.
  IRErrorDestroy( pError );
}

// Retrieve Metallib:
IRMetalLibBinary* pMetallib = IRMetalLibBinaryCreate();
IRObjectGetMetalLibBinary(pOutIR, stage, pMetallib);
size_t metallibSize = IRMetalLibGetBytecodeSize(pMetallib);
uint8_t* metallib = new uint8_t[metallibSize];
IRMetalLibGetBytecode(pMetallib, metallib);

// Store the metallib to custom format or disk, or use to create a MTLLibrary.

delete [] metallib;
IRMetalLibBinaryDestroy(pMetallib);
IRObjectDestroy(pDXIL);
IRObjectDestroy(pOutIR);
IRCompilerDestroy(pCompiler);
```

You can use the library at runtime — as you develop your game, for example — in addition to more typical uses, such as asset conversion and packaging workflows.

Once your game runs on Metal, start converting your shaders ahead of time and directly distributing metallibs in your game.

### Create a MTLLibrary instance from metallib bytecode

After you retrieve the metallib data and its corresponding size, you create a `MTLLibrary` via a `dispatch_data_t` object:

```objc
// Use metallib (at runtime):

NSError* __autoreleasing error = nil;
dispatch_data_t data =
    dispatch_data_create(metallib, metallibSize, dispatch_get_main_queue(), NULL);

id<MTLLibrary> lib = [device newLibraryWithData:data error:&error];

// lib and data are released by ARC.
```

> **Tip:** On macOS, you can use function `IRMetalLibGetBytecodeData` to obtain a direct pointer into the metallib's bytecode, avoiding a copy operation.

### Multithreading considerations

Metal Shader Converter supports multithreading the IR translation process; however, the `IRCompiler` instance isn't reentrant. Each thread in your program needs to create its own instance of `IRCompiler` to avoid race conditions. Once the compilation process completes, your program can reuse a compiler instance to convert further IR.

## Metal GPU binary generation

You can use the offline compiler tool, `metal-tt`, to ingest the output of Metal Shader Converter and produce finalized GPU binaries as part of your shader build system. Use this process to fully compile the non-MSL shader source to GPU binaries that can be loaded into Metal with no pipeline compilation overhead on device.

The following Python script shows an example of a shader pipeline that fully compiles HLSL to Apple GPU binaries. Inputs are the shader source, entry points, and shader profiles, alongside an *mtlp-json* description of the PSO.

```python
import os
import subprocess
cmd = subprocess.call

DXC="dxc"
MSC="metal-shaderconverter"
METAL_TT="xcrun -sdk macosx metal-tt"

products=["compute_pso", "render_pso"]
dependencies={
    "render_pso" : ("render_pso.mtlp-json",
     [("shaders.hlsl", "MainVS", "vs_6_0"), ("shaders.hlsl", "MainFS", "ps_6_0")]),

    "compute_pso" : ("compute_pso.mtlp-json",
     [("shaders.hlsl", "MainCS", "cs_6_0")])
}

shader_source_dir="shader_source/"
output_dir="output_dir/"
target_archs= \
    "".join(subprocess.check_output(['xcrun', 'metal-arch']).replace("\n"," "))

if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

for product in products:
    pso_json, deps = dependencies[product]
    for dep in deps:
        source_file, entry, profile = dep
        cmd([DXC,
             shader_source_dir+source_file,
             "-T", profile,
             "-E", entry,
             "-Fo", output_dir + entry + ".dxil"])

        cmd([MSC,
            "-rename-entry-point", entry,
            output_dir + entry + ".dxil",
            "-o", "./" + output_dir + entry + ".metallib"])

    cmd(METAL_TT.split(" ") + target_archs.split(" ") +
        ["-L", output_dir, shader_source_dir + pso_json,
         "-o", output_dir + product+".gpubin"])
```

Example of an *mtlp-json* file you can use to produce a render pipeline state:

```json
{
  "version": {
    "major": 0,
    "minor": 1,
    "sub_minor": 1
  },
  "generator": "MetalFramework",
  "libraries": {
    "paths": [
      {
        "label": "vtxMetalLib",
        "path": "MainVS.metallib"
      },
      {
        "label": "fragMetalLib",
        "path": "MainFS.metallib"
      }
    ]
  },
  "pipelines": {
    "render_pipelines": [
      {
        "vertex_function": "alias:vtxMetalLib#MainVS",
        "fragment_function": "alias:fragMetalLib#MainFS",
        "vertex_descriptor": {
          "attributes": [
            {
              "format": "Float4"
            }
          ],
          "layouts": [
            {
              "stride": 16
            }
          ]
        },
        "color_attachments": [
          {
            "pixel_format": "BGRA8Unorm_sRGB"
          }
        ]
      }
    ]
  }
}
```

> **Note:** Some limits apply to the offline compilation process. Please review the Apple documentation for the latest set of supported features.

## Shader debugging, profiling, and validation

### Convert debug information

Metal Shader Converter supports carrying debug information from the source IR into Metal libraries. This enables you to debug, profile, and enable shader validation for your converted pipelines on Xcode 16, macOS 15, and iOS 18, or later.

In order to carry debug information, it first needs to be present in the source IR. Shader compilers typically require that you provide command-line arguments to produce and embed debug information. For example, the open-source DXC compiler requires that you specify input arguments `-Zi -Qembed_debug` to produce and embed the debug information into the DXIL container.

> **Note:** If your shaders use the `#line` preprocessor directive, you may need to additionally provide the command-line argument `--ignore-line-directives` to DXC to obtain more accurate shader profiling data.

Carrying debug information requires that you set the minimum OS build version of the target Metal library to be macOS 14 or iOS 17. When using the Metal Shader Converter command-line tool, use argument `--minimum-os-build-version` to specify the minimum operating system version. Using the Metal Shader Converter dynamic library, you instead call function `IRCompilerSetMinimumDeploymentTarget`.

When your input IR contains debug information, Metal Shader Converter automatically carries it into the Metal library it produces. You can override this behavior by passing argument `--ignore-debug-information` to the command-line tool, or by calling function `IRCompilerIgnoreDebugInformation(compiler, true)` when using the Metal Shader Converter dynamic library.

> **Note:** When you are ready to ship your game or app, be sure to recompile your original shader source code with optimizations enabled (typically `-O3`).

### Reduce Metal library size when it contains debug information

Carrying debug information may significantly increase the size of your Metal library files. You can mitigate this size growth by storing the debug information into a separate companion symbol file and then removing it from your converted Metal libraries. The Metal GPU debugger in Xcode enables you to [load the symbol file and resymbolicate](https://developer.apple.com/documentation/metal/shader_libraries/metal_libraries/generating_and_loading_a_metal_library_symbol_file#3871033) your capture.

The following listing shows how to extract symbol and source code data from a Metal library named `shader.metallib` into a separate file and then strip the Metal library to reduce its size:

```sh
# Extract debug information into a metallibsym file:
xcrun -sdk macosx metal-dsymutil -flat -remove-source shader.metallib

# Strip the debug information from the original Metal library file:
xcrun -sdk macosx metal-strip -S shader.metallib
```

The `-remove-source` option of the `metal-dsymutil` tool modifies the Metal library file by removing its embedded source code information, while the command's `-flat` option saves shader source code and other symbol information to a `metallibsym` symbol file.

The `metal-strip` tool removes debug information from the Metal library.

## Related guides

- [Pipeline setup](pipeline-setup.md) — vertex fetch, separate stage-in functions, and adopting Metal language features in HLSL at compile time.
- [Performance](performance.md) — codegen compatibility flags, deployment targets, and other tuning that happens at conversion time.
- [Reference](reference.md) — the feature support matrix and complete code samples.
