# Analyzing resource dependencies

**Framework**: Xcode

Avoid unnecessary work in your Metal app by understanding the relationships between resources.

#### Overview

The Dependencies viewer provides a graphical representation of the structure of your GPU trace and allows you to see the relationships between resources and the encoders that access them. It also highlights the manual synchronizations you use between encoders, and indicates any unnecessary work by showing you all the unused resources in your frame.

![A screenshot of the Dependencies viewer, which includes a dependency graph view, a sidebar, and a control bar.](https://docs-assets.developer.apple.com/published/9792256b993e2819ad485ff530e40b9d/gputools-metal-debugger-dv-overview%402x.png)

##### Inspect the Graph at Different Levels of Detail

At the highest level, the Dependencies viewer shows the overall structure of your frame. At this level, you can see the graph of command encoders inside command buffers. You can also see all of the passes in your frame. Each pass includes a thumbnail preview of its work, as well as the number of resources that it consumed or produced. At this level, you can see whether data is flowing and whether there’s synchronization between passes.

![A screenshot of the Metal debugger’s Dependencies viewer showing the dependency graph with a low level of detail.](https://docs-assets.developer.apple.com/published/4764d72159e10ae6fbcf431ce96ac97d/gputools-metal-debugger-dv-lod-low%402x.png)

As you zoom in to the next level, the Dependencies viewer expands the resources for each pass. Additionally, each resource can have icons above and below it that indicate the consuming and producing actions. For attachments in a render pass, the icons refer to the load and store actions. Otherwise, they refer to general resource read-and-write operations. At this level, you can also view which resources are introducing data flow or synchronization between passes.

![A screenshot of the Metal debugger’s Dependencies viewer showing the dependency graph with a medium level of detail.](https://docs-assets.developer.apple.com/published/48408c4be87ba4cc4eee729d4a9b6e9d/gputools-metal-debugger-dv-lod-mid%402x.png)

As you zoom in more, the Dependencies viewer shows larger thumbnails and metadata for the resources.

![A screenshot of the Metal debugger’s Dependencies viewer showing the dependency graph with a high level of detail.](https://docs-assets.developer.apple.com/published/49049b73095e136bdd9de6722645206a/gputools-metal-debugger-dv-lod-high%402x.png)

##### View a Resources Consuming and Producing Actions

The consuming and producing actions above and below a resource help you understand the resource accesses in a given pass at a quick glance.

For textures in a render pass, the actions refer to the load and store actions for each attachment.

For a multisample render pass, the store action may affect the storing for both the multisample and the resolve textures. With [`MTLStoreAction.storeAndMultisampleResolve`](https://developer.apple.com/documentation/Metal/MTLStoreAction/storeAndMultisampleResolve), the multisample texture shows a store action and the resolve texture shows a store action. With [`MTLStoreAction.multisampleResolve`](https://developer.apple.com/documentation/Metal/MTLStoreAction/multisampleResolve), the multisample texture shows a don’t-care action and the resolve texture shows a store action.

Otherwise, the Dependencies viewer annotates the actions with generic read-and-write operations.

##### Analyze the Data Flow and Synchronization Dependencies

The Dependencies viewer displays two categories of dependencies between passes:

- Solid lines depict data flow. A previous pass produced data and a later pass consumes it.
- Dashed lines depict synchronization. There’s no data flow, but there’s a relationship between the two passes.

For example, a compute pass reading from a texture that a previous render encoder wrote has data flow between the two passes.

Additionally, a render pass that clears an attachment on load has no data dependency on any pass that previously modified the texture. However, that render pass needs to wait until the previous passes finish modifying the texture — a synchronization.

##### Choose a Mode for Viewing Dependencies

You can use the Dependencies viewer to choose different modes for visualization, each with a different subset of edges:

- All: Shows all edges from synchronization primitives, and tracked and untracked resources.
- Synchronzation: Shows dashed synchronization edges from synchronization primitives and tracked resources.
- Data Flow: Shows solid data-flow edges from tracked or untracked resources.

##### Pin Resources From the Resource Pile

To maintain a compact graph, the Dependencies viewer attempts to keep a few interesting resources visible on the graph and hide the rest in a pile under each pass. Clicking the pile opens a popover of the resources.

![A screenshot of the Resources popover at a pass in the Dependencies viewer.](https://docs-assets.developer.apple.com/published/40b0ab325d2c90ada3a97cc0734c37b1/gputools-metal-debugger-dv-popover%402x.png)

You can click the button to the right of each resource to pin or unpin it.

##### Get More Information About a Pass

Clicking any pass in the Dependencies viewer selects it and displays additional information about the pass in the sidebar. You can also determine which resources the pass consumes or produces:

- For a resource the pass consumes, the Dependencies viewer suggests the pass that most recently modified the resource.
- For a resource the pass produces, the Dependencies viewer suggests the passes that later consume the data in the resource.

##### Get More Information About a Resource

Clicking any resource in the Dependencies viewer selects it and displays additional information about the resource in the sidebar. You can also see the passes that last produced, or will later consume, the data in the resource.

When you select a resource, the Dependencies viewer highlights any related resources. For example, when you select a texture view, it highlights the parent textures. When you select a heap, it highlights the resources from the heap.

##### Improve Your Metal Workload with Insights

Click the Insights button in the bottom right corner to open a popover of recommendations in the Dependencies viewer.

![A screenshot of the Insights popover in the Dependencies viewer.](https://docs-assets.developer.apple.com/published/a1153313baa692a1e418b19fa7234605/gputools-metal-debugger-dv-insights%402x.png)

##### Limit Your Scope with Filters

Use the filter field at the bottom of the Dependencies viewer to adjust the graph’s filtering criteria. Type filter terms into the field and the Dependencies viewer displays any related passes that match the filter terms. In addition, when filtering by a resource, you can find passes that consume or produce the resource.

##### Search for Specific Elements

Choose Find > Find to display the search bar above the Dependencies viewer. You can type search terms into the search bar’s text field to find matching passes and resources.

For any search term, you can click it and choose to include or exclude elements that match the term.

The two arrow buttons to the right of the text field let you move to the previous or the next matching element in the Dependencies viewer.

## See Also

- [Analyzing your Metal workload](analyzing-your-metal-workload.md)
  Investigate your app’s workload, dependencies, performance, and memory impact using the Metal debugger.
- [Analyzing memory usage](analyzing-memory-usage.md)
  Manage your Metal app’s memory usage by inspecting its resources.
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

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/analyzing-resource-dependencies)*