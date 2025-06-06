# Analyzing the memory usage of your Metal app

**Framework**: Xcode

Keep your app alive in the background by managing its memory footprint.

#### Overview

Instruments provides the Game Memory template to help you understand the memory growth in your Metal app. Keeping a small memory footprint allows the system to keep the app alive in the background longer, especially on devices with more constrained memory capacity. For more information, see [`Profile and optimize your game’s memory`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10106/).

##### Open the Game Memory Template

Start the memory analysis from your Xcode project by choosing Product > Profile, or by pressing Command-I. Alternatively, you can launch Instruments and then select the process from the drop-down list.

In the Template Selection window, select Game Memory.

![A screenshot of the Template Selection window with the Game Memory template selected.](https://docs-assets.developer.apple.com/published/6ead2ec149cb0e1393b371a0d09a78e4/gputools-instruments-game-memory-choose-template%402x.png)

##### Get to Know the Instruments

##### Record an Instruments Capture

Begin collecting the data by clicking the Record button.

![A screenshot of the Instruments window highlighting the Record button.](https://docs-assets.developer.apple.com/published/28faaed2513959dd83f9299a96e50b69/gputools-instruments-game-memory-record%402x.png)

Within your app, perform the actions that reproduce the memory problem, and then click the Record button to stop recording.

##### Analyze Your Apps Memory Allocations

The Game Memory template shows both memory allocations and memory footprint.

Memory allocations occupy space in the virtual memory address space. When your app allocates memory, these new allocations may not immediately take up space on physical memory. It’s not until your app uses these allocations that they consume physical memory.

The Allocations track provides a detailed view of memory allocations, their sizes, and object reference counts.

> **Note**: The Allocations track doesn’t include Metal resources with private storage mode — only managed and shared storage modes.

![A screenshot of Instruments with the Allocations track selected. The bottom details pane displays the statistics from the Allocations track.](https://docs-assets.developer.apple.com/published/a7ef7ee3f0561d17f3d618a01e1d21b1/gputools-instruments-game-memory-allocations%402x.png)

The Statistics view in the bottom detail area displays the categories of memory allocations. At the top of the Category column, there are three umbrella categories that summarize all allocations:

Below them, you can find more detailed categories. Metal resource allocations are in the `VM: IOAccelerator` category, and drawables are in `VM: IOSurface`.

To inspect the individual allocations in a category, click the arrow button next to the category name in the table.

![A screenshot of the details pane displaying the statistics from the Allocations track.](https://docs-assets.developer.apple.com/published/125f1d944a338303f144905308943203/gputools-instruments-game-memory-allocations-category-button%402x.png)

After selecting a category, you can sort the table by the Size column to find the largest memory allocation during the selected time range.

![A screenshot of the details pane displaying the All Heap Allocations statistics from the Allocations track.](https://docs-assets.developer.apple.com/published/25af05983a96078c9c5c5762fe92b069/gputools-instruments-game-memory-allocations-all-heap-allocations%402x.png)

You can also select an allocation in the list to view its description and stack trace in the inspector on the right.

##### Analyze Metal Resource Allocations

The Metal Resource Events track displays a history of all Metal-specific resource allocations and deallocations, along with their labels (see [`Naming resources and commands`](naming-resources-and-commands.md)).

![A screenshot of Instruments with the Metal Resource Events track selected. The bottom details pane displays the list of resource events.](https://docs-assets.developer.apple.com/published/94673e4047864c5e2d256642b4d96451/gputools-instruments-game-memory-metal-resource-events%402x.png)

The Resource Events view in the bottom detail area lists the resource allocation and deallocation events. It includes events from created or destroyed resources in the selected time range. Not all resources in the list persisted until the end of the time range.

##### Analyze Your Apps Total Virtual Memory Footprint

The Allocations track and the Metal Resource Events track both highlight memory allocations. However, allocations don’t always translate to memory footprint. The VM Tracker track shows the noncompressed and compressed/swapped dirty memory that together make up your app’s memory footprint.

Memory operates on the granularity of pages, and those pages can be either clean or dirty.

To conserve the amount of physical memory that your app uses, the system may compress or swap out some dirty pages that your app hasn’t accessed recently.

> ❗ **Important**: The system charges your app for any compressed/swapped memory based on its orginal size before compression.

![A screenshot of Instruments with the VM Tracker track selected. The bottom details pane displays a summary of the VM regions.](https://docs-assets.developer.apple.com/published/8b246e2860af1db08f3942abbdf92ad3/gputools-instruments-game-memory-vm-tracker%402x.png)

The center timeline area graphs the following metrics:

The corresponding columns are also available in the Summary view of the bottom detail area. There, you can expand the VM region types. In the mapped file type in the screenshot below, you can see the memory-mapped file of the bistro scene that the Modern Renderer app loaded:

![A screenshot of the details pane displaying a summary of the VM regions highlighting the largest memory-mapped file.](https://docs-assets.developer.apple.com/published/59da789811e66b333ea3537a55157f5b/gputools-instruments-game-memory-vm-tracker-mapped-file%402x.png)

## See Also

- [Analyzing the performance of your Metal app](analyzing-the-performance-of-your-metal-app.md)
  Ensure consistent, smooth rendering by profiling your app’s frame time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/analyzing-the-memory-usage-of-your-metal-app)*