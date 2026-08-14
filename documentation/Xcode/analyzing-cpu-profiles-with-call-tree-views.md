# Analyzing CPU profiles with call tree views

**Framework**: Xcode

Use call tree visualizations to find performance bottlenecks in Instruments.

#### Overview

Instruments organizes profiling data into a call tree, a hierarchical view showing which functions consume the most time. Each profiling instrument populates the call tree in its own way. Most use CPU sampling, but some use other techniques, such as Processor Trace, which reconstructs a call tree from hardware branch-tracing instructions, or the Task Creation Call Tree in Swift Concurrency, which captures a backtrace each time your app creates a task.

Instruments provides three ways to visualize the same data: the standard call tree, flame graphs, and Top Functions. Each mode surfaces different patterns, so switching between them helps you find issues that aren’t obvious in any single view.

Run Comparison and [`OSSignposter`](https://developer.apple.com/documentation/os/ossignposter) complement call tree analysis. With `OSSignposter`, you can annotate your code with named intervals that appear as labeled spans in Instruments, and isolate the call tree to a specific operation. Run Comparison creates a diff of the call trees from two separate recordings, making it straightforward to measure whether a code change introduced a regression or an improvement.

#### Switch Between Call Tree View Modes

A segmented control in the top-right corner of the detail area lets you choose from three call tree view modes: Call Tree, Flame Graph, and Top Functions. Click the appropriate button to switch modes. The underlying sample data doesn’t change when you switch; only the presentation changes.

In the flame graph:

1. Pinch on the trackpad or hold Option while scrolling to zoom horizontally.
2. Scroll to pan after zooming.
3. Click a block to select it, use the arrow keys to move the selection, and secondary-click for a context menu.

![A screenshot of the Instruments detail view and the segmented control that switches between Call Tree, Flame Graph, and Top Functions modes.](/images/com.apple.Xcode/call-tree-view-mode-picker@2x.png)

#### Explore Profiles with Flame Graphs

A flame graph presents the same data as a standard call tree, but organizes it visually as a grid of blocks. The x-axis represents the percentage of samples. When more samples include a particular frame at a call-stack position, those blocks are wider. The vertical axis represents call-stack depth, with frames arranged in the order they appear in recorded call stacks.

Within each level, the flame graph places heavier (more sampled) callees on the left and lighter callees on the right, following the same ordering principle as the call tree, which sorts its heaviest branches to the top. In the call tree, you can click a column header to reverse the sort order, but the flame graph always sorts heaviest to the left.

When the call tree has multiple weight columns (for example, Weight and Self Weight in Time Profiler), the flame graph uses whichever column the call tree is currently sorted by. The flame graph doesn’t support self-weight columns because displaying self weight would require placing larger bars under smaller ones. If you’re sorting by a self-weight column when you open the flame graph, Instruments automatically switches to the corresponding total-weight column.

A flame graph is a good starting point for an investigation because you can scan a large profile at a glance, spot wide blocks that represent expensive frames, and quickly identify the shapes that correspond to hotspots. When you select a frame, the inspector on the right shows the heaviest stack trace for that frame — the specific call chain that accounts for the most samples. In many cases, this is enough to identify an optimization target without further exploration of the call hierarchy.

The standard call tree is better suited for detailed analysis of individual code paths; it shows exact sample counts in an expanded tabular format, making it easier to compare call signatures or navigate a specific tree you have in mind. Both views show the same data and support full call-hierarchy navigation, so nothing is lost when you switch between them.

![A screenshot of Instruments showing a flame graph with wide blocks indicating frames that appear in many CPU samples.](/images/com.apple.Xcode/call-tree-flame-graph@2x.png)

#### Find Performance Hotspots with Top Functions

Top Functions aggregates all samples for the same symbol across the entire recording, regardless of which callers invoked that symbol. In a standard call tree, a function called from 10 different callers appears 10 times, once under each caller. In Top Functions, that same function appears once, with all of its samples combined into a single row.

This aggregation surfaces hotspots that a standard call tree or flame graph can obscure. A function that’s individually inexpensive under each caller may look like a significant contributor when you combine all of its samples. Top Functions makes that pattern visible.

The detail area splits into two columns: the Top Functions table on the left and a flame graph on the right. The inspector shows the heaviest stack trace for the selection in the adjacent flame graph.

By default, Instruments sorts the Top Functions table to show the functions that consume the most CPU time at the top. This counts only time spent in each function’s own code, not time it spends waiting on other functions it calls. Select a symbol in the table to populate the adjacent flame graph with all samples charged to that symbol. The flame graph defaults to an Inverted Callers configuration, which shows who called the selected symbol. Switch to Callees to see what the selected symbol calls. When the Invert Call Tree toolbar option is enabled, the flame graph displays Callers or Inverted Callees instead of the normal toggle options. All filters and call tree options in the bottom toolbar apply to Top Functions.

![A screenshot of Instruments showing the Top Functions split-pane layout with the Top Functions table on the left and an adjacent flame graph on the right.](/images/com.apple.Xcode/call-tree-top-functions@2x.png)

#### Mark Performance Intervals

With [`OSSignposter`](https://developer.apple.com/documentation/os/ossignposter), you can annotate your code with named intervals that Instruments displays as labeled spans in a timeline track. Selecting a span in the timeline sets the active time range to that interval, which filters all call tree views to show only the samples from that period.

Create an `OSSignposter` from the [`os`](https://developer.apple.com/documentation/os) framework with a subsystem and category, or initialize one from an existing [`Logger`](https://developer.apple.com/documentation/os/logger). Call `beginInterval(_:id:)` before work starts and `endInterval(_:_:)` when it finishes. The name parameter is a [`StaticString`](https://developer.apple.com/documentation/swift/staticstring), so use a string literal, or a `let` constant of type `StaticString`, as shown here:

```swift
let signposter = OSSignposter(subsystem: "com.example.myapp", category: .pointsOfInterest)
let state = signposter.beginInterval("renderFrame")
defer { signposter.endInterval("renderFrame", state) }
// Perform rendering work.
```

For more details on signpost types, disambiguation, and how to display signpost data in Instruments, see [`Recording Performance Data`](https://developer.apple.com/documentation/os/recording-performance-data).

#### Compare Profiling Runs

Run Comparison shows the differences between two call tree views from separate recordings in the same Instruments document. Use it when you want to measure whether a code change improved or regressed the performance of a specific operation. To compare runs, record at least two runs in the same document by clicking Record multiple times.

For an accurate comparison without ambient noise from unrelated activity, filter both traces to the same `OSSignpost` interval before comparing. Select the corresponding signpost interval in the timeline of each run to set the active time range. This ensures the comparison reflects the same logical operation rather than the entire recording.

To open the comparison popover, click the Compare button (⇆) in the toolbar or press Command-K. The popover lists the call trees from other runs available for comparison. The system matches call trees based on the selected track. For a top-level instrument track like Time Profiler, each run that includes the instrument appears. For other tracks, such as process or thread tracks, the popover lists matching tracks from each run. If a run has no matching tracks, it doesn’t appear at all. Select the baseline run from the dropdown menu to start the comparison.

Instruments labels the candidate run (typically the newer or test build) as (+) and the baseline run (the reference build) as (−). Each run uses a distinct color: Red blocks indicate a regression and green blocks indicate an improvement. The percentages reflect change between runs, not a fraction of the total samples. A node that appears only in the candidate run shows +∞; a node that appears only in the baseline run shows −100%.

By default, Top Functions in the run comparison sorts results to show the biggest regressions at the top. To show improvements instead, click the column header to reverse the sort order.

The comparison flame graph provides a visual overview of the same data. Block size reflects the absolute magnitude of change between the two runs: Blocks for regressions (more samples in the candidate run) appear on the right, blocks for improvements (fewer samples) appear on the left, and gray blocks in the center indicate a change close to zero.

All call tree filtering and manipulation options are available during a run comparison, including Charge, Prune, Flatten, and call tree constraints. These options can help clean up the automatic comparison to produce a more useful visualization. Source view is unavailable during a run comparison.

![A screenshot of Instruments displaying a run comparison in Top Functions mode. The symbol names and their weight comparisons are shown on the left of the detail view, and green blocks indicating improvements are on the right.](/images/com.apple.Xcode/run-comparison-view@2x.png)

## See Also

- [Addressing CPU bottlenecks](addressing-cpu-bottlenecks.md)
  Locate and fix pipeline stalls, cache misses, and other performance issues.
- [Analyzing CPU usage with the Processor Trace instrument](analyzing-cpu-usage-with-processor-trace.md)
  Identify code where your app uses the CPU inefficiently.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/analyzing-cpu-profiles-with-call-tree-views)*