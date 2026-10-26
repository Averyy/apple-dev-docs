---
source: game-porting-toolkit
framework: game-porting-toolkit
url: https://github.com/apple/game-porting-toolkit/blob/main/docs/metal-shader-converter/reflection.md
---

# Offline and library reflection

> Part of the [Metal Shader Converter integration guides](README.md).

Metal Shader Converter produces valuable information as it compiles your shaders. This information is a complement to, but not a replacement of, the reflection capabilities your source compiler may give you. Refer to the `metal_irconverter.h` header to determine the reflection information Metal Shader Converter offers.

Metal Shader Converter produces reflection information in both of its forms: standalone executable and library.

> **Note:** The shader reflection format may change across releases of Metal Shader Converter. Attempting to deserialize reflection data produced by a different version of Metal Shader Converter may cause undefined behavior.

Reflection is the authoritative source for resource offsets within the top-level Argument Buffer. See [Binding model](binding-model.md) for how those offsets are consumed.

## Standalone reflection

When you use the standalone executable, Metal Shader Converter writes offline reflection information into a companion JSON to a file path you specify via argument `--output-reflection-file`. Metal Shader Converter doesn't write reflection information if you don't provide this argument.

### Vertex stage reflection

```
{
    "EntryPoint": (string),
    "NeedsFunctionConstants": (bool),
    "Resources": [
        {
            "abIndex": 2,
            "slot": 0,
            "type": (string: "SRV"|"CBV"|"SMP"|"UAV")
        },
        ...
    ],
    "ShaderType": (string: "Vertex"),
    "TopLevelArgumentBuffer": [
        {
            "EltOffset": (int),
            "Size": (int),
            "Slot": (int),
            "Space": (int),
            "Type": (string: "SRV"|"CBV"|"UAV")
        },
        ...
    ],
    "instance_id_index": (int),
    "line_passthrough_shader": {
        "max_primitives_per_mesh_threadgroup": (int)
    },
    "needs_draw_params": (bool),
    "point_passthrough_shader": {
        "max_primitives_per_mesh_threadgroup": (int)
    },
    "triangle_passthrough_shader": {
        "max_primitives_per_mesh_threadgroup": (int)
    },
    "vertex_id_index": (int),
    "vertex_inputs": [

    ],
    "vertex_output_size_in_bytes": (int),
    "vertex_outputs": [
        {
            "columnCount": (int: 1|2|3|4),
            "elementType": (string),
            "index": (int),
            "name": (string: e.g."sv_position0")
        },
        ...
    ]
}
```

**Example:** the following vertex shader:

```hlsl
struct VertexData
{
    float4 position : POSITION;
    float4 color : COLOR;
    float4 uv : TEXCOORD;
};

struct v2f
{
    float4 position : SV_Position;
    float4 color : USER0;
    float4 uv : TEXCOORD0;
};

v2f MainVS( VertexData vin )
{
    v2f o = (v2f)0;
    o.position = vin.position;
    o.color = vin.color;
    o.uv = vin.uv;
    return o;
}
```

Produces reflection JSON:

```json
{
    "EntryPoint": "MainVS",
    "ShaderType": "Vertex",
    "instance_id_index": -1,
    "is_tessellation_vertex_shader": -1,
    "needs_draw_params": false,
    "vertex_id_index": -1,
    "vertex_inputs": [
        {
            "index": 0,
            "name": "position0"
        },
        {
            "index": 1,
            "name": "color0"
        },
        {
            "index": 2,
            "name": "texcoord0"
        }
    ],
    "vertex_output_size_in_bytes": 48
}
```

### Fragment stage reflection

```
{
    "EntryPoint": (string),
    "NeedsFunctionConstants": (bool),
    "Resources": [
        {
            "abIndex": (int),
            "slot": (int),
            "type": (string: "SRV"|"CBV"|"SMP"|"UAV")
        },
        ...
    ],
    "ShaderType": (string: "Fragment"),
    "TopLevelArgumentBuffer": [
        {
            "EltOffset": (int),
            "Size": (int),
            "Slot": (int),
            "Space": (int),
            "Type": (string: "SRV"|"CBV"|"UAV")
        },
        ...
    ],
    "discards": (bool),
    "num_render_targets": (int),
    "rt_index_int": (int)
}
```

### Compute stage reflection

```
{
    "EntryPoint": (string),
    "NeedsFunctionConstants": (bool),
    "Resources": [
        {
            "abIndex": (int),
            "slot": (int),
            "type": (string: "SRV"|"CBV"|"UAV")
        },
        ...
    ],
    "ShaderType": (string: "Compute"),
    "TopLevelArgumentBuffer": [
        {
            "EltOffset": (int),
            "Size": (int),
            "Slot": (int),
            "Space": (int),
            "Type": (string: "SRV"|"CBV"|"UAV")
        },
        ...
    ],
    "tg_size": [
        (int),
        (int),
        (int)
    ]
}
```

### Amplification stage reflection

```
{
    "EntryPoint": (string),
    "FunctionConstants": [
        ...
    ],
    "NeedsFunctionConstants": (bool),
    "Resources": [
        {
            "abIndex": (int),
            "slot": (int),
            "type": (string: "SRV"|"CBV"|"UAV")
        },
        ...
    ],
    "ShaderID": (string),
    "ShaderType": (string: "Amplification"),
    "TopLevelArgumentBuffer": [
        {
            "EltOffset": (int),
            "Size": (int),
            "Slot": (int),
            "Space": (int),
            "Type": (string: "SRV"|"CBV"|"UAV")
        },
        ...
    ],
    "max_payload_size_in_bytes": (int),
    "num_threads": [
        (int),
        (int),
        (int)
    ]
}
```

### Mesh stage reflection

```
{
    "EntryPoint": (string),
    "FunctionConstants": [

    ],
    "NeedsFunctionConstants": (bool),
    "Resources": [
        {
            "abIndex": (int),
            "slot": (int),
            "type": (string: "SRV"|"CBV"|"UAV")
        },
        ...
    ],
    "ShaderID": (int),
    "ShaderType": (string: "Mesh"),
    "TopLevelArgumentBuffer": [
        {
            "EltOffset": (int),
            "Size": (int),
            "Slot": (int),
            "Space": (int),
            "Type": (string: "SRV"|"CBV"|"UAV")
        },
        ...
    ],
    "max_payload_size_in_bytes": (int),
    "max_primitive_output_count": (int),
    "max_vertex_output_count": (int),
    "num_threads": [
        (int),
        (int),
        (int)
    ],
    "primitive_topology": (string: "Triangle"|"Line"|"Point")
}
```

## Library reflection

When using the Metal Shader Converter library, you access reflection information for any shader you compiled using function `IRObjectGetReflection`. The reflection object contains information for the shader stage you request.

While the `IRReflection` object holds general reflection data — such as the entry point's name — you access detailed information about a shader stage through reflection information structs. To ensure forward compatibility, all reflection structs are versioned.

Example: reflect the entry point's name of a compiled vertex shader:

```c
// Reflect the entry point's name:
IRShaderReflection* pReflection = IRShaderReflectionCreate();
IRObjectGetReflection( pOutIR, IRShaderStageVertex, pReflection );
const char* str = IRShaderReflectionGetEntryPointFunctionName( pReflection );

// ... store entry point name or use it to find the MTLFunction ... //

IRShaderReflectionDestroy( pReflection );
```

Example: reflect the thread group size of a compiled compute shader through the compute information struct:

```c
// Get reflection data:
IRShaderReflection* pReflection = IRShaderReflectionCreate();
IRObjectGetReflection( pOutIR, IRShaderStageCompute, pReflection );

IRVersionedCSInfo csinfo;
if ( IRShaderReflectionCopyComputeInfo( pReflection, IRReflectionVersion_1_0, &csinfo ) )
{
    // Threadgroup sizes available in csinfo.info_1_0.tg_size
}

// Clean up
IRShaderReflectionReleaseComputeInfo( &csinfo );
IRShaderReflectionDestroy( pReflection );
```

## Related guides

- [Binding model](binding-model.md) — using reflected offsets to encode the top-level Argument Buffer.
- [Pipeline setup](pipeline-setup.md) — using reflected entry point names and stage info to build pipelines.
- [Compiling shaders](compiling-shaders.md) — emitting reflection during conversion.
