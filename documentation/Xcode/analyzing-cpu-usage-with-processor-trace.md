# Analyzing CPU usage with the Processor Trace instrument

**Framework**: Xcode

Identify code where your app uses the CPU inefficiently.

#### Overview

Recent Apple silicon devices can capture a  where the CPU stores information about the code it runs, including the branches it takes and the instructions it jumps to. The CPU streams this information to an area on the file system so that you can analyze it with the Processor Trace instrument. A processor trace captures information about all running threads with very little runtime overhead. Your device is typically less than 1% slower than when it isn’t recording a processor trace.

> **Note**:  When you profile your app using Instruments, the system performs other tracing activities, so you may see total runtime overhead that’s greater than 1%.

You can use the Processor Trace instrument in Instruments 16.3 and later to analyze the processor trace for your app, and visualize every function call that your app executes. The Processor Trace instrument includes time that your app spends in all functions, including code that the compiler generates, such as automatic reference counting (ARC) memory management code in Swift, and synthesized constructors and destructors in C++.

Use the Processor Trace instrument to gather information about the functions your code runs while you perform particular activities in your app. Analyze slow, or processor-intensive, operations to identify whether your app might be able to process its data in more efficient ways, such as by using different algorithms, or caching the results of calculations to use again.

#### Use Supported Hardware

You can record a processor trace with the following hardware:

- iPhone 16 and iPhone 16 Pro, or later
- iPad Pro with M4 or later
- Mac with M4 or later

You can use Instruments on any Mac to analyze a saved processor trace file, including those that don’t support  processor traces.

#### Record a Processor Trace

Follow these steps in Xcode to record a processor trace:

1. Choose Product > Profile, select the Processor Trace template, and click Choose.
2. Click the Record button.
3. Interact with your app, performing any specific functions you might want to analyze.
4. Click the Stop button.

Instruments processes the trace data and displays a timeline of the trace, which includes tracks for the Processor Trace and Thread State Trace instruments. You can analyze the trace data, or save the trace file to analyze it later or share it with your team.

![An Instruments screenshot with the Processor Trace timeline highlighted, and a region selected in the timeline. The detail view shows the function call summary for a traced app’s main thread.](https://docs-assets.developer.apple.com/published/7b9a91d35562ac5a46a9bf5d942a091a/processor-trace-summary%402x.png)

To record and analyze processor traces from the build of your app that you distribute to customers, you need to generate and store the debugging information from that build so that Instruments can use it to generate function call backtraces. For more information, see [`Building your app to include debugging information`](building-your-app-to-include-debugging-information.md).

To supply the debugging symbols for your app, follow these steps in Instruments:

1. Choose File > Symbols.
2. In the Symbols window, click the Add Symbols pull-down button at the top right and choose Add Folder of dSYMs.
3. Navigate to the folder that contains the debugging symbol files for your app.
4. Click Add.

> **Note**:  Some addresses, such as branch islands that the compiler creates to support function calls between different libraries, don’t have function names. Instruments shows those addresses as raw pointer values even if you supply all the debugging symbols for your app.

#### Analyze Processor Usage

In the Instruments timeline view, the Target view in the Processor Trace track displays three histograms:

To focus on a region you’re interested in, click in the Processor Trace track in the timeline at one end of the region, and drag to the other end of the region. The detail view below the timeline shows one of three views, which you choose using the Call Tree pop-up button at the top left of the detail view.

The Call Tree view shows a top-down tree of the processor cycles and instructions that run during the process that Instruments traces, with summary statistics for each call. Alternatively, you can switch to a flame graph visualization using the Graph button at the top right of the Call Tree view. The flame graph shows the fraction of time the traced process spends running each function, organized by each function’s position in the call stack. Use the Call Tree view to investigate how functions spend time running their own code, as well as the code in the functions that they call.

![An Instruments screenshot of the Call Tree view showing a flame graph for a traced app.](https://docs-assets.developer.apple.com/published/4de96080e62831a613fdcdf644b355a5/processor-trace-flame-graph%402x.png)

The Summary: Function Calls view shows an aggregation of the functions that your app runs during the recording, along with statistics that include the number of times the app runs each function, the active duration of the function, and the number of instructions the processor uses running each function. The list of functions includes library code, as well as functions that the compiler synthesizes. Use this view to get an overview of where your app spends its time and to prioritize deeper investigation into specific functions.

The Function Calls view shows a list of all the functions that Instruments traces during the recording, along with their duration, the thread they run on, and the number of instructions. Use this view to explore thread backtraces of individual calls to certain functions, or to focus the inspection range in Instruments on the duration of a single function call.

#### View a Time Ordered Flow of Function Calls

Click the disclosure triangle next to your target process’s name in the timeline to see a list of the threads that Instruments traces in that process, along with a visualization in the timeline of the functions that are active in each thread. Select the timeline track for a thread, then choose View > Selected Track > Size to Fit to expand the track and display the names of active functions in their entries in the timeline. Use this view to understand which function is running in your app’s thread, and correlate that information with other events in the Instruments timeline.

![An Instruments screenshot of the timeline view showing the active functions on the main thread of a traced app.](https://docs-assets.developer.apple.com/published/3cc994ab79dbaea029884b14fe63afdb/processor-trace-function-flow%402x.png)

#### Filter Detail Views By Function Process or Thread

In any of the Processor Trace instrument’s detail views, type a function name into the “Input filter” field, or Control-click a function and choose Add to Detail Filter, to filter the view so that it displays only information about that function. You can also filter by process, or by thread, by adding the process or thread’s name to the detail filter.

![An Instruments screenshot of the Input filter field with the word objc, and the Summary: Function Calls view showing only functions that contain objc in their names.](https://docs-assets.developer.apple.com/published/0759841476289c6d21c5653790be82d4/processor-trace-filter%402x.png)

#### Set the Inspection Range to the Lifetime of a Function Call

The Processor Trace instrument’s detail views show information about the processes that Instruments records within the inspection range you select in the timeline. To analyze the behavior of a particular function, set the inspection range to the lifetime of a call to that function.

In the Function Calls view, Control-click a function’s Duration value and choose Set Inspection Range to change the region of interest in the timeline to the interval between the processor starting to run the function and the function exiting.

![An Instruments screenshot of the detail view showing the function calls that a traced process made during the selected inspection range in the timeline view.](https://docs-assets.developer.apple.com/published/bba0927c9af08ebb337de7542d16c592/processor-trace-functions%402x.png)

#### Charge Prune and Flatten Function Profiles

You can charge functions to hide library code from the profile, while continuing to factor the time the processor spends running the library code into your analysis. When you charge a function to its callers, the system adds any instructions and cycles the CPU runs in that function, and in functions it calls, to the instruction and cycle counts for the calling functions. Control-click a symbol name and choose Charge “[]” to Callers to remove calls to that function, as well as functions that it calls, from the view, and to include their profile information in the reported statistics for their callers. You can also charge all the functions in a particular library to their callers by Control-clicking the symbol name of a function from that library and choosing Charge “[]” to Callers.

You can prune functions to hide uninteresting or irrelevant code so that you can focus on the code you want to profile. In the Profile view, Control-click a symbol name and choose Prune “[]” to remove calls to that function, as well as functions that it calls, from the view.

You can flatten library calls to boundary frames to hide internal details of libraries from the profile, without removing the library code from your analysis. Control-click a symbol name and choose Flatten “[]” to Boundary Frames to show only those functions in that library where functions in other libraries call them, and they call functions that are in other libraries.

Review and change your choices by clicking the Charge, Prune, Flatten button at the bottom of the detail view.

![An Instruments screenshot of the detail view showing the call profile for a traced app, where the functions in the AppKit library are flattened to boundary frames.](https://docs-assets.developer.apple.com/published/cb4269b5907b4ab1ff3908f8446689c8/processor-trace-flatten%402x.png)

#### Review Your Apps Processor Usage

Long-running operations on the main thread can cause freezes and hitches in your app’s UI, which a person perceives as your app being unresponsive. If the processor trace shows high levels of processor activity in your app’s main thread, identify opportunities to move processing to the background using Swift concurrency or dispatch queues. For more information, see [`Understanding user interface responsiveness`](understanding-user-interface-responsiveness.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/analyzing-cpu-usage-with-processor-trace)*