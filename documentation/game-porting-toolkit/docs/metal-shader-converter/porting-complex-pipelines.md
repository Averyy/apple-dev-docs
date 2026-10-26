---
source: game-porting-toolkit
framework: game-porting-toolkit
url: https://github.com/apple/game-porting-toolkit/blob/main/docs/metal-shader-converter/porting-complex-pipelines.md
---

# Porting complex pipelines

> Part of the [Metal Shader Converter integration guides](README.md).

Beyond binding data to standard vertex/fragment/compute pipelines, the runtime companion header helps you bring more complex pipelines to Metal: geometry and tessellation stages (emulated via mesh shaders), amplification and mesh shaders, bindless resource models, and ray tracing. This guide assumes familiarity with the [Binding model](binding-model.md) and [Pipeline setup](pipeline-setup.md).

## Emulating geometry and tessellation pipelines

Beyond helping bind data to pipelines, the runtime companion header helps you emulate render pipelines that contain traditional geometry and tessellation stages. Metal Shader Converter allows you to bring these pipelines to Metal by mapping them to Metal mesh shaders.

To help with the process of building mesh render pipeline state objects from the geometry and tessellation shader stages, the companion header offers the following functions:

- `IRRuntimeNewGeometryEmulationPipeline`
- `IRRuntimeNewGeometryTessellationEmulationPipeline`

These helper functions take as input parameters descriptor structures with the building blocks to compile the pipeline.

The descriptor structure members reference the Metal libraries containing the pipeline's shader functions, reflection data, and a base mesh render pipeline descriptor that describes the render attachments.

Structure `IRGeometryEmulationPipelineDescriptor` contains:

- **stageInLibrary**: a `MTLLibrary` containing the stage-in function.
- **vertexLibrary**: a `MTLLibrary` containing the vertex function.
- **vertexFunctionName**: the name of the vertex function to retrieve from the vertex library.
- **geometryLibrary**: a `MTLLibrary` containing the geometry function.
- **geometryFunctionName**: the name of the geometry function to retrieve from the geometry library.
- **fragmentLibrary**: a `MTLLibrary` containing the fragment function.
- **fragmentFunctionName**: the name of the fragment function to retrieve from the fragment library.
- **basePipelineDescriptor**: a `MTLMeshRenderPipeline` descriptor providing template configuration for the pipeline, such as render attachments.
- **pipelineConfig**: reflection data that you obtained during the Metal Shader Converter compilation process.

Structure `IRGeometryTessellationEmulationPipelineDescriptor` shares all members of the `IRGeometryEmulationPipelineDescriptor` structure, and expands it to also include the following members:

- **hullLibrary**: a `MTLLibrary` containing the hull function and tessellator.
- **domainLibrary**: a `MTLLibrary` containing the domain function.

Providing a geometry shader is optional when you emulate a tessellation pipeline. Set the `geometryLibrary` member to `NULL` and set the `geometryFunctionName` to `kIRTrianglePassthroughGeometryShader` (`"irconverter_domain_shader_triangle_passthrough"`), `kIRLinePassthroughGeometryShader` (`"irconverter_domain_shader_line_passthrough"`), or `kIRPointPassthroughGeometryShader` (`"irconverter_domain_shader_point_passthrough"`) for triangle, line, and point pipeline states respectively.

> **Note:** When you use a passthrough geometry shader, you can obtain the values to assign to member `gsMaxInputPrimitivesPerMeshThreadgroup` from the domain shader's reflection.

The companion header provides the following draw helper functions to help you use the emulation render pipeline states. Issue these function calls as part of your render pass encoding process to encode a mesh dispatch workload that emulates your geometry and tessellation pipelines.

- `IRRuntimeDrawIndexedPrimitivesGeometryEmulation`
- `IRRuntimeDrawIndexedPatchesTessellationEmulation`

Before issuing these calls, allocate `IRRuntimeVertexBuffers` to define and bind your vertex and patch buffers and strides at the `kIRVertexBufferBindPoint` (`6`) index of the object stage. In addition, ensure that you make your vertex buffers resident via `useResource` or `useHeap`.

To preserve HLSL semantics (e.g. SV_VertexID, SV_InstanceID) during conversion, the mesh pipeline requires supplemental buffers containing draw call parameters. These companion draw helpers automatically bind these buffers at the correct bind point on your behalf. Without the companion, you need to create these buffers and set them at the correct bind points: `kIRArgumentBufferDrawArgumentsBindPoint` (`4`) and `kIRArgumentBufferUniformsBindPoint` (`5`).

## Using amplification and mesh shaders

Metal Shader Converter supports DX mesh shaders by converting them to Metal mesh shaders. If you use amplification shaders, Metal Shader Converter maps these to the object shader stage.

Just like with other shader stages, Metal Shader Converter produces useful offline reflection data you can use to obtain information about payload sizes, resource layout, number of threads per thread group and more. See [Reflection](reflection.md).

## Creating append and consume buffers

Append/consume buffers provide storage for shaders and an atomic counter to perform unordered insert and remove operations on this storage.

The Metal Shader Converter runtime provides a convenient function, `IRRuntimeCreateAppendBufferView`, that takes an input buffer for storage, creates the atomic counter, and bundles them together in an `IRBufferView` object. The `IRBufferView` object provides an abstraction that enables you to use the input Metal buffer as an append/consume buffer.

Use function `IRDescriptorTableSetBufferView` to bind an `IRBufferView` object as an append/consume buffer to a descriptor table.

Function `IRRuntimeGetAppendBufferCount` allows you to query the current value of the atomic counter associated with the append/consume buffer.

> **Note:** Metal Shader Converter implements the atomic counter through texture atomics, which require macOS 14 Sonoma, iOS 17, or later.

## Using unbounded arrays

Metal Shader Converter supports unbounded arrays, providing a path to implement bindless pipelines. Unbounded arrays are typically declared in shading languages by omitting the size specifier, such as `StructuredBuffer<T> inBuffers[] : register(t0, space0)`.

After declaring an unbounded array, you specify its number of elements at shader conversion time by providing a root signature, opting into Metal Shader Converter's explicit resource layout mode. This mechanism provides the CPU with the flexibility to define the number of resources in the array via a descriptor table. It is not possible to use unbounded resources with the automatic resource layout mode.

When binding resources to your explicit-layout signature pipelines, your top-level Argument Buffer contains the GPU addresses of the descriptor tables your root signature specifies. These, in turn, reference shader resources. In Metal, each descriptor table corresponds to a `MTLBuffer`.

Visually, your hierarchy corresponds to the following diagram:

- **Top-Level Argument Buffer** `-(uint64_t)->` **descriptor table** `-(IRDescriptorTableEntry)->` **resource**

Your descriptor tables may have as many entries as your root signature specifies at conversion time. Each entry in the table corresponds to the memory layout of `IRDescriptorTableEntry`.

## Using "dynamic resources"

Metal Shader Converter enables newer binding models where you bind resource and sampler heaps directly to your shaders and directly index into them. Metal Shader Converter automatically compiles in support for resource and sampler heaps at shader conversion time.

To bind your resources through this mechanism, bind a descriptor table at index `kIRDescriptorHeapBindPoint` (`0`) for general resources, and `kIRSamplerHeapBindPoint` (`1`) for samplers.

The pipeline expects each descriptor table to consist of an argument buffer where each entry corresponds to the layout defined by `IRDescriptorTableEntry`.

Your application needs to call `useResource` or `useHeap` for all indirectly-accessed resources to ensure they are resident when the pipeline executes.

## Leveraging inline ray tracing

Metal Shader Converter supports compiling inline ray tracing shaders to Metal IR. At compilation time, Metal Shader Converter directly maps inputs of type `RaytracingAccelerationStructure` to Metal instance acceleration structures.

You bind a Metal instance acceleration structure to the inline ray tracing pipeline's top-level Argument Buffer indirectly through an acceleration structure header. The Metal Shader Converter runtime companion header provides structure definition `IRRuntimeAccelerationStructureGPUHeader` you can use.

To perform inline raytracing, you provide your pipelines an instance of this structure through a `MTLBuffer` by binding its GPU address to your top-level argument buffer, or descriptor tables.

The `IRRuntimeAccelerationStructureGPUHeader` in this buffer contains the GPU resource ID of the acceleration structure against which to trace rays, as well as an array of instance contributions to the hit index. You can store the instance contribution array in its own buffer, or, alternatively, allocate extra space in the header buffer and use it for storing the instance contributions array.

Use convenience function `IRRaytracingSetAccelerationStructure` to build the acceleration structure header and encode instance contributions to hit groups, and function `IRDescriptorTableSetAccelerationStructure` to encode the acceleration structure header into a `MTLBuffer`.

Once your application creates the acceleration structure header buffer, bind it to the top-level Argument Buffer like any other buffer. It isn't possible to bind *primitive* acceleration structures to an inline ray-tracing shader compiled by Metal Shader Converter as this type is not present in the input IR.

Ensure you call `useResource` or use `useHeap` to make the Metal acceleration structure and the acceleration structure binding header resident. If your program stores the instance contribution data array in a `MTLBuffer` separate from the header, make sure to make it resident as well.

> **Note:** To ensure your rays intersect the acceleration structure, verify that the RayQuery object's template parameters match those of the acceleration structure. For example, `RAY_FLAG_CULL_NON_OPAQUE` culls all acceleration structures that don't have the `MTLAccelerationStructureInstanceOptionOpaque` option.

## Converting and running ray tracing pipelines

Metal Shader Converter enables you to bring ray tracing pipelines consisting of dedicated ray-tracing shader stages to Metal. Metal Shader Converter maps ray generation, intersection, any hit, closest hit, callable, and miss shaders to Metal visible and intersection functions. You use these Metal functions, optionally in conjunction with synthesized indirect intersection functions, to build ray tracing compute pipeline state objects that you can then use to trace rays against Metal acceleration structures and appropriately evaluate using a shader binding table (SBT).

The high-level process consists of the following steps:

1. Converting HLSL shaders to Metal functions.
2. Building ray tracing pipeline states.
3. Building shader binding tables.
4. Dispatching rays.

### Converting HLSL shaders to Metal functions

Metal Shader Converter offers different compilation modes for conversion of ray generation and intersection shaders when setting up your ray tracing pipeline compilation from HLSL to Metal IR.

Ray generation:

- Kernel
- Visible function

Intersection:

- Visible function
- Intersection function table function
- Intersection function buffer function

With Metal Shader Converter 3.0, the default recommendation is to compile your ray generation shaders as kernels and intersection shaders as intersection function buffer functions. With the `metal-shaderconverter` command-line tool, you do this by providing the option `--rt-ray-generation-compilation=kernel` and `--rt-intersection-compilation=ifIntersectionFunctionBufferFunction`. With the Metal Shader Converter dynamic library, specify `IRRayGenerationCompilationKernel` and `IRIntersectionFunctionCompilationIntersectionFunctionBufferFunction` when configuring your ray tracing pipeline with `IRRayTracingPipelineConfiguration`.

> **Note:** Metal intersection function buffer is only supported on GPUFamilyApple9 or later devices, and on macOS 16 or iOS 19 or later OS. For other device or OS configurations, fall back to compiling to visible functions if targeting an older device or OS. Compiling to intersection function table functions may offer a performance improvement, and its details are discussed below under [Performance considerations for ray tracing pipelines](#performance-considerations-for-ray-tracing-pipelines).

If compiling intersection shaders into visible functions, you must synthesize an indirect intersection function for triangles or procedural geometry or both, depending on your pipeline. With the `metal-shaderconverter` command-line tool, you do this with the command options `--synthesize-indirect-intersection-function --rt-hit-group-type=triangles` for triangle geometry and `--synthesize-indirect-intersection-function --rt-hit-group-type=procedural_primitive` for procedural geometry. With the Metal Shader Converter dynamic library, set the hit group type with `IRCompilerSetHitgroupType` to either `IRHitGroupTypeTriangles` or `IRHitGroupTypeProceduralPrimitive` before synthesizing the function with `IRMetalLibSynthesizeIndirectIntersectionFunction`.

When you use a custom intersection function with an any hit shader, Metal Shader Converter requires that you fuse these two shaders together into a single one. Use function `IRCompilerAllocCombineCompileAndLink`, or command-line argument `-fuse-any-hit-name`, to combine the functions together at compile time.

After conversion of your ray tracing stages to Metal IR, generate a Metal function for each. These Metal functions will then be used to build the ray tracing pipeline state.

### Building ray tracing pipeline states

Depending on your ray tracing pipeline configuration, Metal Shader Converter converts all your defined ray tracing stages into Metal libraries consisting of a compute kernel (for ray generation) and with visible and intersection functions (for hit group, miss, and callable shaders).

Build your ray tracing pipeline states by creating a compute pipeline state with the compute kernel function together with all visible and intersection functions as Metal linked functions.

With this ray tracing pipeline state, you create a Metal visible function table for the visible functions and a Metal intersection function table for the intersection functions. These function tables contain function pointers to your converted functions and also represent the shader identifiers we need to encode in your shader binding table (SBT).

> **Note:** For synthesized indirect intersection functions, when Metal performs a ray tracing traversal, it adds together the intersection function offset properties of the geometry and instance acceleration structures, determining the intersection function index it calls from the `MTLIntersectionFunctionTable`. Typically, this index does not match the shader record location in the shader binding table. To bridge this gap between APIs, store the indirection function handles at the positions in the intersection function table corresponding to the summed indices of the geometry and instance acceleration structures. The indirect intersection function re-evaluates the intersection offset into the shader binding table using the standard equation the source IR expects, finds the appropriate shader record, and uses its identifier to index into the visible function table to call your converted closest-hit, any-hit, intersection, and miss shaders.

### Building shader binding tables

Metal represents Shader Binding Tables as instances of `MTLBuffer`. The entries of these buffers consist of shader records, with each record containing a Shader Identifier (`IRShaderIdentifier`) and local root signature data. This arrangement allows you to represent the Shader Binding Table in the same fashion that the source IR expects.

The Shader Identifier in the shader binding table makes the association between the index shader record for the intersection and the offset in the visible function table Metal calls. It consists of the following members:

1. `shaderHandle`: for ray generation, miss, callable shaders, index into visible function table containing the translated function. For HitGroups, index to the converted closest-hit shader.
2. `intersectionShaderHandle`: for HitGroups, index into the visible function table containing a converted custom intersection function.
3. `localRootSignatureSamplersBuffer`: GPU address to a buffer containing static samplers for shader records.

The Metal Shader Converter runtime companion header offers functions `IRShaderIdentifierInit` and `IRShaderIdentifierInitWithCustomIntersection` to help you initialize ShaderIdentifier instances as necessary to build your Shader Binding Tables.

> **Note:** Shader handle 0 is reserved to denote "invalid handle" to the runtime. To ensure your shader handles are non-zero, do not use index 0 when you set function handles into your visible and intersection function tables. Conversely, use `0` as the `shaderHandle` value to denote a "null" shader handle in your SBT.

### Dispatching rays

In order to dispatch rays, dispatch a compute kernel using the ray tracing pipeline state object. You provide the ray dispatch parameters to the kernel by binding a `MTLBuffer` containing an instance of the `IRDispatchRaysArgument` structure to bind point `kIRRayDispatchArgumentsBindPoint`.

The Metal Shader Converter runtime companion header defines the `IRDispatchRaysArgument` and `IRDispatchRaysDescriptor` structures. The first provides the references to the GPU virtual address of the visible and intersection function tables containing your converted shaders and intersection functions, as well as the global root signature data, amongst other members.

The `DispatchRaysDesc` member of the `IRDispatchRaysArgument` structure provides crucial information for accessing the Shader Binding Table, including the start address, and size in bytes for ray generation shaders, as well as the same plus appropriate strides for the hit group, miss, and callable table.

After binding this structure to your pipeline, dispatch compute work as usual to start the ray tracing pipeline.

## Performance considerations for ray tracing pipelines

The following sections provide details on performance considerations and optimization opportunities for your ray tracing pipeline.

### Optimizing parameter passing

While the different shader stages comprising ray tracing may be independent, in order to link them together into a ray tracing pipeline state and pass data between them, you need to specify the maximum shared attribute size in bytes for all shaders in the same pipeline.

Use function `IRRayTracingPipelineConfigurationSetMaxAttributeSizeInBytes` to accomplish this when using the Metal Shader Converter dynamic library, or command-line argument `-rt-maximum-attribute-size-in-bytes` for the standalone executable.

Additionally, this function allows you to narrow the number of ray tracing intrinsic functions at compile time, yielding significant runtime performance improvements to your ray tracing pipelines.

In order to achieve this, before compilation call function `IRObjectGatherRaytracingIntrinsics` on your source IR. This function takes input IR and produces an intrinsic use mask for the shader. Apply this to all your ray tracing shaders to calculate the intrinsic use mask for all applicable stages. If you have multiple shaders of one kind, bitwise-OR the masks together.

With the intrinsic use masks for all your shaders, call function `IRRayTracingPipelineConfigurationSetIntrinsicMasks` when configuring a `IRRayTracingPipelineConfiguration` instance before compiling the shaders that comprise the ray tracing pipeline. This process directs the code generation logic to tailor the IR specifically to the minimum set of intrinsics your pipeline needs, improving runtime performance by reducing parameter passing.

When using the command-line interface of Metal Shader Converter, pass argument `-gather-raytracing-intrinsics` to make the compiler calculate an intrinsic use mask. Metal Shader Converter prints the mask to stdout as well as to an output file.

Similarly to using the dynamic library interface, once you have the intrinsic use masks for all the shaders that comprise your ray tracing pipeline, you compile the shaders passing the intrinsic masks as a uint64 number via the command-line interface using flags:

- `-rt-closest-hit-mask`
- `-rt-miss-mask`
- `-rt-callable-mask`
- `-rt-anyhit-mask`

The Metal Shader Converter command-line interface expects these numbers to start with the prefix `0x`.

### Increasing runtime performance by inlining function calls

You may be able to increase ray tracing runtime performance by limiting your ray tracing pipelines to a single ray generation shader. In this scenario, Metal may inline your ray generation shader into the ray dispatch kernel as it builds your pipeline state object, reducing the cost of starting ray tracing work.

If your pipeline state objects link multiple ray generation shaders, you may still take advantage of this optimization by compiling each specific ray generation function as a ray dispatch kernel, allowing you to build multiple specialized pipeline state objects without modifications to your high-level renderer.

See [Converting HLSL shaders to Metal functions](#converting-hlsl-shaders-to-metal-functions) above for details on how to compile your ray generation shaders as ray dispatch kernels.

You may be able to further reduce the runtime costs of shader function calling by defining function groups using the `groups` property of the `MTLLinkedFunctions` instance you use for linking visible functions to your pipelines.

By aggregating functions that your pipeline state object links into groups that correspond to ray generation, closest hit, or miss shaders, Metal only needs to consider a subset of pipeline-linked functions as potential call candidates.

The Metal Shader Converter runtime header defines the following constants to group visible functions:

- `kIRFunctionGroupRayGeneration`: (`"rayGen"`)
- `kIRFunctionGroupClosestHit`: (`"closestHit"`)
- `kIRFunctionGroupMiss`: (`"miss"`)

### Optimizing the runtime of intersection and any-hit shaders without Metal intersection function buffers

> **Note:** This section only applies if, due to device or OS limits, you are unable to compile your intersection shaders to intersection function buffer functions but would like performance improvements over compiling to visible functions.

If your ray tracing pipeline uses custom intersection or any hit shaders, or custom intersection+any hit shader pairs, and all your ray generation shaders use the same "geometry multiplier" (the total number of ray types), Metal Shader Converter enables you to potentially accelerate runtime performance further by compiling these shader types directly into Metal intersection functions.

Under this configuration, you use Metal intersection function tables — instead of visible functions — to more efficiently describe your game's different ray types to Metal.

Because your geometry multiplier determines the total number of ray types for your ray tracing workload, when you use multiple intersection function tables to implement different ray types, you allocate as many Metal intersection function tables as your geometry multiplier. You then populate each table with the functions that correspond to the intersection and any hit shaders for that ray type.

For convenience, you organize these Metal intersection function tables into a single "intersection function tables" argument buffer that you provide to Metal as part of your `IRRayDispatchArguments` structure when you dispatch ray tracing work.

To implement this optimization, first determine that your geometry multiplier is fixed across all your ray generation shaders. You then compile all your ray tracing shaders using option `IRIntersectionFunctionCompilationIntersectionFunction` when configuring your pipeline with `IRRayTracingPipelineConfiguration`.

Next, set up your shader binding table as usual and iterate over its hit groups to append them (in order) into a temporary CPU intersection functions array according to the following criteria:

1. Obtain a CPU-visible pointer to the beginning of your hit group table in the shader binding table.
2. For each hit group, retrieve its shader identifier, and determine if its intersection shader handle member contains a non-`NULL` value. If it does, retrieve the Metal intersection function corresponding to it and append it to the temporary Metal intersection function array.
3. If the intersection shader handle in the shader identifier is instead `NULL`, append a `NULL` sentinel value to the intersection function array. This reserves the index for a built-in opaque triangle intersection function.

> **Note:** As you calculate the appropriate offset in bytes for each hit group record, remember to take into consideration the hit group table's stride.

Next, you set up your intersection function tables argument buffer:

1. Prior to dispatching ray tracing work, allocate a Metal argument buffer to store as many Metal intersection function tables as your geometry multiplier.
2. Allocate as many Metal intersection function tables as your geometry multiplier. Configure each Metal intersection function table to store as many functions as the total number of functions, divided by the geometry multiplier:
    - `per_table_function_count = function_count / geometry_multiplier`
3. Store the Metal resource ID of each Metal intersection function table in the intersection function table argument buffer. The offset at which you store each table corresponds to each ray type plus the geometry multiplier times `16`:
    - `index = ray_type + (geometry_multiplier * 16) for ray_type in [0..geometry_multiplier)`
4. Populate each table by iterating over its function count. The function to store into each slot corresponds to the slot index times the geometry multiplier plus the table number (note this is not the table index):
    - `function_index = ((table_slot * geometry_multiplier) + table_number) for table_slot in [0..per_table_function_count), table_number in [0..geometry_multiplier)`
5. If the temporary CPU intersection function array at this function index contains a Metal intersection function, retrieve its function handle from the pipeline state object and store it.
6. Otherwise, if there is no Metal intersection function at this index (it's the `NULL` sentinel value), store the built-in opaque intersection function by calling Metal function `setOpaqueTriangleIntersectionFunctionWithSignature`.
7. As you build your Metal instance acceleration structure, you need to divide its `intersectionFunctionTableOffset` by the fixed geometry multiplier.

At ray dispatch time, set the member `IntersectionFunctionTables` of structure `IRDispatchRaysArgument` to point to your Metal argument buffer containing references to the Metal intersection function tables.

> **Note:** Metal intersection function tables are indirect resources that you need to manually mark resident to Metal by calling the `useResource` API or using Metal residency sets.

### Maximizing pipeline state build performance

The time required to build compute pipelines is proportional to the number of visible functions you link into them. You can accelerate the process of building compute pipeline state instances by leveraging Metal binary functions (`MTLLinkedFunctions.binaryFunctions`).

When you compile visible functions into binary functions at runtime, and then reuse them across your pipelines, you avoid the cost of repeatedly lowering each function for each pipeline you build. Using binary functions, however, may prevent Metal from performing some optimizations that could reduce the GPU execution time of your pipeline.

## Related guides

- [Binding model](binding-model.md) — descriptor tables and resource encoding these pipelines rely on.
- [Pipeline setup](pipeline-setup.md) — the companion header and retrieving functions from synthesized metallibs.
- [Reflection](reflection.md) — payload sizes, thread counts, and passthrough shader limits.
- [Performance](performance.md) — general runtime and build-time tuning.
- [Reference](reference.md#complete-code-samples) — complete ray tracing and geometry/tessellation code samples.
