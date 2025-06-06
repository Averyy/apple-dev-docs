# Setting breakpoints to pause your running app

**Framework**: Xcode

Specify where your app pauses when running the debugger to investigate bugs.

#### Overview

When you identify a place in your source code where you want to investigate a bug, set a breakpoint to pause the debugger so you can inspect your variables and step through your code to isolate the bug.

To locate crashes or other bugs where it is difficult to know where to set a breakpoint, use symbolic or issue breakpoints to pause on specific problem conditions and quickly identify where a bug occurs.

For bugs that occur after several iterations or only under certain circumstances, specify conditions on your breakpoint. If you want to log information at specific points in your app or receive notifications when a line of code executes, use breakpoint actions.

##### Specify Where to Pause Your App

Navigate to a line in your code where you want execution to pause, then click the gutter or line number in the source editor to set a breakpoint. Xcode displays a breakpoint icon to indicate the location.

![Xcode displays two blue breakpoint markers on line numbers for two lines of code. Xcode also displays a light blue, disabled breakpoint marker on a line number for a line of code.](https://docs-assets.developer.apple.com/published/490252326a8f9805eb9fde4456d57996/setting-breakpoints-to-pause-your-running-app-1%402x.png)

Drag a breakpoint up or down to move it to another location; drag it away from the gutter to remove it. Click the breakpoint icon in the debug area toolbar to activate or deactivate all breakpoints.

##### Manage Breakpoints Across Your App

When you have many breakpoints set across several source code files, click the Breakpoint Navigator button in the navigator area of the main window to open the Breakpoint navigator to view and manage all breakpoints.

![Xcode displays the Breakpoint Navigator with a list of example breakpoints.](https://docs-assets.developer.apple.com/published/70451144e5b8dc66bad23f08c6db7da2/setting-breakpoints-to-pause-your-running-app-2%402x.png)

Click a breakpoint label in the Breakpoint navigator to quickly navigate to the breakpoint in the source editor. Pressing the Delete key after selecting a breakpoint label deletes the breakpoint from your code. Click a breakpoint icon in the Breakpoint navigator to enable or disable it.

To easily find a frequently used breakpoint in the navigator, Control-click the breakpoint label, choose Edit Breakpoint, and enter a name for it. Then use the filter at the bottom of the Breakpoint navigator.

You can also use the filter to find breakpoints by symbols in the line of code for the breakpoint. The filter tools provide options for showing only modified breakpoints and showing only enabled breakpoints.

##### Specify Conditions for Pausing Your App

For bugs that occur after a certain number of iterations, or under limited conditions that require repetitive actions, it’s cumbersome to pause at the breakpoint and press the Continue button repeatedly until the bug occurs. There are two approaches to handle this type of situation more efficiently in the debugger.

For a bug that occurs after a certain number of iterations, set the debugger to ignore the breakpoint for some iterations. Control-click the breakpoint, choose Edit Breakpoint, and specify the number of times to ignore the breakpoint before stopping.

![Xcode showing an example of a breakpoint with a setting of “Ignore 8 times before stopping”.](https://docs-assets.developer.apple.com/published/dad9eae6778dcfc42e7429814d48d7a8/setting-breakpoints-to-pause-your-running-app-3%402x.png)

For a bug that occurs under limited conditions, set the debugger to pause on a breakpoint when an expression is true. Control-click the breakpoint, choose Edit Breakpoint, and enter a condition using variables available in the local scope.

![Xcode showing an example of a breakpoint with a condition set to “indexPath.row > 8”.](https://docs-assets.developer.apple.com/published/f18819b4ae5ea07a1818a26608630723/setting-breakpoints-to-pause-your-running-app-4%402x.png)

The debugger evaluates the expression each time it reaches the breakpoint in execution, and pauses only if the expression is true.

##### Pause on a Symbol Outside Your Code

To debug some issues, you need to pause on a symbol that your source code doesn’t define. For example, when you encounter an Auto Layout issue, the error message recommends setting a breakpoint on `UIViewAlertForUnsatisfiableConstraints`. To do that, use a symbolic breakpoint.

In the Breakpoint navigator, click the Add button (+) in the lower-left corner, and choose Symbolic Breakpoint. Enter the object and symbol in the Symbol field, using the format of the example text.

![Xcode showing a symbolic breakpoint with the symbol UIViewAlertForUnsatisfiableConstraints.](https://docs-assets.developer.apple.com/published/14845c07ec221953ba10cfcee28e0273/setting-breakpoints-to-pause-your-running-app-5%402x.png)

The debugger pauses when the app or your code calls the symbol you specify. The example symbol `UIViewAlertForUnsatisfiableConstraints` typically pauses in the application’s `main` method and not on a line in your code. When this happens, use the console to view an Auto Layout trace with `po [[UIWindow keyWindow] _autolayoutTrace]`.

> 💡 **Tip**: Some symbols receive calls very frequently and pausing on each can be unmanageable. Add a condition to the breakpoint to reduce the frequency of calls, or disable the symbolic breakpoint until you reach a breakpoint in your code where you want to start diagnosing the issue, and then enable the symbolic breakpoint.

Some symbols receive calls very frequently and pausing on each can be unmanageable. Add a condition to the breakpoint to reduce the frequency of calls, or disable the symbolic breakpoint until you reach a breakpoint in your code where you want to start diagnosing the issue, and then enable the symbolic breakpoint.

##### Pause on an Uncaught Swift Error or Objective C Exception

When your app encounters an unhandled Swift Error or Objective-C exception, it crashes. Frequently, the stack trace doesn’t point directly to where the problem occurs. Set a breakpoint to pause on an uncaught Swift Error or Objective-C exception so you can locate the problem.

When an unhandled Swift error causes a crash, the debugger shows a fatal error on the line with the `try!` and not where the error originally occurs.

![Xcode displaying an app crashed with an uncaught Swift error.](https://docs-assets.developer.apple.com/published/36ed0fd739771f57f0e06b5b785e4405/setting-breakpoints-to-pause-your-running-app-6%402x.png)

If the thrown error has a helpful error message, that may be enough information to resolve the problem. If not, add a Swift error breakpoint to pause on the line that throws the error. In the Breakpoint navigator, click the Add button (+) in the lower-left corner, and choose Swift Error Breakpoint. The app then pauses on the thrown error instead of the `try!`.

![Xcode displaying an app paused at a Swift error breakpoint, showing a line of code throwing a Swift error.](https://docs-assets.developer.apple.com/published/78b461c0ead40074865f1390ff73aadc/setting-breakpoints-to-pause-your-running-app-7%402x.png)

When an uncaught Objective-C error causes a crash, the debugger shows the crash in the `AppDelegate` or `main` method.

![Xcode displaying an app crashed due to an uncaught Objective-C exception, with an error message describing a problem dequeueing a table view cell.](https://docs-assets.developer.apple.com/published/304c61cfdc887b277265ad35ac35bdd3/setting-breakpoints-to-pause-your-running-app-8%402x.png)

Add an Objective-C exception breakpoint to pause on the line where the crash occurs instead of `main`. In the Breakpoint navigator, click the Add button (+) in the lower-left corner, and choose Exception Breakpoint.

![Xcode displaying an app paused on a line of code that dequeues a reusable cell for a table view with an invalid identifier, generating an Objective-C exception.](https://docs-assets.developer.apple.com/published/d485505f90a9c5c3b472b5dfc9359451/setting-breakpoints-to-pause-your-running-app-9%402x.png)

For more information, see [`Identifying the cause of common crashes`](identifying-the-cause-of-common-crashes.md).

##### Pause Automatically When the System Detects a Runtime Issue

Xcode has tools called  to detect several different types of runtime issues: updating the user interface outside the main thread, updating variables from different threads unsafely, accessing addresses unsafely, and executing code that results in undefined behavior. Configure your scheme to enable sanitizers to detect these issues with static analysis at build time. When you disable the sanitizers and your app encounters one of these issues, your app crashes and Xcode may not clearly identify where the issue occurs.

![Xcode displaying an app crashed due to a main thread runtime issue.](https://docs-assets.developer.apple.com/published/c116f770ce869e3713a69387f090ac48/setting-breakpoints-to-pause-your-running-app-10%402x.png)

To pause your app and investigate, click the Add button (+) in the lower-left corner of the Breakpoint navigator,  choose Runtime Issue Breakpoint, and select the type of runtime issue for the breakpoint.

![Xcode displaying an app paused on a line of code that updates the user interface from a background thread.](https://docs-assets.developer.apple.com/published/4bcb34b738e31a681d15e095f8187a8d/setting-breakpoints-to-pause-your-running-app-11%402x.png)

Enable the sanitizer for the issue and run your app. The sanitizer identifies lines of code where it expects runtime issues to occur. When the app pauses at your runtime breakpoint, investigate why the issue occurs. For more information, see [`Diagnosing memory, thread, and crash issues early`](diagnosing-memory-thread-and-crash-issues-early.md).

##### Log Variable Values Run Scripts or Play Sounds at a Breakpoint

Instead of writing code to log variable values and details about your app’s execution, use breakpoint actions to log messages and to perform debugger commands that print variable values to the console.

Breakpoint actions can also play sounds when the debugger reaches a breakpoint, which is useful for knowing when code executes without pausing. Breakpoint actions can execute AppleScripts or shell scripts to perform helpful debugging tasks like taking a screenshot or saving some app data for analysis.

To perform an action with a breakpoint, Control-click the breakpoint, either in the source editor or in the Breakpoint navigator, choose Edit Breakpoint, click Add Action, choose an action and provide any additional information necessary. For example, provide a message for the Log Message action, or a command and parameters for the Debugger Command action.

![Xcode displaying a breakpoint with a debugger command action. The debugger command is “po indexPath”.](https://docs-assets.developer.apple.com/published/f6ac0431871e13b8fe9ede7c698b989b/setting-breakpoints-to-pause-your-running-app-12%402x.png)

To perform more than one action at a breakpoint, click the Add button (+) to the right of an existing action to add another action. To continue executing your app without pausing after performing your action, select the “Automatically continue after evaluating actions” option.

## See Also

- [Stepping through code and inspecting variables to isolate bugs](stepping-through-code-and-inspecting-variables-to-isolate-bugs.md)
  Find the cause of your bugs by watching variables change as you step through your source code in the debugger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/setting-breakpoints-to-pause-your-running-app)*