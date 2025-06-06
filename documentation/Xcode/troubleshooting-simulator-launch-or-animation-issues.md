# Troubleshooting Simulator launch or animation issues

**Framework**: Xcode

Diagnose and resolve issues launching a simulator, or with slow scrolling or animations in Simulator.

#### Overview

When you run multiple simulators concurrently with Xcode and other programs on your Mac, you can run into poor performance in simulators, or even errors launching more simulators. Isolate the cause, then fix these types of issues in Simulator.

For issues that may be part of Simulator or a simulated device, please file a bug.

##### Investigate and Address Insufficient Resources

Launching a simulator can result in an error alert that there are insufficient system resources. This usually occurs when launching a simulator exceeds either the maximum number of active processes or the maximum number of open files. The best solution is to free up resources by closing simulated devices and other Mac applications.

If it’s not possible to free up enough resources, raise the system limits until you restart your Mac.

> **Note**: It’s possible to exceed the maximum number of process or the maximum number of open files when you launch other programs or open other files some time after you’ve launched a simulator. If this occurs, Simulator doesn’t give you a warning. The effects depend on what program is trying to launch the process or open the file.

It’s possible to exceed the maximum number of process or the maximum number of open files when you launch other programs or open other files some time after you’ve launched a simulator. If this occurs, Simulator doesn’t give you a warning. The effects depend on what program is trying to launch the process or open the file.

First, find the current process and file limits:

1. Open Terminal.
2. Run the command `sudo launchctl limit`. Provide your password when Terminal requests it, because you’re running the command as superuser.
3. Note the maximum number of processes next to `maxproc`, and the maximum number of files next to `maxfiles`.

Run the command `ps -A | wc -l` in Terminal to show the current total of running processes.

If you need to increase the maximum number of processes, run the command `sudo launchctl limit maxproc <per user limit> <total limit>`, replacing `<per user limit>` and `<total limit>` with numbers. For example, the command `sudo launchctl limit maxproc 2000 2500` sets the maximum number of concurrent processes for any one user to 2000 and the total number of all concurrent processes to 2500.

> ⚠️ **Warning**: Setting the maximum number of processes to a number that is too low can prevent your Mac from operating correctly. Restart your machine to restore the original limits.

Setting the maximum number of processes to a number that is too low can prevent your Mac from operating correctly. Restart your machine to restore the original limits.

If you need to increase the maximum number of open files, run the command `sudo launchctl limit maxfiles <per process limit> <total limit>`, replacing `<per process limit>` and `<total limit>` with numbers. For example, the command `sudo launchctl limit maxfiles 2000 unlimited` sets the maximum number of open files for any one process to 2000 and the total number of all open files to `unlimited`.

##### Investigate Slow Scrolling or Animations

In some cases slow scrolling or animation is due to the simulator. Use the items in Debug > Graphics Quality Override to check if this is an issue.

##### Report Bugs

For issues that may be part of Simulator or a simulated device, please file a bug through the [`Apple Developer website`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/).

When you file a bug, include the full version number of Xcode in the bug title and in the description. To find the version number, choose Xcode > About Xcode. The full version number including the part in parentheses is in the window that Xcode displays. If the bug is with a simulated device, attach a `sysdiagnose` for that device by opening Terminal and typing the following command:

```None
xcrun simctl diagnose
```

Press Enter again to display the status of the capture as well as the path for the file with the `sysdiagnose`.

For more information on `diagnose`, run the following command:

```None
xcrun simctl diagnose --help
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/troubleshooting-simulator-launch-or-animation-issues)*