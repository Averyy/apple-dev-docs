# Analyzing memory usage

**Framework**: Xcode

Manage your Metal app’s memory usage by inspecting its resources.

#### Overview

The Memory viewer provides comprehensive information about your app’s memory usage in Metal. The Memory viewer’s top section presents a breakdown of memory by categories, and the bottom section displays a table of resources. In the table, you can inspect resources for their memory size, configuration, and other characteristics.

![A screenshot of the Memory viewer showing bar graphs in the top section that summarize the resource memory use, and a resources table in the bottom section.](https://docs-assets.developer.apple.com/published/5ec4a24a30162e3285d0c2c0718a2e5c/gputools-metal-debugger-mv-overview%402x.png)

Metal apps create many resources, and those resources consume a lot of memory. For example, to render an animated character using a physically based renderer, you might need buffers to hold vertex and animation data, and multiple textures to provide material attributes. When you scale these requirements to multiple characters and larger scenes, your app’s memory footprint grows significantly.

Additionally, when you create Metal resources, specifying their configuration precisely has a substantial effect on performance. The Metal debugger analyzes the configuration you provide and uses it to create the underlying GPU representation of a resource. For example, if you create a resource with a private storage mode, Metal can optimize the resource for GPU access, and doesn’t need to store data in a location or format directly accessible from the CPU.

##### Examine the Bar Graphs

The categories in the top section of the Memory viewer organize memory usage data and provide memory totals based on the following criteria:

Each bar graph consists of segments representing the largest resources that it tracks. The final segment of each bar graph shows an aggregate total for its smaller resources. Move your pointer over a segment to view a popover with the name of the resource, its size, and other information. Click a segment to get more information about that specific resource.

![A screenshot of the Memory viewer’s bar graphs highlighting only texture resources. The texture that consumes the most memory is selected.](https://docs-assets.developer.apple.com/published/6aa9f0a25392c4e58685222d0e9e5fbf/gputools-metal-debugger-mv-bar-graph%402x.png)

##### Inspect the Resources Table

To improve how your app creates and manages resources, you need data about how it uses them. The Memory viewer provides information about the resources that are live in your Metal app during a capture.

![A screenshot of the Memory viewer’s resources table.](https://docs-assets.developer.apple.com/published/da04b2c56009c5cd26eced0abfc91385/gputools-metal-debugger-mv-resources-table%402x.png)

The resources table provides the following information for all resource types:

| Column | Property | Description |
| --- | --- | --- |
| Label | [`label`](https://developer.apple.com/documentation/Metal/MTLResource/label) | The label you add when creating the resource. Use this information to identify specific resources in your app. To learn how to name your resources, see [`Naming resources and commands`](naming-resources-and-commands.md). |
| Insights |  | Possible problems or optimizations that might improve memory or resource usage. |
| Type |  | The type of resource. For a texture, this information includes the texture’s subtype. For a heap, it includes the heap’s subtype. |
| Allocated Size | [`allocatedSize`](https://developer.apple.com/documentation/Metal/MTLResource/allocatedSize) | The allocated memory size for the resource. |
| Storage Mode | [`resourceOptions`](https://developer.apple.com/documentation/Metal/MTLResource/resourceOptions) or [`storageMode`](https://developer.apple.com/documentation/Metal/MTLResource/storageMode) | The storage mode you choose when creating the resource. |
| Purgeable State |  | The volatility of the resource. When you mark a resource as volatile, the system can purge it when free memory is low. The operating system doesn’t include volatile resources in the system memory total for your app. |
| Aliasable | [`isAliasable()`](https://developer.apple.com/documentation/Metal/MTLResource/isAliasable()) | An indication of whether the resource shares its associated memory with another resource on the same heap. |
| CPU Access |  | An indication of whether your app has accessed the resource from the CPU. |
| Time Since Last Bound |  | The amount of time since last binding the resource to a Metal command encoder. If you’ve never bound the resource or haven’t bound it for a long time, you can probably release this resource or mark it as volatile. |

For textures, you can add the following columns:

| Column | Property | Description |
| --- | --- | --- |
| Pixel Format | [`pixelFormat`](https://developer.apple.com/documentation/Metal/MTLTexture/pixelFormat) | The Metal pixel format you choose when creating the texture. |
| Width | [`width`](https://developer.apple.com/documentation/Metal/MTLTexture/width) | The width, in pixels, of the texture’s base mipmap. |
| Height | [`height`](https://developer.apple.com/documentation/Metal/MTLTexture/height) | The height, in pixels, of the texture’s base mipmap. |
| Depth | [`depth`](https://developer.apple.com/documentation/Metal/MTLTexture/depth) | The depth, in pixels, of the texture’s base mipmap. |
| Array Length | [`arrayLength`](https://developer.apple.com/documentation/Metal/MTLTexture/arrayLength) | The number of slices in the texture array. |
| Mipmaps | [`mipmapLevelCount`](https://developer.apple.com/documentation/Metal/MTLTexture/mipmapLevelCount) | The number of mipmap levels in the texture. |
| Samples | [`sampleCount`](https://developer.apple.com/documentation/Metal/MTLTexture/sampleCount) | The number of samples in each pixel. |
| Usage | [`usage`](https://developer.apple.com/documentation/Metal/MTLTexture/usage) | Indicates the actions a shader or app can perform on the texture. The more restricted the list, the more optimizations Metal can apply to the texture. |
| Lossless Compression |  | Indicates whether the texture supports lossless compression. |

For buffers, you can add the following column:

| Column | Property | Description |
| --- | --- | --- |
| Length | [`length`](https://developer.apple.com/documentation/Metal/MTLBuffer/length) | The logical length, in bytes, of the buffer. Compare this value to the allocated size. To make memory available to the GPU, Metal sometimes needs to allocate more memory than you request. If you see many small buffers, consolidate those that the system uses together into a single buffer, or allocate the buffers on a heap. These alternative allocation strategies save memory and require less work to track dependencies between commands accessing those resources. |

For heaps, you can add the following columns:

| Column | Property | Description |
| --- | --- | --- |
| Size | [`size`](https://developer.apple.com/documentation/Metal/MTLHeap/size) | The logical size, in bytes, of the heap. |
| Used Size | [`usedSize`](https://developer.apple.com/documentation/Metal/MTLHeap/usedSize) | The number of bytes the heap allocates for other resources. |
| Hazard Tracking Mode | [`resourceOptions`](https://developer.apple.com/documentation/Metal/MTLHeap/resourceOptions) or [`hazardTrackingMode`](https://developer.apple.com/documentation/Metal/MTLHeap/hazardTrackingMode) | The hazard tracking mode of the allocated resources on the heap. |

For indirect command buffers, you can add the following column:

| Column | Property | Description |
| --- | --- | --- |
| Size | [`size`](https://developer.apple.com/documentation/Metal/MTLIndirectCommandBuffer/size) | The number of bytes the system uses to hold encoded commands. This total doesn’t include memory for any commands that the system resets. Compare this size to the allocated size of the indirect command buffers. Choose the size of an indirect command buffer based on the number of commands you expect to execute inside it. |

For acceleration structures, you can add the following column:

| Column | Property | Description |
| --- | --- | --- |
| Size | [`size`](https://developer.apple.com/documentation/Metal/MTLAccelerationStructure/size) | The logical length, in bytes, of the acceleration structure. |

##### Improve Your Metal Workload with Insights

Click the Insights button in the bottom right corner to open a popover of recommendations for the resources.

![A screenshot of the Insights popover showing recommendations related to unused resources.](https://docs-assets.developer.apple.com/published/073a4035dc560b6f89365603c6865bcf/gputools-metal-debugger-mv-insights%402x.png)

##### Limit Your Scope with Filters

Use the filter field at the bottom of the Memory viewer to adjust filtering criteria. Type filter terms into the field, and the resources table displays any resources with labels that match those filter terms.

You can also click the filter button to add filters for specific kinds of resources, to limit the table to resources that the captured frame uses, and to limit the table to just volatile resources.

When there are two or more filter terms, you can click the filter button to choose whether to match any or all of the terms. For any filter term, you can click it to choose to include or exclude resources that match that term.

##### Group and Sort Resources to Detect Patterns

By default, the resources table shows all resources in a single list. You can click a column header to sort the table by that column in ascending or descending order. You can also group the resources by certain criteria.

Control-click an entry in the table to group the resources by any of the following criteria:

From this same context menu, you can also choose to sort by a specific criteria, which is equivalent to clicking a column heading for sorting.

##### Get More Information About a Specific Resource

You can also get more information about a specific resource by Control-clicking it and selecting Get Info.

For example, for a texture, the additional information shows details specific to that texture, such as its pixel format and dimensions. To see the contents of the texture, double-click it.

##### Export a Memory Report

To share the data in the Memory viewer, you can export it in the following ways:

- Export a GPU trace: Choose File > Export and select a location to save the GPU trace file. You can then open the trace file later.
- Export a comma-separated values (CSV) file: Choose Editor > Export Memory Report to generate the CSV file. The resulting file has all of the columns you see in the resource view. You can open this file in Numbers or another spreadsheet app.

## See Also

- [Analyzing your Metal workload](analyzing-your-metal-workload.md)
  Investigate your app’s workload, dependencies, performance, and memory impact using the Metal debugger.
- [Analyzing resource dependencies](analyzing-resource-dependencies.md)
  Avoid unnecessary work in your Metal app by understanding the relationships between resources.
- [Analyzing Apple GPU performance using a visual timeline](analyzing-apple-gpu-performance-using-a-visual-timeline.md)
  Locate performance issues using the Performance timeline.
- [Analyzing Apple GPU performance using counter statistics](analyzing-apple-gpu-performance-using-counter-statistics.md)
  Optimize performance by examining counters for individual passes and commands.
- [Analyzing Apple GPU performance with performance heat maps](analyzing-apple-gpu-performance-using-performance-heatmaps-a17-m3.md)
  Gain insights to SIMD group performance by inspecting source code execution.
- [Analyzing Apple GPU performance using the shader cost graph](analyzing-apple-gpu-performance-using-shader-cost-graph-a17-m3.md)
  Discover potential shader performance issues by examining pipeline states.
- [Analyzing non-Apple GPU performance using counter statistics](analyzing-non-apple-gpu-performance-using-counter-statistics.md)
  Optimize performance by examining counters for individual passes and commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/analyzing-memory-usage)*