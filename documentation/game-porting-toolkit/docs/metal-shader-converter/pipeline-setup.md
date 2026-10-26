---
source: game-porting-toolkit
framework: game-porting-toolkit
url: https://github.com/apple/game-porting-toolkit/blob/main/docs/metal-shader-converter/pipeline-setup.md
---

# Pipeline setup with Metal Shader Converter

> Part of the [Metal Shader Converter integration guides](README.md).

This guide covers wiring up render and compute pipelines for converted shaders: fetching vertex attributes, using the companion header, adopting Metal-language features in HLSL, building hybrid Metal/converted pipelines, and runtime feature toggles. For resource binding, see [Binding model](binding-model.md).

## Vertex attribute fetch

Metal Shader Converter supports two mechanisms to fetch vertex attributes: *Metal vertex fetch* and a *separate stage-in function*.

### Metal vertex fetch

By default, Metal Shader Converter generates IR that leverages the Metal vertex fetch mechanism. When using this mechanism, you typically provide a `MTLVertexDescriptor` instance to your pipeline state descriptors so Metal can automatically retrieve vertex attributes and make them accessible to your vertex shader.

When using Metal vertex fetch, your stage-in attributes need to start at index `kIRStageInAttributeStartIndex` (set to value `11`) defined in `metal_irconverter_runtime.h`, and the buffer bind point for your vertex buffers starts at `kIRVertexBufferBindPoint` (set to value `6`).

The following snippet depicts how to configure Metal vertex fetch for a vertex layout consisting of two `float4` attributes:

```objc
MTLVertexDescriptor* vtxDesc = [[MTLVertexDescriptor alloc] init];

vtxDesc.attributes[kIRStageInAttributeStartIndex + 0].format = MTLVertexFormatFloat4;
vtxDesc.attributes[kIRStageInAttributeStartIndex + 0].offset = 0;
vtxDesc.attributes[kIRStageInAttributeStartIndex + 0].bufferIndex = kIRVertexBufferBindPoint;

vtxDesc.attributes[kIRStageInAttributeStartIndex + 1].format = MTLVertexFormatFloat4;
vtxDesc.attributes[kIRStageInAttributeStartIndex + 1].offset = sizeof(simd_float4);
vtxDesc.attributes[kIRStageInAttributeStartIndex + 1].bufferIndex = kIRVertexBufferBindPoint;

vtxDesc.layouts[kIRVertexBufferBindPoint].stride = sizeof(simd_float4) + sizeof(simd_float4);
vtxDesc.layouts[kIRVertexBufferBindPoint].stepRate = 1;
vtxDesc.layouts[kIRVertexBufferBindPoint].stepFunction = MTLVertexStepFunctionPerVertex;
```

When you use a render pipeline state following this vertex descriptor, you bind your vertex buffer to it like so:

```objc
[renderEnc setVertexBuffer:vertices offset:0 atIndex:kIRVertexBufferBindPoint];
```

### Visible function vertex fetch

Metal vertex fetch is fast and requires very little setup at both IR conversion time and at pipeline state object creation time. In some situations, however, if your IR requires very flexible datatype conversions, you need to use a separate stage-in function.

To synthesize a separate vertex stage-in function, pass configuration parameter `IRStageInCodeGenerationModeUseSeparateStageInFunction` to function `IRCompilerSetStageInGenerationMode` in the `libmetalirconverter` library before compiling your vertex stage, and call `IRMetalLibSynthesizeStageInFunction` afterward to generate the stage-in function.

You can also use the command-line argument `--vertex-stage-in` to direct the Metal Shader Converter standalone tool to produce both a vertex function and a separate stage-in function. Metal Shader Converter stores each function in its own metallib.

Metal Shader Converter generates separate stage-in functions as *Metal visible functions* that you need to link to your pipeline state via its descriptor's `linkedFunctions` property. At runtime, the converted shader code automatically invokes the visible stage-in function, performing any needed type conversions or applying dynamic offsets via software.

The following example compiles a vertex shader that leverages a separate stage-in function:

```c
IRObject* pIR = // input IR

IRCompiler* pCompiler = IRCompilerCreate();

// Synthesize a separate stage-in function by providing a vertex input layout:
IRVersionedInputLayoutDescriptor inputDesc;
inputDesc.version = IRInputLayoutDescriptorVersion_1;
    inputDesc.desc_1_0.numElements = 3;
    inputDesc.desc_1_0.semanticNames[0] = "POSITION";
    inputDesc.desc_1_0.semanticNames[1] = "COLOR";
    inputDesc.desc_1_0.semanticNames[2] = "TEXCOORD";
    inputDesc.desc_1_0.inputElementDescs[0] = {
        .semanticIndex = 0,
        .format = IRFormatR32G32B32A32Float,
        .inputSlot = 0,
        .alignedByteOffset = 0,
        .inputSlotClass = IRInputClassificationPerVertexData,
        .instanceDataStepRate = 0 /* needs to be 0 for per-vertex data */
    };
    inputDesc.desc_1_0.inputElementDescs[1] = {
        .semanticIndex = 0,
        .format = IRFormatR32G32B32A32Float,
        .inputSlot = 1,
        .alignedByteOffset = sizeof(float)*4,
        .inputSlotClass = IRInputClassificationPerVertexData,
        .instanceDataStepRate = 0 /* needs to be 0 for per-vertex data */
    };
    inputDesc.desc_1_0.inputElementDescs[2] = {
        .semanticIndex = 0,
        .format = IRFormatR32G32B32A32Float,
        .inputSlot = 2,
        .alignedByteOffset = sizeof(float)*4*2,
        .inputSlotClass = IRInputClassificationPerVertexData,
        .instanceDataStepRate = 0 /* needs to be 0 for per-vertex data */
    };

IRError* pError = nullptr;
IRCompilerSetStageInGenerationMode(pCompiler,
                              IRStageInCodeGenerationModeUseSeparateStageInFunction);
IRObject* pIR = IRCompilerAllocCompileAndLink(pCompiler, nullptr, pIR, &pError);

// Validate pIR != null and no error.

IRShaderReflection* pVertexReflection = IRShaderReflectionCreate();
IRObjectGetReflection(pIR, IRShaderStageVertex, pVertexReflection);

IRMetalLibBinary* pStageInMetalLib = IRMetalLibBinaryCreate();
bool success = IRMetalLibSynthesizeStageInFunction(pCompiler,
                                                   pVertexReflection,
                                                   &inputDesc,
                                                   pStageInMetalLib);

// Verify success

IRMetalLibBinary* pVertexStageMetalLib = IRMetalLibBinaryCreate();
success = IRObjectGetMetalLibBinary(pIR, IRShaderStageVertex, pVertexStageMetalLib);

// Verify success

if (pError)
{
    IRErrorDestroy(pError);
}

IRMetalLibBinaryDestroy(pVertexStageMetalLib);
IRMetalLibBinaryDestroy(pStageInMetalLib);
IRShaderReflectionDestroy(pVertexReflection);
IRObjectDestroy(pIR);
IRCompilerDestroy(pCompiler);
```

You can also provide the vertex input layout in JSON format to the command-line tool by using parameter `--vertex-input-layout-file`. The following example demonstrates the JSON format that describes the input layout for 5 `float4` input attributes:

```json
{
    "InputElements": [
        {
            "AlignedByteOffset": 0,
            "Format": "R32G32B32A32_FLOAT",
            "InputSlot": 0,
            "InputSlotClass": "PerVertexData",
            "InstanceDataStepRate": 0,
            "SemanticIndex": 0
        },
        {
            "AlignedByteOffset": 16,
            "Format": "R32G32B32A32_FLOAT",
            "InputSlot": 1,
            "InputSlotClass": "PerVertexData",
            "InstanceDataStepRate": 0,
            "SemanticIndex": 0
        },
        {
            "AlignedByteOffset": 32,
            "Format": "R32G32B32A32_FLOAT",
            "InputSlot": 2,
            "InputSlotClass": "PerVertexData",
            "InstanceDataStepRate": 0,
            "SemanticIndex": 0
        },
        {
            "AlignedByteOffset": 48,
            "Format": "R32G32B32A32_FLOAT",
            "InputSlot": 3,
            "InputSlotClass": "PerVertexData",
            "InstanceDataStepRate": 0,
            "SemanticIndex": 0
        },
        {
            "AlignedByteOffset": 64,
            "Format": "R32G32B32A32_FLOAT",
            "InputSlot": 4,
            "InputSlotClass": "PerVertexData",
            "InstanceDataStepRate": 0,
            "SemanticIndex": 0
        }
    ],
    "SemanticNames": [
        "POSITION",
        "NORMAL",
        "TANGENT",
        "TEXCOORD",
        "COLOR"
    ]
}
```

The command-line tool provides option `--generate-vertex-input-template` that you can use to generate a JSON file template to manually customize with your shader's input layout.

At runtime, after you generate a separate stage-in function, you need to create the pipeline state object by linking the functions together. The next example shows how:

```objc
id<MTLDevice> device = MTLCreateSystemDefaultDevice();

id<MTLLibrary> vertexLib = [device newLibraryWithData: /* vertex stage metallib */ ];

id<MTLLibrary> stageInLib = [device newLibraryWithData: /* stage-in metallib */ ];

MTLRenderPipelineDescriptor* rpd = [[MTLRenderPipelineDescriptor alloc] init];
rpd.vertexFunction =
          [vertexLib newFunctionWithName:vertexLib.functionNames.firstObject];

MTLLinkedFunctions* linkedFunctions = [[MTLLinkedFunctions alloc] init];
linkedFunctions.functions = @[
          [stageInLib newFunctionWithName:stageInLib.functionNames.firstObject]
];
rpd.vertexLinkedFunctions = linkedFunctions;

// ... continue configuring the pipeline state descriptor...

id<MTLRenderPipelineState> pso =
                      [device newRenderPipelineStateWithDescriptor:rpd error:&error];
```

## The Metal Shader Converter companion header

The Metal Shader Converter companion header provides convenience functions to accomplish common tasks:

1. Helps encode resources into descriptor tables (3 `uint64_t` encoding).
2. Aids the emulation of Geometry and Tessellation pipelines via Metal mesh shaders.

To use the companion header, include file `metal_irconverter_runtime.h`.

This header depends on Metal, and you need to include it after including `Metal/Metal.h` or `Metal/Metal.hpp`.

Because this is a header-only library, it requires you to generate its implementation once. You generate the implementation by defining `IR_PRIVATE_IMPLEMENTATION` in a single `.m`, `.mm`, or `.cpp` file before including the header. **You need to define this macro exactly once.**

The Metal Shader Converter companion header is compatible with metal-cpp. To configure the header for metal-cpp usage, define `IR_RUNTIME_METALCPP` before including it. Your program needs to define this macro for every inclusion directive, ensuring types match across the entire program.

You can download metal-cpp from [developer.apple.com/metal/cpp](http://developer.apple.com/metal/cpp).

Example: include the Metal Shader Converter companion header in a single `.cpp` file that uses metal-cpp for rendering, and generate its implementation.

```cpp
#include <Metal/Metal.hpp>
#define IR_RUNTIME_METALCPP       // enable metal-cpp compatibility mode
#define IR_PRIVATE_IMPLEMENTATION // define only once in an implementation file
#include <metal_irconverter_runtime/metal_irconverter_runtime.h>
```

For a worked example of encoding an Argument Buffer / descriptor table generated with the automatic layout, see [Reference](reference.md#encoding-argument-buffers-and-descriptor-tables-generated-with-an-automatic-layout).

## Adopting Metal language features in HLSL

Metal Shader Converter 3.0 provides support to adopt the following Metal language features:

- Function constants, for efficient specialization of your shaders.
- Framebuffer fetch, to enable techniques such as programmable blending.

For more details about these features, see the [Metal Shading Language Specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) (on *Program Scope Function Constants* and *Fragment Function Input Attributes*).

Both features are exposed to HLSL with the header file `Metal_HLSL.inc` which, after installation, can be found at `<install_path>/include/metal_irconverter_ext/Metal_HLSL.inc`, for both macOS and Windows.

Enabling both features requires the definition of unique register spaces for each before including `Metal_HLSL.inc` in your shader:

- define `MTL_FUNCTION_CONSTANT_SPACE=<value>` for function constants.
- define `MTL_FRAMEBUFFER_FETCH_SPACE=<value>` for framebuffer fetch.

```c
// 1. Define unique register spaces to enable the features
// You can also set these using dxc's -D <macro>=<value> command option
#define MTL_FRAMEBUFFER_FETCH_SPACE 2147420893
#define MTL_FUNCTION_CONSTANT_SPACE 2147420894

// 2. Then include the header into your HLSL shader
#include "Metal_HLSL.inc"
```

> **Note:** If either `MTL_FRAMEBUFFER_FETCH_SPACE` or `MTL_FUNCTION_CONSTANT_SPACE` is defined, and if your shader uses the root signature attribute, then you must explicitly include these defined register spaces in your shader's root signature as needed. (This is because these features depend on the HLSL binding model — CBVs for function constants and SRVs for framebuffer fetch. However, these resources are special and even when included in a root signature definition, will be skipped and take up no space in the root signature.) Here's an example, using the values defined above:

```c
#define RootSig \
    "DescriptorTable(CBV(b0), SRV(t0))," \
    "DescriptorTable(Sampler(s0))," \
    "DescriptorTable(CBV(b0, space=2147420894), SRV(t0, space=2147420893))," \
```

### Using function constants

Use the macro `MTL_FUNCTION_CONSTANT(var_type, var_name, fc_index)` to declare a variable as a function constant in HLSL. Here is an example of a `float4` variable named `ConstantColor` with a function constant index `0`:

```c
MTL_FUNCTION_CONSTANT(float4, ConstantColor, 0);
```

During conversion of your HLSL shader to Metal IR, you must also specify the `MTL_FUNCTION_CONSTANT_SPACE` value. Do this with the command option `--function-constant-register-space` if using the `metal-shaderconverter` command line tool, or with the function `IRCompilerSetFunctionConstantResourceSpace` if using the dynamic library.

At runtime, bind a value to your shader-declared function constant in host code using `MTLFunctionConstantValues` to specialize your HLSL-converted Metal function. The specified data type in host code must always be of type `MTLDataTypeUInt4`.

```objc
MTLFunctionConstantValues *functionConstantValues = [[MTLFunctionConstantValues alloc] init];
simd_float4 color = simd_make_float4( 1.0, 1.0, 0.0, 1.0);
[functionConstantValues setConstantValue:&color type:MTLDataTypeUInt4 atIndex:0];
```

The companion header also provides a convenience function for setting function constant values:

```c
IRRuntimeFunctionConstantValue colorFC = { .f0 = color.x, .f1 = color.y, .f2 = color.z, .f3 = color.w };
IRRuntimeSetFunctionConstantValue(functionConstantValues, 0, &colorFC);
```

### Using framebuffer fetch

Use the macro `MTL_LOAD_FRAMEBUFFER(attachment_index, data_type)` to read back color values from the attachment index. The attachment index must be known at compile time and the supported color data types are `float4`, `half4`, `int4`, `uint4`. Here is an example:

```c
half4 destColor = MTL_LOAD_FRAMEBUFFER(0, half4);
```

During conversion of your HLSL shader to Metal IR, you must also specify the `MTL_FRAMEBUFFER_FETCH_SPACE` value. Do this with the command option `--framebuffer-fetch-register-space` if using the `metal-shaderconverter` command line tool, or with the function `IRCompilerSetFramebufferFetchResourceSpace` if using the dynamic library.

## Creating hybrid pipelines

Metal Shader Converter joins the Metal compiler as another mechanism to produce Metal libraries from your existing shader IR.

Since all shaders become Metal IR, you can combine Metal libraries coming from Metal Shader Converter and from the Metal compiler in a single app and even in a single pipeline. This opens the possibility of using the Metal shading language to access unique features — like programmable blending and tile shaders — not typically available in third-party IR.

To take advantage of programmable blending, after your converted pipeline has output its color, use pipelines with a Metal Shading Language fragment stage to perform frame buffer fetch. A good use case for this is implementing an on-tile post-processing stack.

To read back the on-tile color, observe the following mapping. Color data your converted fragment shader stores in `SV_Target0` is available through attribute `color(0)`:

```
SV_Target0 → [[color(0)]]
```

You can also combine shader stages. This allows you, for example, to take advantage of render pipelines with tessellation and geometry stages while calculating the final coloring in Metal Shading Language.

To accomplish this, match the shader interface using the `user` attribute in your struct member declarations:

```
SV_Position  →  [[user(SV_Position)]]
SV_NORMAL    →  [[user(SV_Normal0)]]
SV_TEXCOORD0 →  [[user(SV_Texcoord0)]]
```

## IR runtime model compatibility

### Dual-source blending

Metal Shader Converter supports dual source blending. By default, Metal Shader Converter doesn't inject this capability into its generated Metal IR, but exposes controls to allow you to enable it always, or to defer the decision to pipeline state creation time.

To request support for dual source blending, pass `IRDualSourceBlendingConfigurationForceEnabled` to function `IRCompilerSetDualSourceBlendingConfiguration`, or `-dualSourceBlending` via the command-line interface.

You can alternatively defer the decision to perform dual-source blending to runtime. In that case, use options `IRDualSourceBlendingConfigurationDecideAtRuntime` or `decideAtRuntime` when configuring dual-source blending support. In this case, Metal Shader Converter injects a function constant `dualSourceEnabled` into your fragment shader that you then provide when retrieving the function from the produced Metal library.

### Sample mask

Metal Shader Converter supports setting the sample mask bitmask to inform which samples get updated in active render targets when converting IR.

By default the value is `0xffffffff`, which updates all the samples. This parameter is reset after each compilation:

```c
IRCompiler* pCompiler = IRCompilerCreate();
// Setting the compiler sample mask bit to 0x2 bitmask
IRCompilerSetSampleMask(pCompiler, 0x2);

IRError* pIRError = nullptr;
// Converting pFirstDXIL blob with '0x2' sample mask bitmask
// After IRCompilerAllocCompileAndLink call, the compiler sample mask bitmask is reset to '0xffffffff'
IRObject* pFirstAIR = IRCompilerAllocCompileAndLink(pCompiler, nullptr, pFirstDXIL, &pIRError);

// ... Getting the metal lib binary from pFirstAir

// Setting the compiler sample mask bit to 0x4 bitmask
IRCompilerSetSampleMask(pCompiler, 0x4);

// Converting pSecondDXIL blob with '0x4' sample mask bitmask
// Another IRCompilerAllocCompileAndLink call, the compiler sample mask bitmask is reset to '0xffffffff'
IRObject* pAIR = IRCompilerAllocCompileAndLink(pCompiler, nullptr, pSecondDXIL, &pIRError);
```

### Raster order view

Metal Shader Converter supports DXIL raster order view resources when converting IR.

To support this feature, ensure that your app binds a nil buffer to `kIRArgumentBufferUniformsBindPoint` before issuing draw calls with shaders that access raster order view resources:

```objc
uint64_t bufferROG = 0;
// Bind a nil buffer to kIRArgumentBufferUniformsBindPoint index to support raster order view resources access in Metal IR
[rce setFragmentBytes:&bufferROG length:sizeof(uint64_t) atIndex:kIRArgumentBufferUniformsBindPoint];

// Issue draw calls with shaders that access raster order view resources
// ...
```

## Related guides

- [Binding model](binding-model.md) — the top-level Argument Buffer, root signatures, and resource encoding.
- [Compiling shaders](compiling-shaders.md) — producing the metallibs these pipelines consume.
- [Reflection](reflection.md) — retrieving entry point names and reflection structs needed to build pipelines.
- [Porting complex pipelines](porting-complex-pipelines.md) — geometry/tessellation emulation and ray tracing pipelines.
