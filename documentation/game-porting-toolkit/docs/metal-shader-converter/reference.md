---
source: game-porting-toolkit
framework: game-porting-toolkit
url: https://github.com/apple/game-porting-toolkit/blob/main/docs/metal-shader-converter/reference.md
---

# Reference

> Part of the [Metal Shader Converter integration guides](README.md).

This guide collects lookup material: the feature support matrix, standalone code snippets, and pointers to the complete sample programs.

## Feature support matrix

Metal Shader Converter supports a large subset of DXIL IR that enables AAA-grade content on Metal. Use the following reference table, as well as error detection features in Metal Shader Converter, to ensure the correct conversion of your IR.

| Shader Model | Feature | Support | Error-detected | Notes |
|---|---|---|---|---|
| **Pre-6.0** | - | Limited | Limited | Some features not supported |
| **SM6.0** | Wave intrinsics | Yes | - | |
| | 64-bit integers | Yes | - | |
| **SM6.1** | SV_ViewID | No | No | |
| | SV_Barycentrics | Yes | - | Linear interpolation only, *GetAttributeAtVertex* not supported |
| **SM6.2** | 16-bit scalar types | Yes | - | |
| | denorm mode | No | No | |
| **SM6.3** | Ray tracing | Yes | - | |
| **SM6.4** | Packed dot-product intrinsics | Yes | - | |
| | VRS | No | No | |
| | Library subobjects | No | No | |
| **SM6.5** | Sampler Feedback | No | No | |
| | Mesh/Amplification shaders | Yes | - | |
| **SM6.6** | 64-bit atomics | Limited | No | |
| | Dynamic resources | Yes | No | |
| | IsHelperLane | Yes | - | |
| | Pack/unpack intrinsics | No | Yes | |
| | Compute derivatives | Yes | - | |
| | Wave size | No | Yes | Wave size needs to be 32 |
| | Raytracing payload qualifiers | No | No | |

This list is non-exhaustive. Metal Shader Converter may not support other features not listed above, including:

- `SV_StencilRef`.
- `minLODClamp` with texture read.

> **Note:** Globally-coherent textures require macOS 15 Sequoia, iOS 18, or later. Some math operations like sine and cosine may offer different precision than other implementations of the input IR.

## Example snippets

### Save a MetalLibBinary to disk

You can link the Metal Shader Converter library to enhance your custom offline shader compilation pipelines, and produce metallib files. The following snippet stores the metallib to disk for later consumption:

```c
bool saveMetalLibToFile(const char* filepath,
                        const IRMetalLibBinary* pMetalLib)
{
    FILE* f = fopen(filepath, "w");
    size_t siz = IRMetalLibGetBytecodeSize(pMetalLib);
    uint8_t* bytes = (uint8_t*)malloc(siz);
    IRMetalLibGetBytecode(pMetalLib, bytes);

    fwrite(bytes, siz, 1, f);
    if (ferror(f)) {
        // ...error...
    }

    fclose(f);
    free(bytes);
}
```

A custom shader pipeline processor may choose to store the metallib bytecode and size in a custom asset packaging format.

### Define a global root signature using the Metal Shader Converter library

The global root signature defines a sampler and a texture 2D. You need to put both samplers and texture references into their own tables. You may only reference raw resources directly from the top-level Argument Buffer, such as constants, constant buffers, buffer SRVs, buffer UAVs.

Root signatures in Metal Shader Converter are subject to the same limitations as in Microsoft's DirectX. If you aren't familiar with these requirements, please refer to Microsoft's documentation. Supplying an invalid root signature to Metal Shader Converter may trigger a validation error. If your program disables validation, the tool's behavior is undefined.

```cpp
IRVersionedRootSignatureDescriptor desc;
desc.version = IRRootSignatureVersion_1_1;
desc.desc_1_1.Flags = IRRootSignatureFlagNone;

// Samplers are placed in their own table:
desc.desc_1_1.NumStaticSamplers = 1;
IRStaticSamplerDescriptor pSSDesc[] = { {
    .Filter = IRFilterMinMagMipLinear,
    .AddressU = IRTextureAddressModeWrap,
    .AddressV = IRTextureAddressModeWrap,
    .AddressW = IRTextureAddressModeWrap,
    .MipLODBias = 0,
    .MaxAnisotropy = 0,
    .ComparisonFunc = IRComparisonFunctionNever,
    .BorderColor = IRStaticBorderColorOpaqueBlack,
    .MinLOD = 0,
    .MaxLOD = std::numeric_limits<float>::max(),
    .ShaderRegister = 0,
    .RegisterSpace = 0,
    .ShaderVisibility = IRShaderVisibilityPixel
} };
desc.desc_1_1.pStaticSamplers = pSSDesc;

// Parameters (1 texture):
IRDescriptorRange1 ranges[1] = { [0] = {
    .RangeType = IRDescriptorRangeTypeSRV,
    .NumDescriptors = 1,
    .BaseShaderRegister = 0,
    .RegisterSpace = 0,
    .Flags = IRDescriptorRangeFlagDataStatic,
    .OffsetInDescriptorsFromTableStart = 0
}
};
IRRootParameter1 pParams[] = { {
    .ParameterType = IRRootParameterTypeDescriptorTable,
    .DescriptorTable = { .NumDescriptorRanges = 1, .pDescriptorRanges = ranges },
    .ShaderVisibility = IRShaderVisibilityPixel
} };
desc.desc_1_1.NumParameters = 1;
desc.desc_1_1.pParameters = pParams;

IRError* pRootSigError = nullptr;
IRRootSignature* pRootSig = IRRootSignatureCreateFromDescriptor( &desc, &pRootSigError );
if ( !pRootSig )
{
    // handle and release error
}

// After compiling DXIL bytecode to Metal IR using this root signature,
// it should have 2 entries:
//
// offset 0: a uint64_t referencing a table that contains a
// void* resource (SRV).
//
// offset 8 (sizeof(uint_64)): a uint64_t referencing a table with
// one sampler.

// The sampler table should be encoded like so:
// For each sampler:
// 64-bits: GPU VA of the sampler.
// 64-bits: 0
// 64-bits: Sampler's LOD Bias.

// The SRV table should be encoded like so:
// 64-bits: 0
// 64-bits: Texture GPU Resource ID
// 64-bits: 0

// Use the Companion Header for help encoding resources into descriptor tables.

IRCompiler* pCompiler = IRCompilerCreate();
IRCompilerSetGlobalRootSignature( pCompiler, pRootSig );

// Compile DXIL to Metal IR
IRError* pError = nullptr;
IRObject* pDXIL = IRObjectCreateFromDXIL(dxilFragmentBytecode,
                                         dxilFragmentSize,
                                         IRBytecodeOwnershipNone);

IRObject* pOutIR = IRCompilerAllocCompileAndLink(pCompiler,
                                                 NULL,
                                                 pDXIL,
                                                 &pError);

// if pOutIR is null, inspect pError for causes. Release pError afterwards.

IRMetalLibBinary* pMetallib = IRMetalLibBinaryCreate();
IRObjectGetMetalLibBinary( pOutIR, IRShaderStageFragment, pMetallib );

size_t metallibSize = IRMetalLibGetBytecodeSize( pMetallib );
uint8_t* metallib = new uint8_t[ metallibSize ];
if ( IRMetalLibGetBytecode( pMetallib, metallib ) == metallibSize )
{
    // Store metallib for later use or directly create a MTLLibrary
}

delete [] metallib;

IRMetalLibBinaryDestroy( pMetallib );

IRObjectDestroy( pOutIR );
IRObjectDestroy( pDXIL );

IRRootSignatureDestroy( pRootSig );
IRCompilerDestroy( pCompiler );
```

### Define a root signature via a JSON file

```json
{
  "RootSignature": {
    "Flags": "IRRootSignatureFlagNone",
    "NumParameters": 3,
    "NumStaticSamplers": 1,
    "Parameters": [
      {
        "DescriptorTable": {
          "DescriptorRanges": [
            {
              "BaseShaderRegister": 0,
              "Flags": "IRDescriptorRangeFlagDataStatic",
              "NumDescriptors": 1,
              "OffsetInDescriptorsFromTableStart": 0,
              "RangeType": "IRDescriptorRangeTypeSRV",
              "RegisterSpace": 0
            }
          ],
          "NumDescriptorRanges": 1
        },
        "ParameterType": "IRRootParameterTypeDescriptorTable",
        "ShaderVisibility": "IRShaderVisibilityPixel"
      },
      {
        "Descriptor": {
          "Flags": "IRRootDescriptorFlagNone",
          "RegisterSpace": 2,
          "ShaderRegister": 0
        },
        "ParameterType": "IRRootParameterTypeCBV",
        "ShaderVisibility": "IRShaderVisibilityPixel"
      },
      {
        "Constants": {
          "Num32BitValues": 4,
          "RegisterSpace": 2,
          "ShaderRegister": 1
        },
        "ParameterType": "IRRootParameterType32BitConstants",
        "ShaderVisibility": "IRShaderVisibilityAll"
      }
    ],
    "StaticSamplers": [
      {
        "AddressU": "IRTextureAddressModeWrap",
        "AddressV": "IRTextureAddressModeWrap",
        "AddressW": "IRTextureAddressModeWrap",
        "BorderColor": "IRStaticBorderColorOpaqueBlack",
        "ComparisonFunc": "IRComparisonFunctionNever",
        "Filter": "IRFilterMinMagMipLinear",
        "MaxAnisotropy": 0,
        "MaxLOD": 3.4028234663852886e+38,
        "MinLOD": 0,
        "MipLODBias": 0,
        "RegisterSpace": 0,
        "ShaderRegister": 0,
        "ShaderVisibility": "IRShaderVisibilityPixel"
      }
    ]
  },
  "version": "IRRootSignatureVersion_1_1"
}
```

### Encoding Argument Buffers and descriptor tables generated with an automatic layout

Encode a descriptor table with two entries: first a texture array, followed by a sampler state object.

```cpp
const int kNumEntries = 2;
size_t size = sizeof(IRDescriptorTableEntry) * kNumEntries;
MTL::Buffer* pDescriptorTable =
    _pDevice->newBuffer(size, MTL::ResourceStorageModeShared );

auto* pResourceTable = (IRDescriptorTableEntry *)pDescriptorTable->contents();
IRDescriptorTableSetTexture( &pResourceTable[0], pTexture, 0, 0 );
IRDescriptorTableSetSampler( &pResourceTable[1], pSampler, 0 );
```

### C++ bump allocator

This snippet demonstrates a simple C++ bump allocator, implemented using **metal-cpp**. Note: this allocator is not thread safe. For multithreaded encoding, create one of these instances per thread per frame.

```cpp
#ifndef BUMPALLOCATOR_HPP
#define BUMPALLOCATOR_HPP

#include <Metal/Metal.hpp>
#include <tuple>
#include <cassert>
#include <cstdint>

namespace mem
{
constexpr uint64_t alignUp(uint64_t n, uint64_t alignment)
{
    return (n + alignment - 1) & ~(alignment - 1);
}
}

/// This allocator is not thread safe. For multithreaded encoding,
/// create one of these instances per thread per frame.
class BumpAllocator
{
public:
    BumpAllocator(MTL::Device* pDevice,
                  size_t capacityInBytes,
                  MTL::ResourceOptions resourceOptions)
    {
        assert(resourceOptions != MTL::ResourceStorageModePrivate);
        _offset = 0;
        _capacity = capacityInBytes;
        _pBuffer = pDevice->newBuffer(capacityInBytes, resourceOptions);
        _contents = (uint8_t*)_pBuffer->contents();
    }

    ~BumpAllocator()
    {
        _pBuffer->release();
    }

    // Disable copy and move constructors and assignment operators

    void reset() { _offset = 0; }

    template< typename T >
    std::pair<T*, uint64_t> addAllocation(uint64_t count=1) noexcept
    {
        // Shader converter requires an alignment of 8-bytes:
        uint64_t allocSize = mem::alignUp(sizeof(T) * count, 8);

        // If you hit this assert, the allocation data doesn't fit in
        // the amount estimated.
        assert((_offset + allocSize) <= _capacity);

        T* dataPtr          = reinterpret_cast<T*>(_contents + _offset);
        uint64_t dataOffset = _offset;

        _offset += allocSize;

        return { dataPtr, dataOffset };
    }

    MTL::Buffer* baseBuffer() const noexcept
    {
        return _pBuffer;
    }

private:
    MTL::Buffer* _pBuffer;
    uint64_t _offset;
    uint64_t _capacity;
    uint8_t* _contents;
};

#endif // BUMPALLOCATOR_HPP
```

## Complete code samples

All code samples can be found at the [Metal sample code](https://developer.apple.com/metal/sample-code/?q=hlsl) page. These samples are complete programs you can use as a starting point for your next project, or just to try out Metal Shader Converter.

### Dynamic library

This sample builds on the "[Learn Metal with C++](https://developer.apple.com/metal/sample-code/)" code sample to add a grass floor to the scene via geometry and tessellation pipeline emulation. The UI allows you to select across the different pipelines available.

The geometry pipeline uses an HLSL geometry shader to generate one strand of grass for each triangle comprising the floor mesh. The geometry stage consumes a buffer to perform a subtle wind animation of the grass mesh.

The tessellation pipeline expands this to subdivide the floor triangle patches, increasing the density of the grass. It also adds an extra wave effect to the wind animation that's implemented in the domain shader. This sample requires macOS 14 or later.

### Ray query

This sample shows how to build a compute kernel that performs ray query operations to find intersections against an acceleration structure containing two triangle instances. This sample requires macOS 13 or later.

### Ray tracing pipelines

This sample shows how to build a compute kernel that performs ray tracing via the following shader stages: Ray Generation, Intersection, Any Hit, Closest Hit, and Miss. The compute kernel finds intersections against an acceleration structure containing two triangle and two sphere instances. This sample requires macOS 13 or later.

### Function constants and framebuffer fetch

This sample shows how to adopt Metal-language features in HLSL by demonstrating programmable blending utilizing framebuffer fetch. It also shows how to specialize your HLSL pipelines with function constants.

### Ray tracing with intersection function buffer

This sample demonstrates how to convert a DXR ray tracing pipeline to Metal, and then emulate a DXR shader table with Metal intersection function buffer if available. This sample requires macOS 16 or later on an Apple M3 or later. Otherwise, this sample falls back to using Metal visible function table.

## Related guides

- [Binding model](binding-model.md) — context for the root signature and descriptor table snippets above.
- [Compiling shaders](compiling-shaders.md) — context for the save-to-disk snippet.
- [Porting complex pipelines](porting-complex-pipelines.md) — context for the ray tracing and geometry/tessellation samples.
